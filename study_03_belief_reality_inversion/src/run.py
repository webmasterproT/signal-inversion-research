#!/usr/bin/env python3
"""
Study 3: The Belief-Reality Inversion Matrix
Signal Inversion Effect — Standalone Reproducible Analysis

Matches 23 deception cues across two datasets:
  - Public belief strength: Global Deception Research Team (2006), N=11,227, 75 countries
  - Actual diagnostic value: DePaulo et al. (2003) meta-analysis, 158 cues
  - Disfluency finding: Current Study 1

Computes: inversion rate, binomial sign test, weighted inversion index,
Spearman correlation (belief strength vs actual |d|), category breakdown.
Generates: forest plot, belief-reality scatter, inversion rate summary.
"""

import os
import sys
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Shared OMXUS figure style (optional — works without it)
try:
    import sys as _sys
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'shared'))
    from style import apply_style, COLORS, save_figure
    apply_style()
    _HAS_STYLE = True
except ImportError:
    _HAS_STYLE = False

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
csv_path = os.path.join(DATA_DIR, "inversion_matrix.csv")
if not os.path.exists(csv_path):
    print(f"ERROR: {csv_path} not found. Run from the study_3 directory.")
    sys.exit(1)

df = pd.read_csv(csv_path)
df["inverted"] = df["inverted"].map({"True": True, "False": False, True: True, False: False})
df["abs_d"] = df["actual_d"].abs()
n_total = len(df)
n_inverted = df["inverted"].sum()
inversion_rate = n_inverted / n_total

print("=" * 90)
print("STUDY 3: THE BELIEF-REALITY INVERSION MATRIX (23 CUES)")
print("=" * 90)

# ---------------------------------------------------------------------------
# Table
# ---------------------------------------------------------------------------
print(f"\n{'Cue':35s} {'Belief%':>8s} {'d':>7s} {'Category':>15s} {'Inverted':>9s}")
print("-" * 80)
for _, row in df.iterrows():
    inv_str = "YES" if row["inverted"] else "no"
    print(f"{row['cue']:35s} {row['belief_pct']:8.1f} {row['actual_d']:7.2f} "
          f"{row['category']:>15s} {inv_str:>9s}")
print("-" * 80)

# ---------------------------------------------------------------------------
# Inversion rate + binomial test
# ---------------------------------------------------------------------------
binom = stats.binomtest(int(n_inverted), n_total, 0.5, alternative="greater")
ci = binom.proportion_ci(confidence_level=0.95)

print(f"\nInversion Rate: {n_inverted}/{n_total} = {inversion_rate*100:.1f}%")
print(f"Binomial Test (H0: rate = 50%): p = {binom.pvalue:.6f}")
print(f"  95% CI: [{ci.low*100:.1f}%, {ci.high*100:.1f}%]")
print(f"  {'SIGNIFICANT' if binom.pvalue < 0.05 else 'NOT SIGNIFICANT'} at alpha = .05")

# ---------------------------------------------------------------------------
# Weighted Inversion Index
# ---------------------------------------------------------------------------
weighted_sum = 0.0
total_belief = df["belief_pct"].sum()
for _, row in df.iterrows():
    if row["inverted"]:
        weighted_sum += row["belief_pct"]
    else:
        weighted_sum -= row["belief_pct"]
weighted_index = weighted_sum / total_belief

print(f"\nWeighted Inversion Index: {weighted_index:.3f}  (scale: -1.0 to +1.0)")
print(f"  Interpretation: beliefs weighted by endorsement rate are {weighted_index*100:.1f}% net inverted")

# ---------------------------------------------------------------------------
# Spearman correlation: belief strength vs actual |d|
# ---------------------------------------------------------------------------
rho, rho_p = stats.spearmanr(df["belief_pct"], df["abs_d"])
print(f"\nSpearman Correlation (belief strength vs |d|):")
print(f"  rho = {rho:.3f}, p = {rho_p:.3f}")
print(f"  {'Significant' if rho_p < 0.05 else 'NOT significant'}: "
      f"how strongly the public believes a cue {'is' if rho_p < 0.05 else 'is NOT'} related to its actual validity")

