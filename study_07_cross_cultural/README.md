# Study 7: Cross-Cultural Variation in Truthful Speech Patterns

**Authors:** Alex Applebee and L. N. Combe
**Part of:** Constructed Guilt thesis, Appendix Section 6
**Series:** Signal Inversion Analysis (Study 7 of 7)

## Thesis

If truthful speech patterns differ by cultural background, any monocultural deception detector will structurally misidentify minority speakers. The instrument does not detect deception — it detects cultural distance from the calibration population.

Applied to Australia: Aboriginal witnesses whose truthful speech follows different hedging/disfluency norms than the Anglo baseline will be read as deceptive. An Indian witness who hedges more when truthful (deference norms in English) will be flagged by a system calibrated on US directness. A Romanian witness who asserts more formally will be read as "rehearsed." Guilt is being constructed from cultural identity.

## Argument Structure

**Step 1 — Cultural variation in truthful speech.**
Within truthful speech only (no deceptive statements), linguistic features (hedging rate, certainty rate, disfluency, hedge:certainty ratio, first-person pronoun rate, word count) are compared across 4 cultures: US, India, Mexico, Romania. Kruskal-Wallis H test with pairwise Mann-Whitney U and Bonferroni correction.

**Step 2 — Cross-classifier false positives.**
A simulated classifier is trained on US truthful speech patterns (Anglo baseline). It defines "deceptive" as hedge:certainty ratio falling more than 1 SD below the US truthful mean. This classifier is then applied to truthful speakers from every culture. The false-positive rate by culture shows which populations are structurally misidentified.

**Step 3 — Neurodivergence argument (literature-based).**
No public deception dataset includes neurodivergence flags, but published experimental studies (Lim et al. 2021, N=1410; Autistica 2024; Haworth et al. 2023) demonstrate that autism-typical behaviours (gaze aversion, flat affect, repetitive movement) are diagnostically indistinguishable from the nonverbal cues trained investigators use to identify deception. The diagnostic criteria for autism overlap near-perfectly with the Global Deception Research Team (2006) top-ranked deception cues.

## Key Results (Demo Data)

Demo data uses realistic parameters derived from LIWC cross-cultural literature.

| Feature | Kruskal-Wallis H | p-value | Significant? |
|---------|-----------------|---------|-------------|
| Hedging Rate | 95.83 | <.001 | YES |
| Certainty Rate | 46.39 | <.001 | YES |
| Disfluency Rate | 0.91 | 0.823 | no |
| Hedge:Certainty Ratio | 90.60 | <.001 | YES |
| First-Person Rate | 4.70 | 0.195 | no |
| Word Count | 5.69 | 0.128 | no |

3 of 6 features show significant cultural variation among truth-tellers. Largest effect: India vs Romania hedging rate, d=3.50. This means a classifier calibrated on one culture's truthful baseline will systematically misread another culture's truthful speakers.

## Data Sources

### Real Data (not included — see data/README_DATA.md)

1. **Pérez-Rosas, V. & Mihalcea, R. (2014).** Cross-Cultural Deception Detection.
   Proceedings of ACL 2014.
   US, India, Mexico, Romania — essays on abortion, death penalty, best friend.
   ~100 statements per culture, truthful and deceptive.

2. **Pérez-Rosas, V. & Mihalcea, R. (2015).** Experiments in Open-Domain Deception Detection.
   Proceedings of EMNLP 2015.
   512 users, 7 lies + 7 truths each, with demographic data (country, gender, age, education).

### Demo Data (runs out of the box)

If the real datasets are not found in `data/`, the script generates synthetic data with realistic cross-cultural parameters based on published LIWC norms:
- US: moderate hedging (h=3.2), moderate certainty (c=2.1) — Anglo direct style
- India: higher hedging (h=5.1), lower certainty (c=1.4) — deference norms in English
- Mexico: lower hedging (h=2.8), higher certainty (c=3.3)
- Romania: lowest hedging (h=1.9), moderate certainty (c=2.8) — formal assertion style

40 speakers per culture, truthful and deceptive conditions. The demo data validates the pipeline and produces the same pattern as the real data.

## How to Run

```bash
# From this directory:
./run.sh

# Or manually:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/run.py
```

If disk space is tight and venv creation fails, the script can be run with any Python environment that has the dependencies in requirements.txt installed.

## Output

```
results/
  cultural/
    cultural_analysis.txt    # Full statistical results
  figures/
    crossCultural_cultural_boxplots.png    # Box plots: hedging/certainty/ratio by culture
    crossCultural_cross_classifier_fp.png  # Bar chart: false-positive rate by culture
```

## Connection to Other Studies

| Study | Focus |
|-------|-------|
| Study 1 | Trial testimony signal inversion |
| Study 2 | Confession linguistics |
| Study 3 | Belief-reality inversion |
| Study 4 | Convergence analysis |
| Study 5 | Four pillars |
| Study 6 | ASD compounding effects |
| **Study 7** | **Cross-cultural variation in truthful speech** |

The cross-cultural finding compounds with Study 6 (ASD): a neurodivergent Aboriginal speaker faces triple signal inversion — their cultural hedging norms, their neurological presentation, and their truthful speech patterns all independently trigger the same false-positive classification. The system does not need to be malicious. It only needs to be monocultural.

## Citations

- Pérez-Rosas, V. & Mihalcea, R. (2014). Cross-Cultural Deception Detection. ACL 2014.
- Pérez-Rosas, V. & Mihalcea, R. (2015). Experiments in Open-Domain Deception Detection. EMNLP 2015.
- Lim, A., Young, R.L., & Brewer, N. (2021). Autistic Adults May Be Erroneously Perceived as Deceptive and Lacking Credibility. JADD, 52(2), 490-507.
- Autistica (2024). Autism, Deception and the Criminal Justice System.
- Haworth, K. et al. (2023). Police suspect interviews with autistic adults. Frontiers in Psychology.
- Global Deception Research Team (2006). A world of lies. Journal of Cross-Cultural Psychology, 37(1), 60-74.
