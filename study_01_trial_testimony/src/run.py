#!/usr/bin/env python3
"""
Study 1: Linguistic Markers of Veracity in Trial Testimony
Signal Inversion Effect — Standalone Analysis

Dataset: Perez-Rosas et al. (2015) Real-Life Trial Corpus
N = 121 (60 truthful, 61 deceptive)
Ground truth: verdicts + post-conviction exonerations
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.optimize import minimize
from scipy.special import expit
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import csv

# Shared OMXUS figure style (optional — works without it)
try:
    import sys as _sys
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'shared'))
    from style import apply_style, COLORS, save_figure
    apply_style()
    _HAS_STYLE = True
except ImportError:
    _HAS_STYLE = False

# ── Paths ──────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")

os.makedirs(FIGURES_DIR, exist_ok=True)

output_lines = []
def log(text=""):
    print(text)
    output_lines.append(text)

# ── Load Data ──────────────────────────────────────────────────────
log("=" * 80)
log("STUDY 1: LINGUISTIC MARKERS OF VERACITY IN TRIAL TESTIMONY")
log("Dataset: Perez-Rosas et al. (2015) Real-Life Trial Corpus")
log("N = 121 (60 truthful, 61 deceptive)")
log("=" * 80)

df = pd.read_csv(os.path.join(DATA_DIR, "spss_ready.csv"))
truth = df[df['label'] == 0]
decep = df[df['label'] == 1]

log(f"\nSample: {len(truth)} truthful, {len(decep)} deceptive clips")

# ── Mann-Whitney U Tests ──────────────────────────────────────────
variables = ['hedging_rate', 'certainty_rate', 'filler_rate', 'experiencer_rate',
             'passive_rate', 'neg_emotion_rate', 'first_person_rate', 'word_count']
var_labels = ['Hedging Rate', 'Certainty Markers', 'Disfluency/Filler Rate',
              'Experiencer Framing', 'Passive Constructions', 'Negative Emotion',
              'First-Person Pronouns', 'Word Count']

log("\nTable 1: Group Comparisons (Mann-Whitney U Test)")
log("-" * 120)
log(f"{'Variable':35s} {'Truth M':>9s} {'Truth SD':>9s} {'Decep M':>9s} {'Decep SD':>9s} {'U':>10s} {'p':>8s} {'d':>7s} {'r_pb':>7s} {'Sig':>5s}")
log("-" * 120)

study1_results = {}
table_rows = []

for var, label in zip(variables, var_labels):
    t_vals = truth[var].values
    d_vals = decep[var].values

    t_mean, t_sd = np.mean(t_vals), np.std(t_vals, ddof=1)
    d_mean, d_sd = np.mean(d_vals), np.std(d_vals, ddof=1)

    u_stat, u_p = stats.mannwhitneyu(t_vals, d_vals, alternative='two-sided')

    # Cohen's d
    pooled_sd = np.sqrt(((len(t_vals)-1)*t_sd**2 + (len(d_vals)-1)*d_sd**2) / (len(t_vals)+len(d_vals)-2))
    cohens_d = (t_mean - d_mean) / pooled_sd if pooled_sd > 0 else 0

    # Point-biserial correlation
    all_vals = np.concatenate([t_vals, d_vals])
    all_labels = np.concatenate([np.ones(len(t_vals)), np.zeros(len(d_vals))])  # 1=truth
    r_pb, r_p = stats.pointbiserialr(all_labels, all_vals)

    sig = "**" if u_p < .01 else ("*" if u_p < .05 else "\u2020" if u_p < .10 else "ns")

    study1_results[var] = {
        'label': label, 't_mean': t_mean, 't_sd': t_sd, 'd_mean': d_mean, 'd_sd': d_sd,
        'u': u_stat, 'p': u_p, 'd': cohens_d, 'r_pb': r_pb, 'r_p': r_p, 'sig': sig
    }

    table_rows.append({
        'Variable': label, 'Truth_M': round(t_mean, 4), 'Truth_SD': round(t_sd, 4),
        'Decep_M': round(d_mean, 4), 'Decep_SD': round(d_sd, 4),
        'U': round(u_stat, 1), 'p': round(u_p, 4), 'Cohen_d': round(cohens_d, 2),
        'r_pb': round(r_pb, 3), 'Sig': sig
    })

    log(f"{label:35s} {t_mean:9.2f} {t_sd:9.2f} {d_mean:9.2f} {d_sd:9.2f} {u_stat:10.1f} {u_p:8.4f} {cohens_d:7.2f} {r_pb:7.3f} {sig:>5s}")

log("-" * 120)
log("* p < .05, ** p < .01, \u2020 p < .10")

# ── Effect Size Context ───────────────────────────────────────────
log("\nEffect Size Context:")
log(f"  DePaulo et al. (2003) median cue effect size: d = 0.10")
log(f"  Current disfluency finding: d = {study1_results['filler_rate']['d']:.2f}")
log(f"  Ratio: {abs(study1_results['filler_rate']['d']) / 0.10:.1f}x larger than typical deception cue")

# ── Logistic Regression (Single Predictor) ────────────────────────
log("\nBinary Classification Analysis:")
log("  (Logistic regression via maximum likelihood estimation)")

X = df['filler_rate'].values
y = 1 - df['label'].values  # 0=deceptive, 1=truthful (flip from original coding)

def neg_log_likelihood(params, X, y):
    b0, b1 = params
    p = expit(b0 + b1 * X)
    p = np.clip(p, 1e-10, 1 - 1e-10)
    return -np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))

result = minimize(neg_log_likelihood, [0, 0], args=(X, y), method='Nelder-Mead')
b0, b1 = result.x
predictions = (expit(b0 + b1 * X) > 0.5).astype(int)
accuracy = np.mean(predictions == y)
log(f"  Disfluency-only model: B0={b0:.3f}, B1={b1:.3f}")
log(f"  Classification accuracy: {accuracy*100:.1f}%")
log(f"  (Chance = 50%, Human deception detection = 54%)")

# ── Multi-Variable Logistic Regression (10-fold CV) ──────────────
feature_cols = ['filler_rate', 'hedging_rate', 'certainty_rate', 'experiencer_rate', 'neg_emotion_rate', 'first_person_rate']
X_multi = df[feature_cols].values
y_multi = 1 - df['label'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_multi)

lr = LogisticRegression(max_iter=1000, random_state=42)
cv_scores = cross_val_score(lr, X_scaled, y_multi, cv=10, scoring='accuracy')
log(f"\n  Multi-variable model (10-fold cross-validation):")
log(f"  Variables: {', '.join(feature_cols)}")
log(f"  Mean accuracy: {cv_scores.mean()*100:.1f}% (SD={cv_scores.std()*100:.1f}%)")
log(f"  Range: {cv_scores.min()*100:.1f}% - {cv_scores.max()*100:.1f}%")

# Fit full model for coefficients
lr.fit(X_scaled, y_multi)
log(f"\n  Full model coefficients (standardised):")
for feat, coef in zip(feature_cols, lr.coef_[0]):
    direction = "\u2191 Truth" if coef > 0 else "\u2191 Decep"
    log(f"    {feat:25s}: \u03b2 = {coef:+.3f}  {direction}")

# ── Save Results Text ─────────────────────────────────────────────
results_path = os.path.join(RESULTS_DIR, "study_1_results.txt")
with open(results_path, 'w') as f:
    f.write('\n'.join(output_lines))
log(f"\nResults saved to: {results_path}")

# ── Save Table CSV ────────────────────────────────────────────────
table_path = os.path.join(RESULTS_DIR, "study_1_table.csv")
keys = ['Variable', 'Truth_M', 'Truth_SD', 'Decep_M', 'Decep_SD', 'U', 'p', 'Cohen_d', 'r_pb', 'Sig']
with open(table_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(table_rows)
log(f"Table saved to: {table_path}")

# ── Effect Size Bar Chart ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

labels_sorted = sorted(study1_results.items(), key=lambda x: abs(x[1]['d']), reverse=True)
bar_labels = [v['label'] for _, v in labels_sorted]
bar_values = [v['d'] for _, v in labels_sorted]
bar_colors = ['#2ecc71' if d > 0 else '#e74c3c' for d in bar_values]
bar_sigs = [v['sig'] for _, v in labels_sorted]

bars = ax.barh(range(len(bar_labels)), bar_values, color=bar_colors, edgecolor='#333', linewidth=0.5)
ax.set_yticks(range(len(bar_labels)))
ax.set_yticklabels(bar_labels, fontsize=11)
ax.set_xlabel("Cohen's d (positive = higher in truthful speakers)", fontsize=12)
ax.set_title("Study 1: Effect Sizes for Linguistic Veracity Markers\n"
             "Perez-Rosas et al. (2015) Trial Corpus, N=121", fontsize=13, fontweight='bold')

# Add significance markers
for i, (bar, sig) in enumerate(zip(bars, bar_sigs)):
    width = bar.get_width()
    offset = 0.02 if width >= 0 else -0.02
    ha = 'left' if width >= 0 else 'right'
    if sig != 'ns':
        ax.text(width + offset, bar.get_y() + bar.get_height()/2, sig, va='center', ha=ha, fontsize=10, fontweight='bold')

# Reference line: DePaulo median
ax.axvline(x=0, color='black', linewidth=0.8)
ax.axvline(x=0.10, color='gray', linewidth=1, linestyle='--', alpha=0.7)
ax.axvline(x=-0.10, color='gray', linewidth=1, linestyle='--', alpha=0.7)
ax.text(0.10, len(bar_labels) - 0.3, 'DePaulo\nmedian\nd=0.10', fontsize=8, color='gray', ha='center')

ax.invert_yaxis()
plt.tight_layout()

fig_path = os.path.join(FIGURES_DIR, "effect_sizes.png")
fig.savefig(fig_path, dpi=150, bbox_inches='tight')
plt.close()
log(f"Figure saved to: {fig_path}")

log("\nDone.")
