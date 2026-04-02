 THE SIGNAL INVERSION EFFECT
                                  —
How Authentic Cognition Mimics Deception Across Domains: A Cross-
                 Disciplinary Research Proposal


               Research Design & Statistical Analysis Plan
                          Draft — March 2026




               CONFIDENTIAL — FOR RESEARCH PURPOSES ONLY

---
Executive Summary
This proposal outlines a cross-disciplinary study designed to demonstrate what we term
the Signal Inversion Effect: the systematic pattern whereby authentic cognitive and
linguistic behaviours are misidentified as indicators of deception, while performed or
rehearsed behaviours are mistakenly interpreted as signals of honesty.

The core thesis is deliberately counterintuitive: the people who sound most guilty are
most likely to be telling the truth, and the people who sound most credible are most
likely to be lying. This is not a marginal effect. It operates across criminal justice,
education, medicine, employment, and interpersonal relationships, and it is supported
by converging evidence from multiple independent research traditions.

By reanalysing existing large-scale datasets using SPSS, we aim to demonstrate
statistically significant negative correlations between authentic truth markers and
perceived credibility markers across multiple domains simultaneously, producing
evidence that is, in the words of our research question, implausible to dismiss.

The Core Paradox
Across every domain studied, the same inversion pattern emerges:

 Behaviour                      What It Actually Signals        What Observers Believe
 Hedging ("I think," "maybe")   Genuine memory retrieval;       Evasion; hiding something
                                honest uncertainty
 Breaking eye contact           Cognitive effort; accessing     Shifty; untrustworthy
                                memory
 Fragmented narrative           Authentic trauma recall; real   Incoherent; fabricating
                                memory is messy
 Saying "I don't know"          High competence (Dunning-       Incompetent; evasive
                                Kruger); genuine limits of
                                knowledge
 Confident, fluent delivery     Rehearsed narrative;            Honest; credible
                                possible deception
 Impersonal pronouns ("it,"     Distancing from false           Not typically noticed
 "that")                        narrative (false confessions)
 Reporting confusion after      Deep engagement; desirable      Failure to understand
 learning                       difficulty

---
Why This Matters
If this inversion is as systematic as the converging evidence suggests, it has profound
implications. Innocent people are being convicted because they sound guilty.
Competent students are being underestimated because they report confusion.
Genuinely ill patients are being dismissed because their symptom descriptions sound
vague. The entire folk psychology of credibility assessment may be functioning as an
inverted compass.

---
Foundational Evidence
1. Deception Detection Is Barely Above Chance
Bond & DePaulo (2006) conducted the definitive meta-analysis: 206 studies, 24,483
judges. Average accuracy in detecting lies was 54%, barely above a coin flip. People
correctly identified only 47% of lies as deceptive. Critically, people are more confident in
their incorrect judgments than their correct ones.

This alone should be disqualifying for any system that relies on human credibility
assessment, yet the entire criminal justice system depends on exactly this capacity.

2. What People Believe Signals Lying Is Wrong
The Global Deception Research Team (2006) surveyed over 11,000 participants across
75 countries in 43 languages. The dominant finding: 64% of people worldwide believe
liars avoid eye contact. This belief is essentially universal and essentially wrong. Meta-
analyses of actual deception cues show gaze aversion has no reliable relationship with
lying. Liars, if anything, maintain more eye contact because they know the stereotype
and overcompensate.

3. Actual Cues to Deception Are Inverted
DePaulo et al. (2003) analysed 158 cues across 1,338 estimates from 120 studies. The
findings relevant to our thesis:

   •   Liars tell less compelling tales with fewer ordinary imperfections
   •   Truth-tellers include more spontaneous corrections, hedging, and admissions of
       memory gaps
   •   The only consistently reliable cues (higher vocal pitch, larger pupil dilation) are
       invisible to untrained observers
   •   The average effect size across all 158 cues was d = 0.10, which is functionally
       negligible

4. False Confessions Are Linguistically Distinct
Rizzelli, Kassin & Gales (2021) compared 37 proven false confessions (Innocence
Project, DNA exonerations) with 98 presumed true confessions (FBI case files) using
LIWC and corpus analysis. Three linguistic predictors distinguished the two with 74–
83% accuracy:

---
   •   Impersonal pronouns ("it," "that," "this"): higher in false confessions
   •   Personal pronouns ("I," "me," "mine"): higher in true confessions
   •   Conjunctions ("but," "and," "because"): higher in true confessions
