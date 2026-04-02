# Study 4: Human vs Algorithmic Deception Detection — Convergence

## Key Finding

Human deception detection accuracy is 54% overall (Bond & DePaulo, 2006; k=206 studies, N=24,483) — barely above the 50% chance baseline. Lie detection specifically is 47%, **below chance**. Training does not help: police officers (55%), customs officials (55%), and judges (54%) perform no better than the untrained public.

Algorithmic detection using linguistic features reaches 60.3% (disfluency alone), 63.5% (multi-variable, 10-fold CV), and 74-83% (Rizzelli et al., 2021, 3-predictor model). The gap exists because:

- The features humans **can** perceive (gaze, fidgeting, disfluency) are **inverted** — they indicate truthfulness, not deception (Study 3).
- The features that **work** (pronoun rates, conjunction patterns, linguistic distancing) are **imperceptible** to human observers in real-time.

This is the Signal Inversion Effect operating at the system level. The credibility assessment framework used by courts, police, and juries is not merely inaccurate — it is directionally wrong.

## Citation

Bond, C. F., & DePaulo, B. M. (2006). Accuracy of deception judgments. *Personality and Social Psychology Review*, 10(3), 214-234. https://doi.org/10.1207/s15327957pspr1003_2

## Reproduction

```bash
chmod +x run.sh
./run.sh
```

## Output

- `results/study_4_convergence.txt` — Full analysis text
- `results/figures/convergence_accuracy.png` — Bar chart comparing human vs algorithmic accuracy with chance line at 50%

## Data

- `data/convergence_data.csv` — Accuracy rates from Bond & DePaulo (2006) and current studies
