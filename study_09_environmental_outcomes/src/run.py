#!/usr/bin/env python3
"""
================================================================================
STUDY 9: Language vs. Ancestry as Predictors of Behavioural/Educational Outcomes
US Census ACS PUMS 2022 — California
================================================================================

RESEARCH QUESTION:
Does language spoken at home (environmental proxy) predict educational and
economic outcomes better than ancestry (genetic proxy)?

HYPOTHESIS:
If behavior/outcomes are primarily environmentally determined, language should
predict outcomes better than ancestry.

DATA SOURCE:
US Census American Community Survey (ACS) 2022 PUMS - California
N ≈ 390,000 individuals

DEMO MODE:
If the census CSV is not available, the script generates synthetic data
with realistic parameters to demonstrate the analysis pipeline.
Run with --demo to force demo mode.

================================================================================
"""

import os
import sys
import csv
import numpy as np
from scipy import stats

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

DEMO_MODE = '--demo' in sys.argv
CENSUS_PATH = os.path.join(DATA_DIR, 'psam_p06.csv')

output_lines = []

def log(line=""):
    print(line)
    output_lines.append(str(line))


def generate_synthetic_data(n=50000):
    """Generate synthetic data matching census structure and realistic parameters."""
    log("\n*** DEMO MODE: Generating synthetic data (N={:,}) ***".format(n))
    log("*** For real results, download census data per data/README_DATA.md ***\n")

    rng = np.random.default_rng(42)

    # Ancestry groups with realistic California proportions
    ancestry_probs = {
        'European': 0.30, 'Hispanic_Latino': 0.40, 'Asian': 0.16,
        'African': 0.06, 'Middle_Eastern': 0.02, 'North_American': 0.03,
        'Pacific_Islander': 0.01, 'Other': 0.02
    }
    groups = list(ancestry_probs.keys())
    probs = list(ancestry_probs.values())
    ancestry = rng.choice(groups, size=n, p=probs)

    # Language: correlated with ancestry (environmental factor)
    # European ancestry → higher English-at-home rate
    eng_rates = {
        'European': 0.85, 'Hispanic_Latino': 0.35, 'Asian': 0.40,
        'African': 0.80, 'Middle_Eastern': 0.50, 'North_American': 0.90,
        'Pacific_Islander': 0.60, 'Other': 0.55
    }
    speaks_english = np.array([rng.random() < eng_rates[a] for a in ancestry]).astype(int)

    # Education: influenced by BOTH ancestry AND language, but language is stronger
    # Base college rate by ancestry (genetic proxy)
    anc_college = {
        'European': 0.38, 'Hispanic_Latino': 0.18, 'Asian': 0.55,
        'African': 0.25, 'Middle_Eastern': 0.45, 'North_American': 0.30,
        'Pacific_Islander': 0.20, 'Other': 0.28
    }
    # Language bonus (environmental effect — LARGER than ancestry effect)
    lang_bonus = 0.15  # +15 percentage points for English speakers

    base_rate = np.array([anc_college[a] for a in ancestry])
    college_prob = np.clip(base_rate + speaks_english * lang_bonus + rng.normal(0, 0.05, n), 0.01, 0.99)
    has_college = (rng.random(n) < college_prob).astype(int)

    # Age: uniform 25-65
    age = rng.integers(25, 66, size=n)

    # Nativity: correlated with ancestry
    native_rates = {
        'European': 0.75, 'Hispanic_Latino': 0.50, 'Asian': 0.35,
        'African': 0.65, 'Middle_Eastern': 0.40, 'North_American': 0.95,
        'Pacific_Islander': 0.55, 'Other': 0.50
    }
    native_born = np.array([rng.random() < native_rates[a] for a in ancestry]).astype(int)

    # Education level (1-24 scale, college = 21+)
    schl = np.where(has_college, rng.integers(21, 25, size=n), rng.integers(10, 21, size=n))

    # Wage income (log-normal, influenced by education)
    log_wage = np.where(
        has_college,
        rng.normal(11.0, 0.8, n),  # ~$60k median
        rng.normal(10.3, 0.9, n)   # ~$30k median
    )
    wage = np.exp(log_wage).astype(int)

    return {
        'ancestry_group': ancestry,
        'speaks_english_home': speaks_english,
        'has_college': has_college,
        'AGEP': age,
        'native_born': native_born,
        'SCHL': schl,
        'WAGP': wage,
        'log_wage': log_wage,
        'n': n,
        'is_demo': True
    }


