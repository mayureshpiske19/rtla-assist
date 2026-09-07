# 07 · Demo video script (≤ 2:00)

Goal: one crisp story that shows **automation + insight + Responsible AI + real domain value**. Build the whole video around a single **hero moment** — the agent finds a missing clock gate.

Target length: **1:50**. Keep it under the 2:00 hard cap.

---

## Storyboard

| Time | Scene | Voiceover (script) | On screen |
|------|-------|--------------------|-----------|
| 0:00–0:12 | **Hook / problem** | "Every milestone, our RTL team burns hours turning raw RTLA reports into Excel summaries and review decks — time we'd rather spend on design." | Pile of report files → tired engineer / clock ticking |
| 0:12–0:25 | **Enter the assistant** | "Meet RTLA AI Assistant — point it at a run, and it does the busywork." | Select an RTLA run folder in the UI |
| 0:25–0:45 | **Automation payoff** | "In seconds it generates a consolidated Excel summary, a milestone review deck, and a written key-observations page — all from the raw data." | Excel + PPTX + observations appear side by side with source dump |
| 0:45–1:05 | **Cited Q&A** | "Ask it anything. 'Why did power go up in ciu_ctrl?' — and it answers from the data, with a citation you can click." | Type question → grounded answer with `[source: power.rpt row 42]` |
| 1:05–1:35 | **HERO MOMENT** | "But it doesn't just report — it finds problems. Here it flagged a missing clock gate, pointing to the exact RTL line, with a suggested fix and a confidence score." | Zoom on: `ciu_ctrl · data_reg · ciu_ctrl.sv:214 · suggest ICG · conf 0.82` |
| 1:35–1:48 | **Responsible AI + human control** | "Every number is computed, not guessed. Every insight is cited. The agent drafts — the engineer approves." | Click "Approve" on the suggestion; show citation trail |
| 1:48–1:55 | **Close** | "RTLA AI Assistant: automated reporting today, intelligent design guidance tomorrow." | Logo + team names + challenge tags |

---

## Recording tips
- Record at 1080p, clean desktop, hide confidential project names if needed (blur module names that are sensitive).
- Use a real (or realistic sample) RTLA run so outputs look authentic.
- Keep cuts tight; the hero moment (1:05–1:35) is the part judges remember — give it room.
- Add captions/subtitles; many judges watch muted.
- End card must show: project name, challenge tags (*Reimagine the Future of Work*, *Hack for Responsible AI*), and "Built on Azure OpenAI".

## Shot checklist
- [ ] Folder-select → generate (automation)
- [ ] Excel + PPTX + observations visible
- [ ] One cited Q&A exchange
- [ ] Missing clock-gate flag with RTL line pointer (**hero**)
- [ ] Approve action (human-in-the-loop)
- [ ] End card with tags

## Export
Save the final file to `assets/video/rtla-assistant-demo.mp4` (≤ 2:00, ≤ typical upload size limit). Hand to the owner (Veekshitha) to upload to the Innovation Studio page.
