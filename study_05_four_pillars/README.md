# Study 5: Convergent Validity — The Four Empirical Pillars

## Key Finding

Each of the four pillars independently rejects its null hypothesis. Together they close the logical space: if the construction thesis were false, you would expect (a) detection above chance, (b) memory stability, (c) low false confessions, (d) minimal detention effect. The data show the **opposite** on all four.

### The Four Pillars

| Pillar | Key Statistic | Null Hypothesis | Effect Size | Rejected |
|--------|--------------|-----------------|-------------|----------|
| I. Deception Detection | 54% accuracy (CI: 53.6-54.6) | Accuracy = chance | h = 0.08 | YES |
| II. Memory Distortion | d = 0.72; ~24% false memory | Language doesn't affect memory | d = 0.72 | YES |
| III. False Confessions | 12-30% of exonerations | No systemic bias | OR = 0.21 | YES |
| IV. Suggestibility | +80-120% baseline elevation | Detention doesn't affect voluntariness | d = 1.0 | YES |

### Garrett (2011) DNA Data

Binomial test: 27 out of 250 DNA-confirmed exonerations involved detailed, signed false confessions. Against a 1% baseline: p < 10^-30. Twenty-seven factually innocent people — confirmed by DNA — provided full fabricated confessions. This is not error. This is system output.

## Citations

- Bond, C. F., & DePaulo, B. M. (2006). *Personality and Social Psychology Review*, 10(3), 214-234.
- Loftus, E. F. (2005). *Learning & Memory*, 12(4), 361-366.
- Garrett, B. L. (2011). *Convicting the Innocent*. Harvard University Press.
- Gudjonsson, G. H. (2003). *The Psychology of Interrogations and Confessions*. Wiley.

## Reproduction

```bash
chmod +x run.sh
./run.sh
```

## Output

- `results/study_5_convergent_validity.txt` — Full analysis text
- `results/figures/four_pillars_convergence.png` — Four-panel convergence summary figure

## Data

- `data/pillars.csv` — Summary convergence table
- `data/memory_studies.csv` — Loftus et al. effect sizes and false memory rates
- `data/confession_rates.csv` — False confession rates across exoneration datasets
