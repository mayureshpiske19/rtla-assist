# RTLA AI Assistant

**Automated Reporting Today, Intelligent Design Guidance Tomorrow.**

An AI-powered engineering copilot for silicon design teams that turns raw **RTL Analysis (RTLA)** outputs into consolidated reports, milestone review decks, and — most importantly — **actionable design insights**: missing clock-gate detection, cross-run regression diffs, anomaly triage, and testcase recommendations.

> Built for **Microsoft Global Hackathon 2026** · Challenges: *Reimagine the Future of Work* + *Hack for Responsible AI* · Stack: **Azure OpenAI**

---

## The problem

Every milestone, RTL designers and verification engineers spend **hours** manually:

- Consolidating dozens of RTLA report files into a single Excel summary.
- Hand-building milestone review PowerPoint decks.
- Eyeballing power, performance, coverage, and clock-gating numbers to spot regressions and anomalies.
- Cross-referencing results across runs to explain *what changed and why*.

This is repetitive, error-prone, and pulls senior engineers away from actually solving design problems.

## What RTLA AI Assistant does

| Stage | Capability | Value |
|-------|-----------|-------|
| **Today** | Auto-generate consolidated Excel summary + milestone PPTX + key-observations writeup from RTLA outputs | Hours → minutes per milestone |
| **Today** | Interactive Q&A over power / performance / coverage / clock-gating with **cited, grounded answers** | Trustworthy, no hallucinated numbers |
| **Next** | Cross-run regression diff with root-cause narrative | "Power ↑3.2% in `ciu_ctrl`, driven by X toggle activity" |
| **Next** | Missing clock-gate detection with **exact RTL line pointers** | Finds real bugs, not just summaries |
| **Vision** | Anomaly triage, testcase recommendation, QoR tracking, design-optimization guidance | A living design-intelligence platform |

## Why it's different

Most "AI assistants" are generic chat-over-documents. RTLA AI Assistant is **domain-native**:

1. **Schema-aware ingestion** of real RTLA report formats — not generic PDF chat.
2. **Deterministic numbers, AI for narrative** — metrics are computed in code; the LLM only *explains* them. No fabricated figures.
3. **Grounded & cited** — every insight links back to the source report cell/section.
4. **Finds bugs, not just words** — the missing clock-gate detector points to the exact module/signal/RTL line.
5. **Human-in-the-loop by design** — the agent proposes, the engineer approves. It drafts; it never decides.

## Repository map

```
RtlaAssist/
├─ README.md                ← you are here
├─ docs/
│  ├─ 01-overview.md         ← problem, users, value
│  ├─ 02-architecture.md     ← system design + component diagram
│  ├─ 03-flows.md            ← end-to-end flows (Mermaid)
│  ├─ 04-features.md         ← detailed feature specs + status
│  ├─ 05-responsible-ai.md   ← grounding, HITL, safeguards
│  ├─ 06-roadmap.md          ← staged delivery plan
│  └─ 07-demo-script.md      ← 2-minute demo video script
├─ src/                      ← implementation (skeleton)
├─ samples/                  ← sample RTLA inputs & generated outputs
└─ assets/
   ├─ presentation/          ← drop the hackathon PPTX here
   ├─ video/                 ← drop the ≤2:00 demo video here
   └─ images/                ← screenshots / diagrams
```

---
*Microsoft Confidential — Internal hackathon project.*