The guilty person who actually committed the crime says "I" more. The innocent person
performing a coerced confession distances themselves with "it" and "that." Yet jurors,
judges, and police cannot distinguish between the two. False confessions remain
persuasive even when contradicted by DNA evidence.

5. Desirable Difficulty and the Confusion Paradox
Bjork & Bjork (2011) established that learning conditions which feel difficult and
confusing actually produce superior long-term retention. Students who report confusion
after a lesson have engaged more deeply than students who report confidence. The
confident students experienced a fluency illusion: the material felt easy, so they
assumed they understood it.

This is the same inversion in a different domain. The signal of genuine cognitive
engagement (confusion, difficulty, uncertainty) is interpreted as failure, while the signal
of superficial processing (confidence, fluency) is interpreted as success.

---
Available Datasets
The following publicly or semi-publicly available datasets can be used for the proposed
analyses:

 Dataset               N                  Contents               Access          Domain
 Michigan Real-Life    121 videos (61     Transcripts, gesture   Request from    Criminal
 Trial (Pérez-Rosas    deceptive, 60      annotations,           U-Michigan      justice
 et al., 2015)         truthful)          ground-truth labels    LIT lab
                                          via
                                          verdict/exoneration
 Rizzelli Confession   135                LIWC-coded             CUNY            Criminal
 Corpus (2021)         confessions (37    linguistic features;   Academic        justice
                       false, 98 true)    pronoun                Works (open)
                                          frequencies;
                                          conjunction rates
 Global Deception      11,000+            Beliefs about          Published       Belief
 Research Team         participants, 75   deception cues;        data tables     systems
 (2006)                countries          cross-cultural         (open)
                                          stereotypes
 DePaulo et al.        1,338 estimates    Effect sizes for       Published       Deception
 (2003) Meta-          of 158 cues        each cue;              tables (open)   cues
 Analysis                                 moderator analyses
 Bond & DePaulo        206 studies,       Accuracy rates;        Published       Detection
 (2006) Meta-          24,483 judges      modality effects;      tables (open)   accuracy
 Analysis                                 motivation effects

---
Methodology
Study Design Overview
This study uses a convergent cross-disciplinary design, reanalysing existing datasets
with consistent coding frameworks to demonstrate the Signal Inversion Effect across
domains. The primary statistical tool is SPSS (version 28+).

Phase 1: Linguistic Coding of Trial Transcripts
Dataset: Michigan Real-Life Trial Dataset (121 transcripts)

Each transcript will be coded for the following linguistic variables using LIWC (Linguistic
Inquiry and Word Count) software:

 Variable                Operationalisation                   Predicted Direction
 Hedging frequency       Count of uncertainty markers: "I     Higher in truthful statements
                         think," "maybe," "sort of," "I'm
                         not sure," "perhaps"
 Certainty markers       Count of absolute terms:             Higher in deceptive statements
                         "definitely," "absolutely," "I'm
                         certain," "clearly"
 Experiencer framing     Passive/agentless                    Higher in truthful trauma
                         constructions: "it happened,"        accounts
                         "things got out of hand"
 First-person pronoun    Frequency of "I," "me," "my,"        Higher in truthful statements
 rate                    "mine" per 100 words
 Impersonal pronoun      Frequency of "it," "that," "this,"   Higher in deceptive statements
 rate                    "those" per 100 words
 Narrative coherence     Rated 1–5 by blinded coders:         Moderate coherence = truthful;
                         logical flow, chronological order,   very high or very low =
                         completeness                         deceptive
 Spontaneous             Self-repairs, backtracking,          Higher in truthful statements
 corrections             "actually, no, it was..."
 "I don't remember"      Frequency and syntactic context      Different patterns in true vs.
 usage                   of memory-gap admissions             false statements (Rizzelli, 2021)



Phase 2: Belief–Reality Inversion Matrix
Datasets: Global Deception Research Team (2006) + DePaulo et al. (2003)

---
We construct a matrix comparing what people believe signals deception (from the
GDRT survey data) against what actually correlates with deception (from the DePaulo
meta-analysis). For each cue, we code:

   •   Belief direction: Do people think this cue increases or decreases with lying?
   •   Actual direction: Does this cue actually increase or decrease with lying?
   •   Concordance: Do belief and reality match, or are they inverted?
Our prediction: a statistically significant proportion of cues will show inversion (belief
direction opposite to actual direction), concentrated specifically in the hedging,
uncertainty, and gaze categories.

Phase 3: False Confession Linguistic Replication
Dataset: Rizzelli Confession Corpus (37 false, 98 true)

