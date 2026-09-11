# 04 · Feature catalog

Status legend: ✅ done · 🔨 in progress · 📅 planned · 💡 vision

## Core (MVP for the hackathon demo)

### F1 · Consolidated Excel summary — 🔨
Auto-generate a multi-sheet Excel from RTLA outputs (per-module power, coverage, clock-gating, QoR).
- **Input:** RTLA report folder.
- **Output:** `summary.xlsx` with a dashboard sheet + per-domain sheets.
- **Differentiator:** deterministic aggregation; numbers are traceable to source rows.

### F2 · Milestone review PPTX — 🔨
Generate the milestone deck from a template: title, per-block metrics, trends, key observations, risks.
- **Output:** `milestone_review.pptx`.
- **Differentiator:** the "key observations" slide is AI-written from computed facts, cited.

### F3 · Key-observations writer — 🔨
Narrative summary of what matters this run (regressions, anomalies, wins).
- **Differentiator:** grounded — every observation links to data.

### F4 · Interactive analysis copilot — 🔨
Ask about power, performance, coverage, clock-gating in natural language; get cited answers.
- **Guardrail:** refuses to answer without supporting retrieved data.

## Signature differentiators (build ≥1 for the demo hero moment)

### F5 · Missing clock-gate detector — 📅 ⭐
Flags free-running clocks and points to `module:signal:file:line` with a suggested ICG.
- **Why it wins:** the agent *finds a real bug*, not just summarizes. This is the demo climax.

### F6 · Cross-run regression diff — 📅 ⭐
Ranked per-module deltas between two runs with an AI root-cause narrative.
- **Why it wins:** "power ↑3.2% in `<module_x>` driven by higher toggle activity" is a concrete, credible insight.

### F7 · Anomaly / outlier triage — 📅
Statistical outlier detection with confidence score + evidence rows.
- **Ties to Responsible AI:** confidence + evidence make it auditable.

## Roadmap features (state the vision, don't over-claim)

### F8 · QoR tracking over milestones — 💡
Living trend dashboard (power/perf/area/coverage) auto-updated per run.

### F9 · Testcase recommender — 💡
Coverage hole → recommended existing UVM tests / stimulus stub.

### F10 · Clock-gating effectiveness analysis — 💡
Quantify actual vs. potential gating savings per block.

### F11 · Traffic-based comparisons — 💡
Compare results across workloads/traffic profiles.

### F12 · Design-optimization guidance — 💡
Surface optimization opportunities (e.g., restructuring high-toggle logic).

---

## Feature status table (keep this current for judges)

| ID | Feature | Status | Demo priority |
|----|---------|--------|---------------|
| F1 | Excel summary | 🔨 | High |
| F2 | Milestone PPTX | 🔨 | High |
| F3 | Key-observations writer | 🔨 | High |
| F4 | Interactive copilot | 🔨 | High |
| F5 | Missing clock-gate detector | 📅 | **Hero** |
| F6 | Regression diff | 📅 | High |
| F7 | Anomaly triage | 📅 | Medium |
| F8–F12 | Vision features | 💡 | Narrative only |

> Be honest about status in the submission. Judges reward a working MVP + credible vision over an over-claimed everything.
