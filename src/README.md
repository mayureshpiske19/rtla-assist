# src — implementation skeleton

Proposed module layout for the MVP. Create these as you build.

```
src/
├─ ingest/          # schema-aware RTLA report parsers -> normalized metrics
│  ├─ parsers.py
│  └─ schema.py     # normalized metric record: module, metric, value, unit, run_id, source_location
├─ analysis/        # deterministic engine (no LLM) — unit tested
│  ├─ regression.py     # F6 cross-run diff
│  ├─ clockgate.py      # F5 missing clock-gate detector
│  ├─ anomaly.py        # F7 outlier triage
│  ├─ coverage.py       # coverage holes
│  └─ qor.py            # F8 QoR tracking
├─ ai/              # Azure OpenAI layer
│  ├─ retriever.py      # grounded retrieval + citations
│  ├─ narrator.py       # key-observations writer
│  └─ copilot.py        # interactive cited Q&A
├─ generate/        # output artifacts
│  ├─ excel.py         # openpyxl consolidated summary
│  ├─ pptx.py          # python-pptx milestone deck
│  └─ observations.py  # written review notes
├─ app/             # UI (Streamlit / web) — chat + QoR dashboard
│  └─ main.py
└─ config.py        # Azure OpenAI endpoint/deployment via env vars (never hardcode keys)
```

## Ground rules for the code
1. **Numbers come from `analysis/`, never from the LLM.** The `ai/` layer only explains computed facts.
2. Every insight object carries `source_location` + `confidence` (the auditability contract).
3. Secrets via environment variables only — see `.env.example`. Never commit keys.
4. `analysis/` modules are pure functions with unit tests — they must be trustworthy.

## Getting started (once code exists)
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
copy .env.example .env       # then fill in Azure OpenAI values
streamlit run src/app/main.py
```
