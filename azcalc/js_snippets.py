"""JavaScript injected into the calculator page.

Two responsibilities:
1. Watch the page in real time with a MutationObserver so Python can wait
   until the DOM settles after any interaction (adding a product, expanding
   a collapsible section, ...).
2. Walk a component's DOM and extract every form control together with a
   robust CSS selector that is unique *within that component*, so the result
   can be persisted to a JSON schema and replayed later.
"""

# ---------------------------------------------------------------------------
# MutationObserver: window.__azWatch tracks mutation activity per watch-id.
# Python polls `mutations` and considers the DOM settled when the counter
# stops moving.
# ---------------------------------------------------------------------------
INSTALL_OBSERVER_JS = r"""
const root = arguments[0] || document.body;
const watchId = arguments[1] || 'default';
window.__azWatch = window.__azWatch || {};
if (window.__azWatch[watchId] && window.__azWatch[watchId].observer) {
    window.__azWatch[watchId].observer.disconnect();
}
const state = { mutations: 0, last: Date.now(), observer: null };
state.observer = new MutationObserver((muts) => {
    state.mutations += muts.length;
    state.last = Date.now();
});
state.observer.observe(root, {
    childList: true, subtree: true, attributes: true,
    attributeFilter: ['aria-expanded', 'class', 'style', 'disabled', 'hidden']
});
window.__azWatch[watchId] = state;
return true;
"""

READ_OBSERVER_JS = r"""
const watchId = arguments[0] || 'default';
const s = (window.__azWatch || {})[watchId];
if (!s) return null;
return { mutations: s.mutations, msSinceLast: Date.now() - s.last };
"""

