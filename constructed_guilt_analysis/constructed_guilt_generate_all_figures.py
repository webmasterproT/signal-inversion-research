#!/usr/bin/env python3
"""
Generate ALL figures for the Signal Inversion Effect analyses.
Outputs to results/figures/
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "results")
FIG_DIR = os.path.join(RESULTS_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# Style
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'sans-serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
})

RED = '#D94040'
GREEN = '#4CAF50'
GREY = '#888888'
DARK = '#333333'

# ================================================================
# DATA — from the analyses
# ================================================================

# Study 1 results
study1_vars = [
    ('Disfluency/Fillers', 5.14, 4.21, 3.03, 2.68, 0.60, 0.004),
    ('Negative Emotion', 0.02, 0.17, 0.13, 0.52, -0.27, 0.103),
    ('First-Person Pron.', 6.13, 4.38, 7.15, 4.16, -0.24, 0.164),
    ('Experiencer Framing', 0.60, 1.51, 0.34, 0.94, 0.21, 0.448),
    ('Certainty Markers', 0.35, 1.25, 0.76, 3.15, -0.17, 0.265),
    ('Hedging Rate', 0.86, 1.31, 1.05, 1.41, -0.14, 0.376),
    ('Word Count', 80.57, 41.99, 75.84, 46.49, 0.11, 0.258),
    ('Passive Constructions', 3.93, 2.64, 4.04, 2.89, -0.04, 0.963),
]

# 23-cue inversion matrix (from analysis_3b)
inversion_23 = [
    ("Gaze aversion", 63.7, 0.05, "nonverbal", True),
    ("Fidgeting/restlessness", 52.0, 0.01, "nonverbal", True),
    ("Nervous appearance", 45.0, -0.01, "nonverbal", False),
    ("Face touching", 25.0, -0.02, "nonverbal", True),
    ("Posture shifts", 24.0, 0.04, "nonverbal", True),
    ("Blink rate changes", 15.0, 0.01, "nonverbal", True),
    ("Head movements", 18.0, 0.01, "nonverbal", True),
    ("Illustrators (gestures)", 15.0, -0.09, "nonverbal", True),
    ("Leg/foot movements", 12.0, -0.04, "nonverbal", True),
    ("Pupil dilation", 10.0, 0.39, "nonverbal", False),
    ("Smile frequency", 14.0, -0.01, "nonverbal", True),
    ("Speech hesitations", 38.0, 0.00, "paralinguistic", True),
    ("Disfluency/fillers", 35.0, -0.60, "paralinguistic", True),
    ("Vocal pitch change", 20.0, 0.21, "paralinguistic", False),
    ("Slower speech rate", 18.0, 0.07, "paralinguistic", True),
    ("Response latency", 22.0, 0.02, "paralinguistic", True),
    ("Self-corrections", 12.0, -0.12, "verbal", True),
    ("Story inconsistency", 30.0, 0.13, "verbal", False),
    ("Lack of detail", 28.0, 0.30, "verbal", False),
    ("Negative statements", 10.0, 0.21, "verbal", False),
    ("Hedging/uncertainty", 25.0, -0.14, "verbal", True),
    ("Exaggerated certainty", 15.0, -0.17, "verbal", True),
    ("Shorter responses", 20.0, 0.12, "verbal", True),
]

# Confession data (Study 2 key discriminators)
confession_words = [
    ("'you'", 9.4, 71.3, 7.59),
    ("'that's'", 1.7, 19.3, 11.67),
    ("'it's'", 1.2, 14.6, 12.17),
    ("'that'", 16.4, 80.2, 4.89),
    ("'it'", 16.8, 71.7, 4.28),
    ("'what'", 4.5, 26.7, 5.90),
    ("'but'", 5.2, 19.6, 3.78),
    ("'so'", 4.6, 16.4, 3.58),
    ("'or'", 4.3, 15.8, 3.66),
]


# ================================================================
# FIGURE 1: Forest Plot — All 23 Cues
# ================================================================
print("Generating Figure 1: Forest plot (23 cues)...")

fig, ax = plt.subplots(figsize=(12, 10))

# Sort by belief %
sorted_cues = sorted(inversion_23, key=lambda x: x[1])
cue_names = [c[0] for c in sorted_cues]
belief_pcts = [c[1] for c in sorted_cues]
actual_ds = [c[2] for c in sorted_cues]
inverted = [c[4] for c in sorted_cues]

y_pos = range(len(cue_names))
colors = [RED if inv else GREEN for inv in inverted]

bars = ax.barh(y_pos, actual_ds, color=colors, height=0.7, alpha=0.85, edgecolor='white', linewidth=0.5)

# Add belief % labels on right
for i, (name, pct) in enumerate(zip(cue_names, belief_pcts)):
    ax.text(max(actual_ds) + 0.08, i, f"{pct:.0f}%", va='center', fontsize=9, color=GREY)

ax.set_yticks(y_pos)
ax.set_yticklabels(cue_names, fontsize=10)
ax.axvline(x=0, color=DARK, linewidth=0.8, linestyle='-')
ax.set_xlabel("Effect Size (Cohen's d)\n← Higher in truth-tellers  |  Higher in liars →", fontsize=11)

n_inv = sum(inverted)
n_tot = len(inverted)

ax.set_title(
    f"Deception Cues: What People Believe vs. What Evidence Shows\n"
    f"Red = inverted (belief is wrong) | Green = aligned (belief is correct)\n"
    f"Percentage = global belief endorsement rate (GDRT 2006)",
    fontsize=12, fontweight='bold', pad=15
)

inv_patch = mpatches.Patch(color=RED, label=f'Belief INVERTED ({n_inv}/{n_tot})')
ali_patch = mpatches.Patch(color=GREEN, label=f'Belief ALIGNED ({n_tot-n_inv}/{n_tot})')
ax.legend(handles=[inv_patch, ali_patch], loc='lower right', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig1_forest_plot_23cues.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 2: Belief-Reality Scatter Plot
# ================================================================
print("Generating Figure 2: Belief-Reality scatter...")

fig, ax = plt.subplots(figsize=(10, 8))

for cue, belief, d, cat, inv in inversion_23:
    color = RED if inv else GREEN
    size = 80 + belief * 2
    ax.scatter(belief, d, c=color, s=size, alpha=0.7, edgecolors='white', linewidth=0.5, zorder=3)

# Label key points
for cue, belief, d, cat, inv in inversion_23:
    if belief > 50 or abs(d) > 0.25 or cue in ['Disfluency/fillers', 'Gaze aversion']:
        offset = (5, 5) if d > 0 else (5, -12)
        ax.annotate(cue, (belief, d), textcoords="offset points", xytext=offset,
                   fontsize=8, color=DARK, alpha=0.8)

ax.axhline(y=0, color=GREY, linewidth=0.5, linestyle='--')
ax.axvline(x=50, color=GREY, linewidth=0.3, linestyle=':')

# Quadrant labels
ax.text(55, 0.35, "ALIGNED\n(Belief matches reality)", fontsize=9, color=GREEN, alpha=0.6, ha='center')
ax.text(55, -0.35, "INVERTED\n(Belief is backwards)", fontsize=9, color=RED, alpha=0.6, ha='center')
ax.text(5, -0.35, "Correctly\nignored", fontsize=8, color=GREY, alpha=0.4, ha='center')

ax.set_xlabel('Belief Endorsement Rate (%)\n"What percentage believe this cue indicates deception?"', fontsize=11)
ax.set_ylabel('Actual Effect Size (Cohen\'s d)\nPositive = higher in liars | Negative = higher in truth-tellers', fontsize=11)
ax.set_title(
    "The Belief-Reality Inversion Matrix\n"
    "Human beliefs about deception cues vs. empirical evidence\n"
    "DePaulo et al. (2003) meta-analysis × GDRT (2006) global survey",
    fontsize=12, fontweight='bold', pad=15
)

inv_patch = mpatches.Patch(color=RED, label='Inverted (belief is backwards)')
ali_patch = mpatches.Patch(color=GREEN, label='Aligned (belief matches evidence)')
grey_patch = mpatches.Patch(color=GREY, alpha=0.3, label='False belief (no real effect)')
ax.legend(handles=[ali_patch, inv_patch, grey_patch], loc='upper left', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig2_belief_reality_scatter.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 3: Inversion Rates — Pie + Category Bar
# ================================================================
print("Generating Figure 3: Inversion rates...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Pie chart
n_inv = sum(1 for c in inversion_23 if c[4])
n_ali = len(inversion_23) - n_inv
inv_pct = n_inv / len(inversion_23) * 100

wedges, texts, autotexts = ax1.pie(
    [n_inv, n_ali], labels=[f'Inverted\n(belief wrong)', f'Aligned\n(belief correct)'],
    colors=[RED, GREEN], autopct='%1.0f%%', startangle=90,
    textprops={'fontsize': 12}, pctdistance=0.6
)
for t in autotexts:
    t.set_fontsize(14)
    t.set_fontweight('bold')
    t.set_color('white')

# Binomial test
binom_p = stats.binomtest(n_inv, len(inversion_23), 0.5, alternative='greater').pvalue
ax1.set_title(f"Inversion Rate: {inv_pct:.0f}%\nBinomial test p = {binom_p:.4f}", fontsize=13, fontweight='bold')

# Category bar chart
categories = {}
for _, _, _, cat, inv in inversion_23:
    if cat not in categories:
        categories[cat] = [0, 0]
    categories[cat][1] += 1
    if inv:
        categories[cat][0] += 1

cat_names = list(categories.keys())
cat_rates = [categories[c][0] / categories[c][1] for c in cat_names]
cat_labels = [f"{categories[c][0]}/{categories[c][1]}" for c in cat_names]

bars = ax2.barh(cat_names, cat_rates, color=RED, alpha=0.8, height=0.5)
ax2.axvline(x=0.5, color=DARK, linewidth=1, linestyle='--', alpha=0.5)
ax2.set_xlim(0, 1.0)

for i, (rate, label) in enumerate(zip(cat_rates, cat_labels)):
    ax2.text(rate + 0.02, i, f"{rate*100:.0f}% ({label})", va='center', fontsize=11, fontweight='bold')

ax2.set_xlabel("Inversion Rate", fontsize=11)
ax2.set_title("Inversion Rate by Cue Category", fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig3_inversion_rates.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 4: Belief Strength vs Actual Validity Correlation
# ================================================================
print("Generating Figure 4: Belief-validity correlation...")

fig, ax = plt.subplots(figsize=(9, 7))

belief_vals = [c[1] for c in inversion_23]
validity_vals = [abs(c[2]) for c in inversion_23]
inv_flags = [c[4] for c in inversion_23]
colors = [RED if inv else GREEN for inv in inv_flags]

ax.scatter(belief_vals, validity_vals, c=colors, s=100, alpha=0.7, edgecolors='white', linewidth=0.5, zorder=3)

# Trend line
rho, rho_p = stats.spearmanr(belief_vals, validity_vals)
z = np.polyfit(belief_vals, validity_vals, 1)
p_line = np.poly1d(z)
x_range = np.linspace(min(belief_vals)-2, max(belief_vals)+2, 100)
ax.plot(x_range, p_line(x_range), '--', color=GREY, alpha=0.5, label=f'Trend (ρ = {rho:.2f})')

ax.set_xlabel("Belief Endorsement Rate (%)", fontsize=11)
ax.set_ylabel("Actual Validity (|d|)", fontsize=11)
ax.set_title(
    f"Do Stronger Beliefs Indicate More Valid Cues?\n"
    f"Spearman ρ = {rho:.3f}, p = {rho_p:.3f}\n"
    f"{'No significant relationship' if rho_p > .05 else 'Significant'}",
    fontsize=12, fontweight='bold', pad=15
)
ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig4_belief_validity_correlation.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 5: Study 1 — Effect Sizes
# ================================================================
print("Generating Figure 5: Study 1 effect sizes...")

fig, ax = plt.subplots(figsize=(10, 6))

sorted_s1 = sorted(study1_vars, key=lambda x: x[5])  # sort by d
labels = [s[0] for s in sorted_s1]
ds = [s[5] for s in sorted_s1]
ps = [s[6] for s in sorted_s1]

colors_s1 = []
for d, p in zip(ds, ps):
    if p < 0.01:
        colors_s1.append('#1a5276')  # dark blue = significant
    elif p < 0.05:
        colors_s1.append('#2e86c1')
    elif p < 0.10:
        colors_s1.append('#85c1e9')
    else:
        colors_s1.append('#d5dbdb')

bars = ax.barh(range(len(labels)), ds, color=colors_s1, height=0.6, edgecolor='white')
ax.axvline(x=0, color=DARK, linewidth=0.8)
ax.axvline(x=0.10, color=RED, linewidth=1, linestyle='--', alpha=0.5, label='DePaulo median (d=0.10)')

for i, (d, p) in enumerate(zip(ds, ps)):
    sig = "**" if p < .01 else ("*" if p < .05 else "†" if p < .10 else "")
    ax.text(d + 0.02 if d >= 0 else d - 0.08, i, f"d={d:.2f}{sig}", va='center', fontsize=9)

ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=10)
ax.set_xlabel("Cohen's d (positive = higher in truthful speech)", fontsize=11)
ax.set_title(
    "Study 1: Linguistic Markers of Veracity in Trial Testimony\n"
    "N = 121 (Pérez-Rosas et al. 2015 Real-Life Trial Dataset)\n"
    "Disfluency finding: d = 0.60, 6× larger than typical deception cue",
    fontsize=12, fontweight='bold', pad=15
)
ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig5_study1_effect_sizes.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 6: Study 2 — Confession Word Ratios
# ================================================================
print("Generating Figure 6: Confession word ratios...")

fig, ax = plt.subplots(figsize=(10, 6))

words = [w[0] for w in confession_words]
true_rates = [w[1] for w in confession_words]
false_rates = [w[2] for w in confession_words]
ratios = [w[3] for w in confession_words]

x = np.arange(len(words))
width = 0.35

bars1 = ax.bar(x - width/2, true_rates, width, label='True confessions', color='#2e86c1', alpha=0.8)
bars2 = ax.bar(x + width/2, false_rates, width, label='False confessions', color=RED, alpha=0.8)

for i, ratio in enumerate(ratios):
    ax.text(i, max(true_rates[i], false_rates[i]) + 2, f"{ratio:.1f}×",
            ha='center', fontsize=9, fontweight='bold', color=DARK)

ax.set_xticks(x)
ax.set_xticklabels(words, fontsize=10)
ax.set_ylabel("Per-confession frequency", fontsize=11)
ax.set_title(
    "Study 2: Linguistic Distancing in False Confessions\n"
    "Rizzelli et al. (2021): 37 proven false vs 98 presumed true confessions\n"
    "Numbers above bars = false/true ratio (all p < .001)",
    fontsize=12, fontweight='bold', pad=15
)
ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig6_confession_ratios.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 7: Convergence — Detection Accuracy Comparison
# ================================================================
print("Generating Figure 7: Detection accuracy comparison...")

fig, ax = plt.subplots(figsize=(10, 6))

methods = [
    'Human lie detection\n(Bond & DePaulo 2006)',
    'Human overall\n(Bond & DePaulo 2006)',
    'Police/Judges\n(Bond & DePaulo 2006)',
    'Algorithm: disfluency\n(Current Study 1)',
    'Algorithm: multi-var\n(Current Study 1)',
    'Algorithm: 3-predictor\n(Rizzelli 2021)',
]
accuracies = [47, 54, 55, 60.3, 63.5, 78.5]  # midpoint of 74-83
colors_conv = ['#d5dbdb', '#d5dbdb', '#d5dbdb', '#2e86c1', '#2e86c1', '#1a5276']

bars = ax.barh(range(len(methods)), accuracies, color=colors_conv, height=0.6, edgecolor='white')
ax.axvline(x=50, color=RED, linewidth=2, linestyle='--', label='Chance (50%)')

for i, acc in enumerate(accuracies):
    ax.text(acc + 0.5, i, f"{acc:.1f}%", va='center', fontsize=10, fontweight='bold')

ax.set_yticks(range(len(methods)))
ax.set_yticklabels(methods, fontsize=10)
ax.set_xlabel("Classification Accuracy (%)", fontsize=11)
ax.set_xlim(40, 90)
ax.set_title(
    "Study 4: Human vs Algorithmic Deception Detection\n"
    "Grey = human judgment | Blue = linguistic analysis\n"
    "Humans use inverted cues; algorithms use actual markers",
    fontsize=12, fontweight='bold', pad=15
)
ax.legend(fontsize=10, loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig7_detection_accuracy.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 8: ASD Compounding Effect
# ================================================================
print("Generating Figure 8: ASD compounding effect...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left: ASD trait overlap with inverted cues
asd_cues = [
    ("Gaze aversion", 63.7, True),
    ("Fidgeting/stimming", 52.0, True),
    ("Flat affect", 45.0, True),
    ("Disfluent speech", 35.0, True),
    ("Reduced reciprocity", 30.0, True),
    ("Fewer details", 28.0, False),
    ("Response latency", 22.0, True),
    ("Visible anxiety", 45.0, True),
]

names = [a[0] for a in asd_cues]
beliefs = [a[1] for a in asd_cues]
inv = [a[2] for a in asd_cues]
colors_asd = [RED if i else GREEN for i in inv]

sorted_idx = np.argsort(beliefs)
bars = ax1.barh([names[i] for i in sorted_idx], [beliefs[i] for i in sorted_idx],
                color=[colors_asd[i] for i in sorted_idx], height=0.6, alpha=0.85)

ax1.set_xlabel("Global Belief Endorsement Rate (%)", fontsize=11)
ax1.set_title("ASD Features That Trigger\nInverted Deception Cues", fontsize=12, fontweight='bold')
inv_p = mpatches.Patch(color=RED, label='Belief INVERTED')
ali_p = mpatches.Patch(color=GREEN, label='Belief aligned')
ax1.legend(handles=[inv_p, ali_p], fontsize=9)

# Right: Compound effect (simulated)
np.random.seed(42)
n_sims = 50000
cue_probs_asd = [0.85, 0.70, 0.60, 0.55, 0.65, 0.50, 0.45]
cue_probs_nt = [0.15, 0.20, 0.15, 0.10, 0.10, 0.10, 0.20]
cue_weights = [63.7, 52.0, 35.0, 45.0, 52.0, 22.0, 28.0]

asd_scores = np.zeros(n_sims)
nt_scores = np.zeros(n_sims)
for p_a, p_n, w in zip(cue_probs_asd, cue_probs_nt, cue_weights):
    asd_scores += np.random.binomial(1, p_a, n_sims) * w
    nt_scores += np.random.binomial(1, p_n, n_sims) * w

ax2.hist(nt_scores, bins=40, alpha=0.6, color='#2e86c1', label='Neurotypical', density=True)
ax2.hist(asd_scores, bins=40, alpha=0.6, color=RED, label='Autistic', density=True)

pooled = np.sqrt((np.std(asd_scores)**2 + np.std(nt_scores)**2) / 2)
d_compound = (np.mean(asd_scores) - np.mean(nt_scores)) / pooled

ax2.axvline(np.mean(nt_scores), color='#2e86c1', linewidth=2, linestyle='--')
ax2.axvline(np.mean(asd_scores), color=RED, linewidth=2, linestyle='--')

ax2.set_xlabel("'Perceived Deceptiveness' Score\n(sum of triggered inverted cues × belief weight)", fontsize=10)
ax2.set_ylabel("Density", fontsize=11)
ax2.set_title(
    f"Compound Credibility Penalty\n"
    f"Cohen's d = {d_compound:.2f} | Ratio = {np.mean(asd_scores)/np.mean(nt_scores):.1f}×",
    fontsize=12, fontweight='bold'
)
ax2.legend(fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig8_asd_compound_effect.png"), dpi=200, bbox_inches='tight')
plt.close()


# ================================================================
# FIGURE 9: Four Pillars Convergence Summary
# ================================================================
print("Generating Figure 9: Four Pillars convergence...")

fig, ax = plt.subplots(figsize=(10, 6))

pillars = [
    'I. Deception\nDetection',
    'II. Memory\nMalleability',
    'III. False\nConfessions',
    'IV. Pre-Interrogation\nSuggestibility',
]
# Normalized "distance from truth-finding" (higher = worse)
values = [
    0.54,   # 54% accuracy (barely above chance)
    0.72,   # d = 0.72 memory distortion
    0.21,   # 21% midpoint of 12-30% false confession rate
    1.0,    # 100% = doubles suggestibility
]
descriptions = [
    '54% accuracy\n(chance = 50%)',
    'd = 0.72\n(~1 in 4 memories altered)',
    '12-30%\n(of exonerations)',
    '+80-120%\n(doubles baseline)',
]

colors_p = ['#e74c3c', '#e67e22', '#f39c12', '#c0392b']

bars = ax.bar(range(len(pillars)), values, color=colors_p, width=0.6, alpha=0.85, edgecolor='white')

for i, (val, desc) in enumerate(zip(values, descriptions)):
    ax.text(i, val + 0.03, desc, ha='center', fontsize=9, fontweight='bold')

ax.set_xticks(range(len(pillars)))
ax.set_xticklabels(pillars, fontsize=10)
ax.set_ylabel("Effect Magnitude (normalized)", fontsize=11)
ax.set_ylim(0, 1.2)
ax.set_title(
    "Analysis 5: Convergent Validity — Four Independent Pillars\n"
    "All four reject their null hypotheses independently\n"
    "Together: the system produces guilt, not truth",
    fontsize=12, fontweight='bold', pad=15
)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig9_four_pillars.png"), dpi=200, bbox_inches='tight')
plt.close()


print(f"\nAll 9 figures saved to {FIG_DIR}/")
print("  fig1_forest_plot_23cues.png")
print("  fig2_belief_reality_scatter.png")
print("  fig3_inversion_rates.png")
print("  fig4_belief_validity_correlation.png")
print("  fig5_study1_effect_sizes.png")
print("  fig6_confession_ratios.png")
print("  fig7_detection_accuracy.png")
print("  fig8_asd_compound_effect.png")
print("  fig9_four_pillars.png")
