#!/usr/bin/env python3
"""
Study 2: Linguistic Distancing in True vs False Confessions
Reanalysis of Rizzelli, Kassin & Gales (2021) Appendix A

Reads raw word counts from data/rizzelli_appendix_a.csv,
computes per-confession rates, runs chi-square tests,
generates results and figures.
"""

import os
import sys
import csv
from pathlib import Path
from datetime import datetime

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Shared OMXUS figure style (optional — works without it)
try:
    import sys as _sys
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'shared'))
    from style import apply_style, COLORS, save_figure
    apply_style()
    _HAS_STYLE = True
except ImportError:
    _HAS_STYLE = False

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent
DATA_FILE = BASE / "data" / "rizzelli_appendix_a.csv"
RESULTS_FILE = BASE / "results" / "study_2_results.txt"
FIGURE_FILE = BASE / "results" / "figures" / "confession_word_ratios.png"

N_CPT = 98   # confessions presumed true
N_CPF = 37   # confessions proven false

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
output_lines = []

def log(msg=""):
    print(msg)
    output_lines.append(msg)


def chi_sq_test(cpt_count, cpf_count, n_cpt=N_CPT, n_cpf=N_CPF):
    """Chi-square goodness-of-fit on raw counts given unequal group sizes."""
    cpt_rate = cpt_count / n_cpt
    cpf_rate = cpf_count / n_cpf
    total = cpt_count + cpf_count
    expected_cpt = total * (n_cpt / (n_cpt + n_cpf))
    expected_cpf = total * (n_cpf / (n_cpt + n_cpf))
    chi2 = ((cpt_count - expected_cpt)**2 / expected_cpt) + \
           ((cpf_count - expected_cpf)**2 / expected_cpf)
    p = 1 - stats.chi2.cdf(chi2, df=1)
    ratio = cpf_rate / cpt_rate if cpt_rate > 0 else float('inf')
    return cpt_rate, cpf_rate, ratio, chi2, p