# ---------------------------------------------------------------------------
# Field extraction. arguments[0] = component root element.
# Returns a list of control descriptors (JSON-safe dicts).
# ---------------------------------------------------------------------------
EXTRACT_FIELDS_JS = r"""
const root = arguments[0];
const esc = (s) => (window.CSS && CSS.escape) ? CSS.escape(s) : s.replace(/(["\\])/g, '\\$1');

function visible(el) {
    if (!el) return false;
    const st = window.getComputedStyle(el);
    if (st.display === 'none' || st.visibility === 'hidden') return false;
    const r = el.getBoundingClientRect();
    return (r.width > 0 && r.height > 0);
}

const UUID_RE = /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ig;

function cleanText(s) {
    if (!s) return s;
    return s.replace(/More info[\s\S]*$/i, '')
            .replace(/\$[\d,.]+\s*$/, '')
            .replace(/:\s*$/, '')
            .replace(/\s+/g, ' ')
            .trim();
}

function labelFor(el) {
    // 1. aria-label
    const aria = el.getAttribute('aria-label');
    if (aria && aria.trim()) return aria.trim();
    // 2. <label for=...>
    if (el.id) {
        const lab = root.querySelector(`label[for="${esc(el.id)}"]`) ||
                    document.querySelector(`label[for="${esc(el.id)}"]`);
        if (lab && lab.textContent.trim()) return lab.textContent.replace(/:\s*$/, '').trim();
    }
    // 3. label keyed by name (the calculator uses <label for="<name>">)
    const nm = el.getAttribute('name');
    if (nm) {
        const lab = el.closest('div')?.parentElement?.querySelector(`label[for="${esc(nm)}"]`) ||
                    el.closest('.calculator-dropdown, .calculator-input, .column')?.querySelector('label');
        if (lab && lab.textContent.trim()) return lab.textContent.replace(/:\s*$/, '').trim();
    }
    // 4. closest wrapping label
    const wrap = el.closest('label');
    if (wrap && wrap.textContent.trim()) return wrap.textContent.replace(/:\s*$/, '').trim();
    // 5. placeholder
    const ph = el.getAttribute('placeholder');
    if (ph) return ph.trim();
    return null;
}

function candidateSelectors(el) {
    const tag = el.tagName.toLowerCase();
    const cands = [];
    const attrs = ['data-testid', 'name', 'aria-label', 'data-name-override', 'placeholder'];
    const parts = {};
    for (const a of attrs) {
        const v = el.getAttribute(a);
        // attribute values containing per-instance UUIDs do not replay on a
        // freshly added module – never bake them into selectors
        if (v && !UUID_RE.test(v)) parts[a] = `[${a}="${esc(v)}"]`;
        UUID_RE.lastIndex = 0;
    }
    const type = el.getAttribute('type');
    const typeSel = (tag === 'input' && type) ? `[type="${esc(type)}"]` : '';
    const valSel = ((type === 'radio' || type === 'checkbox') && el.getAttribute('value'))
        ? `[value="${esc(el.getAttribute('value'))}"]` : '';

    if (parts['data-testid']) cands.push(tag + parts['data-testid']);
    if (parts['data-name-override']) cands.push(tag + parts['data-name-override'] + valSel);
    if (parts['name'] && parts['aria-label']) cands.push(tag + parts['aria-label'] + parts['name'] + valSel);
    if (parts['aria-label']) cands.push(tag + parts['aria-label'] + valSel);
    if (parts['name']) cands.push(tag + parts['name'] + typeSel + valSel);
    if (el.id && !/\d{4,}|[0-9a-f]{8}-/.test(el.id)) cands.push(`#${esc(el.id)}`);
    if (parts['placeholder']) cands.push(tag + parts['placeholder']);
    return cands;
}

function uniqueSelector(el) {
    for (const sel of candidateSelectors(el)) {
        try {
            const found = root.querySelectorAll(sel);
            if (found.length === 1 && found[0] === el) return { selector: sel, unique: true };
        } catch (e) { /* invalid selector, skip */ }
    }
    // fall back to first candidate (still useful, engine scopes to module root)
    const c = candidateSelectors(el);
    if (c.length) return { selector: c[0], unique: false };
    return { selector: null, unique: false };
}

function describe(el) {
    const tag = el.tagName.toLowerCase();
    const rawName = el.getAttribute('name') || null;
    // strip per-instance UUIDs so the name is stable across modules
    // e.g. 'radioButton-6f80...-computeBillingOption' -> 'computeBillingOption'
    let cleanName = rawName;
    if (rawName) {
        cleanName = rawName.replace(UUID_RE, '').replace(/^radioButton-?/i, '')
                           .replace(/--+/g, '-').replace(/^-|-$/g, '') || rawName;
        UUID_RE.lastIndex = 0;
    }
    const d = {
        tag: tag,
        control: tag,
        type: el.getAttribute('type') || null,
        name: rawName,
        clean_name: cleanName,
        id: el.id || null,
        aria_label: el.getAttribute('aria-label') || null,
        data_testid: el.getAttribute('data-testid') || null,
        data_name_override: el.getAttribute('data-name-override') || null,
        placeholder: el.getAttribute('placeholder') || null,
        label: cleanText(labelFor(el)),
        value: null,
        options: null,
        visible: visible(el),
    };
    const u = uniqueSelector(el);
    d.selector = u.selector;
    d.selector_unique = u.unique;

    if (tag === 'select') {
        d.control = 'select';
        d.options = Array.from(el.options).map(o => ({
            value: o.value, text: o.textContent.trim(),
            group: o.closest('optgroup') ? o.closest('optgroup').label : null
        }));
        d.value = el.value;
    } else if (tag === 'input') {
        const t = (el.getAttribute('type') || 'text').toLowerCase();
        if (t === 'radio') d.control = 'radio';
        else if (t === 'checkbox') d.control = 'checkbox';
        else if (t === 'number') d.control = 'number';
        else d.control = 'text';
        d.value = (t === 'radio' || t === 'checkbox') ? String(el.checked) : el.value;
        if (t === 'radio') d.radio_value = el.getAttribute('value');
    } else if (tag === 'textarea') {
        d.control = 'text';
        d.value = el.value;
    } else if (tag === 'button') {
        d.control = 'button';
        d.text = cleanText(el.textContent) || null;
        d.label = d.label ? cleanText(d.label) : d.text;
        d.aria_expanded = el.getAttribute('aria-expanded');
        d.classes = el.className || null;
    }
    // signature: stable identity for diffing before/after a toggle click
    d.signature = [d.tag, d.type, d.clean_name, d.aria_label, d.data_name_override,
                   d.radio_value || '', d.placeholder, d.text || ''].join('|');
    return d;
}

const controls = [];
root.querySelectorAll('input, select, textarea, button').forEach(el => {
    if ((el.getAttribute('type') || '').toLowerCase() === 'hidden') return;
    // skip the module chrome buttons (clone/delete/info) – keep collapsibles
    if (el.tagName === 'BUTTON') {
        const cls = el.className || '';
        const isCollapsible = cls.includes('collapsible') || el.hasAttribute('aria-expanded');
        if (!isCollapsible) return;
    }
    controls.push(describe(el));
});
return controls;
"""

