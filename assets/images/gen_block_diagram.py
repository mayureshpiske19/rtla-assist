"""Render the RTLA AI Assistant implementation block diagram as a PNG."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Palette
C_IN   = "#E8F1FB"; E_IN   = "#2B6CB0"
C_ING  = "#FCEFE3"; E_ING  = "#C05621"
C_ANA  = "#E6F4EA"; E_ANA  = "#2F855A"
C_AI   = "#F0E8FB"; E_AI   = "#6B46C1"
C_OUT  = "#FDECEC"; E_OUT  = "#C53030"
C_BAND = "#F7FAFC"
TXT    = "#1A202C"

fig, ax = plt.subplots(figsize=(15, 9.2))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

def band(x, y, w, h, color, label):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc=color, ec="#CBD5E0", lw=1.2, zorder=1))
    ax.text(x + 1.2, y + h - 2.6, label, fontsize=12.5, fontweight="bold",
            color="#4A5568", zorder=3)

def box(x, y, w, h, fc, ec, title, sub=""):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.0",
                                fc=fc, ec=ec, lw=2, zorder=4))
    ax.text(x + w/2, y + h/2 + (1.1 if sub else 0), title, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=TXT, zorder=5)
    if sub:
        ax.text(x + w/2, y + h/2 - 1.9, sub, ha="center", va="center",
                fontsize=8.2, color="#4A5568", zorder=5)

def arrow(x1, y1, x2, y2, color="#2D3748", style="-|>", lw=2, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                 mutation_scale=16, lw=lw, color=color, ls=ls,
                 connectionstyle="arc3,rad=0", zorder=6))

ax.text(50, 97.5, "RTLA AI Assistant — Proposed Implementation Block Diagram",
        ha="center", fontsize=16.5, fontweight="bold", color=TXT)

# ---- Bands (left labels) ----
band(2, 80, 96, 14, C_BAND, "INPUTS")
band(2, 62.5, 96, 14, C_BAND, "INGESTION")
band(2, 41, 96, 18.5, C_BAND, "ANALYSIS ENGINE  (deterministic — no LLM)")
band(2, 23.5, 96, 15, C_BAND, "AI LAYER  (Azure OpenAI)")
band(2, 4, 96, 16.5, C_BAND, "OUTPUTS")

# ---- Inputs ----
box(8, 82.5, 24, 8.5, C_IN, E_IN, "RTLA reports", "power / coverage / clock-gating")
box(38, 82.5, 24, 8.5, C_IN, E_IN, "Prior-run reports", "for regression diff")
box(68, 82.5, 24, 8.5, C_IN, E_IN, "RTL source", "for line pointers")

# ---- Ingestion ----
box(14, 64.5, 30, 9, C_ING, E_ING, "Schema-aware parsers", "detect report type, normalize")
box(56, 64.5, 30, 9, C_ING, E_ING, "Normalized metrics store", "module·metric·value·run·source")

# ---- Analysis engine (5 modules) ----
aw = 16.5; ay = 45.5; ah = 9.5
axs = [6.5, 25, 43.5, 62, 80.5]
alabels = [
    ("Regression\ndiff", "run N-1 vs N"),
    ("Missing clock-\ngate detector", "module:sig:line"),
    ("Anomaly\ntriage", "conf + evidence"),
    ("Coverage /\nQoR tracker", "trends"),
    ("Testcase\nrecommender", "hole -> tests"),
]
for x, (t, s) in zip(axs, alabels):
    box(x, ay, aw, ah, C_ANA, E_ANA, t, s)

# ---- AI layer ----
box(10, 26, 24, 8.5, C_AI, E_AI, "Grounded RAG", "retrieve + cite")
box(38, 26, 24, 8.5, C_AI, E_AI, "Narrative writer", "key observations")
box(66, 26, 24, 8.5, C_AI, E_AI, "Interactive copilot", "cited Q&A")

# ---- Outputs ----
box(6, 6.5, 20, 8.5, C_OUT, E_OUT, "Excel summary", "openpyxl")
box(29, 6.5, 20, 8.5, C_OUT, E_OUT, "Milestone PPTX", "python-pptx")
box(52, 6.5, 20, 8.5, C_OUT, E_OUT, "Key observations", "review notes")
box(75, 6.5, 19, 8.5, C_OUT, E_OUT, "Chat / dashboard", "Q&A + QoR charts")

# ---- Arrows: inputs -> ingestion ----
arrow(20, 82.5, 26, 73.5, E_ING)
arrow(50, 82.5, 34, 73.5, E_ING)
arrow(80, 82.5, 71, 73.5, E_ING)
# parsers -> store
arrow(44, 69, 56, 69, E_ING)
# store -> analysis (fan out)
for x in axs:
    arrow(62, 64.5, x + aw/2, ay + ah, E_ANA, lw=1.4)
# RTL source -> clock-gate detector (dashed direct)
arrow(80, 82.5, 25 + aw/2, ay + ah, E_IN, lw=1.6, ls=(0, (4, 3)))
# analysis -> AI layer (converge to RAG)
for x in axs:
    arrow(x + aw/2, ay, 22, 34.5, E_AI, lw=1.2)
# RAG -> narrator -> copilot
arrow(34, 30.2, 38, 30.2, E_AI)
arrow(62, 30.2, 66, 30.2, E_AI)
# AI -> outputs
arrow(30, 26, 16, 15, E_OUT, lw=1.5)      # narrator -> excel/pptx region
arrow(46, 26, 39, 15, E_OUT, lw=1.5)
arrow(52, 26, 62, 15, E_OUT, lw=1.5)
arrow(78, 26, 84, 15, E_OUT, lw=1.5)      # copilot -> chat
# clock-gate pointer -> chat/dashboard (dashed)
arrow(25 + aw/2, ay, 84, 15, E_ANA, lw=1.3, ls=(0, (4, 3)))

# Legend
ax.text(50, 1.4,
        "Deterministic core computes all numbers  •  AI only explains cited facts  •  Human approves every draft (HITL)",
        ha="center", fontsize=9.5, style="italic", color="#4A5568")

plt.tight_layout()
out = "rtla_block_diagram.png"
plt.savefig(out, dpi=170, bbox_inches="tight", facecolor="white")
print("saved", out)
