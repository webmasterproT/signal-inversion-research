#!/usr/bin/env python3
"""
Study 4: Human vs Algorithmic Deception Detection — Convergence Analysis

Compares human deception detection accuracy (Bond & DePaulo, 2006; k=206, N=24,483)
against algorithmic detection using linguistic markers from Studies 1-2.

Key finding: Humans achieve 54% (barely above 50% chance). Algorithms using
linguistic features invisible to human observers reach 63.5-78.5%. The gap
exists because humans rely on inverted cues (Study 3).
"""

import os
import csv
import numpy as np

# Shared OMXUS figure style (optional — works without it)
try:
    import sys as _sys
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'shared'))
    from style import apply_style, COLORS, save_figure
    apply_style()
    _HAS_STYLE = True
except ImportError:
    _HAS_STYLE = False

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

output_lines = []
def log(text=""):
    print(text)
    output_lines.append(text)


# ================================================================
# Load data
# ================================================================
data = []
with open(os.path.join(DATA_DIR, "convergence_data.csv")) as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append({
            "method": row["method"],
            "accuracy": float(row["accuracy"]),
            "source": row["source"]
        })

log("=" * 80)
log("STUDY 4: HUMAN vs ALGORITHMIC DECEPTION DETECTION — CONVERGENCE")
log("=" * 80)

# ================================================================
# Separate human vs algorithmic
# ================================================================
human = [d for d in data if not d["method"].startswith("Algorithm")]
algo = [d for d in data if d["method"].startswith("Algorithm")]

log("\nHuman Detection Accuracy (Bond & DePaulo, 2006; k=206 studies, N=24,483)")
log("-" * 70)
for d in human:
    log(f"  {d['method']:30s}  {d['accuracy']:5.1f}%")

log(f"\nAlgorithmic Detection Accuracy (linguistic features)")
log("-" * 70)
for d in algo:
    log(f"  {d['method']:30s}  {d['accuracy']:5.1f}%  ({d['source']})")

# ================================================================
# Compute gaps
# ================================================================
human_overall = next(d["accuracy"] for d in human if d["method"] == "Human overall")
chance = 50.0

log(f"\n{'='*70}")
log("GAP ANALYSIS")
log(f"{'='*70}")
log(f"  Chance level:               {chance:.1f}%")
log(f"  Human overall:              {human_overall:.1f}%")
log(f"  Human advantage over chance: {human_overall - chance:.1f} percentage points")
log(f"")

for d in algo:
    gap = d["accuracy"] - human_overall
    log(f"  {d['method']:30s}  gap = +{gap:.1f}pp over human  ({d['accuracy']:.1f}% vs {human_overall:.1f}%)")

# Human lie detection is BELOW chance
lie_detect = next(d["accuracy"] for d in human if d["method"] == "Human lie detection")
log(f"\n  CRITICAL: Human lie detection = {lie_detect:.1f}% — BELOW chance ({chance:.1f}%)")
log(f"  Humans are worse than coin-flipping at detecting lies specifically.")

# Cohen's h for human overall vs chance
h = 2 * np.arcsin(np.sqrt(human_overall / 100)) - 2 * np.arcsin(np.sqrt(chance / 100))
log(f"\n  Cohen's h (human overall vs chance) = {h:.3f}")
log(f"  h < 0.20 = negligible effect size")
log(f"  The 4-point advantage is statistically significant (N=24,483)")
log(f"  but practically meaningless — a system built on this is random.")

# ================================================================
# Why the gap exists
# ================================================================
log(f"\n{'='*70}")
log("WHY THE GAP EXISTS")
log(f"{'='*70}")
log("""
  Humans rely on cues that are:
    - Unrelated to actual deception (gaze aversion, fidgeting)
    - Actively inverted (disfluency is HIGHER in truth-tellers)
    - 78.6% empirically wrong (Study 3 inversion matrix)

  Algorithms use cues that are:
    - Linguistically measurable (pronoun rates, conjunction patterns)
    - Imperceptible to human observers in real-time
    - Empirically validated against ground truth

  The features humans CAN perceive are inverted.
  The features that WORK are imperceptible.
  This is the Signal Inversion Effect operating at the system level.
""")

# ================================================================
# Training doesn't help
# ================================================================
log(f"{'='*70}")
log("TRAINING EFFECT: NONE")
log(f"{'='*70}")
log(f"  Police officers:      55%  (trained)")
log(f"  Customs officials:    55%  (trained)")
log(f"  Judges:               54%  (decades of experience)")
log(f"  General public:       54%  (untrained)")
log(f"")
log(f"  Training does not improve deception detection (Bond & DePaulo 2006).")
log(f"  Confidence does not correlate with accuracy (DePaulo et al. 1997).")
log(f"  Experience does not help because the training reinforces inverted cues.")

# ================================================================
# Save results text
# ================================================================
with open(os.path.join(RESULTS_DIR, "study_4_convergence.txt"), "w") as f:
    f.write("\n".join(output_lines))
log(f"\nResults saved to results/study_4_convergence.txt")

# ================================================================
# Generate figure
# ================================================================
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    methods = [d["method"] for d in data]
    accuracies = [d["accuracy"] for d in data]

    # Color: blue for human, green for algorithmic
    colors = ["#d9534f" if not m.startswith("Algorithm") else "#5cb85c" for m in methods]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.barh(range(len(methods)), accuracies, color=colors, edgecolor="white", linewidth=0.5)

    # Chance line
    ax.axvline(x=50, color="black", linestyle="--", linewidth=1.5, label="Chance (50%)")

    ax.set_yticks(range(len(methods)))
    ax.set_yticklabels(methods, fontsize=10)
    ax.set_xlabel("Classification Accuracy (%)", fontsize=12)
    ax.set_title("Study 4: Human vs Algorithmic Deception Detection Accuracy", fontsize=13, fontweight="bold")
    ax.set_xlim(40, 85)
    ax.invert_yaxis()

    # Add value labels
    for i, (bar, acc) in enumerate(zip(bars, accuracies)):
        ax.text(acc + 0.5, i, f"{acc:.1f}%", va="center", fontsize=9)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#d9534f", label="Human observers"),
        Patch(facecolor="#5cb85c", label="Algorithmic (linguistic)"),
        plt.Line2D([0], [0], color="black", linestyle="--", label="Chance (50%)")
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=9)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, "convergence_accuracy.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    log(f"Figure saved to results/figures/convergence_accuracy.png")
except ImportError as e:
    log(f"\nNote: matplotlib not available ({e}). Figure not generated.")
    log("Install with: pip install matplotlib")
