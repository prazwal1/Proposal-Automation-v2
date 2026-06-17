"""Generic estimate builder.

Reads the schemas learned by SchemaLearner and a plain JSON estimate config,
then drives the Azure Pricing Calculator for ANY product — no hand-written
page objects needed.

Estimate config format (generic):
{
  "estimate_name": "My Estimate",
  "components": [
    {
      "product": "Virtual Machines",          # or "slug": "virtual-machines"
      "name": "web-01",                        # optional display name
      "fields": {
        "Region": "Southeast Asia",            # keys are matched fuzzily
        "Operating system": "Windows",         # against label/aria-label/name
        "Tier": "Standard",
        "Instance": "D2 v3",
        "Virtual machines": 2,
        "savings_plan": "3 year"               # radios match by value/label
      }
    }
  ]
}
"""
import json
import re
import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)

from .learner import (
    CALCULATOR_URL,
    MODULES_CSS,
    PRODUCT_SEARCH_CSS,
    SchemaLearner,
)


def norm(s):
    """Normalize a key/label for fuzzy matching."""
    return re.sub(r"[^a-z0-9]+", "", str(s).lower())


# common aliases so old-style keys keep working out of the box
ALIASES = {
    "os": "operatingsystem",
    "vmname": "productname",
    "name": "productname",
    "instance": "size",
    "quantity": "virtualmachines",
    "count": "virtualmachines",
}


class SchemaStore:
    def __init__(self, schema_dir="schemas"):
        self.schema_dir = Path(schema_dir)
        index_path = self.schema_dir / "index.json"
        if not index_path.exists():
            raise FileNotFoundError(
                f"No learned schemas found in {self.schema_dir}/ — run learn.py first."
            )
        self.index = json.loads(index_path.read_text(encoding="utf-8"))
        self._cache = {}

    def resolve(self, component):
        """Find schema by explicit slug or by (fuzzy) product name."""
        slug = component.get("slug")
        if not slug:
            wanted = norm(component["product"])
            exact = [
                s for s, m in self.index.items()
                if wanted in (norm(m["product"]), norm(s))
            ]
            partial = [
                s for s, m in self.index.items()
                if any(wanted in n or n in wanted for n in (norm(m["product"]), norm(s)))
            ]
            matches = exact or partial
            if not matches:
                raise KeyError(f"No learned schema matches product '{component['product']}'")
            if len(matches) > 1:
                raise KeyError(
                    f"Product '{component['product']}' is ambiguous: {matches}. "
                    "Use 'slug' in the config."
                )
            slug = matches[0]
        if slug not in self._cache:
            path = self.schema_dir / self.index[slug]["file"]
            self._cache[slug] = json.loads(path.read_text(encoding="utf-8"))
        return self._cache[slug]


