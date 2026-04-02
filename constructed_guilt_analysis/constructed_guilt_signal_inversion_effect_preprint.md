  The Signal Inversion Effect: How Authentic Cognition
           Mimics Deception Across Domains
    A Cross-Disciplinary Analysis of Linguistic Markers, Public Beliefs, and Credibility
                                        Assessment

                                       Working Paper — Preprint
                                             March 2026


Abstract
      This paper presents converging evidence for what we term the Signal Inversion Effect: a
      systematic pattern whereby authentic cognitive and linguistic behaviours associated with
      truthfulness are misidentified as indicators of deception by human observers, while rehearsed
      or performed behaviours are mistakenly interpreted as signals of honesty. Across four studies
      drawing on real-life trial testimony (N = 121), proven false versus true criminal confessions (N
      = 135), cross-cultural deception belief surveys (75 countries, N > 11,000), and meta-analytic
      deception cue data (k = 206 studies, N = 24,483 judges), we find: (1) disfluency is significantly
      higher in truthful speech (d = 0.60, p = .004), a medium effect 6 times larger than the median
      deception cue; (2) false confessions show massive linguistic distancing, with impersonal
      pronoun contractions up to 12x higher and second-person references 7.6x higher than true
      confessions; (3) 78.6% of publicly believed deception cues are empirically unrelated or
      inversely related to actual deception (binomial test p = .029); and (4) human deception
      detection accuracy averages 54%, with lie detection specifically at 47% — below chance. These
      findings suggest that demeanour-based credibility assessment does not merely fail to detect
      deception but systematically penalises truthful speakers whose authentic cognitive effort
      produces the signals misread as guilt.

      Keywords: deception detection, credibility assessment, linguistic markers, false confessions,
      signal inversion, disfluency, cognitive load, wrongful conviction



1. Introduction
Can humans reliably determine whether someone is telling the truth? The accumulated empirical
evidence suggests they cannot. Bond and DePaulo (2006), synthesising 206 studies involving 24,483
judges, found that people achieve an average accuracy of just 54% in distinguishing lies from truths —
barely above the 50% rate expected by chance. More troubling still, accuracy for detecting lies
specifically was only 47%, meaning that when someone is actually lying, untrained observers are more
likely to believe them than to identify the deception.
    This paper argues that the failure of human deception detection is not merely a matter of insufficient
skill or training. Rather, it reflects a fundamental directional inversion in the cues that humans rely
upon when assessing credibility. The behaviours that people worldwide believe indicate deception —
gaze aversion, disfluency, nervous appearance, hedging language — are either empirically unrelated to
deception or, in several cases, are actually more characteristic of truthful speech. Conversely, the
smooth, confident, fluent delivery that observers interpret as honesty is more consistent with rehearsed or

---
deceptive communication.
   We term this pattern the Signal Inversion Effect and present evidence for its operation across four
converging lines of investigation: (1) original analysis of linguistic markers in real-life trial testimony,
(2) reanalysis of proven false versus true criminal confessions, (3) a systematic comparison of public
beliefs about deception cues against their empirical validity, and (4) a convergence analysis
demonstrating that algorithmic classification using linguistic features consistently outperforms human
judgment because it bypasses the inverted heuristics that humans rely upon.
   The implications extend beyond academic interest. If credibility assessment in legal contexts relies on
cues that are systematically inverted, then truthful individuals — particularly those exhibiting authentic
cognitive effort, fragmented recall, or genuine uncertainty — are structurally disadvantaged in
adversarial proceedings. The Signal Inversion Effect suggests that demeanour evidence is not merely
unreliable; it is directionally harmful.


2. Study 1: Linguistic Markers of Veracity in Trial Testimony

2.1 Method
We analysed 121 video transcripts from the Real-Life Trial Dataset (Pérez-Rosas, Abouelenien,
Mihalcea, & Burzo, 2015), comprising 60 truthful and 61 deceptive clips drawn from actual court
proceedings. Ground truth labels were established through guilty verdicts, not-guilty verdicts, and
post-conviction exonerations. Each transcript was coded for eight linguistic variables: hedging rate,
certainty marker rate, disfluency/filler rate, experiencer framing rate, passive construction rate, negative
emotion rate, first-person pronoun rate, and total word count. All rates were computed per 100 words.
Group comparisons used Mann-Whitney U tests (due to non-normal distributions), with effect sizes
reported as Cohen's d and point-biserial correlations.

