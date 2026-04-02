# Study 8: Geographic Birthplace and Language Acquisition

## What This Proves

Language — the most complex behavioural pattern humans acquire — is **100% environmentally determined**. No child is born speaking a language. Across 8 countries and 1.8 billion people, birthplace predicts dominant language with overwhelming effect sizes (mean Cohen's h = 0.93).

This matters for credibility assessment because: if language (a behaviour far more complex than "gaze aversion" or "fidgeting") is entirely environmental, then the simpler behavioural patterns used to judge credibility are *at least* partially environmental. Judging someone's honesty by how they behave is judging where they grew up.

## Key Results

| Metric | Value |
|--------|-------|
| Total N | 1,811,487,320 |
| Countries | 8 |
| Mean Cohen's h | 0.93 (Very Large) |
| All p-values | < .001 |
| Range of h | 0.47 – 1.30 |

## Method

- Chi-square goodness-of-fit test per country (H₀: language independent of birthplace at 50%)
- Cohen's h effect size for each country
- Data: official national census reports (hardcoded — no external download needed)

## How to Run

```bash
./run.sh
# Or manually:
pip install -r requirements.txt
python src/run.py
```

## Output

- `results/study_08_results.txt` — Full statistical output
- `results/tables/study_08_table.csv` — Results table
- `results/figures/study_08_language_by_country.png` — Bar charts
