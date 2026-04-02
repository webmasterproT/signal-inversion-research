# Study 1: Linguistic Markers of Veracity in Trial Testimony

## What This Proves

Truthful speakers produce MORE disfluency (fillers, hedges, self-corrections) than deceptive speakers, with an effect size of d=0.60 (p=.004) -- 6x larger than the median deception cue identified in DePaulo et al.'s (2003) meta-analysis of 1,338 estimates. This directly inverts the folk belief that hesitation signals lying.

## Dataset

- **Source:** Perez-Rosas, V., Abouelenien, M., Mihalcea, R., & Burzo, M. (2015). Deception detection using real-life trial data. *Proceedings of ACM ICMI 2015*, 59-66.
- **N** = 121 video transcripts (60 truthful, 61 deceptive)
- **Ground truth:** jury verdicts cross-validated with post-conviction exonerations from the Innocence Project
- **Location:** `data/spss_ready.csv`
- **Variables:** `hedging_rate`, `certainty_rate`, `filler_rate`, `experiencer_rate`, `passive_rate`, `neg_emotion_rate`, `first_person_rate`, `word_count`

## Method

- Mann-Whitney U tests (non-parametric, appropriate for non-normal distributions)
- Point-biserial correlations
- Binary logistic regression (single predictor: disfluency only)
- Multi-variable logistic regression with 10-fold cross-validation

## Key Results

| Variable | Truth M | Decep M | d | p |
|---|---|---|---|---|
| Disfluency/Fillers | 5.14 | 3.03 | 0.60 | .004** |
| Negative Emotion | 0.02 | 0.13 | -0.27 | .103 |
| First-Person Pron. | 6.13 | 7.15 | -0.24 | .164 |

Classification: 63.5% accuracy (10-fold CV) vs 54% human judgment (Bond & DePaulo, 2006).

## How to Run

```bash
./run.sh
```

Or manually:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python src/run.py
```

Results go to `results/study_1_results.txt`, `results/study_1_table.csv`, and `results/figures/effect_sizes.png`.

## Citation

Perez-Rosas, V., Abouelenien, M., Mihalcea, R., & Burzo, M. (2015). Deception detection using real-life trial data. *Proceedings of ACM ICMI 2015*, 59-66. https://doi.org/10.1145/2818346.2820758
