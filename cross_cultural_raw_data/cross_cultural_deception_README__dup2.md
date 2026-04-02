# Cross-Cultural Variation in Truthful Speech

**Deception beliefs and truthful speech patterns vary dramatically across cultures — but the system assumes universality.**

Original analysis of a 4-culture deception corpus demonstrating that speech patterns used to assess credibility vary by culture, making universal credibility heuristics fundamentally unreliable.

---

## Research Methodology

### Study Type
**Original Cross-Cultural Corpus Analysis** — Statistical comparison of deception-related linguistic features across 4 cultural groups.

### Dataset
- **Source:** Cross-Cultural Deception Corpus (2014)
- **Cultures:** 4 cultural groups
- **Analysis:** Kruskal-Wallis H-test for cultural variation

### Key Result
- **H = 383.64** — massive cultural variation in truthful speech patterns
- Features that indicate truthfulness in one culture may indicate deception in another
- Universal credibility heuristics are culturally invalid

---

## Contents

| Location | Description |
|----------|-------------|
| `data/raw/crossCulturalDeception.2014/` | 4-culture deception corpus |
| `src/cultural_analysis.py` | Cross-cultural analysis script |
| `results/tables/cultural_analysis.txt` | Statistical output |
| `results/tables/cultural_analysis_v1.txt` | Earlier analysis output |
| `results/figures/crossCultural_cultural_boxplots.png` | Cultural variation boxplots |
| `results/figures/crossCultural_cross_classifier_fp.png` | Cross-classifier false positive rates |

---

## Breadcrumbs

- **Supports:** [the_91_percent](../the_91_percent/) — cue inversion varies culturally
- **Extends:** [disfluency_truthful_speech](../disfluency_truthful_speech/) — same features, different cultures
- **Feeds into:** [constructed_guilt_thesis](../constructed_guilt_thesis/) — Study 5 of 5 original contributions
- **Connects:** [environmental_determination](../environmental_determination/) — environment determines communication style
- **Closes:** "This is the best available system"

---

*A credibility test that works in Sydney fails in Seoul. The system doesn't know this.*