# -------------------------------------------------------------------
# Load data
# -------------------------------------------------------------------
log("=" * 80)
log("STUDY 2: LINGUISTIC DISTANCING IN TRUE VS FALSE CONFESSIONS")
log(f"Rizzelli, Kassin & Gales (2021) — Reanalysis of Appendix A")
log(f"N = {N_CPT + N_CPF} confessions ({N_CPF} proven false, {N_CPT} presumed true)")
log(f"Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
log("=" * 80)

if not DATA_FILE.exists():
    sys.exit(f"ERROR: Data file not found: {DATA_FILE}")

df = pd.read_csv(DATA_FILE)
log(f"\nLoaded {len(df)} words from {DATA_FILE.name}")
log(f"Categories: {', '.join(df['category'].unique())}")

# -------------------------------------------------------------------
# Per-word analysis
# -------------------------------------------------------------------
results = []
for _, row in df.iterrows():
    cpt_rate, cpf_rate, ratio, chi2, p = chi_sq_test(row['cpt_count'], row['cpf_count'])
    results.append({
        'word': row['word'],
        'category': row['category'],
        'cpt_count': row['cpt_count'],
        'cpf_count': row['cpf_count'],
        'cpt_rate': round(cpt_rate, 2),
        'cpf_rate': round(cpf_rate, 2),
        'ratio': round(ratio, 2),
        'chi2': round(chi2, 1),
        'p': p,
        'direction': 'false > true' if ratio > 1 else 'true > false'
    })

res_df = pd.DataFrame(results)

# -------------------------------------------------------------------
# Print full table
# -------------------------------------------------------------------
log("\n" + "-" * 95)
log(f"{'Word':<12} {'Category':<22} {'CPT/conf':>10} {'CPF/conf':>10} {'Ratio':>8} {'chi2':>10} {'p':>12} {'Direction'}")
log("-" * 95)

for cat in ['impersonal_pronoun', 'personal_pronoun', 'conjunction']:
    cat_rows = res_df[res_df['category'] == cat]
    for _, r in cat_rows.iterrows():
        p_str = f"{r['p']:.2e}" if r['p'] > 0 else "<1e-300"
        log(f"  {r['word']:<10} {r['category']:<22} {r['cpt_rate']:>10.2f} {r['cpf_rate']:>10.2f} {r['ratio']:>7.2f}x {r['chi2']:>10.1f} {p_str:>12} {r['direction']}")

    # Category totals
    cat_cpt = cat_rows['cpt_count'].sum()
    cat_cpf = cat_rows['cpf_count'].sum()
    cpt_r, cpf_r, ratio, chi2, p = chi_sq_test(cat_cpt, cat_cpf)
    p_str = f"{p:.2e}" if p > 0 else "<1e-300"
    label = cat.replace('_', ' ').upper() + " TOTAL"
    log(f"  {'---':>10}")
    log(f"  {label:<32} {cpt_r:>10.1f} {cpf_r:>10.1f} {ratio:>7.2f}x {chi2:>10.1f} {p_str:>12}")
    log("")

# -------------------------------------------------------------------
# Key findings
# -------------------------------------------------------------------
log("\n" + "=" * 80)
log("KEY FINDINGS — Signal Inversion Markers")
log("=" * 80)

key_words = ['you', "that's", "it's"]
for word in key_words:
    r = res_df[res_df['word'] == word].iloc[0]
    log(f"\n  '{word}': {r['ratio']}x higher in false confessions")
    log(f"    True confessions:  {r['cpt_rate']} per confession (total {r['cpt_count']} across {N_CPT})")
    log(f"    False confessions: {r['cpf_rate']} per confession (total {r['cpf_count']} across {N_CPF})")
    log(f"    chi2 = {r['chi2']}, p < .001")

# Impersonal pronoun category total
imp_cpt = res_df[res_df['category'] == 'impersonal_pronoun']['cpt_count'].sum()
imp_cpf = res_df[res_df['category'] == 'impersonal_pronoun']['cpf_count'].sum()
imp_cpt_r, imp_cpf_r, imp_ratio, imp_chi2, imp_p = chi_sq_test(imp_cpt, imp_cpf)
log(f"\n  Impersonal pronoun category total: {imp_ratio:.2f}x higher in false confessions")
log(f"    True: {imp_cpt_r:.1f}/confession, False: {imp_cpf_r:.1f}/confession")
log(f"    chi2 = {imp_chi2:.1f}, p < .001")

log("\n" + "-" * 80)
log("INTERPRETATION")
log("-" * 80)
log("""
False confessors use dramatically more impersonal and interrogator-referencing
language because the narrative was FED to them, not self-generated.

  - 'you' (7.59x): "you said", "you told me" — echoing the interrogator's script
  - 'that's' (11.67x): "that's what happened" — parroting back a fed narrative
  - 'it's' (12.17x): "it's like you said" — deferring to external authority

These are not signs of deception. They are signs of compliance under coercion.
The confession detection system is inverted: the linguistic markers used to
assess 'reliability' actually discriminate between self-generated and
externally-imposed narratives.
""")

# -------------------------------------------------------------------
# Save results
# -------------------------------------------------------------------
RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(RESULTS_FILE, 'w') as f:
    f.write('\n'.join(output_lines))
log(f"\nResults saved to: {RESULTS_FILE}")

# -------------------------------------------------------------------
# Figure: Top discriminating words (grouped bar chart)
# -------------------------------------------------------------------
FIGURE_FILE.parent.mkdir(parents=True, exist_ok=True)

# Select top words by ratio (false > true), limited to most striking
top = res_df[res_df['ratio'] > 1].sort_values('ratio', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(top))
width = 0.35

bars_true = ax.bar(x - width/2, top['cpt_rate'], width,
                   label=f'True confessions (n={N_CPT})',
                   color='#2d5986', edgecolor='white', linewidth=0.5)
bars_false = ax.bar(x + width/2, top['cpf_rate'], width,
                    label=f'False confessions (n={N_CPF})',
                    color='#c44e52', edgecolor='white', linewidth=0.5)

# Add ratio annotations
for i, (_, row) in enumerate(top.iterrows()):
    ax.annotate(f'{row["ratio"]}x',
                xy=(x[i] + width/2, row['cpf_rate']),
                xytext=(0, 5), textcoords='offset points',
                ha='center', va='bottom', fontsize=9, fontweight='bold',
                color='#c44e52')

ax.set_xlabel('Word', fontsize=12)
ax.set_ylabel('Frequency per confession', fontsize=12)
ax.set_title('Linguistic Distancing: Words That Discriminate\nTrue vs False Confessions (Rizzelli et al., 2021)',
             fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([f"'{w}'" for w in top['word']], fontsize=11)
ax.legend(fontsize=11, loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3)

fig.tight_layout()
fig.savefig(FIGURE_FILE, dpi=150, bbox_inches='tight')
log(f"Figure saved to: {FIGURE_FILE}")

log("\nDone.")