2.2 Results
Table 1. Group comparisons for linguistic variables (Mann-Whitney U).

  Variable                    Truth M       Truth SD       Decep M        Decep SD             U        p      Cohen's d

  Disfluency/Fillers            5.14           4.21           3.03           2.68            2380.5   .004**     0.60

  Negative Emotion              0.02           0.17           0.13           0.52        1711.0       .103       -0.27

  First-Person Pron.            6.13           4.38           7.15           4.16        1561.5       .164       -0.24

  Experiencer Framing           0.60           1.51           0.34           0.94        1934.0       .448       0.21

  Certainty Markers             0.35           1.25           0.76           3.15        1687.5       .265       -0.17

  Hedging Rate                  0.86           1.31           1.05           1.41        1675.5       .376       -0.14
** p < .01. Only variables with |d| > 0.10 shown. Full results in supplementary materials.


The primary finding was a significant medium effect for disfluency/filler rate: truthful speakers produced
significantly more speech disfluencies (M = 5.14 per 100 words) than deceptive speakers (M = 3.03), U
= 2380.5, p = .004, d = 0.60, rpb = .290. This effect is approximately six times larger than the median
deception cue effect size of d = 0.10 reported in DePaulo et al.'s (2003) comprehensive meta-analysis of
158 cues across 120 independent samples.
   A logistic regression model using all six linguistic predictors achieved 63.5% classification accuracy
(10-fold cross-validation, SD = 11.5%), compared to the 54% accuracy rate for human judges established
by Bond and DePaulo (2006). This gap is notable because the algorithm uses features that are largely
imperceptible to human observers in real time, while the features humans do perceive (gaze, demeanour,

---
general nervousness) lack empirical validity as deception cues.


3. Study 2: Linguistic Analysis of True and False Confessions

3.1 Method
We reanalysed published data from Rizzelli, Kassin, and Gales (2021), who compared 37 confessions
proven false through DNA exoneration or equivalent evidence (sourced from the Innocence Project and
DNA Exoneration Database) with 98 confessions presumed true from FBI case files housed at John Jay
College of Criminal Justice. Using the raw word frequency counts published in their Appendix A, we
computed per-confession rates and conducted chi-square tests of proportionality for individual words
within three categories: impersonal pronouns, personal pronouns, and conjunctions.

3.2 Results
Table 2. Selected word-level frequencies in true vs. false confessions (highest discrimination ratios).

                                         True Conf.         False Conf.
               Marker                    (per conf.)        (per conf.)       Ratio            χ²             p

               'you'                          9.4              71.3           7.59x         3903.7         < .001

               'that’s'                       1.7              19.3           11.67x        1288.6         < .001

               'it’s'                         1.2              14.6           12.17x         993.1         < .001

               'but'                          5.2              19.6           3.78x          610.7         < .001

               'if'                           2.9              11.2           3.90x          361.3         < .001

               Impers. pron. (total)         49.0              253.6          5.18x         10701.9        < .001
All chi-square tests df = 1. Per-confession rates computed from published Appendix A totals (ntrue = 98, nfalse = 37).


The most striking individual finding was the rate of second-person pronoun 'you' in false confessions:
71.3 instances per confession compared to 9.4 in true confessions, a ratio of 7.59x (χ²(1) = 3903.7, p <
.001). This reflects the interrogation dynamic underlying false confessions: innocent individuals who
have been coerced into confessing orient their language toward the interrogator ('you said,' 'you told me,'
'you showed me') because the narrative they are recounting was supplied to them rather than
self-generated. True confessors, narrating events they actually experienced, have no comparable need to
reference the interrogator.
    Impersonal pronoun contractions showed the most extreme discrimination. 'That’s' appeared 11.7
times more frequently and 'it’s' 12.2 times more frequently in false confessions. These constructions
('that’s what happened,' 'it’s like I said') represent linguistic distancing: even while confessing, innocent
individuals frame the narrative impersonally rather than using first-person agency ('I did it'). This
distancing occurs below conscious awareness and is not a strategic choice.


4. Study 3: The Belief–Reality Inversion Matrix

4.1 Method
We systematically compared public beliefs about deception cues with their empirical validity by
matching data from two sources: the Global Deception Research Team (2006), who surveyed over
11,000 participants across 75 countries in 43 languages about believed indicators of deception, and
DePaulo et al. (2003), whose meta-analysis of 158 cues across 120 samples established the actual
relationship between each cue and deception. For each cue appearing in both datasets, we coded whether

---
the public belief direction matched or was inverted relative to the empirical finding. We supplemented
the DePaulo effect sizes with the disfluency finding from our Study 1.

