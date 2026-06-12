# Future: AI Quotation Agent on top of v2

Roadmap and design notes for turning the v2 self-learning calculator into an
AI-driven "Microsoft recommendation expert" that chats with users, picks the
right Azure services/VMs, and returns accurate quotations (xlsx).

Status: **planning only** — nothing here is built yet. Prerequisite chores:
clean up repo, move v2 into its own GitHub repository, commit.

---

## 1. Concepts (plain-language reference)

### What an AI agent is
A chat model + a list of functions it may ask us to run + a while-loop.
The model can't execute anything; it replies "call `validate_config` with
{...}", our Python runs the real function, pastes the result back into the
conversation, and the model continues. All "agent" behavior is this loop:

```python
while True:
    reply = model.chat(messages, tools=[...])
    if reply.wants_tool_call:
        result = run_my_function(reply.tool_name, reply.arguments)  # our code
        messages.append(result)
    else:
        return reply.text
```

The intelligence = model choosing which tool, when, with what arguments.
The actual work (sizing, validation, Selenium, pricing) stays deterministic
in our code. **v2 already provides most of the tools.**

### What MCP is
A standard plug format (think USB-C) for exposing tools so existing chat
apps (Claude Desktop / Claude Code / VS Code) can use them with zero UI work.
It is an optional adapter, NOT a requirement: our own Azure-hosted chat
backend calls the same tool functions directly. Useful as a 1-day add-on for
internal/dev chat while iterating.

### Key design rule (accuracy guardrail)
The LLM never computes prices. It selects services and authors configs;
numbers come from the Azure Retail Prices API (instant ballpark in chat) or
the calculator build (the official quotation xlsx).

### Small/local model reality check
- "Local = cheaper" is usually FALSE on Azure at presales volume: GPU VM
  ≈ $400–1,500+/mo always-on, vs pay-per-token small hosted models
  (Haiku-class / Azure AI Foundry serverless) ≈ dollars/month for tens of
  chats/day.
- Small models (e.g. llama3.2 3B used in csv_to_assessment.py) are weak at
  multi-step tool orchestration and strict JSON.
- Mitigation lever: **the smarter the tools, the dumber the model can be.**
  Deterministic sizing engine + precise validator errors mean a mid-tier
  model only routes and rephrases.
- Hedge: model adapter layer (LiteLLM or a thin wrapper) so provider is a
  config switch — Claude / Azure OpenAI / Ollama, never married to one.

---

## 2. Target architecture

```
┌─ Intake ────────────────────────────────────────────────┐
│  Chat web UI (Azure)  |  Claude Code via MCP (dev)      │
│  Assessment upload (Azure Migrate xlsx / CSV)           │
│  n8n (Phase 4 only): email / Teams / CRM ──► REST       │
└──────────────────────┬──────────────────────────────────┘
┌─ Agent service (Python, LLM tool-calling loop) ─────────┐
│  Tools:                                                 │
│   1. search_catalog(query)        ← catalog/catalog.json│
│   2. get_service_doc(slug)        ← catalog/services/   │
│   3. recommend_vm(vcpu, ram, …)   ← NEW sizing engine   │
│   4. quick_price(sku, region, …)  ← Azure Retail Prices │
│   5. validate_config(json)        ← validate.py         │
│   6. build_estimate(json)         ← build.py (queued)   │
│   7. search_docs(question)        ← NEW RAG over MS docs│
│   8. parse_assessment(file)       ← existing extractors │
└──────────────────────┬──────────────────────────────────┘
┌─ Workers ───────────────────────────────────────────────┐
│  Selenium build queue (headless Chrome container/VM)    │
│  Output: <estimate_name>.xlsx → blob storage + summary  │
└─────────────────────────────────────────────────────────┘
```

Azure deployment shape:
1. **Chat frontend** — simple web page (Teams bot later); dumb relay.
2. **Agent service** — small Python web app (App Service / Container App):
   the loop, system prompt (Microsoft expert persona + Cloud Catalyst house
   rules), tool functions importing v2 code.
3. **Build worker** — needs real Chrome → own container/small VM + job
   queue; builds run async ("your quotation is being generated").
4. **Model** — swappable via adapter; start hosted, revisit only if token
   bills justify self-hosting.

### Agent conversation loop
1. Gather requirements (chat or parsed assessment) → workload profile
   (vCPU/RAM/storage/OS/region/HA/DR/budget posture).
2. Recommend: sizing engine picks SKUs deterministically; LLM explains
   rationale + 1–2 alternatives.
3. Quick ballpark via Retail Prices API → user confirms direction.
4. Author estimate config → `validate_config` → auto-fix loop
   (absent_when/present_when errors feed straight back to the model).
5. Queue `build_estimate` → return xlsx + summary table.

---

## 3. Knowledge layer (Microsoft docs collection plan)

Priority order — first two are STRUCTURED DATA, not RAG:

1. **VM size dataset**: every SKU with vCPU, RAM, family purpose,
   premium-disk support, temp storage. Source: Azure Retail Prices API
   (free, no auth, live prices per region) joined with VM sizes docs.
   Learned schemas hold per-region instance lists as a cross-check.
   → makes `recommend_vm` deterministic and defensible.
2. **Decision guides** (~20 short curated rule docs): Azure Architecture
   Center compute/storage/database decision trees + SKU family guidance +
   **Cloud Catalyst house rules** (default series, prod = Premium SSD,
   when to quote 3-yr RI vs savings plan). House rules are the
   differentiation.
3. **General docs corpus (RAG)**: service overviews, limits, region
   availability. Local vector store (Chroma/LanceDB) is fine at this scale.

---

## 4. Phased roadmap

- **Phase 0 (manual, in progress)**: repo cleanup; move v2 out of the old
  automation code into its own GitHub repo; commit.
- **Phase 1 — tool layer + MCP (fastest win)**: plain Python functions for
  tools 1, 2, 5, 6 + thin MCP server so the agent can be driven from
  Claude Code immediately. No UI, no infra. Proves the whole concept.
- **Phase 2 — knowledge layer**: Retail Prices ingester, VM size table,
  `recommend_vm` sizing function, curated decision rules, RAG store.
- **Phase 3 — assessment intake + persona**: wire existing xlsx/CSV
  extractors as a tool; system prompt with expert persona + house rules;
  **golden-set tests** (5–10 past real quotes — does the agent reproduce
  them?). Use golden set to test cheaper models before downgrading.
- **Phase 4 — productize on Azure**: REST API + build queue + chat web UI;
  n8n only here, for channel plumbing (email/Teams/CRM intake, delivery).

### Commit now / defer / avoid
- **Commit**: tools-first Python agent service; model adapter layer;
  intelligence pushed into deterministic tools.
- **Defer**: final model choice (config switch + golden-set comparison);
  MCP (optional); n8n/Teams/CRM (Phase 4).
- **Avoid**: GPU VM for self-hosted models until volume proves it.

### n8n verdict
Not for the agent's brain (weak at reasoning loops / validation retries).
Only as outer plumbing in Phase 4, or earlier if n8n is already running for
other Cloud Catalyst workflows.

---

## 5. Open decisions

| Decision | Default | Revisit when |
|---|---|---|
| Model | Hosted, capable first (prove flow), then test downgrade | Golden-set pass rate of cheaper model |
| Self-host LLM | No | Token costs > GPU VM cost, or data-residency requirement |
| MCP server | Yes, Phase 1 (dev convenience) | Skip if going straight to web UI |
| n8n | Phase 4 only | Already-running n8n instance exists |
| Official quote source | Calculator build xlsx only | Never — auditable against MS's own tool |
