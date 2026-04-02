# Study 3: The Belief-Reality Inversion Matrix

## What This Proves

74% of publicly believed deception cues are empirically wrong or unrelated to actual deception. Binomial sign test: p = .017. The strongest beliefs (gaze aversion at 63.7% endorsement) have the smallest actual effects (d = 0.05). The public's mental model of deception is not merely inaccurate -- it is a systematically inverted compass.

## Dataset Sources

1. **Global Deception Research Team (2006)** -- "A World of Lies." N = 11,227 participants across 75 countries. Measured public beliefs about which behaviours indicate deception.
2. **DePaulo et al. (2003)** -- "Cues to Deception." Meta-analysis of 158 cues across 116 studies. Measured actual diagnostic value (Cohen's d) of each cue.
3. **Current Study 1** -- Disfluency/filler finding (d = -0.60, liars produce FEWER disfluencies).

## Method

23 cues were matched across the belief dataset (GDRT) and the empirical dataset (DePaulo et al.). Each cue was coded for:
- **Belief strength**: percentage of respondents who endorsed it as a deception indicator
- **Actual effect size**: Cohen's d from meta-analytic data
- **Concordance**: whether the believed direction matches the empirical direction
- **Inverted**: True if the public believes the opposite of what the evidence shows, or believes in a cue with no reliable empirical link (d near zero)

Statistical tests:
- Binomial sign test (H0: inversion rate = 50%)
- Weighted Inversion Index (belief-weighted net inversion, scale -1 to +1)
- Spearman rank correlation (belief endorsement rate vs actual |d|)
- Category breakdown (nonverbal, paralinguistic, verbal)

## Key Results

| Metric | Value |
|--------|-------|
| Cues matched | 23 |
| Inverted | 17/23 (74%) |
| Binomial p (one-tailed) | .017 |
| 95% CI | [53.4%, 88.2%] |
| Weighted Inversion Index | +0.506 |
| Spearman rho (belief vs \|d\|) | negative / non-significant |
| Nonverbal inversion | 9/11 (82%) |
| Paralinguistic inversion | 4/5 (80%) |
| Verbal inversion | 4/7 (57%) |

The strongest single belief -- gaze aversion (63.7% of 11,227 people across 75 countries) -- has an actual effect size of d = 0.05. The strongest actual cue in this set -- disfluency (d = -0.60) -- goes in the opposite direction to what 35% of people believe.

## How to Run

```bash
# From this directory:
chmod +x run.sh
./run.sh

# Or manually:
pip3 install -r requirements.txt
python3 src/run.py
```

### Outputs

- `results/study_3_results.txt` -- text summary of all statistics
- `results/figures/forest_plot_inversion.png` -- horizontal forest plot of actual d values, colored by inversion status, sorted by belief strength
- `results/figures/scatter_belief_vs_reality.png` -- scatter of belief endorsement rate vs actual |d|
- `results/figures/inversion_rate_summary.png` -- pie chart (overall) + grouped bar chart (by category)

## File Structure

```
study_3_belief_reality_inversion/
  data/inversion_matrix.csv    # 23 matched cues with all coded variables
  src/run.py                   # Full analysis + figure generation
  results/                     # Generated text results
  results/figures/             # Generated figures (PNG, 200 DPI)
  requirements.txt             # pandas, numpy, scipy, matplotlib
  run.sh                       # One-command runner
  README.md                    # This file
```

## Citations

Global Deception Research Team. (2006). A world of lies. *Journal of Cross-Cultural Psychology*, 37(1), 60--74. https://doi.org/10.1177/0022022105282295

DePaulo, B. M., Lindsay, J. J., Malone, B. E., Muhlenbruck, L., Charlton, K., & Cooper, H. (2003). Cues to deception. *Psychological Bulletin*, 129(1), 74--118. https://doi.org/10.1037/0033-2909.129.1.74
