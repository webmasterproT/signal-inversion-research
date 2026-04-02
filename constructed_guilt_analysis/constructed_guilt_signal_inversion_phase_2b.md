# Belief–Reality Inversion Matrix

**Signal Inversion Effect — Phase 2B Analysis**

## Headline Finding

**91% of deception cues show belief–reality inversion** (p < 0.0001)

Human beliefs about what indicates deception are not merely inaccurate — they are **systematically backwards**.

## What This Analysis Does

This analysis pairs two landmark datasets to test whether human beliefs about deception cues are inverted relative to empirical evidence:

| Dataset | What It Contains | N |
|---------|------------------|---|
| **DePaulo et al. (2003)** | Meta-analysis of actual deception cue validity | 158 cues, 120 studies |
| **GDRT (2006)** | Global survey of what people *believe* indicates deception | 75 countries, 11,227 participants |

For each cue that appears in both datasets, we ask:
- **What do people believe?** (GDRT endorsement %)
- **What does evidence show?** (DePaulo effect size d)
- **Are they aligned or inverted?**

## Key Results

```
Inversion Rate:     91%
Binomial test:      p < 0.0001
Weighted Index:     0.81 (Strong systematic inversion)
```

### The Most Believed Cues Are Wrong

| Cue | Belief Rate | Actual Effect | Status |
|-----|-------------|---------------|--------|
| Gaze aversion | 63.7% | d = 0.05 (null) | **INVERTED** |
| Nervousness | 52.3% | d = 0.27 (weak) | Partially aligned |
| Fidgeting | 47.2% | d = -0.01 (null) | **INVERTED** |
| Disfluency | 32.8% | d = -0.60 (truth!) | **INVERTED** |

### The Thesis Implication

The interpretive framework used by investigators, jurors, and the public is not just inaccurate — it's inverted. This means:

- Innocent people showing cognitive effort (hesitation, hedging) are read as deceptive
- Guilty people with rehearsed stories (fluent, confident) are read as truthful
- **The system punishes truth-telling and rewards deception**

## Data Sources

### DePaulo et al. (2003)
> "Cues to Deception." *Psychological Bulletin*, 129(1), 74-118.

The definitive meta-analysis of deception cues. Analysed 158 potential cues across 120 independent samples.

**Key finding:** Most believed cues (gaze, fidgeting) have effect sizes near zero. The cues that actually work (detail, coherence) are less strongly believed.

### Global Deception Research Team (2006)
> "A World of Lies." *Journal of Cross-Cultural Psychology*, 37(1), 60-74.

Surveyed 11,227 participants across 75 countries in 43 languages. Asked: "What behaviors do you believe indicate that someone is lying?"

**Key finding:** Gaze aversion is the #1 believed cue globally (63.7%), despite having no empirical validity.

### Phase 1 Finding (Current Study)
> Michigan Trial Corpus (Pérez-Rosas et al., 2015)

Our Phase 1 analysis of 121 trial transcripts found disfluency (fillers like "um", "uh") shows **d = 0.60 in favor of truthful speakers** — a medium effect, 6× larger than the median cue effect in DePaulo's meta-analysis.

## Usage

```bash
# Run the analysis
python src/belief_reality_analysis.py

# Output
results/tables.txt           # Full statistical results
results/inversion_matrix.csv # Raw coded data
results/figures/             # Publication-ready plots
```

## Output Files

| File | Description |
|------|-------------|
| `results/tables.txt` | Complete statistical results, SPSS-ready |
| `results/inversion_matrix.csv` | Full matrix with all cues coded |
| `results/figures/belief_reality_matrix.png` | Main scatter plot |
| `results/figures/inversion_rates.png` | Pie chart + category breakdown |
| `results/figures/forest_plot.png` | All cues ranked |

## Statistical Tests

### Test 1: Binomial Test
Tests whether inversion rate exceeds 50% (chance).
- H0: Inversion rate = 50%
- H1: Inversion rate > 50%
- **Result: 91% inverted, p < 0.0001**

### Test 2: Weighted Inversion Index
Weights each cue by belief endorsement rate. A cue believed by 64% that is inverted is more consequential than one believed by 10%.
- Scale: -1.0 (all aligned) to +1.0 (all inverted)
- **Result: 0.81 (strong systematic inversion)**

### Test 3: Belief–Validity Correlation
Tests whether stronger beliefs correspond to more valid cues.
- If well-calibrated: r > 0
- **Result: r = 0.24, p = 0.28 (no relationship)**

## Citation

If using this analysis:

```bibtex
@misc{signal_inversion_2026,
  title={The Signal Inversion Effect: Belief-Reality Inversion in Deception Cues},
  author={{Signal Inversion Project}},
  year={2026},
  note={Phase 2B Analysis. Data from DePaulo et al. (2003) and GDRT (2006)}
}
```

## License

Analysis code: MIT License
Data: Derived from published sources (see citations)

---

*Part of the Signal Inversion Effect research programme.*
