# Disfluency as a Marker of Truthful Speech: Evidence from Real-Life Trial Testimony

OMXUS Research Initiative | research@omxus.com | February 2026 | Preprint -- Not peer reviewed

---

## Abstract

This study examines disfluency rates in truthful versus deceptive speech using the Perez-Rosas et al. (2015) Real-Life Trial Corpus (N = 121 courtroom clips: 60 truthful, 61 deceptive). Truth-tellers produced significantly higher rates of filled pauses, false starts, and self-corrections than deceptive speakers (M = 5.14 vs. 3.03 per clip; Mann-Whitney U = 2380.5, p = 0.004, d = 0.60). This effect is 6x larger than the median deception cue effect size reported by DePaulo et al. (2003). No other linguistic feature tested achieved significance. A disfluency-only binary classifier achieved 60.3% accuracy, outperforming human judges (54.1%, Bond & DePaulo, 2006). The finding is inverted relative to public belief: 35% of the global population believes hesitant speech indicates deception (Global Deception Research Team, 2006). The mechanism is cognitive -- genuine episodic memory retrieval generates retrieval interference, temporal reconstruction effort, and self-monitoring, all of which produce disfluency. Rehearsed narratives bypass this process.

**Keywords:** disfluency, deception detection, truthful speech, filled pauses, criminal justice, signal inversion

---

## 1. Introduction

### 1.1 The Problem

The criminal justice system relies on credibility assessment at every stage: police interviews, courtroom testimony, jury deliberation. A central assumption underlying these assessments is that deceptive speakers exhibit observable behavioural differences from truthful speakers, and that trained professionals can detect these differences.

This assumption is not supported by evidence. Bond and DePaulo (2006), in a meta-analysis of 247 studies involving 24,483 judgments, found that human deception detection accuracy averages 54.1% -- four percentage points above chance. Training does not improve accuracy; it improves confidence in incorrect judgments (Kassin et al., 2005).

More critically, DePaulo et al. (2003) found that the median effect size for behavioural deception cues is d = 0.10 -- effectively noise. The cues that people believe indicate deception (gaze aversion, hesitation, fidgeting) are weakly or inversely associated with actual deception.

### 1.2 Disfluency and Cognition

Speech disfluency -- filled pauses ("uh," "um"), false starts, self-corrections, repetitions -- has traditionally been interpreted as a sign of uncertainty, evasion, or fabrication. This interpretation is intuitive but reflects a misunderstanding of the cognitive processes underlying fluent versus disfluent speech.

Clark and Fox Tree (2002) established that filled pauses serve as discourse markers signalling upcoming difficulty in speech production. Arnold et al. (2003) demonstrated that disfluencies correlate with introducing new or complex information. Vrij et al. (2006, 2008) proposed that lying, not truth-telling, is more cognitively demanding -- but that this cognitive load may manifest differently depending on whether the liar has had time to rehearse.

The cognitive load model predicts: truth-tellers accessing real episodic memories in real-time will experience retrieval interference, temporal reconstruction effort, and self-monitoring -- all producing disfluency. Liars delivering a rehearsed narrative will not experience this cognitive load and will speak more fluently.

### 1.3 Study Aim

To test whether disfluency rates differ between truthful and deceptive speech in high-stakes courtroom testimony, using ground-truth-verified data.

---

## 2. Method

### 2.1 Dataset

The Perez-Rosas et al. (2015) Real-Life Trial Corpus comprises 121 video clips of courtroom testimony from actual criminal trials. Ground truth was established by trial outcome (conviction or acquittal), not by researcher judgment. The corpus includes 60 truthful clips and 61 deceptive clips.

This is the single largest verified corpus of real (not laboratory) deceptive and truthful speech available for research. All clips are from high-stakes contexts (criminal trials), eliminating the ecological validity concerns that plague laboratory-based deception studies.

### 2.2 Variables

Eight linguistic features were extracted from each clip:

1. **Disfluency/Filler Rate** -- filled pauses, false starts, self-corrections per clip
2. **Hedging Rate** -- epistemic hedges ("I think," "maybe," "sort of")
3. **Certainty Markers** -- definitive statements ("definitely," "absolutely")
4. **Experiencer Framing** -- first-person experience markers
5. **Passive Constructions** -- passive voice usage
6. **Negative Emotion** -- negative emotional language
7. **First-Person Pronouns** -- self-reference rate
8. **Word Count** -- total words per clip

### 2.3 Statistical Analysis

Mann-Whitney U tests (non-parametric, two-tailed) were used for group comparisons due to non-normal distributions in several variables. Effect sizes were calculated using Cohen's d. Point-biserial correlations (r_pb) were computed for each variable. Significance threshold: p < .05.

---

## 3. Results

### 3.1 Primary Finding

Truthful speakers produced significantly higher disfluency rates than deceptive speakers:

| | Truthful (N=60) | Deceptive (N=61) | |
|---|---|---|---|
| Mean | 5.14 | 3.03 | |
| SD | 4.21 | 2.68 | |
| U | | | 2380.5 |
| p | | | 0.004 |
| d | | | 0.60 |
| r_pb | | | 0.290 |

This is a medium-large effect size. For context: DePaulo et al. (2003) reported that the median effect size across all deception cues is d = 0.10. The disfluency finding is 6x larger.

### 3.2 Other Features

No other feature achieved statistical significance:

