"""Render the RTLA AI Assistant implementation block diagram as a PNG.

Clean orthogonal ("bus") routing: no diagonal spaghetti. Structural flows are
neutral right-angle connectors; the two special paths (RTL -> detector, and the
clock-gate finding -> dashboard) are dashed and colour-coded.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ---- palette ----
C_IN, E_IN   = "#E8F1FB", "#2B6CB0"
C_ING, E_ING = "#FCEFE3", "#C05621"
C_ANA, E_ANA = "#E6F4EA", "#2F855A"
C_AI, E_AI   = "#EDE7FA", "#6B46C1"
C_OUT, E_OUT = "#FDECEC", "#C53030"
BAND   = "#F6F8FB"
TXT    = "#1A202C"
NEU    = "#4A5568"
DASH_R = "#2B6CB0"
DASH_G = "#2F855A"

fig, ax = plt.subplots(figsize=(15.5, 9.6))
ax.set_xlim(0, 100); ax.set_ylim(-4, 100); ax.axis("off")

def band(x, y, w, h, label):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.1",
                                fc=BAND, ec="#D6DEE8", lw=1.2, zorder=1))
    ax.text(x + 1.4, y + h - 2.3, label, fontsize=11.5, fontweight="bold",
            color="#5A6B7B", zorder=9,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85))

def box(x, y, w, h, fc, ec, title, sub=""):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=0.9",
                                fc=fc, ec=ec, lw=2, zorder=4))
    ax.text(x + w/2, y + h/2 + (1.3 if sub else 0), title, ha="center", va="center",
            fontsize=10.3, fontweight="bold", color=TXT, zorder=5)
    if sub:
        ax.text(x + w/2, y + h/2 - 1.9, sub, ha="center", va="center",
                fontsize=8, color="#5A6B7B", zorder=5)

def flow(pts, color=NEU, dashed=False, lw=1.9):
    ls = (0, (5, 3)) if dashed else "-"
    for i in range(len(pts) - 2):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        ax.plot([x1, x2], [y1, y2], color=color, lw=lw, ls=ls, zorder=6,
                solid_capstyle="round")
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=13, lw=lw, color=color, ls=ls, zorder=7))

def bus(x1, x2, y, color=NEU, lw=1.9):
    ax.plot([x1, x2], [y, y], color=color, lw=lw, zorder=6, solid_capstyle="round")

ax.text(50, 97.8, "RTLA AI Assistant — Implementation Block Diagram",
        ha="center", fontsize=17, fontweight="bold", color=TXT)

# ---- bands ----
band(2, 82, 96, 13, "INPUTS")
band(2, 64, 96, 13, "INGESTION")
band(2, 44, 96, 15, "ANALYSIS ENGINE   (deterministic — no LLM)")
band(2, 26, 96, 13, "AI LAYER   (Azure OpenAI)")
band(2, 5, 96, 14, "OUTPUTS")

# ---- inputs ----
box(6, 84, 20, 8, C_IN, E_IN, "RTLA reports", "power / coverage / clock-gating")
box(28, 84, 20, 8, C_IN, E_IN, "Prior-run reports", "for regression diff")
box(74, 84, 20, 8, C_IN, E_IN, "RTL source", "for line pointers")

# ---- ingestion ----
box(8, 66, 32, 9, C_ING, E_ING, "Schema-aware parsers", "detect report type, normalize")
box(52, 66, 30, 9, C_ING, E_ING, "Normalized metrics store", "module·metric·value·run·source")

# ---- analysis (clock-gate rightmost, under RTL source) ----
mods = [
    (5,  "Regression diff", "run N-1 vs N"),
    (23, "Anomaly triage", "conf + evidence"),
    (41, "Coverage / QoR", "trends"),
    (59, "Testcase rec.", "hole -> tests"),
    (78, "Missing clock-\ngate detector", "module:sig:line"),
]
for x, t, s in mods:
    box(x, 46, 16, 10, C_ANA, E_ANA, t, s)
mcx = [x + 8 for x, _, _ in mods]

# ---- AI layer ----
box(6, 28, 24, 9, C_AI, E_AI, "Grounded RAG", "retrieve + cite")
box(38, 28, 24, 9, C_AI, E_AI, "Narrative writer", "key observations")
box(68, 28, 24, 9, C_AI, E_AI, "Interactive copilot", "cited Q&A")

# ---- outputs ----
box(5, 7, 20, 9, C_OUT, E_OUT, "Excel summary", "openpyxl")
box(28, 7, 20, 9, C_OUT, E_OUT, "Milestone PPTX", "python-pptx")
box(51, 7, 20, 9, C_OUT, E_OUT, "Key observations", "review notes")
box(74, 7, 20, 9, C_OUT, E_OUT, "Chat / dashboard", "Q&A + QoR charts")

# ================= arrows =================
# inputs -> parsers
flow([(16, 84), (16, 75)])
flow([(38, 84), (38, 75)])
# parsers -> store
flow([(40, 70.5), (52, 70.5)])
# store -> distribution bus -> each analysis module
flow([(67, 66), (67, 61)])
bus(13, 86, 61)
for cx in mcx:
    flow([(cx, 61), (cx, 56)])
# analysis modules -> collector bus -> Grounded RAG
for cx in mcx:
    ax.plot([cx, cx], [46, 41], color=NEU, lw=1.9, zorder=6)
bus(13, 86, 41)
flow([(18, 41), (18, 37)])
# RTL source -> clock-gate detector (dashed)
flow([(84, 84), (84, 58.5), (86, 58.5), (86, 56)], color=DASH_R, dashed=True, lw=2)
# AI internal chain
flow([(30, 32.5), (38, 32.5)], color=E_AI)
flow([(62, 32.5), (68, 32.5)], color=E_AI)
# AI layer -> distribution bus -> outputs
ax.plot([50, 50], [28, 22], color=NEU, lw=1.9, zorder=6)
ax.plot([80, 80], [28, 22], color=NEU, lw=1.9, zorder=6)
bus(15, 84, 22)
for cx in (15, 38, 61, 84):
    flow([(cx, 22), (cx, 16)])
# clock-gate finding -> dashboard (dashed, far-right)
flow([(94, 51), (96.5, 51), (96.5, 11.5), (94, 11.5)], color=DASH_G, dashed=True, lw=2)

# ---- legend ----
ax.add_patch(FancyBboxPatch((6, 0.2), 88, 3.4, boxstyle="round,pad=0.2,rounding_size=0.6",
                            fc="white", ec="#D6DEE8", lw=1, zorder=2))
ax.plot([9, 13], [1.9, 1.9], color=NEU, lw=2, zorder=3)
ax.text(14, 1.9, "data flow", va="center", fontsize=8.5, color=TXT, zorder=3)
ax.plot([28, 32], [1.9, 1.9], color=DASH_R, lw=2, ls=(0, (5, 3)), zorder=3)
ax.text(33, 1.9, "RTL feeds detector", va="center", fontsize=8.5, color=TXT, zorder=3)
ax.plot([56, 60], [1.9, 1.9], color=DASH_G, lw=2, ls=(0, (5, 3)), zorder=3)
ax.text(61, 1.9, "clock-gate flag -> dashboard", va="center", fontsize=8.5, color=TXT, zorder=3)
ax.text(50, -2.6, "Deterministic core computes all numbers  •  AI only explains cited facts  •  Human approves every draft (HITL)",
        ha="center", fontsize=9, style="italic", color="#5A6B7B")

plt.savefig("rtla_block_diagram.png", dpi=175, bbox_inches="tight", facecolor="white")
print("saved rtla_block_diagram.png")