class GenericEngine:
    def __init__(self, driver, schema_dir="schemas", wait_time=10):
        self.driver = driver
        self.store = SchemaStore(schema_dir)
        if driver is not None:
            self.wait = WebDriverWait(driver, wait_time)
            # reuse learner's module bookkeeping (open page, new module, observer)
            self.nav = SchemaLearner(driver, schema_dir=schema_dir)

    @classmethod
    def offline(cls, schema_dir="schemas"):
        """Matcher-only instance (no browser) for validation/catalog tooling."""
        return cls(None, schema_dir=schema_dir)

    # ------------------------------------------------------------------
    def build(self, config):
        self.nav.open_calculator()
        print(f"🚀 Building estimate: {config.get('estimate_name', 'Unnamed')}")

        for comp in config["components"]:
            schema = self.store.resolve(comp)
            label = comp.get("name") or schema["product"]
            print(f"➕ Adding {schema['product']} ({label})")
            module_id = self._add_component(schema)
            root = self.nav._module_root(module_id)
            self.wait.until(lambda d: root.is_displayed())

            fields = dict(comp.get("fields", {}))
            if comp.get("name") and not any(
                norm(k) in ("productname", "name") for k in fields
            ):
                fields = {"product-name": comp["name"], **fields}

            for key, value in self._order_fields(schema, fields):
                try:
                    self._set_field(module_id, schema, key, value)
                    print(f"   ✅ {key} = {value}")
                except Exception as e:
                    print(f"   ❌ {key} = {value}: {str(e)[:160]}")
                    raise
                # the module is reactive — let it re-render before the next
                # (often dependent) field, so controls revealed/replaced by this
                # change are mounted before we look for them
                try:
                    r = self.nav._module_root(module_id)
                    self.nav.watch(r, "module")
                    self.nav.wait_settled("module", timeout=4)
                except Exception:
                    pass

        if config.get("estimate_name"):
            self._set_estimate_name(config["estimate_name"])
        print("✅ Estimate build complete.")

    # ------------------------------------------------------------------
    def _add_component(self, schema):
        self.nav.mark_existing_modules()
        self.nav._click_picker(schema["picker_testid"], schema["product"])
        module_id = self.nav.wait_new_module()
        self.nav.watch(self.nav._module_root(module_id), "module")
        self.nav.wait_settled("module")
        return module_id

    # ------------------------------------------------------------------
    def _order_fields(self, schema, fields):
        """Apply config fields in on-page (schema) order.

        The page flows top-down: instance choice gates disk tiers, tier gates
        SKUs, etc. The learner stores fields in DOM order, so sorting config
        keys by their matched field's position replays a natural human flow
        and satisfies the learned depends_on edges.
        """
        order = {id(f): i for i, f in enumerate(schema["fields"])}

        def rank(item):
            try:
                f = self._match_field(schema, item[0], item[1])
                return order.get(id(f), len(order))
            except KeyError:
                return len(order) + 1

        items = list(fields.items())
        return sorted(items, key=rank)  # stable for unmatched keys

    def _match_field(self, schema, key, value):
        """Pick the schema field that best matches a config key."""
        k = norm(key)
        k = ALIASES.get(k, k)
        candidates = []
        for f in schema["fields"]:
            primary = {
                norm(f.get("label") or ""),
                norm(f.get("aria_label") or ""),
                norm(f.get("name") or ""),
                norm(f.get("clean_name") or ""),
                norm(f.get("id") or ""),
                norm(f.get("data_name_override") or ""),
            }
            primary.discard("")
            # placeholder often just echoes the product name — weakest signal
            secondary = {norm(f.get("placeholder") or "")}
            secondary.discard("")
            hidden_penalty = 0 if f.get("visible", True) else 4
            if k in primary:
                candidates.append((0 + hidden_penalty, f))
            elif any(k in n or n in k for n in primary if n):
                candidates.append((1 + hidden_penalty, f))
            elif k in secondary:
                candidates.append((2 + hidden_penalty, f))
            elif any(k in n or n in k for n in secondary if n):
                candidates.append((3 + hidden_penalty, f))

        if not candidates:
            raise KeyError(
                f"No field matching '{key}' in {schema['product']} schema. "
                f"Known fields: {sorted({f.get('label') or f.get('name') for f in schema['fields']})}"
            )
        candidates.sort(key=lambda c: c[0])
        best_rank = candidates[0][0]
        best = [f for r, f in candidates if r == best_rank]

        # radios: several controls share a name; choose by value/label
        radios = [f for f in best if f["control"] == "radio"]
        if radios and len(best) > 1:
            v = norm(value)
            for f in radios:
                if norm(f.get("radio_value") or "") == v or norm(f.get("label") or "") == v:
                    return f
            for f in radios:
                if v in norm(f.get("radio_value") or "") or v in norm(f.get("label") or ""):
                    return f
        return best[0]

    # ------------------------------------------------------------------
    def _set_field(self, module_id, schema, key, value):
        field = self._match_field(schema, key, value)

        if field.get("revealed_by"):
            self._ensure_section_open(module_id, schema, field["revealed_by"])

        control = field["control"]
        last = None
        # the module re-renders after some interactions (e.g. instance pick),
        # so re-find the element fresh on every attempt
        for _ in range(4):
            try:
                root = self.nav._module_root(module_id)
                elem = self._find(root, field)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", elem
                )
                if control == "select":
                    self._set_select(elem, value)
                elif control in ("text", "number"):
                    self._set_input(elem, value)
                elif control == "combobox":
                    self._set_combobox(elem, value)
                elif control == "radio":
                    self.driver.execute_script("arguments[0].click();", elem)
                elif control == "checkbox":
                    desired = bool(value) if isinstance(value, bool) else \
                        str(value).lower() in ("1", "true", "yes", "on")
                    if elem.is_selected() != desired:
                        self.driver.execute_script("arguments[0].click();", elem)
                else:
                    raise ValueError(f"Unsupported control '{control}' for '{key}'")
                return
            except (StaleElementReferenceException, ElementClickInterceptedException,
                    TimeoutException, NoSuchElementException) as e:
                # NoSuchElement included on purpose: a reactive re-render may not
                # have mounted the control yet — wait and re-find rather than
                # failing the whole build on a transient miss.
                last = e
                time.sleep(0.7)
        raise last

    def _find(self, root, field, retries=3):
        # primary selector first, then any state-specific selector variants
        # the learner observed (a control's name can change per page state)
        selectors = [field["selector"]] + [
            v["selector"] for v in field.get("selector_variants", []) or []
            if v.get("selector")
        ]
        last = None
        for _ in range(retries):
            for sel in selectors:
                try:
                    elem = root.find_element(By.CSS_SELECTOR, sel)
                    if elem.is_displayed():
                        return elem
                    last = TimeoutException(f"{sel} not visible")
                except Exception as e:
                    last = e
            time.sleep(0.4)
        if field.get("present_when"):
            hints = ", ".join(
                f"{c['field']}={c.get('text') or c.get('value')}"
                for c in field["present_when"][:4]
            )
            raise TimeoutException(
                f"Field '{field.get('label') or field.get('name')}' only exists "
                f"when: {hints}. Set that field first in your config. ({last})"
            )
        raise last

    def _ensure_section_open(self, module_id, schema, toggle_label):
        root = self.nav._module_root(module_id)
        for t in schema.get("toggles", []):
            label = t.get("text") or t.get("label") or t.get("aria_label") or ""
            if norm(label) == norm(toggle_label):
                try:
                    btn = self.nav._find_toggle(root, t)
                    if btn is not None and btn.get_attribute("aria-expanded") == "false":
                        self.driver.execute_script("arguments[0].click();", btn)
                        self.nav.watch(root, "module")
                        self.nav.wait_settled("module", timeout=5)
                except Exception:
                    pass
                return

    # ------------------------------------------------------------------
    def _set_select(self, elem, value):
        dropdown = Select(elem)
        v = str(value).strip().lower()
        opts = dropdown.options
        # exact text, then exact value, then partial text (v1 behaviour)
        for opt in opts:
            if opt.text.strip().lower() == v:
                dropdown.select_by_visible_text(opt.text)
                return
        for opt in opts:
            if (opt.get_attribute("value") or "").lower() == v:
                dropdown.select_by_value(opt.get_attribute("value"))
                return
        for opt in opts:
            if v and v in opt.text.strip().lower():
                dropdown.select_by_visible_text(opt.text)
                return
        # reverse containment, e.g. value 'Premium SSD' vs option 'Premium'
        for opt in opts:
            t = opt.text.strip().lower()
            if t and t in v:
                dropdown.select_by_visible_text(opt.text)
                return
        # token-subset: one side's words are all contained in the other's.
        # Bridges label variance like 'SQL Server Standard' (the Linux-style
        # name an agent may guess) vs the Windows option 'SQL Standard', where
        # the inserted word breaks plain substring matching. Pick the option
        # that shares the most words and adds the fewest extras.
        vt = set(re.findall(r"[a-z0-9]+", v))
        best, best_score = None, None
        for opt in opts:
            ot = set(re.findall(r"[a-z0-9]+", opt.text.lower()))
            if not ot or not vt:
                continue
            if ot <= vt or vt <= ot:
                score = (len(ot & vt), -len(ot ^ vt))
                if best_score is None or score > best_score:
                    best, best_score = opt, score
        if best is not None:
            dropdown.select_by_visible_text(best.text)
            return
        raise ValueError(
            f"No option matching '{value}'. Available: "
            f"{[o.text.strip() for o in opts][:12]}"
        )

    def _set_combobox(self, elem, value):
        """Drive a React-Select typeahead (e.g. the VM 'Instance' size picker).

        The visible control is an <input role="combobox"> with no name; the
        chosen value is committed to a sibling hidden input. Type the query,
        wait for the menu (rendered as [role=option] at document level), then
        click the best matching option.
        """
        v = str(value).strip().lower()
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
        try:
            elem.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].focus();", elem)
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys(str(value))

        chosen, deadline = None, time.time() + 8
        while time.time() < deadline:
            opts = [o for o in self.driver.find_elements(
                By.CSS_SELECTOR, "[role='option']") if o.is_displayed()]
            if opts:
                # option text looks like "D2as v6: 2 vCPUs, 8 GB RAM, ..." —
                # match on the head before the colon, then a prefix fallback
                for o in opts:
                    label = o.text.strip().lower()
                    head = label.split(":", 1)[0].strip()
                    if head == v or label.startswith(v):
                        chosen = o
                        break
                chosen = chosen or opts[0]
                break
            time.sleep(0.3)

        if chosen is None:
            raise NoSuchElementException(
                f"No typeahead suggestion appeared for '{value}'")
        try:
            chosen.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.driver.execute_script("arguments[0].click();", chosen)

    def _set_input(self, elem, value):
        try:
            elem.click()
        except ElementClickInterceptedException:
            # sticky headers can overlap; focus via JS instead
            self.driver.execute_script("arguments[0].focus();", elem)
        self.driver.execute_script(
            "arguments[0].select && arguments[0].select();", elem
        )
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys(str(value))
        # typeahead inputs (e.g. VM instance picker) open a suggestion
        # list — commit the highlighted suggestion with ENTER
        time.sleep(0.5)
        if self._suggestions_open():
            elem.send_keys(Keys.ENTER)
        else:
            elem.send_keys(Keys.TAB)

    def _suggestions_open(self):
        return self.driver.execute_script(
            "return Array.from(document.querySelectorAll("
            "\"[role='option'], [role='listbox'] li, .autocomplete li, .suggestions li\""
            ")).some(e => e.offsetWidth > 0 && e.offsetHeight > 0);"
        )

    # ------------------------------------------------------------------
    def _set_estimate_name(self, name):
        try:
            elem = self.driver.find_element(By.ID, "estimate-name")
            self._set_input(elem, name)
            print(f"📦 Estimate name set: {name}")
        except Exception as e:
            print(f"⚠️  Could not set estimate name: {str(e)[:120]}")

    def export_excel(self, download_path="Azure_Estimates", timeout=60,
                     rename_to=None):
        """Click Export and wait for the .xlsx download.

        rename_to: optional name (e.g. the estimate name) — the downloaded
        file (default 'ExportedEstimate.xlsx') is renamed to '<rename_to>.xlsx',
        with a numeric suffix if that file already exists.
        """
        import os
        clicked = False
        for sel in [
            "button[aria-label*='Export']",
            "//button[contains(., 'Export')]",
        ]:
            try:
                if sel.startswith("//"):
                    btn = self.driver.find_element(By.XPATH, sel)
                else:
                    btn = self.driver.find_element(By.CSS_SELECTOR, sel)
                self.driver.execute_script("arguments[0].click();", btn)
                clicked = True
                break
            except Exception:
                continue
        if not clicked:
            print("⚠️  Export button not found")
            return None
        start = time.time()
        while time.time() - start < timeout:
            files = sorted(
                (os.path.join(download_path, f) for f in os.listdir(download_path)
                 if f.endswith(".xlsx")),
                key=os.path.getmtime, reverse=True,
            )
            if files and os.path.getmtime(files[0]) > start - 5:
                path = files[0]
                if rename_to:
                    safe = re.sub(r'[<>:"/\\|?*]+', "_", str(rename_to)).strip() or "Estimate"
                    target = os.path.join(download_path, f"{safe}.xlsx")
                    n = 1
                    while os.path.exists(target):
                        n += 1
                        target = os.path.join(download_path, f"{safe}_{n}.xlsx")
                    os.replace(path, target)
                    path = target
                return path
            time.sleep(1)
        return None