4.2 Results
Table 3. Belief–Reality Inversion Matrix. 'Belief %' = percentage of global respondents endorsing this cue as a deception
indicator (GDRT, 2006). 'Actual d' = meta-analytic effect size (DePaulo et al., 2003; ** = current Study 1).
                     Believed Cue                  Belief %         Actual d             Match?
                     Gaze aversion                  63.7%           0.05 (ns)           INVERTED
                     Fidgeting                      52.0%           0.01 (ns)           INVERTED
                     Nervous appearance             45.0%          -0.01 (ns)           INVERTED
                     Speech hesitations             38.0%           0.00 (ns)           INVERTED
                     Disfluency/fillers             35.0%            -0.60**            INVERTED
                     Face touching                  25.0%          -0.02 (ns)           INVERTED
                     Posture shifts                 24.0%           0.04 (ns)           INVERTED
                     Response latency               22.0%           0.02 (ns)           INVERTED
                     Vocal pitch                    20.0%            0.21*               Correct
                     Slower speech                  18.0%           0.07 (ns)           INVERTED
                     Blink rate                     15.0%           0.01 (ns)           INVERTED
                     Self-corrections               12.0%            -0.12              INVERTED
                     Story inconsistency            30.0%             0.13               Correct
                     Lack of detail                 28.0%            0.30*               Correct

Of 14 matched cues, 11 (78.6%) were either empirically unrelated to deception or inversely related to
what the public believes. A one-tailed binomial test confirmed that this inversion rate is significantly
above the 50% chance level (p = .029). The Weighted Inversion Index — computed by summing belief
endorsement percentages with positive signs for inverted cues and negative signs for correct cues — was
+271.7, indicating that the most strongly held beliefs are the most empirically wrong. The three cues
with correct public beliefs (vocal pitch change, story inconsistency, lack of detail) had substantially
lower endorsement rates than the inverted cues.


5. Study 4: Convergence and the Detection Accuracy Gap
The four preceding analyses converge on a single pattern. Table 4 summarises the key comparisons.
Table 4. Convergence summary across all studies.

           Comparison                                                           Accuracy / Effect

           Human deception detection (Bond & DePaulo, 2006; k=206)              54%

           Human lie detection specifically                                     47% (below chance)

           Police officers                                                      ≈55%

           Judges                                                               ≈54%

           Algorithmic (disfluency only, current Study 1)                       60.3%

           Algorithmic (multi-variable, current Study 1)                        63.5%

           Algorithmic (3-predictor, Rizzelli et al., 2021)                     74–83%

           Believed cues that are wrong/unrelated (Study 3)                     78.6%

---
          Disfluency effect size (Study 1)                          d = 0.60 (6x median)

          'you' ratio in false confessions (Study 2)                7.59x




6. General Discussion
The present findings support the existence of a Signal Inversion Effect operating across criminal justice,
forensic linguistics, and public belief systems. The effect is not subtle: the single strongest believed
deception cue worldwide — gaze aversion, endorsed by 63.7% of the global population — has
effectively zero empirical relationship with deception (d = 0.05). Meanwhile, disfluency, which
observers interpret as evasion or nervousness, shows a robust medium-sized association with truthfulness
(d = 0.60). The entire framework of folk credibility assessment is operating with an inverted compass.

6.1 Implications for Legal Proceedings
The implications for credibility assessment in legal contexts are substantial. When judges, jurors, or
investigators assess a witness's demeanour, they are drawing on a set of heuristics that are empirically
inverted. A witness who pauses, says 'um,' breaks eye contact to search memory, qualifies statements
with 'I think' or 'maybe,' and produces a fragmented narrative is exhibiting the cognitive signatures of
genuine recall. These same behaviours activate the observer's folk model of deception, producing a
credibility judgment that is directionally wrong.
   Critically, this is not a problem that can be solved through judicial training or improved instructions
to jurors. Bond and DePaulo (2006) found that professional training does not improve deception
detection accuracy: police officers (~55%), customs officials (~55%), and judges (~54%) perform no
better than untrained members of the public. The inversion operates at the level of deeply held cognitive
heuristics that are resistant to explicit instruction.

6.2 The Adaptation Problem
An additional concern, not previously addressed in the literature, is the behavioural adaptation
feedback loop. Individuals who are repeatedly disbelieved despite telling the truth — because their
authentic speech patterns trigger observers' inverted credibility heuristics — may learn to suppress those
authentic patterns and adopt performed behaviours (steady eye contact, fluent delivery, reduced hedging)
that match observers' expectations of honest communication. This adaptation process means that
repeated exposure to demeanour-based credibility assessment does not merely fail to identify deception;
it actively trains truthful speakers to communicate in ways that resemble deceptive speech, thereby
eroding the very cues that might otherwise assist in veridical assessment.