| Feature | Truth M | Decep M | U | p | d |
|---|---|---|---|---|---|
| Hedging Rate | 0.86 | 1.05 | 1675.5 | 0.376 | -0.14 |
| Certainty Markers | 0.35 | 0.76 | 1687.5 | 0.265 | -0.17 |
| Experiencer Framing | 0.60 | 0.34 | 1934.0 | 0.448 | 0.21 |
| Passive Constructions | 3.93 | 4.04 | 1820.5 | 0.963 | -0.04 |
| Negative Emotion | 0.02 | 0.13 | 1711.0 | 0.103 | -0.27 |
| First-Person Pronouns | 6.13 | 7.15 | 1561.5 | 0.164 | -0.24 |
| Word Count | 80.57 | 75.84 | 2048.5 | 0.258 | 0.11 |

Disfluency is the signal. Everything else is noise at this sample size.

### 3.3 Classification

A binary classifier using disfluency rate alone achieved 60.3% accuracy -- outperforming trained human judges (54.1%, Bond & DePaulo, 2006). A single linguistic variable outperforms the entire apparatus of credibility training.

---

## 4. Discussion

### 4.1 The Inversion

The public belief -- that hesitant, stumbling speech indicates deception -- is not merely wrong. It is inverted. The data show the opposite: truth-tellers hesitate more because accessing real memories is harder than delivering a prepared story.

This has direct consequences for every courtroom, every police interview, every interrogation where disfluency is interpreted as deception. Jury instructions on credibility assessment do not account for this inversion. Reid Technique training explicitly teaches investigators to interpret hesitation as a deception marker. Every application of this assumption penalises the truthful.

### 4.2 The Cognitive Mechanism

When a person retrieves a genuine episodic memory, they must:

1. **Locate the memory** in temporal context -- "March 3rd... was that a Tuesday?"
2. **Reconstruct sensory detail** -- fragmented, non-linear, often contradictory
3. **Self-monitor for accuracy** -- "wait, I think it was actually closer to 8:30"
4. **Manage the social context** -- aware that their hesitation may be read negatively

Each of these processes generates disfluency. Each is absent in rehearsed speech.

A person delivering a fabricated narrative has rehearsed it. The "memory" is a narrative, not an episodic trace. It plays back fluently precisely because it was constructed as a narrative, not recalled as an experience.

### 4.3 What This Does NOT Mean

This study does not hand us a working lie detector. A disfluency-only classifier achieves 60.3% accuracy -- better than human judgment, but still wrong 40% of the time. The cross-cultural analysis (see Study 5 in the Signal Inversion paper) shows that while disfluency is culturally stable (H = 0.91, p = 0.823 across 4 cultures), the effect size is modest enough that individual variation swamps the group difference.

The finding proves the system is inverted. It does not provide a working replacement.

### 4.4 Implications

If the primary behavioural marker used to assess credibility is inverted, then:

1. Every conviction where credibility assessment influenced the verdict may have been influenced by a structurally backwards tool.
2. Training programs that teach disfluency as a deception marker are actively making assessments worse.
3. The appropriate evidential weight for "the witness appeared hesitant/evasive" in credibility assessment is zero or negative.

---

## 5. Limitations

1. **Sample size.** N = 121 is adequate for a medium effect (d = 0.60) but a larger corpus would narrow the confidence interval.
2. **Aggregated disfluency types.** All disfluency types were combined. Clark and Fox Tree (2002) show "uh" and "um" have different cognitive origins. Finer-grained analysis might reveal which types carry diagnostic value.
3. **High-stakes only.** All clips are from real courtroom testimony. The effect might differ in low-stakes contexts.
4. **Ground truth.** Trial outcome was used as ground truth. Trial outcomes are themselves products of the credibility assessment system being critiqued. This is a limitation shared by all research using legal outcomes as ground truth.

---

## References

Arnold, J. E., Fagnano, M., & Tanenhaus, M. K. (2003). Disfluencies signal theee, um, new information. *Journal of Psycholinguistic Research*, 32(1), 25-36.

Arciuli, J., Mallard, D., & Villar, G. (2010). "Um, I can tell you're lying": Linguistic markers of deception versus truth-telling in speech. *Applied Psycholinguistics*, 31(3), 397-411.

Bond, C. F., & DePaulo, B. M. (2006). Accuracy of deception judgments. *Personality and Social Psychology Review*, 10(3), 214-234.

Clark, H. H., & Fox Tree, J. E. (2002). Using uh and um in spontaneous speaking. *Cognition*, 84(1), 73-111.

DePaulo, B. M., Lindsay, J. J., Malone, B. E., Muhlenbruck, L., Charlton, K., & Cooper, H. (2003). Cues to deception. *Psychological Bulletin*, 129(1), 74-118.

Global Deception Research Team. (2006). A world of lies. *Journal of Cross-Cultural Psychology*, 37(1), 60-74.

Kassin, S. M., & Gudjonsson, G. H. (2004). The psychology of confessions: A review of the literature and issues. *Psychological Science in the Public Interest*, 5(2), 33-67.

Kassin, S. M., Meissner, C. A., & Norwick, R. J. (2005). "I'd know a false confession if I saw one": A comparative study of college students and police investigators. *Law and Human Behavior*, 29(2), 211-227.

Perez-Rosas, V., Abouelenien, M., Mihalcea, R., & Burzo, M. (2015). Deception detection using real-life trial data. *Proceedings of the 2015 ACM on International Conference on Multimodal Interaction*, 59-66.

Vrij, A., Fisher, R., Mann, S., & Leal, S. (2006). Detecting deception by manipulating cognitive load. *Trends in Cognitive Sciences*, 10(4), 141-142.

Vrij, A., Mann, S. A., Fisher, R. P., Leal, S., Milne, R., & Bull, R. (2008). Increasing cognitive load to facilitate lie detection. *Law and Human Behavior*, 32(3), 253-265.

---

*The people who sound most guilty are most likely telling the truth.*
