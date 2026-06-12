"""Self-learning agent for the Azure Pricing Calculator.

For every product in the picker it:
  1. adds the product to the estimate,
  2. watches the page with a MutationObserver until the new module's DOM settles,
  3. extracts every form control (selects, inputs, radios, checkboxes,
     collapsible toggles) with a robust selector scoped to the module,
  4. expands each collapsible section and diffs the control list to learn
     which fields are revealed by which toggle,
  5. deletes the module and persists the learned schema to schemas/<slug>.json.

The output schemas are consumed by engine.py to build estimates for ANY
product from a plain JSON config.
"""
import json
import re
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)

from .js_snippets import (
    DISCOVER_PRODUCTS_JS,
    EXTRACT_FIELDS_JS,
    FIND_NEW_MODULE_JS,
    INSTALL_OBSERVER_JS,
    MARK_SERVICES_JS,
    READ_OBSERVER_JS,
)

CALCULATOR_URL = "https://azure.microsoft.com/en-us/pricing/calculator/"
MODULES_CSS = "div.wa-calcService[data-testid] > div[id]"
PRODUCT_SEARCH_CSS = (
    "input.product-search, .product-search input, "
    "input[class*='product-search'], input[aria-label*='earch']"
)
SCHEMA_VERSION = 2


def slugify(testid: str) -> str:
    """Filesystem-safe slug (some testids contain backslashes, e.g.
    'storage\\files-picker-item')."""
    slug = re.sub(r"-picker-item$", "", testid)
    return re.sub(r"[\\/]+", "--", slug)


