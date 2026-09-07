# 03 · End-to-end flows

## Flow A — Milestone report generation (the "today" hero flow)

```mermaid
sequenceDiagram
    actor Eng as Engineer
    participant UI as RTLA Assistant
    participant Ing as Ingestion
    participant An as Analysis Engine
    participant AI as Azure OpenAI
    participant Gen as Output Gen

    Eng->>UI: Point to RTLA run folder
    UI->>Ing: Parse reports
    Ing->>An: Normalized metrics
    An->>An: Compute summaries, deltas, anomalies
    An->>AI: Computed facts (+ citations)
    AI->>Gen: Key-observations narrative
    Gen-->>Eng: Excel + PPTX + observations (draft)
    Eng->>UI: Review & approve
```

**Steps**
1. Engineer selects a run folder (or the tool watches a results dir).
2. Parsers normalize every report into the metric schema.
3. Analysis engine computes per-module summaries, run-over-run deltas, and anomalies — **in code**.
4. AI layer writes the narrative *from the computed facts only*, attaching citations.
5. Generators emit the Excel summary, the milestone PPTX, and the key-observations doc.
6. Engineer reviews; nothing is "final" until approved.

## Flow B — Interactive analysis Q&A

```mermaid
sequenceDiagram
    actor Eng as Engineer
    participant UI as Chat
    participant Ret as Retriever
    participant AI as Azure OpenAI

    Eng->>UI: "Why did power go up in ciu_ctrl this run?"
    UI->>Ret: Retrieve relevant metrics + prior run
    Ret->>AI: Cited context (rows + sections)
    AI-->>UI: Grounded answer + [source: power.rpt row 42]
    UI-->>Eng: Answer with clickable citation
```

Guardrail: if retrieval returns no supporting data, the copilot says *"I don't have data for that"* rather than guessing.

## Flow C — Missing clock-gate detection (the "wow" flow)

```mermaid
flowchart LR
    A[Activity + enable data] --> D{Free-running\nclock?}
    RTL[RTL source] --> D
    D -- yes --> F[Flag: module:signal:line]
    F --> S[Suggest ICG insertion]
    S --> H[Engineer approves / dismisses]
    D -- no --> OK[No action]
```

**Output example:**
```
⚠ Missing clock gate
  module : ciu_ctrl
  signal : data_reg[31:0]
  file   : ciu_ctrl.sv:214
  reason : register free-running while enable inactive 87% of cycles
  suggest: insert ICG on `data_reg` gated by `ciu_active`
  confidence: 0.82   [evidence: toggle.rpt rows 88–91]
```

## Flow D — Cross-run regression diff

```mermaid
flowchart LR
    R1[Run N-1] --> DIFF[Delta engine]
    R2[Run N] --> DIFF
    DIFF --> RANK[Rank by impact]
    RANK --> AI[Root-cause narrative]
    AI --> REP[Regression report]
```

Produces a ranked table (biggest power/coverage movers first) with an AI-written *why* for each, each line cited to source rows.

## Flow E — Testcase recommendation

```mermaid
flowchart LR
    COV[Coverage report] --> HOLE[Detect holes]
    HOLE --> MAP[Map hole -> existing UVM tests]
    MAP --> REC[Recommend tests / stimulus stub]
    REC --> Eng[Engineer runs / edits]
```

Connects *analysis → action*: a coverage hole becomes a concrete "run these tests" recommendation.