We replicate and extend Rizzelli’s (2021) findings by:

   •   Running a discriminant function analysis in SPSS using their three predictor
       variables (personal pronouns, impersonal pronouns, conjunctions)
   •   Adding our hedging and certainty marker variables to test whether they improve
       classification accuracy
   •   Cross-validating with the Michigan trial transcript data

Phase 4: Cross-Domain Convergence Test
This is the critical phase. We standardise the inversion effect across all datasets into a
common metric and test whether the same directional pattern holds:

   •   In criminal justice: hedging/fragmentation predicts innocence but perceived guilt
   •   In education: reported confusion predicts deeper learning but perceived failure
   •   In deception beliefs: the cues people trust most are the least diagnostic
A consistent negative correlation between authentic markers and perceived credibility
markers across three or more independent domains would constitute strong evidence
for a domain-general Signal Inversion Effect.

---
SPSS Analysis Plan
Primary Analyses
Analysis 1: Correlation Matrix (Trial Transcripts)
Bivariate Pearson correlations between each linguistic variable and ground-truth
veracity label (0 = deceptive, 1 = truthful). We predict significant positive correlations
between truthfulness and hedging frequency, spontaneous corrections, first-person
pronoun rate, and memory-gap admissions.

SPSS syntax: CORRELATIONS /VARIABLES=veracity hedging certainty experiencer
firstperson impersonal coherence corrections memory_gaps /PRINT=TWOTAIL NOSIG.

Analysis 2: Binary Logistic Regression (Confession Data)
Dependent variable: confession type (0 = true, 1 = false). Predictors: personal pronoun
rate, impersonal pronoun rate, conjunction rate, hedging rate, certainty marker rate.

SPSS syntax: LOGISTIC REGRESSION VARIABLES confession_type
/METHOD=ENTER personal_pron impersonal_pron conjunctions hedging certainty
/CLASSPLOT /CASEWISE OUTLIER(2) /PRINT=GOODFIT CI(95).

Analysis 3: Sign Test for Belief–Reality Inversion
For each cue studied in both the GDRT belief data and the DePaulo actual-cue data, we
code whether the belief direction matches or opposes the empirical direction. A one-
sample binomial test against chance (50%) determines whether inversions occur
significantly more often than expected.

SPSS syntax: NPAR TESTS /BINOMIAL (.50)=inversion_coded.

Analysis 4: Discriminant Function Analysis (Cross-Validation)
Using the Michigan trial data as a training set, we build a discriminant function from our
linguistic variables and test classification accuracy against known veracity labels. We
then cross-validate against the Rizzelli confession corpus.

SPSS syntax: DISCRIMINANT /GROUPS=veracity(0 1) /VARIABLES=hedging
certainty firstperson impersonal coherence corrections /METHOD=WILKS /PRIORS
EQUAL /STATISTICS=MEAN STDDEV UNIVF BOXM COEFF RAW TABLE
CROSSVALID.

Secondary Analyses
Effect Size Comparison Across Domains

---
We convert all inversion effects to a common metric (Cohen’s d) and test whether the
magnitude of inversion is consistent across criminal justice, education, and belief
domains using a heterogeneity test (Q statistic).

"I Don’t Remember" Deep Dive
Following Rizzelli’s finding that variations of "I don’t remember" differed between true
and false confessions, we conduct a targeted analysis of this specific phrase across
both the confession corpus and the trial transcripts. Syntactic context, frequency, and
position within narrative are coded and compared.

---
Predicted Outcomes
If the Signal Inversion Effect is real and domain-general, we predict:

   1. Negative correlation (r < –0.30) between hedging frequency and perceived
      credibility, despite a positive correlation between hedging and actual truthfulness
   2. Classification accuracy of 70–80% in distinguishing true from false statements
      using linguistic markers that observers cannot reliably detect
   3. Significant inversion rate (>65%) when comparing believed deception cues
      against empirically validated cues, with gaze aversion, hedging, and nervous
      behaviour showing the strongest inversions
   4. Consistent effect direction across criminal justice, education, and belief
      domains, with non-significant heterogeneity (Q test p > .05)
   5. The phrase "I don’t remember" will show qualitatively different syntactic
      patterns in true versus false statements, with true statements using it as a
      genuine memory boundary and false statements using it as a narrative
      placeholder