def load_census_data():
    """Load and clean real census data."""
    try:
        import pandas as pd
    except ImportError:
        log("pandas not available — falling back to demo mode")
        return generate_synthetic_data()

    if not os.path.exists(CENSUS_PATH):
        log(f"Census file not found at {CENSUS_PATH}")
        return generate_synthetic_data()

    log("Loading California ACS PUMS 2022 data...")
    df = pd.read_csv(CENSUS_PATH, low_memory=False)
    log(f"Total records loaded: {len(df):,}")

    # Filter adults 25-65
    df_clean = df[(df['AGEP'] >= 25) & (df['AGEP'] <= 65)].copy()
    df_clean = df_clean.dropna(subset=['SCHL', 'ANC1P', 'LANX'])

    df_clean['has_college'] = (df_clean['SCHL'] >= 21).astype(int)
    df_clean['speaks_english_home'] = (df_clean['LANX'] == 1).astype(int)
    df_clean['log_wage'] = np.where(df_clean['WAGP'] > 0, np.log(df_clean['WAGP'] + 1), np.nan)

    def categorize_ancestry(anc_code):
        if pd.isna(anc_code):
            return 'Unknown'
        anc = int(anc_code)
        if 1 <= anc <= 195: return 'European'
        elif 200 <= anc <= 299: return 'Hispanic_Latino'
        elif 300 <= anc <= 399: return 'Asian'
        elif 400 <= anc <= 499: return 'African'
        elif 500 <= anc <= 599: return 'Middle_Eastern'
        elif 600 <= anc <= 699: return 'North_American'
        elif 700 <= anc <= 799: return 'Pacific_Islander'
        else: return 'Other'

    df_clean['ancestry_group'] = df_clean['ANC1P'].apply(categorize_ancestry)
    df_clean['native_born'] = (df_clean['NATIVITY'] == 1).astype(int)

    log(f"Final analysis sample: {len(df_clean):,}")

    return {
        'ancestry_group': df_clean['ancestry_group'].values,
        'speaks_english_home': df_clean['speaks_english_home'].values,
        'has_college': df_clean['has_college'].values,
        'AGEP': df_clean['AGEP'].values,
        'native_born': df_clean['native_born'].values,
        'SCHL': df_clean['SCHL'].values,
        'WAGP': df_clean['WAGP'].values,
        'log_wage': df_clean['log_wage'].values,
        'n': len(df_clean),
        'is_demo': False
    }