6.3 Limitations
Several limitations should be noted. Study 1 relies on a relatively small corpus (N = 121) with short clips
averaging 28 seconds. The disfluency finding, while robust (d = 0.60, p = .004), requires replication with
larger and more diverse samples. Study 2 uses aggregate raw counts from published appendices rather
than individual-level data, precluding more sophisticated statistical modelling. Study 3's belief–reality
matching required judgment calls about which GDRT belief categories correspond to which DePaulo
meta-analytic cues; different matching decisions could alter the inversion rate. These limitations
notwithstanding, the convergence of findings across independent datasets, methodologies, and research
groups strengthens confidence in the general pattern.

6.4 Conclusion

---
Demeanour-based credibility assessment — the practice of inferring veracity from how someone speaks,
looks, and behaves — is not merely unreliable. It is systematically biased against truthful
communication. The cues that authentic cognitive effort produces during genuine recall (disfluency,
hedging, fragmented narrative, gaze aversion during memory search) are precisely the cues that human
observers interpret as indicators of deception. This Signal Inversion Effect operates across trial
testimony, criminal confessions, and global belief systems, and it is resistant to professional training.
Until credibility assessment practices are reformed to eliminate reliance on demeanour evidence, truthful
individuals will continue to be structurally disadvantaged in any context where their honesty is judged by
how they appear rather than what they say.

---
References
Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable
     difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), Psychology and the real world (pp. 56–64).
     Worth Publishers.
Bond, C. F., Jr., & DePaulo, B. M. (2006). Accuracy of deception judgments. Personality and Social Psychology
    Review, 10(3), 214–234.
Bond, C. F., Jr., & The Global Deception Research Team. (2006). A world of lies. Journal of Cross-Cultural
    Psychology, 37(1), 60–74.
DePaulo, B. M., Lindsay, J. J., Malone, B. E., Muhlenbruck, L., Charlton, K., & Cooper, H. (2003). Cues to
    deception. Psychological Bulletin, 129(1), 74–118.
Hartwig, M., & Bond, C. F., Jr. (2011). Why do lie-catchers fail? A lens model meta-analysis of human lie
    judgments. Psychological Bulletin, 137(4), 643–659.
Kassin, S. M. (2014). False confessions: Causes, consequences, and implications for reform. Policy Insights from
     the Behavioral and Brain Sciences, 1(1), 112–121.
Luke, T. J., et al. (2023). What have we learned about cues to deception? A survey of expert opinions. Psychology,
    Crime & Law. Advance online publication.
Pennebaker, J. W., & Francis, M. E. (1999). Linguistic Inquiry and Word Count: LIWC. Erlbaum Publishers.
Pérez-Rosas, V., Abouelenien, M., Mihalcea, R., & Burzo, M. (2015). Deception detection using real-life trial data.
     Proceedings of the ACM International Conference on Multimodal Interaction (ICMI 2015), 59–66.
Rizzelli, L., Kassin, S., & Gales, T. (2021). The language of criminal confessions: A corpus analysis of confessions
     presumed true vs. proven false. The Wrongful Conviction Law Review, 2(3), 205–225.
Sen, U. M., et al. (2022). Multimodal deception detection using real-life trial data. IEEE Transactions on Affective
     Computing, 13(1), 306–319.
Vrij, A., Granhag, P. A., & Porter, S. B. (2010). Pitfalls and opportunities in nonverbal and verbal lie detection.
      Psychological Science in the Public Interest, 11(3), 89–121.

---
Supplementary Materials: Full Statistical Output
The complete analysis code (Python/SciPy), raw data files, and SPSS-compatible CSV files are available
from the corresponding author upon request and will be deposited in the Open Science Framework
repository upon acceptance.

S1. Study 1 Classification Model
Logistic regression (maximum likelihood estimation) with disfluency rate as sole predictor: B0 = -0.740,
B1 = 0.183, classification accuracy = 60.3%. Multi-variable model (10-fold cross-validated) using
disfluency rate, hedging rate, certainty markers, experiencer framing, negative emotion, and first-person
pronoun rate: mean accuracy = 63.5% (SD = 11.5%, range 41.7%–84.6%). Standardised coefficients:
disfluency (β = +0.546), experiencer framing (β = +0.364), negative emotion (β = -0.366), first-person
pronouns (β = -0.194), certainty (β = -0.097), hedging (β = -0.080).

S2. Study 3 Binomial Test
One-tailed binomial test: observed inversions = 11/14 = 78.6%, H0: inversion rate = 50%, p = .029. 95%
CI [57.1%, 100.0%]. Weighted Inversion Index = +271.7 (positive values indicate that the most strongly
endorsed beliefs are the most wrong).

---