# ---------------------------------------------------------------------------
# New-module detection. IDs are unreliable (some contain backslashes, some
# inner divs have no id at all), so instead we mark every existing service
# wrapper before clicking the picker and afterwards look for the unmarked one,
# assigning it a synthetic id if needed.
# ---------------------------------------------------------------------------
MARK_SERVICES_JS = r"""
document.querySelectorAll('div.wa-calcService')
        .forEach(e => e.setAttribute('data-azlearn-seen', '1'));
return true;
"""

FIND_NEW_MODULE_JS = r"""
const svcs = Array.from(
    document.querySelectorAll('div.wa-calcService:not([data-azlearn-seen])'));
if (!svcs.length) return null;
const svc = svcs[svcs.length - 1];
let root = svc.querySelector("div[id$='-layout']");
if (!root) {
    root = Array.from(svc.querySelectorAll('div[id]'))
                .find(d => d.querySelector('select, input')) || null;
}
if (!root) root = svc.querySelector('div.product-module') || svc;
if (!root.querySelector('select, input, textarea')) return null;  // not rendered yet
if (!root.id) root.id = 'azlearn-' + Math.random().toString(36).slice(2, 10);
return root.id;
"""

# Returns [{name, picker_testid, category}] for every product visible in the picker.
DISCOVER_PRODUCTS_JS = r"""
const out = [];

function fromSlug(testid) {
    return testid
        .replace(/-picker-item$/, '')
        .split(/[\\/]/).pop()
        .split('-')
        .map(w => w ? w[0].toUpperCase() + w.slice(1) : w)
        .join(' ');
}

function productName(btn) {
    // The card heading lives in an ancestor of the picker button
    // (the button itself is just "Add to estimate").
    let scope = btn;
    for (let i = 0; i < 6 && scope; i++) {
        scope = scope.parentElement;
        if (!scope) break;
        const h = scope.querySelector('h2, h3, h4, .service-name, [class*="product-name"], [class*="serviceName"]');
        if (h) {
            const t = h.textContent.trim();
            if (t && !/^(add|products?)$/i.test(t) && t.length < 90) return t;
        }
    }
    let name = (btn.getAttribute('aria-label') || btn.textContent || '').trim();
    name = name.replace(/^Add\s+/i, '').replace(/\s*to estimate\s*$/i, '').trim();
    if (name && !/^to estimate$/i.test(name)) return name;
    return fromSlug(btn.getAttribute('data-testid'));
}

document.querySelectorAll("button[data-testid$='-picker-item']").forEach(btn => {
    const testid = btn.getAttribute('data-testid');
    let category = null;
    const catEl = btn.closest('[data-testid$="-category"], .product-category');
    if (catEl) {
        const h = catEl.querySelector('h2, h3, .category-name');
        if (h) category = h.textContent.trim();
    }
    out.push({ name: productName(btn), picker_testid: testid, category: category });
});
return out;
"""
