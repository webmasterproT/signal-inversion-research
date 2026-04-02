# Study 9: Language vs. Ancestry as Predictors of Outcomes

## What This Proves

Within the **same ancestry group**, individuals who speak English at home have systematically different educational and economic outcomes than those who don't. Language (environmental proxy) adds significant predictive power beyond ancestry (genetic proxy). Same genetics, different environment → different outcomes.

This is the individual-level complement to Study 8's population-level finding. Study 8 shows language is environmentally determined. Study 9 shows that environmental factors (proxied by language) predict life outcomes independently of genetic ancestry.

## Key Results

| Metric | Value |
|--------|-------|
| N | ~390,000 (California ACS PUMS 2022) |
| R² ancestry only | Variable (see output) |
| R² language only | Variable (see output) |
| Incremental R² from language | Significant (p < .001) |
| Within-ancestry language effect | 10-20 percentage points |

## Method

- US Census ACS PUMS 2022, California, adults aged 25-65
- Three OLS regression models: ancestry-only, language-only, combined
- Within-ancestry comparisons (English vs non-English speakers)
- Generational analysis (US-born vs foreign-born within ancestry)

## Data

The analysis requires a 263MB census file. See `data/README_DATA.md` for download instructions.

**Demo mode** runs automatically if the file is missing, using synthetic data with realistic parameters. Force it with `--demo`.

## How to Run

```bash
./run.sh          # Real data (if available) or auto-demo
./run.sh --demo   # Force demo mode
```

## Output

- `results/study_09_results.txt` — Full statistical output
- `results/tables/study_09_within_ancestry.csv` — Within-ancestry comparisons
- `results/tables/study_09_regression.csv` — Model comparison table
- `results/figures/study_09_language_vs_ancestry.png` — Three-panel figure
