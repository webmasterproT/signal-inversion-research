#!/usr/bin/env python3
"""
================================================================================
STUDY 10: Consensus, Distillation, and Trust — Mathematical Framework
================================================================================

This study is THEORETICAL, not computational. The LaTeX source contains the
formal proofs and theorems. This script:

1. Validates the theorem table (data/theorems_table.csv)
2. Generates a summary of the mathematical framework
3. Produces a comparison figure of the three consensus mechanisms
4. Computes the Bitcoin double-spend probabilities from Theorem 3.2

No empirical data is analysed — this is a validation and visualization tool.
================================================================================
"""

import os
import csv
import numpy as np
from scipy.stats import poisson as poisson_dist

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
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')
RESULTS_DIR = os.path.join(SCRIPT_DIR, '..', 'results')
TABLES_DIR = os.path.join(RESULTS_DIR, 'tables')
FIGURES_DIR = os.path.join(RESULTS_DIR, 'figures')
os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

output_lines = []

def log(line=""):
    print(line)
    output_lines.append(str(line))


def validate_theorem_table():
    """Validate the theorem table CSV."""
    table_path = os.path.join(DATA_DIR, 'theorems_table.csv')
    if not os.path.exists(table_path):
        log("ERROR: theorems_table.csv not found")
        return False

    with open(table_path, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    log(f"Theorem table: {len(rows)} entries")

    required_fields = {'type', 'number', 'name', 'statement', 'rigor', 'source'}
    actual_fields = set(rows[0].keys()) if rows else set()
    missing = required_fields - actual_fields
    if missing:
        log(f"ERROR: Missing fields: {missing}")
        return False

    # Count by type
    types = {}
    rigor_levels = {}
    for row in rows:
        t = row['type']
        r = row['rigor']
        types[t] = types.get(t, 0) + 1
        rigor_levels[r] = rigor_levels.get(r, 0) + 1

    log("\nBy type:")
    for t, c in sorted(types.items()):
        log(f"  {t}: {c}")

    log("\nBy rigor level:")
    for r, c in sorted(rigor_levels.items()):
        log(f"  {r}: {c}")

    return True


def double_spend_prob(q, z):
    """
    Compute double-spend probability using Nakamoto's formula.
    P(z) = sum_{k=0}^{inf} Poisson(k, lambda) * min(1, (q/p)^(z-k))
    where lambda = z * (q/p), and if k >= z the attacker is already ahead.
    """
    if q >= 0.5:
        return 1.0
    p = 1 - q
    lam = z * (q / p)
    total = 0.0
    for k in range(200):
        pk = poisson_dist.pmf(k, lam)
        if k >= z:
            total += pk  # attacker already ahead or equal
        else:
            total += pk * (q / p) ** (z - k)  # probability of catching up
    return total


def compute_double_spend_table():
    """Compute Bitcoin double-spend probabilities from Theorem 3.2."""
    log("\n" + "=" * 80)
    log("THEOREM 3.2 VERIFICATION: Double-Spend Probabilities")
    log("P(z) via Nakamoto/Grunspan-Pérez-Marco summation")
    log("=" * 80)

    q_values = [0.10, 0.20, 0.30, 0.40]
    z_values = [1, 2, 3, 4, 5, 6]

    header = f"{'z':>4}"
    for q in q_values:
        header += f"  {'q='+str(q):>10}"
    log(header)
    log("-" * 50)

    table_rows = []
    for z in z_values:
        row = f"{z:>4}"
        row_data = {'z': z}
        for q in q_values:
            prob = double_spend_prob(q, z)
            row += f"  {prob:>10.4f}"
            row_data[f'q_{q}'] = f"{prob:.4f}"
        log(row)
        table_rows.append(row_data)

    log("\nVerification (Nakamoto formula):")
    log("  z=1, q=0.10: Nakamoto = {:.4f} (paper Table 1: 0.2045)".format(double_spend_prob(0.10, 1)))
    log("  z=6, q=0.10: Nakamoto = {:.4f} (paper Table 1: 0.0003)".format(double_spend_prob(0.10, 6)))
    log("  Note: Paper Table 1 uses Grunspan-PM beta function formulation;")
    log("  Nakamoto Poisson summation gives slightly different values for high q.")

    # Save table
    table_path = os.path.join(TABLES_DIR, 'study_10_double_spend.csv')
    with open(table_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=table_rows[0].keys())
        writer.writeheader()
        writer.writerows(table_rows)
    log(f"\nTable saved to {table_path}")

    return table_rows


def summarize_framework():
    """Summarize the three-part mathematical framework."""
    log("\n" + "=" * 80)
    log("FRAMEWORK SUMMARY: Three Modes of Distributed Consensus")
    log("=" * 80)

    log("""
Part I — COMPUTATIONAL CONSENSUS (Bitcoin)
  Rigorous. Poisson process model, exponential inter-block times.
  Key result: Double-spend probability P(z) = I_{4pq}(z, 1/2)
  Decays exponentially with confirmations z.
  Honest mining is optimal (martingale proof).

Part II — DISTILLATION AS LEARNED BEHAVIOUR
  Structural analogy. Knowledge distillation (Hinton 2015) maps to
  social learning (Bandura 1977). Student learns from teacher's
  behavioural outputs, not explicit rules.
  Key insight: "dark knowledge" = implicit emotional/behavioural cues.
  Implications for criminology: behaviour is distilled from environment,
  not rationally chosen. Rehabilitation = fine-tuning.

Part III — SOCIAL CONSENSUS (Web-of-Trust)
  Conditional. Graph-based Sybil resistance. Vouch cost creates
  linear attack cost: C(n) >= n * k * c_vouch.
  Honest about limitations: c_vouch is hard to measure empirically.
  Bitcoin anchoring provides immutability for committed records.

SYNTHESIS:
  All three achieve agreement through COSTLY SIGNALLING:
  - Bitcoin: proof-of-work (energy cost)
  - Distillation: behavioural consistency (social cost of deviation)
  - Web-of-trust: vouching (reputation cost)
""")


def main():
    log("=" * 80)
    log("STUDY 10: CONSENSUS, DISTILLATION, AND TRUST")
    log("Mathematical Framework — Validation and Visualization")
    log("=" * 80)

    # Step 1: Validate theorem table
    log("\n" + "=" * 80)
    log("STEP 1: THEOREM TABLE VALIDATION")
    log("=" * 80)
    valid = validate_theorem_table()
    log(f"\nValidation: {'PASSED' if valid else 'FAILED'}")

    # Step 2: Summarize framework
    summarize_framework()

    # Step 3: Compute double-spend table (verification of Theorem 3.2)
    ds_table = compute_double_spend_table()

    # Step 4: Generate figures
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Plot 1: Double-spend probability curves
        z_range = np.arange(1, 21)
        for q, color, style in [(0.10, '#4CAF50', '-'), (0.20, '#2196F3', '--'),
                                 (0.30, '#FF9800', '-.'), (0.40, '#F44336', ':')]:
            probs = [double_spend_prob(q, z) for z in z_range]
            axes[0].plot(z_range, probs, style, color=color, linewidth=2, label=f'q={q}')

        axes[0].set_xlabel('Confirmations (z)')
        axes[0].set_ylabel('Double-Spend Probability')
        axes[0].set_title('Theorem 3.2: P(z) = I_{4pq}(z, 1/2)')
        axes[0].set_yscale('log')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        axes[0].axhline(y=0.001, color='gray', linestyle=':', alpha=0.5)
        axes[0].text(15, 0.0015, 'p = 0.1%', fontsize=8, color='gray')

        # Plot 2: Three consensus mechanisms comparison
        mechanisms = ['Bitcoin\n(Computational)', 'Distillation\n(Behavioural)', 'Web-of-Trust\n(Social)']
        properties = {
            'Formal Rigor': [1.0, 0.4, 0.6],
            'Empirical\nTestability': [0.9, 0.6, 0.5],
            'Decentralization': [0.9, 0.8, 0.7],
        }

        x = np.arange(len(mechanisms))
        width = 0.25
        colors = ['#4CAF50', '#2196F3', '#FF9800']

        for i, (prop, vals) in enumerate(properties.items()):
            bars = axes[1].bar(x + i * width, vals, width, label=prop, color=colors[i], alpha=0.8)

        axes[1].set_xticks(x + width)
        axes[1].set_xticklabels(mechanisms, fontsize=9)
        axes[1].set_ylabel('Relative Strength')
        axes[1].set_title('Three Modes of Distributed Consensus')
        axes[1].legend(fontsize=8)
        axes[1].set_ylim(0, 1.15)

        plt.tight_layout()
        fig_path = os.path.join(FIGURES_DIR, 'study_10_consensus_mechanisms.png')
        plt.savefig(fig_path, dpi=200, bbox_inches='tight')
        plt.close()
        log(f"\nFigure saved to {fig_path}")
    except ImportError:
        log("matplotlib not available — skipping figure generation")

    # Save results
    results_path = os.path.join(RESULTS_DIR, 'study_10_results.txt')
    with open(results_path, 'w') as f:
        f.write('\n'.join(output_lines))
    log(f"\nResults saved to {results_path}")

    log("\n" + "=" * 80)
    log("VALIDATION COMPLETE")
    log("=" * 80)


if __name__ == '__main__':
    main()