# ---------------------------------------------------------------------------
# Category breakdown
# ---------------------------------------------------------------------------
print("\nCategory Breakdown:")
for cat in ["nonverbal", "paralinguistic", "verbal"]:
    sub = df[df["category"] == cat]
    inv = sub["inverted"].sum()
    tot = len(sub)
    print(f"  {cat:15s}: {inv}/{tot} = {inv/tot*100:.0f}% inverted")

# ---------------------------------------------------------------------------
# Save text results
# ---------------------------------------------------------------------------
results_text = []
results_text.append("Study 3: Belief-Reality Inversion Matrix — Results Summary")
results_text.append("=" * 70)
results_text.append(f"N cues matched: {n_total}")
results_text.append(f"Inverted: {n_inverted}/{n_total} = {inversion_rate*100:.1f}%")
results_text.append(f"Binomial p = {binom.pvalue:.6f} (one-tailed, H0: 50%)")
results_text.append(f"95% CI: [{ci.low*100:.1f}%, {ci.high*100:.1f}%]")
results_text.append(f"Weighted Inversion Index: {weighted_index:.3f}")
results_text.append(f"Spearman rho = {rho:.3f}, p = {rho_p:.3f}")
results_text.append("")
results_text.append("Category Breakdown:")
for cat in ["nonverbal", "paralinguistic", "verbal"]:
    sub = df[df["category"] == cat]
    inv = sub["inverted"].sum()
    tot = len(sub)
    results_text.append(f"  {cat:15s}: {inv}/{tot} = {inv/tot*100:.0f}%")
results_text.append("")
results_text.append("Key Finding:")
results_text.append("  74% of publicly believed deception cues are empirically wrong or unrelated.")
results_text.append("  The strongest beliefs (gaze aversion 63.7%) have the smallest actual effects (d=0.05).")
results_text.append("  The public's deception model is not merely inaccurate -- it is systematically inverted.")

results_path = os.path.join(RESULTS_DIR, "study_3_results.txt")
with open(results_path, "w") as f:
    f.write("\n".join(results_text))
print(f"\nResults saved to {results_path}")

# ---------------------------------------------------------------------------
# Figure 1: Forest Plot — Actual Effect Size by Cue, Colored by Inversion
# ---------------------------------------------------------------------------
fig1, ax1 = plt.subplots(figsize=(10, 10))
df_sorted = df.sort_values("belief_pct", ascending=True).reset_index(drop=True)
y_pos = np.arange(n_total)
colors = ["#c0392b" if inv else "#27ae60" for inv in df_sorted["inverted"]]

ax1.barh(y_pos, df_sorted["actual_d"], color=colors, edgecolor="white", height=0.7, alpha=0.85)
ax1.set_yticks(y_pos)
ax1.set_yticklabels([f"{row['cue']}  ({row['belief_pct']:.0f}%)"
                     for _, row in df_sorted.iterrows()], fontsize=9)
ax1.set_xlabel("Actual Effect Size (Cohen's d)", fontsize=11)
ax1.set_title("Belief-Reality Inversion: Actual Effect Sizes of Believed Deception Cues\n"
              "(sorted by public belief strength; % = endorsement rate)",
              fontsize=12, fontweight="bold")
ax1.axvline(x=0, color="black", linewidth=0.8, linestyle="-")
ax1.axvline(x=0.20, color="gray", linewidth=0.5, linestyle="--", alpha=0.5)
ax1.axvline(x=-0.20, color="gray", linewidth=0.5, linestyle="--", alpha=0.5)

inv_patch = mpatches.Patch(color="#c0392b", label=f"Inverted ({n_inverted}/{n_total})")
align_patch = mpatches.Patch(color="#27ae60", label=f"Aligned ({n_total - n_inverted}/{n_total})")
ax1.legend(handles=[inv_patch, align_patch], loc="lower right", fontsize=10)
ax1.set_xlim(-0.75, 0.50)
plt.tight_layout()
fig1_path = os.path.join(FIGURES_DIR, "forest_plot_inversion.png")
fig1.savefig(fig1_path, dpi=200)
plt.close(fig1)
print(f"Figure 1 saved: {fig1_path}")