Implications
A confirmed domain-general Signal Inversion Effect would suggest that:

   •   Human credibility assessment systems (jury trials, police interrogation, job
       interviews, clinical assessment) are operating with inverted assumptions
   •   Training programmes that teach people to detect deception through behavioural
       cues may actively worsen accuracy by reinforcing inverted beliefs
   •   Linguistic analysis tools (LIWC, corpus analysis) can outperform human
       judgment because they bypass the folk-psychological inversion
   •   Innocent defendants who display authentic trauma responses (hedging,
       fragmentation, gaze aversion) are systematically disadvantaged in adversarial
       legal systems
   •   Educational assessment that rewards confident self-reports over honest
       confusion systematically underestimates the students who are learning most
       deeply

---
Historical Parallels: When Consensus Was Wrong
The Signal Inversion Effect sits within a broader pattern of scientific reversals where
expert consensus persisted for decades despite being fundamentally incorrect. These
parallels are included not as direct evidence but as precedent for how deeply
counterintuitive findings can meet institutional resistance.

Peptic Ulcers and H. pylori
For decades, the medical establishment was certain that peptic ulcers were caused by
stress, spicy food, and personality type. Barry Marshall could not convince anyone that
a bacterial infection was the true cause. In 1984, he drank a petri dish of H. pylori,
developed gastritis, and proved his case. He and Robin Warren received the Nobel
Prize in 2005. The stress-personality model had persisted because it felt intuitively
correct and matched existing cultural assumptions about psychosomatic illness.

Dietary Fat and Heart Disease
In the 1960s, the sugar industry funded research that successfully shifted public health
blame from sugar to dietary fat. The resulting low-fat dietary guidelines dominated
nutritional science for 40 years and likely contributed to the obesity epidemic by
encouraging high-carbohydrate diets. The manipulation was not revealed until 2016
when researchers at UCSF discovered the industry documents.

The Four-Minute Mile
Before Roger Bannister broke the four-minute mile in 1954, it was widely believed to be
a physical impossibility. Within 46 days, his record was broken again. Within three
years, sixteen runners had done it. The barrier was not physical but perceptual. The
consensus itself was the constraint.

Lobotomy
António Egas Moniz received the Nobel Prize in Physiology or Medicine in 1949 for
developing the prefrontal lobotomy. The procedure was endorsed by the psychiatric
establishment and performed on tens of thousands of patients. It is now regarded as
one of the most damaging episodes in the history of medicine.

The common thread: in each case, the consensus position was not merely slightly
wrong but directionally wrong. The treatment caused the disease. The diet caused the
obesity. The perceived limit created the actual limit. The Signal Inversion Effect follows

---
this same pattern: the cues people use to detect deception are the cues that actually
signal honesty.

---
Key References
Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way:
Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.),
Psychology and the real world (pp. 56–64). Worth Publishers.

Bond, C. F., Jr., & DePaulo, B. M. (2006). Accuracy of deception judgments. Personality
and Social Psychology Review, 10(3), 214–234.

Bond, C. F., Jr., & The Global Deception Research Team. (2006). A world of lies.
Journal of Cross-Cultural Psychology, 37(1), 60–74.

DePaulo, B. M., Lindsay, J. J., Malone, B. E., Muhlenbruck, L., Charlton, K., & Cooper,
H. (2003). Cues to deception. Psychological Bulletin, 129(1), 74–118.

Hartwig, M., & Bond, C. F., Jr. (2011). Why do lie-catchers fail? A lens model meta-
analysis of human lie judgments. Psychological Bulletin, 137(4), 643–659.

Kassin, S. M. (2014). False confessions: Causes, consequences, and implications for
reform. Policy Insights from the Behavioral and Brain Sciences, 1(1), 112–121.

Luke, T. J., et al. (2023). What have we learned about cues to deception? A survey of
expert opinions. Psychology, Crime & Law.

Pérez-Rosas, V., Abouelenien, M., Mihalcea, R., & Burzo, M. (2015). Deception
detection using real-life trial data. Proceedings of the ACM International Conference on
Multimodal Interaction (ICMI 2015), 59–66.

Rizzelli, L., Kassin, S., & Gales, T. (2021). The language of criminal confessions: A
corpus analysis of confessions presumed true vs. proven false. The Wrongful
Conviction Law Review, 2(3), 205–225.

Sen, U. M., et al. (2022). Multimodal deception detection using real-life trial data. IEEE
Transactions on Affective Computing, 13(1), 306–319.

Sporer, S. L., & Schwandt, B. (2006). Paraverbal indicators of deception: A meta-
analytic synthesis. Applied Cognitive Psychology, 20, 421–446.

Vrij, A., Granhag, P. A., & Porter, S. B. (2010). Pitfalls and opportunities in nonverbal
and verbal lie detection. Psychological Science in the Public Interest, 11(3), 89–121.

---
