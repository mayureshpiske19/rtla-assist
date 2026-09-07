# 05 · Responsible AI

RTLA AI Assistant is entered in the **Hack for Responsible AI** challenge. Responsible-AI thinking is built into the architecture, not bolted on. This is a competitive differentiator: the agent operates on real engineering data where a fabricated number could mislead a design decision, so trust is the product.

## The five safeguards

### 1. No fabricated numbers — deterministic core
All metrics, deltas, and anomaly scores are **computed in code**. The LLM never produces a number; it only explains numbers it is given. This structurally eliminates the most dangerous hallucination (a made-up power/coverage figure).

### 2. Grounded & cited answers
Every insight carries a source handle: report file + cell/section, and `module:signal:line` for RTL findings. If the user can't trace it, we don't show it. Answers include clickable citations.

### 3. Refuse-when-unsupported
If retrieval returns no supporting data, the copilot explicitly says *"I don't have data to answer that"* instead of guessing. Coverage of the answer by evidence is a first-class check.

### 4. Human-in-the-loop — draft, don't decide
The agent **proposes**: draft decks, suggested clock gates, recommended tests. A human engineer reviews and approves. No RTL change or design decision is auto-applied. Every generated artifact is a *draft* until a person signs off.

### 5. Confidence + evidence on every finding
Anomaly and clock-gate findings expose a confidence score and the underlying evidence rows, so engineers calibrate trust rather than accepting a black-box verdict.

## Additional considerations

- **Data privacy / confidentiality.** RTLA data and RTL are Microsoft Confidential. The tool runs against internal Azure OpenAI; no design data leaves the trusted boundary. No content is used to train external models.
- **Bias / scope honesty.** The tool is scoped to reporting and *advisory* insight. It does not claim design sign-off authority.
- **Transparency of limits.** The roadmap features (F8–F12) are labeled as vision, not shipped, to avoid over-claiming capability.
- **Auditability.** The insight data-flow contract (`claim`, `computed_value`, `source`, `confidence`) makes every output reproducible and reviewable.

## One-line RAI statement for the submission

> RTLA AI Assistant computes all metrics deterministically and uses Azure OpenAI only to explain cited, human-reviewed insights — it drafts, engineers decide, and every claim is traceable to its source.