# ---------------------------------------------------------------------------
# Figure 2: Scatter — Belief Strength vs Actual |d|
# ---------------------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(8, 6))
colors2 = ["#c0392b" if inv else "#27ae60" for inv in df["inverted"]]
ax2.scatter(df["belief_pct"], df["abs_d"], c=colors2, s=80, edgecolors="white",
            linewidths=0.5, alpha=0.85, zorder=3)

# Annotate notable cues
for _, row in df.iterrows():
    if row["belief_pct"] > 40 or row["abs_d"] > 0.25:
        ax2.annotate(row["cue"], (row["belief_pct"], row["abs_d"]),
                     textcoords="offset points", xytext=(6, 4), fontsize=7.5,
                     fontstyle="italic", alpha=0.8)

# Regression line
z = np.polyfit(df["belief_pct"], df["abs_d"], 1)
p = np.poly1d(z)
x_line = np.linspace(df["belief_pct"].min() - 2, df["belief_pct"].max() + 2, 100)
ax2.plot(x_line, p(x_line), "--", color="gray", alpha=0.5, linewidth=1)

ax2.set_xlabel("Public Belief Strength (%)", fontsize=11)
ax2.set_ylabel("Actual Diagnostic Value (|d|)", fontsize=11)
ax2.set_title(f"Belief Strength vs Actual Validity (Spearman rho = {rho:.3f}, p = {rho_p:.3f})\n"
              f"N = {n_total} cues matched across GDRT (2006) and DePaulo et al. (2003)",
              fontsize=11, fontweight="bold")
inv_patch2 = mpatches.Patch(color="#c0392b", label="Inverted")
align_patch2 = mpatches.Patch(color="#27ae60", label="Aligned")
ax2.legend(handles=[inv_patch2, align_patch2], loc="upper right", fontsize=10)
plt.tight_layout()
fig2_path = os.path.join(FIGURES_DIR, "scatter_belief_vs_reality.png")
fig2.savefig(fig2_path, dpi=200)
plt.close(fig2)
print(f"Figure 2 saved: {fig2_path}")

# ---------------------------------------------------------------------------
# Figure 3: Inversion Rate Summary (pie + category bar)
# ---------------------------------------------------------------------------
fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(12, 5))

# Pie
ax3a.pie([n_inverted, n_total - n_inverted],
         labels=[f"Inverted\n{n_inverted}/{n_total} ({inversion_rate*100:.0f}%)",
                 f"Aligned\n{n_total - n_inverted}/{n_total} ({(1 - inversion_rate)*100:.0f}%)"],
         colors=["#c0392b", "#27ae60"], autopct="", startangle=90,
         textprops={"fontsize": 11}, wedgeprops={"edgecolor": "white", "linewidth": 2})
ax3a.set_title("Overall Inversion Rate", fontsize=12, fontweight="bold")

# Category bar
categories = ["nonverbal", "paralinguistic", "verbal"]
cat_inv = []
cat_align = []
for cat in categories:
    sub = df[df["category"] == cat]
    inv = sub["inverted"].sum()
    cat_inv.append(inv)
    cat_align.append(len(sub) - inv)

x = np.arange(len(categories))
width = 0.35
bars1 = ax3b.bar(x - width / 2, cat_inv, width, label="Inverted", color="#c0392b", edgecolor="white")
bars2 = ax3b.bar(x + width / 2, cat_align, width, label="Aligned", color="#27ae60", edgecolor="white")
ax3b.set_xticks(x)
ax3b.set_xticklabels([c.capitalize() for c in categories], fontsize=10)
ax3b.set_ylabel("Number of Cues", fontsize=11)
ax3b.set_title("Inversion by Category", fontsize=12, fontweight="bold")
ax3b.legend(fontsize=10)

# Add count labels
for bar in bars1:
    ax3b.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
              str(int(bar.get_height())), ha="center", fontsize=10, fontweight="bold")
for bar in bars2:
    ax3b.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
              str(int(bar.get_height())), ha="center", fontsize=10, fontweight="bold")

plt.tight_layout()
fig3_path = os.path.join(FIGURES_DIR, "inversion_rate_summary.png")
fig3.savefig(fig3_path, dpi=200)
plt.close(fig3)
print(f"Figure 3 saved: {fig3_path}")

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
print(f"\nAll outputs in {RESULTS_DIR}/")
print("Done.")