def css_attr(value: str) -> str:
    """Escape a value for use inside a CSS attribute selector string."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


class SchemaLearner:
    def __init__(self, driver, schema_dir="schemas", settle_ms=700, settle_timeout=12):
        self.driver = driver
        self.schema_dir = Path(schema_dir)
        self.schema_dir.mkdir(parents=True, exist_ok=True)
        self.settle_ms = settle_ms
        self.settle_timeout = settle_timeout
        self.wait = WebDriverWait(driver, 15)

    # ------------------------------------------------------------------
    # Page-level helpers
    # ------------------------------------------------------------------
    def open_calculator(self):
        self.driver.get(CALCULATOR_URL)
        self.wait.until(lambda d: d.execute_script(
            "return document.querySelectorAll(\"button[data-testid$='-picker-item']\").length > 0"
        ))
        self._dismiss_banners()

    def _dismiss_banners(self):
        for sel in ["#onetrust-accept-btn-handler", "button[aria-label='Close']"]:
            try:
                btn = self.driver.find_element(By.CSS_SELECTOR, sel)
                if btn.is_displayed():
                    btn.click()
                    time.sleep(0.3)
            except Exception:
                pass

    def watch(self, element=None, watch_id="default"):
        """Install a MutationObserver on `element` (or body)."""
        self.driver.execute_script(INSTALL_OBSERVER_JS, element, watch_id)

    def wait_settled(self, watch_id="default", timeout=None):
        """Block until the watched DOM has been quiet for `settle_ms`."""
        timeout = timeout or self.settle_timeout
        deadline = time.time() + timeout
        while time.time() < deadline:
            state = self.driver.execute_script(READ_OBSERVER_JS, watch_id)
            if state is None or state["msSinceLast"] >= self.settle_ms:
                return True
            time.sleep(0.15)
        return False  # never settled; caller proceeds with what is there

    # ------------------------------------------------------------------
    # Product discovery
    # ------------------------------------------------------------------
    def discover_products(self):
        """Enumerate every product available in the picker.

        Clicks through every category tab/section so lazy-rendered picker
        buttons get mounted, then collects the union.
        """
        self.watch(None, "discover")
        seen = {}

        def harvest():
            for p in self.driver.execute_script(DISCOVER_PRODUCTS_JS):
                if p["picker_testid"] not in seen and p["name"]:
                    seen[p["picker_testid"]] = p

        harvest()

        # Click every category/tab control we can find to force-render all lists
        cat_selectors = [
            "[role='tablist'] [role='tab']",
            "button[data-testid$='-category-item']",
            ".categories button, .category-list button, nav.categories a",
        ]
        for sel in cat_selectors:
            try:
                tabs = self.driver.find_elements(By.CSS_SELECTOR, sel)
            except Exception:
                continue
            for i in range(len(tabs)):
                try:
                    tabs = self.driver.find_elements(By.CSS_SELECTOR, sel)
                    tab = tabs[i]
                    if not tab.is_displayed():
                        continue
                    self.driver.execute_script("arguments[0].click();", tab)
                    self.wait_settled("discover", timeout=4)
                    harvest()
                except (StaleElementReferenceException, IndexError):
                    continue
            if seen:
                break  # first selector family that worked is enough

        products = sorted(seen.values(), key=lambda p: p["name"].lower())
        return products

    # ------------------------------------------------------------------
    # Module helpers
    # ------------------------------------------------------------------
    def _module_ids(self):
        return {
            el.get_attribute("id")
            for el in self.driver.find_elements(By.CSS_SELECTOR, MODULES_CSS)
        }

    def _visible_search_box(self):
        return next(
            (s for s in self.driver.find_elements(By.CSS_SELECTOR, PRODUCT_SEARCH_CSS)
             if s.is_displayed()),
            None,
        )

    def _reveal_picker(self, selector, product_name):
        """Try to get the picker button mounted: search by name, then by
        name tokens, then iterate every category tab (the discovered name may
        not match the real card title, e.g. 'Redis Cache' vs
        'Azure Cache for Redis')."""
        search = self._visible_search_box()
        if search is not None:
            queries = [product_name]
            # individual informative words, longest first
            words = [w for w in re.split(r"\W+", product_name)
                     if len(w) > 3 and w.lower() not in ("azure", "service", "services")]
            queries += sorted(words, key=len, reverse=True)
            # prefix probe helps when the discovered name is a slug mash-up,
            # e.g. 'Githubenterprise' vs the real card 'GitHub Enterprise'
            if len(product_name) > 8:
                queries.append(product_name[:6])
            for q in queries:
                try:
                    search.clear()
                    search.send_keys(q)
                    time.sleep(1.0)
                    btns = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if btns:
                        return btns[0]
                except Exception:
                    pass
            try:
                search.clear()
            except Exception:
                pass

        # last resort: click through every category tab until the button mounts
        for sel in [
            "[role='tablist'] [role='tab']",
            "button[data-testid$='-category-item']",
            ".categories button, .category-list button, nav.categories a",
        ]:
            try:
                n = len(self.driver.find_elements(By.CSS_SELECTOR, sel))
            except Exception:
                continue
            for i in range(n):
                try:
                    tabs = self.driver.find_elements(By.CSS_SELECTOR, sel)
                    if i >= len(tabs) or not tabs[i].is_displayed():
                        continue
                    self.driver.execute_script("arguments[0].click();", tabs[i])
                    time.sleep(0.5)
                    btns = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if btns:
                        return btns[0]
                except StaleElementReferenceException:
                    continue
            if n:
                break
        return None

    def _click_picker(self, picker_testid, product_name):
        """Click the picker button, falling back to search / category tabs."""
        selector = f'button[data-testid="{css_attr(picker_testid)}"]'
        # a leftover search filter from a previous product hides everything
        search = self._visible_search_box()
        if search is not None and search.get_attribute("value"):
            try:
                search.clear()
                time.sleep(0.5)
            except Exception:
                pass

        # The picker panel re-renders aggressively (buttons unmount between a
        # find and a click), so each attempt gets a fresh handle and falls
        # back to re-surfacing the button via search / category tabs.
        last = None
        for attempt in range(4):
            btn = None
            try:
                btn = self.driver.find_element(By.CSS_SELECTOR, selector)
                if not btn.is_displayed() and attempt == 0:
                    btn = self._reveal_picker(selector, product_name) or btn
            except Exception:
                btn = self._reveal_picker(selector, product_name)
            if btn is None:
                last = TimeoutException(
                    f"Picker button not found for {product_name} ({picker_testid})"
                )
                continue
            try:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", btn
                )
                try:
                    if btn.is_displayed():
                        btn.click()
                    else:
                        # JS click still dispatches React handlers on hidden buttons
                        self.driver.execute_script("arguments[0].click();", btn)
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", btn)
                return
            except StaleElementReferenceException as e:
                last = e
                time.sleep(0.5)
        raise last or TimeoutException(f"Could not click picker for {product_name}")

    def mark_existing_modules(self):
        """Tag current service wrappers so the next one added is identifiable."""
        self.driver.execute_script(MARK_SERVICES_JS)

    def wait_new_module(self, timeout=15):
        """Return the form-root id of the module added since the last mark.

        Detection is element-based (not id-diff based) because some products
        have backslashes in their ids or no id at all — in that case a
        synthetic id is assigned in the page.
        """
        deadline = time.time() + timeout
        while time.time() < deadline:
            module_id = self.driver.execute_script(FIND_NEW_MODULE_JS)
            if module_id:
                return module_id
            time.sleep(0.3)
        # distinguish "nothing happened" from "module rendered broken"
        broken = self.driver.execute_script(
            "const s = document.querySelector("
            "'div.wa-calcService:not([data-azlearn-seen])');"
            "return s ? s.textContent.trim().slice(0, 200) : null;"
        )
        if broken and "error" in broken.lower():
            raise TimeoutException(
                "Calculator failed to render this product's form "
                f"(page shows an error): {broken[:120]}"
            )
        raise TimeoutException("New module did not appear after adding product")

    def _module_root(self, module_id):
        # By.ID breaks on ids containing backslashes (e.g. storage\files...)
        return self.driver.find_element(
            By.CSS_SELECTOR, f'[id="{css_attr(module_id)}"]'
        )

    def _service_root(self, module_id):
        """The wa-calcService wrapper (summary + layout) for delete/testid."""
        el = self._module_root(module_id)
        if "wa-calcService" in (el.get_attribute("class") or ""):
            return el
        return el.find_element(
            By.XPATH, "./ancestor-or-self::div[contains(@class,'wa-calcService')]"
        )

    def extract_fields(self, root):
        return self.driver.execute_script(EXTRACT_FIELDS_JS, root)

    # ------------------------------------------------------------------
    # Learning one product
    # ------------------------------------------------------------------
    def learn_product(self, product, explore_toggles=True, interact=True,
                      max_options=12, skip_sweep_names=("region", "destinationRegion")):
        """Add product, map every control, explore collapsibles, then *play*
        with the page: select every option of every driving dropdown, watch
        the DOM react in real time, and record how options / fields / selectors
        change per state. Finally delete the module.

        Returns the schema dict.
        """
        name, picker_testid = product["name"], product["picker_testid"]
        slug = slugify(picker_testid)
        self.mark_existing_modules()

        self._click_picker(picker_testid, name)
        module_id = self.wait_new_module()
        root = self._module_root(module_id)

        # watch this module so we know when its DOM is fully rendered
        self.watch(root, "module")
        self.wait_settled("module")

        fields = self.extract_fields(root)
        known = {f["signature"] for f in fields}
        for f in fields:
            f["revealed_by"] = None

        if explore_toggles:
            fields = self._explore_toggles(module_id, fields, known)

        if interact:
            fields = self._sweep_select_states(
                module_id, fields, max_options=max_options,
                skip_names=set(skip_sweep_names),
            )

        service = self._service_root(module_id)
        schema = {
            "schema_version": SCHEMA_VERSION,
            "product": name,
            "slug": slug,
            "picker_testid": picker_testid,
            "module_testid": service.get_attribute("data-testid"),
            "category": product.get("category"),
            "learned_at": datetime.now(timezone.utc).isoformat(),
            "fields": [f for f in fields if f["control"] != "button"],
            "toggles": [f for f in fields if f["control"] == "button"],
        }

        self._delete_module(module_id)
        return schema

    # ------------------------------------------------------------------
    # Interactive state sweep: the page is reactive — picking an option can
    # rewrite other dropdowns' options (S10 -> P10), add/remove fields, or
    # even change a control's name/selector. We try every option of every
    # driving select and record the observed differences.
    # ------------------------------------------------------------------
    def _sweep_select_states(self, module_id, fields, max_options, skip_names):
        drivers = [
            f for f in fields
            if f["control"] == "select"
            and f.get("selector") and f.get("options")
            and 2 <= len(f["options"]) <= max_options
            and (f.get("clean_name") or f.get("name") or "") not in skip_names
        ]
        for drv in drivers:
            drv_key = drv.get("clean_name") or drv.get("name") or drv.get("label")
            original = drv.get("value")
            print(f"        🎛  sweeping '{drv.get('label') or drv_key}' "
                  f"({len(drv['options'])} options)")

            # baseline re-extracted fresh per driver: previous sweeps/toggles
            # may have changed the page
            baseline = self._extract_settled(module_id)
            base_map = {f["signature"]: f for f in baseline if f["control"] != "button"}

            for opt in drv["options"]:
                if opt["value"] == original:
                    continue
                if not self._select_option(module_id, drv, opt["value"]):
                    continue
                after = self._extract_settled(module_id)
                when = {"field": drv_key, "value": opt["value"], "text": opt["text"]}
                self._merge_state_diff(fields, base_map, after, when, drv_key)

            # restore the original state for the next driver
            if original is not None:
                self._select_option(module_id, drv, original)
                self._extract_settled(module_id)
        return fields

    def _extract_settled(self, module_id):
        root = self._module_root(module_id)
        self.watch(root, "module")
        self.wait_settled("module", timeout=6)
        return self.extract_fields(self._module_root(module_id))

    def _select_option(self, module_id, field, value):
        from selenium.webdriver.support.ui import Select
        for _ in range(3):
            try:
                root = self._module_root(module_id)
                elem = root.find_element(By.CSS_SELECTOR, field["selector"])
                Select(elem).select_by_value(value)
                return True
            except StaleElementReferenceException:
                time.sleep(0.4)
            except Exception:
                return False
        return False

    def _merge_state_diff(self, fields, base_map, after, when, drv_key):
        """Fold one observed page state into the schema fields."""
        field_by_sig = {f["signature"]: f for f in fields if f["control"] != "button"}
        after_map = {f["signature"]: f for f in after if f["control"] != "button"}

        def opt_texts(f):
            return [o["text"] for o in (f.get("options") or [])]

        def add_dep(f):
            deps = f.setdefault("depends_on", [])
            if drv_key not in deps:
                deps.append(drv_key)

        # 1. existing fields whose options changed in this state
        for sig, now in after_map.items():
            base = base_map.get(sig)
            if base is not None:
                schema_f = field_by_sig.get(sig)
                if schema_f is None:
                    continue
                if now.get("options") is not None and opt_texts(now) != opt_texts(base):
                    variants = schema_f.setdefault("option_variants", [])
                    variants.append({"when": when, "options": now["options"]})
                    add_dep(schema_f)
                continue

            # 2. field not present in baseline: either truly new in this
            #    state, or an existing field whose name/selector changed
            absent_twins = [
                f for f in field_by_sig.values()
                if f["signature"] not in after_map
                and f.get("label") == now.get("label")
                and f["control"] == now["control"]
            ]
            if absent_twins:
                twin = absent_twins[0]
                variants = twin.setdefault("selector_variants", [])
                variants.append({
                    "when": when,
                    "selector": now.get("selector"),
                    "name": now.get("name"),
                    "options": now.get("options"),
                })
                add_dep(twin)
                continue

            # truly new field for this state
            existing_new = next(
                (f for f in fields if f["signature"] == sig), None
            )
            if existing_new is not None:
                conds = existing_new.setdefault("present_when", [])
                if when not in conds:
                    conds.append(when)
            else:
                now["revealed_by"] = None
                now["present_when"] = [when]
                now["depends_on"] = [drv_key]
                fields.append(now)
                field_by_sig[sig] = now

        # 3. baseline fields missing in this state
        for sig, base in base_map.items():
            if sig not in after_map:
                schema_f = field_by_sig.get(sig)
                if schema_f is None or schema_f.get("selector_variants"):
                    continue
                conds = schema_f.setdefault("absent_when", [])
                if when not in conds:
                    conds.append(when)
                add_dep(schema_f)

    def _explore_toggles(self, module_id, fields, known):
        """Click each collapsed section button; diff DOM to find revealed fields.

        This is the real-time part: after each click we let the
        MutationObserver tell us when the page stopped changing, then
        re-extract and diff by control signature.
        """
        # iterate over snapshot of toggle texts; re-find elements each time
        # (toggle buttons have no name/aria-label, so we locate them by text)
        toggles = [
            f for f in fields
            if f["control"] == "button" and f.get("aria_expanded") == "false"
            and (f.get("text") or f.get("label"))
        ]
        for t in toggles:
            toggle_label = t.get("text") or t.get("label")
            try:
                root = self._module_root(module_id)
                btn = self._find_toggle(root, t)
                if btn is None or btn.get_attribute("aria-expanded") != "false":
                    continue
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", btn
                )
                self.driver.execute_script("arguments[0].click();", btn)

                self.watch(root, "module")
                self.wait_settled("module", timeout=6)

                after = self.extract_fields(self._module_root(module_id))
                for f in after:
                    if f["signature"] not in known:
                        f["revealed_by"] = toggle_label
                        known.add(f["signature"])
                        fields.append(f)
            except (StaleElementReferenceException, TimeoutException):
                continue
            except Exception:
                traceback.print_exc()
                continue
        return fields

    def _find_toggle(self, root, toggle):
        """Locate a collapsible button by its (cleaned) visible text."""
        text = (toggle.get("text") or toggle.get("label") or "").strip()
        if not text:
            return None
        # XPath: collapsible button whose text starts with the recorded text
        safe = text.replace('"', "")
        xpath = (
            ".//button[(contains(@class,'collapsible') or @aria-expanded)"
            f" and starts-with(normalize-space(.), \"{safe[:40]}\")]"
        )
        try:
            matches = root.find_elements(By.XPATH, xpath)
            return matches[0] if matches else None
        except Exception:
            return None

    def _delete_module(self, module_id):
        try:
            service = self._service_root(module_id)
            btn = service.find_element(
                By.CSS_SELECTOR, "button.calculator-button.delete, button[title='Delete']"
            )
            self.driver.execute_script("arguments[0].click();", btn)
            WebDriverWait(self.driver, 8).until(
                lambda d: not d.find_elements(
                    By.CSS_SELECTOR, f'[id="{css_attr(module_id)}"]'
                )
            )
        except Exception:
            # last resort: page reload keeps the crawl going
            self.open_calculator()

    # ------------------------------------------------------------------
    # Crawl loop with persistence / resume
    # ------------------------------------------------------------------
    def schema_path(self, slug):
        return self.schema_dir / f"{slug}.json"

    def save_schema(self, schema):
        path = self.schema_path(schema["slug"])
        path.write_text(json.dumps(schema, indent=2), encoding="utf-8")
        self._update_index(schema)
        return path

    def _update_index(self, schema):
        index_path = self.schema_dir / "index.json"
        index = {}
        if index_path.exists():
            index = json.loads(index_path.read_text(encoding="utf-8"))
        index[schema["slug"]] = {
            "product": schema["product"],
            "picker_testid": schema["picker_testid"],
            "module_testid": schema["module_testid"],
            "category": schema.get("category"),
            "file": f"{schema['slug']}.json",
            "n_fields": len(schema["fields"]),
            "learned_at": schema["learned_at"],
        }
        index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")

    def learn_all(self, products=None, only=None, force=False, max_products=None,
                  interact=True, max_options=12):
        """Crawl the picker and learn schemas for every product.

        only: optional list of product names (case-insensitive substring match)
        force: re-learn even if a schema file already exists
        """
        self.open_calculator()
        catalog = products or self.discover_products()
        if only:
            wanted = [o.lower() for o in only]
            catalog = [
                p for p in catalog
                if any(w in p["name"].lower() for w in wanted)
            ]
        if max_products:
            catalog = catalog[:max_products]

        print(f"📚 {len(catalog)} products to learn")
        results, failures = [], []
        for i, product in enumerate(catalog, 1):
            slug = slugify(product["picker_testid"])
            if not force and self.schema_path(slug).exists():
                print(f"[{i}/{len(catalog)}] ⏭  {product['name']} (already learned)")
                continue
            print(f"[{i}/{len(catalog)}] 🔍 Learning {product['name']} ...")
            last_err = None
            for attempt in range(1, 3):
                try:
                    schema = self.learn_product(
                        product, interact=interact, max_options=max_options
                    )
                    path = self.save_schema(schema)
                    n_revealed = sum(1 for f in schema["fields"] if f.get("revealed_by"))
                    print(
                        f"            ✅ {len(schema['fields'])} fields "
                        f"({n_revealed} behind toggles) → {path.name}"
                    )
                    results.append(slug)
                    last_err = None
                    break
                except Exception as e:
                    last_err = e
                    print(f"            ⚠️  attempt {attempt} failed: {str(e)[:120]}")
                    # recover the page before retrying / moving on
                    try:
                        self.open_calculator()
                    except Exception:
                        pass
            if last_err is not None:
                print(f"            ❌ {product['name']}: {str(last_err)[:160]}")
                failures.append(
                    {"product": product["name"], "error": str(last_err)[:300]}
                )

        if failures:
            fail_path = self.schema_dir / "_failures.json"
            fail_path.write_text(json.dumps(failures, indent=2), encoding="utf-8")
            print(f"⚠️  {len(failures)} failures written to {fail_path}")
        print(f"🏁 Done. {len(results)} new schemas in {self.schema_dir}/")
        return results, failures