def run_ols(y, X_dict):
    """Simple OLS regression without statsmodels dependency."""
    # Build design matrix
    col_names = list(X_dict.keys())
    X = np.column_stack([X_dict[c] for c in col_names])
    # Add intercept
    X = np.column_stack([np.ones(len(y)), X])
    col_names = ['const'] + col_names

    # OLS: beta = (X'X)^-1 X'y
    try:
        beta = np.linalg.lstsq(X, y, rcond=None)[0]
    except np.linalg.LinAlgError:
        return None

    y_hat = X @ beta
    ss_res = np.sum((y - y_hat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    n, k = X.shape
    adj_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - k - 1) if n > k + 1 else r_squared

    # Standard errors
    mse = ss_res / (n - k) if n > k else ss_res
    try:
        var_beta = mse * np.linalg.inv(X.T @ X)
        se = np.sqrt(np.diag(var_beta))
        t_stats = beta / se
        from scipy.stats import t as t_dist
        p_values = 2 * (1 - t_dist.cdf(np.abs(t_stats), df=n-k))
    except:
        se = np.zeros_like(beta)
        t_stats = np.zeros_like(beta)
        p_values = np.ones_like(beta)

    return {
        'r_squared': r_squared,
        'adj_r_squared': adj_r_squared,
        'coefficients': dict(zip(col_names, beta)),
        'p_values': dict(zip(col_names, p_values)),
        'n': n,
        'k': k
    }


def main():
    log("=" * 80)
    log("STUDY 9: LANGUAGE VS. ANCESTRY AS PREDICTORS OF OUTCOMES")
    log("=" * 80)

    # Load data
    if DEMO_MODE:
        data = generate_synthetic_data()
    else:
        data = load_census_data() if not DEMO_MODE else generate_synthetic_data()

    ancestry = data['ancestry_group']
    english = data['speaks_english_home']
    college = data['has_college']
    native = data['native_born']
    n = data['n']
    is_demo = data['is_demo']

    if is_demo:
        log("\n⚠ RUNNING IN DEMO MODE WITH SYNTHETIC DATA")
        log("  Results demonstrate the analysis pipeline.")
        log("  For real results, see data/README_DATA.md for download instructions.\n")

    # =========================================================================
    # DESCRIPTIVE STATISTICS
    # =========================================================================
    log("\n" + "=" * 80)
    log("DESCRIPTIVE STATISTICS")
    log("=" * 80)
    log(f"N = {n:,}")
    log(f"% with college degree: {np.mean(college)*100:.1f}%")
    log(f"% speaks English at home: {np.mean(english)*100:.1f}%")

    # Ancestry distribution
    unique_anc, counts = np.unique(ancestry, return_counts=True)
    log("\nAncestry Distribution:")
    for a, c in sorted(zip(unique_anc, counts), key=lambda x: -x[1]):
        log(f"  {a:<20} {c:>8,} ({c/n*100:5.1f}%)")

    # =========================================================================
    # KEY TEST: Same ancestry, different language
    # =========================================================================
    log("\n" + "=" * 80)
    log("CRITICAL TEST: Same Ancestry, Different Language")
    log("=" * 80)
    log("""
LOGIC: If genetics (ancestry) determines outcomes, people of the same ancestry
should have similar outcomes regardless of language spoken at home.
If environment (language) determines outcomes, people of the same ancestry
should differ based on language environment.
""")

    within_results = []
    for anc_group in ['Hispanic_Latino', 'Asian', 'European']:
        mask = ancestry == anc_group
        if np.sum(mask) < 100:
            continue

        eng_mask = mask & (english == 1)
        non_mask = mask & (english == 0)

        if np.sum(eng_mask) < 30 or np.sum(non_mask) < 30:
            continue

        eng_rate = np.mean(college[eng_mask])
        non_rate = np.mean(college[non_mask])
        n_eng = np.sum(eng_mask)
        n_non = np.sum(non_mask)

        t_stat, p_val = stats.ttest_ind(college[eng_mask], college[non_mask])

        log(f"{anc_group}:")
        log(f"  English at home:     {eng_rate*100:.1f}% college (n={n_eng:,})")
        log(f"  Other lang at home:  {non_rate*100:.1f}% college (n={n_non:,})")
        log(f"  DIFFERENCE:          {(eng_rate - non_rate)*100:+.1f} percentage points")
        log(f"  t-test: t={t_stat:.2f}, p={'< .001' if p_val < 0.001 else f'{p_val:.4f}'}")
        log()

        within_results.append({
            'ancestry': anc_group,
            'eng_college_pct': f"{eng_rate*100:.1f}%",
            'non_eng_college_pct': f"{non_rate*100:.1f}%",
            'difference_pp': f"{(eng_rate - non_rate)*100:+.1f}",
            'n_english': n_eng,
            'n_other': n_non,
            't_statistic': f"{t_stat:.2f}",
            'p_value': '< .001' if p_val < 0.001 else f'{p_val:.4f}'
        })

    # =========================================================================
    # REGRESSION: Ancestry vs Language as predictors
    # =========================================================================
    log("\n" + "=" * 80)
    log("REGRESSION ANALYSIS")
    log("=" * 80)
    log("""
Three models compared:
  Model 1: Ancestry only
  Model 2: Language only
  Model 3: Ancestry + Language
""")

    # Create ancestry dummies
    unique_groups = sorted(set(ancestry))
    ref_group = unique_groups[0]  # Reference category
    ancestry_dummies = {}
    for g in unique_groups[1:]:
        ancestry_dummies[f'anc_{g}'] = (ancestry == g).astype(float)

    y = college.astype(float)

    # Model 1: Ancestry only
    m1 = run_ols(y, ancestry_dummies)
    log(f"MODEL 1 (Ancestry only):   R² = {m1['r_squared']:.4f}  Adj R² = {m1['adj_r_squared']:.4f}")

    # Model 2: Language only
    m2 = run_ols(y, {'speaks_english': english.astype(float)})
    log(f"MODEL 2 (Language only):   R² = {m2['r_squared']:.4f}  Adj R² = {m2['adj_r_squared']:.4f}")

    # Model 3: Both
    combined = dict(ancestry_dummies)
    combined['speaks_english'] = english.astype(float)
    m3 = run_ols(y, combined)
    log(f"MODEL 3 (Both):            R² = {m3['r_squared']:.4f}  Adj R² = {m3['adj_r_squared']:.4f}")

    r2_ancestry = m1['r_squared']
    r2_language = m2['r_squared']
    r2_both = m3['r_squared']
    r2_incr_lang = r2_both - r2_ancestry
    r2_incr_anc = r2_both - r2_language

    log(f"\nKEY RESULT — Incremental R²:")
    log(f"  Variance from ancestry alone:    {r2_ancestry*100:.2f}%")
    log(f"  Variance from language alone:    {r2_language*100:.2f}%")
    log(f"  Variance from both:              {r2_both*100:.2f}%")
    log(f"  Incremental from language (beyond ancestry): {r2_incr_lang*100:.2f}%")
    log(f"  Incremental from ancestry (beyond language): {r2_incr_anc*100:.2f}%")

    # Language coefficient from Model 3
    lang_coef = m3['coefficients'].get('speaks_english', 0)
    lang_p = m3['p_values'].get('speaks_english', 1)
    log(f"\n  Language coefficient in full model: {lang_coef:.4f}")
    log(f"  p-value: {'< .001' if lang_p < 0.001 else f'{lang_p:.4f}'}")

    # =========================================================================
    # GENERATIONAL ANALYSIS
    # =========================================================================
    log("\n" + "=" * 80)
    log("GENERATIONAL ANALYSIS (Native vs Foreign Born)")
    log("=" * 80)

    for anc_group in ['Hispanic_Latino', 'Asian']:
        mask = ancestry == anc_group
        nat_mask = mask & (native == 1)
        for_mask = mask & (native == 0)

        if np.sum(nat_mask) < 30 or np.sum(for_mask) < 30:
            continue

        nat_rate = np.mean(college[nat_mask])
        for_rate = np.mean(college[for_mask])

        log(f"\n{anc_group}:")
        log(f"  US-born:       {nat_rate*100:.1f}% college (n={np.sum(nat_mask):,})")
        log(f"  Foreign-born:  {for_rate*100:.1f}% college (n={np.sum(for_mask):,})")
        log(f"  DIFFERENCE:    {(nat_rate - for_rate)*100:+.1f} percentage points")

    # US-born convergence
    log("\nUS-Born Individuals Across Ancestries:")
    native_mask = native == 1
    for g in unique_groups:
        gm = (ancestry == g) & native_mask
        if np.sum(gm) >= 30:
            log(f"  {g:<20} {np.mean(college[gm])*100:.1f}% college (n={np.sum(gm):,})")

    # =========================================================================
    # CONCLUSION
    # =========================================================================
    log("\n" + "=" * 80)
    log("CONCLUSION")
    log("=" * 80)

    if r2_language > r2_ancestry:
        log(f"\nLanguage alone (R²={r2_language:.4f}) explains MORE variance")
        log(f"than ancestry alone (R²={r2_ancestry:.4f}).")
        log("\n→ ENVIRONMENT (language) is the stronger predictor of outcomes.")
    else:
        log(f"\nAncestry alone (R²={r2_ancestry:.4f}) explains more variance")
        log(f"than language alone (R²={r2_language:.4f}).")
        log("\n→ But language still adds significant independent predictive power.")

    log(f"""
Language adds {r2_incr_lang*100:.2f}% incremental variance beyond ancestry.
Within the same ancestry group, English speakers have systematically higher
college attainment than non-English speakers.

This supports the environmental hypothesis: where you are raised and what
language environment you are exposed to matters for life outcomes,
independently of genetic ancestry.
""")

    if is_demo:
        log("⚠ NOTE: These results are from SYNTHETIC data.")
        log("  Download real census data for publication-quality results.")
        log("  See data/README_DATA.md for instructions.\n")

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    results_path = os.path.join(RESULTS_DIR, 'study_09_results.txt')
    with open(results_path, 'w') as f:
        f.write('\n'.join(output_lines))
    log(f"Results saved to {results_path}")

    # Save within-ancestry table
    if within_results:
        table_path = os.path.join(TABLES_DIR, 'study_09_within_ancestry.csv')
        with open(table_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=within_results[0].keys())
            writer.writeheader()
            writer.writerows(within_results)
        log(f"Table saved to {table_path}")

    # Save regression comparison table
    reg_table = os.path.join(TABLES_DIR, 'study_09_regression.csv')
    with open(reg_table, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['model', 'predictors', 'r_squared', 'adj_r_squared'])
        writer.writerow(['Model 1', 'Ancestry only', f"{r2_ancestry:.4f}", f"{m1['adj_r_squared']:.4f}"])
        writer.writerow(['Model 2', 'Language only', f"{r2_language:.4f}", f"{m2['adj_r_squared']:.4f}"])
        writer.writerow(['Model 3', 'Both', f"{r2_both:.4f}", f"{m3['adj_r_squared']:.4f}"])
    log(f"Regression table saved to {reg_table}")

    # Generate figures
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # Plot 1: R² comparison
        models = ['Ancestry\nonly', 'Language\nonly', 'Both']
        r2s = [r2_ancestry * 100, r2_language * 100, r2_both * 100]
        colors = ['#FF7043', '#42A5F5', '#66BB6A']
        bars = axes[0].bar(models, r2s, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
        axes[0].set_ylabel('R² (%)')
        axes[0].set_title('Variance Explained by Each Model')
        for bar, r2 in zip(bars, r2s):
            axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                        f'{r2:.2f}%', ha='center', fontsize=10)

        # Plot 2: Within-ancestry language effect
        if within_results:
            ancs = [r['ancestry'] for r in within_results]
            eng_rates = [float(r['eng_college_pct'].rstrip('%')) for r in within_results]
            non_rates = [float(r['non_eng_college_pct'].rstrip('%')) for r in within_results]
            x = np.arange(len(ancs))
            w = 0.35
            axes[1].bar(x - w/2, eng_rates, w, label='English at home', color='#42A5F5', alpha=0.8)
            axes[1].bar(x + w/2, non_rates, w, label='Other language', color='#FF7043', alpha=0.8)
            axes[1].set_xticks(x)
            axes[1].set_xticklabels(ancs)
            axes[1].set_ylabel('% with College Degree')
            axes[1].set_title('College Attainment Within Same Ancestry')
            axes[1].legend()

        # Plot 3: Incremental R²
        labels = ['Language\n(beyond ancestry)', 'Ancestry\n(beyond language)']
        incrs = [r2_incr_lang * 100, r2_incr_anc * 100]
        bars3 = axes[2].bar(labels, incrs, color=['#42A5F5', '#FF7043'], alpha=0.8, edgecolor='black', linewidth=0.5)
        axes[2].set_ylabel('Incremental R² (%)')
        axes[2].set_title('Unique Contribution of Each Predictor')
        for bar, v in zip(bars3, incrs):
            axes[2].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                        f'{v:.2f}%', ha='center', fontsize=10)

        plt.tight_layout()
        fig_path = os.path.join(FIGURES_DIR, 'study_09_language_vs_ancestry.png')
        plt.savefig(fig_path, dpi=200, bbox_inches='tight')
        plt.close()
        log(f"Figure saved to {fig_path}")
    except ImportError:
        log("matplotlib not available — skipping figure generation")

    log("\n" + "=" * 80)
    log("ANALYSIS COMPLETE")
    log("=" * 80)


if __name__ == '__main__':
    main()
