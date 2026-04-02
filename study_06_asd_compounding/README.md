# Study 6: The ASD Compounding Effect

## Key Finding

Autistic individuals face a compound credibility penalty because their neurological traits trigger MULTIPLE inverted deception heuristics simultaneously. Monte Carlo simulation (100,000 iterations) yields Cohen's d = 3.18 — an autistic truth-teller triggers approximately 4.5x more inverted deception heuristics than a neurotypical truth-teller in the same situation.

Critically, Maras et al. (2019) showed that **disclosure reverses the bias**. When mock jurors were told a witness was autistic, the credibility penalty disappeared and slightly reversed. The problem is not the person — it is the interpretive framework.

## The Overlap

10 ASD diagnostic features map directly onto believed deception cues from the Global Deception Research Team (2006). Of 10 overlapping behaviours, 7 (70%) trigger inverted credibility judgments — the observer reads neurological difference as deception.

| Behaviour | GDRT Belief % | Actual d | Inverted |
|-----------|:------------:|:--------:|:--------:|
| Gaze aversion | 63.7% | 0.05 | YES |
| Fidgeting/stimming | 52.0% | 0.01 | YES |
| Flat affect | 45.0% | -0.01 | YES |
| Visible anxiety | 45.0% | -0.01 | YES |
| Disfluency | 35.0% | -0.60 | YES |
| Social reciprocity | 30.0% | 0.00 | YES |
| Response latency | 22.0% | 0.02 | YES |

## Empirical Evidence

- **Lim et al. (2022)**: 1,410 observers rated autistic adults as MORE deceptive and LESS credible than neurotypical adults — when telling the truth. *J Autism Dev Disorders*, 52(2), 490-507.
- **Bagnall et al. (2023)**: Innocent autistic suspects showed fewer innocence-supporting details, greater question difficulty, higher anxiety. *Frontiers in Psychology*, 14, 1117415.
- **Maras et al. (2019)**: Disclosure reversed the credibility penalty. Without disclosure: less credible. With disclosure: slightly more credible. *Research in Autism Spectrum Disorders*, 67, 101438.

## Reproduction

```bash
chmod +x run.sh
./run.sh
```

## Output

- `results/study_6_asd_compounding.txt` — Full analysis text
- `results/figures/asd_compounding.png` — ASD trait overlap bars + compound effect histogram

## Data

- `data/asd_overlap.csv` — 10-row mapping of ASD features to inverted deception cues
- `data/asd_studies.csv` — Three key ASD credibility studies
