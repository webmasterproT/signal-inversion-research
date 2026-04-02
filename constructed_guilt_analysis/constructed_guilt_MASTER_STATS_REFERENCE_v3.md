# CONSTRUCTED GUILT — Master Stats Reference v3
### Key Claims · Sources · Flags
*Final version — all uploaded research files reviewed*

---

## HOW TO READ THIS DOCUMENT

- ✅ **Consistent & sourced** — use as-is
- 🔵 **Original research (your analysis)** — needs method note when cited
- 🟡 **Needs minor clarification** — correct but inconsistently presented
- 🔴 **Needs fixing** — unsupported or genuinely wrong

---
---

## PILLAR 1: Deception Detection Failure

---

### ✅ Overall accuracy: 54.1%
**Source:** Bond & DePaulo (2006) — 247 studies, 24,483 judges, 95% CI [53.6, 54.6]
**Also consistent with:** Ekman & O'Sullivan (1991): 52.8%; Vrij (2008): 54.0%; Hartwig & Bond (2011): 53.9%

The 54.1% is the *overall* rate (truth + lie trials combined). The same study breaks down as:
- Truth detection: **61%** — people have a truth bias (tend to believe)
- Lie detection: **47%** — below chance; people are *worse* than guessing at detecting lies specifically

**This resolves the "47% figure" issue from earlier audits.** It is not a contradiction — it is a component. The Nuremberg document uses 47% without this framing. Fix: cite as *"lie detection specifically: 47% — below chance (Bond & DePaulo, 2006)"*.

---

### ✅ Training increases confidence, not accuracy
**Source:** Kassin et al. (2005) — directly cited in statistical appendix
Trained investigators are more certain of assessments that are barely above chance. Confidence and accuracy are dissociated.

---

### 🟡 DePaulo et al. (2003) vs Bond & DePaulo (2006) — two different papers
These serve different functions and must not be conflated:

| Paper | What it measures | Key figure |
|---|---|---|
| Bond & DePaulo (2006) | Detection *accuracy* (how well people detect lies) | **54.1%**, N=24,483 |
| DePaulo et al. (2003) | Which *cues* actually correlate with deception | Effect sizes per cue, N>10,000 |

**Fix needed in Institutional Negligence supplement:** It attributes "54.1% accuracy" to "DePaulo et al. (2003), 120+ studies, 2,000+ participants." This is the wrong paper and wrong N. Change to Bond & DePaulo (2006).

---

### 🔴 "~23% false accusation rate" — this is a DERIVED CALCULATION, not an empirical finding
**Currently appears in:** statistical appendix, full thesis, What If It Is You — stated as plain fact

**The derivation (from statistical appendix, Section 1.3):**
> "A trained investigator assessing 100 suspects will correctly identify approximately 54 and incorrectly classify approximately 46. Of the incorrectly classified, approximately half will be innocent persons assessed as deceptive — approximately 23%."

This is an inference from the 54.1% figure, not a separate study result. It assumes a 50/50 base rate of truth-tellers to liars in the assessed population, which is unlikely in real interrogation settings (where the proportion of guilty suspects is higher, which would change the calculation).

**Fix:** Every time 23% is cited, add: *"(derived from Bond & DePaulo, 2006 accuracy rate, assuming equal base rates)"* — or reframe it as the illustrative calculation it is. Do not cite it as an independent empirical finding.

---

### 🔵 91.3% of credibility cues are inverted (21/23) — ORIGINAL RESEARCH
**Your analysis.** Method: 23 cues matched between GDRT (2006) belief data (N=11,227, 75 countries) and DePaulo et al. (2003) effect sizes. Binomial test p<0.0001, 95% CI [75.1%, 100%].

By category:
- Nonverbal cues: 10/11 inverted (90.9%)
- Paralinguistic cues: 5/5 inverted (100%)
- Verbal cues: 6/7 inverted (85.7%)

**Standard citation:** *"Original analysis (this thesis): Belief-Reality Inversion Matrix; Global Deception Research Team (2006) × DePaulo et al. (2003), N=23 matched cues, binomial test p<0.0001"*

Note: An earlier draft used 78.6% (11/14 cues). This is the same analysis on a 14-cue subset used in Study 3. Use **91.3% (21/23) as the headline everywhere.** The 78.6% only appears in detailed Study 3 tables.

---

### 🔵 Disfluency significantly higher in truthful speech — d = 0.60, p = 0.004 — ORIGINAL RESEARCH
**Your analysis.** Dataset: Pérez-Rosas et al. (2015) Michigan Real-Life Trial Corpus, N=121. Mann-Whitney U test.

Context: d=0.60 is 6× the median deception cue effect size (DePaulo et al. 2003 median = d=0.10). DePaulo shows speech hesitations at d=0.05 (null). Your finer-grained disfluency/filler coding reveals a real signal invisible in DePaulo's broader category.

**Standard citation:** *"Original analysis (this thesis), Study 1: reanalysis of Pérez-Rosas et al. (2015) corpus, d=0.60, p=0.004"*

---

### 🔵 Algorithmic detection outperforms human judgment — ORIGINAL RESEARCH
- Single variable (disfluency): 60.3%
- Multi-variable model (10-fold CV): 63.5%
- Vs human judgment: 54% (Bond & DePaulo, 2006)
- Gap: 9.5 percentage points

**Standard citation:** *"Original analysis (this thesis), Study 4: Pérez-Rosas et al. (2015) corpus; human baseline from Bond & DePaulo (2006)"*

---
---

## PILLAR 2: Memory Distortion

---

### ✅ Full memory distortion table — all studies now identified

| Study | Manipulation | d | False Memory % | Notes |
|---|---|---|---|---|
| Loftus & Palmer (1974) | Single verb change | 0.89 | 32% vs 14% controls | "Smashed" vs "contacted"; 16 km/h speed diff |
| Loftus et al. (1978) | Leading question | 0.72 | 17% | Subjects "recalled" non-existent barn |
| McCloskey & Zaragoza (1985) | Post-event info | 0.61 | ~25% | False recall in 1-in-4 subjects |
| Belli (1989) | Misleading questions | 0.68 | ~22% | Memory substitution in majority |
| Loftus (1993) — Lost in Mall | False narrative | — | 25% | 25% developed detailed false memories |
| Hyman et al. (1995) | False childhood events | — | 20–25% | Subjects elaborated entirely fabricated events |
| Loftus (2005) — 30-year review | Various | 0.60–0.95 | 15–35% | Consistent replication across 30 years |
| **AGGREGATE** | Post-event language | **d=0.72** | **~22%** | 1-in-5 subjects |

**The three previously unnamed rows are now confirmed: Loftus et al. (1978), McCloskey & Zaragoza (1985), and Belli (1989).** All documents should use these names in the table.

---
---

## PILLAR 3: False Confessions

---

### ✅ Aggregate range: 12–30% of exonerations involve false confessions
This is correct as a range drawn across multiple datasets — not a single study's finding. The range reflects genuine methodological variation: different jurisdictions, different evidentiary thresholds, different population samples.

**Full source table:**

| Study | N | False Confession % | Notes |
|---|---|---|---|
| Kassin & Gudjonsson (2004) | Review | 14–25% | US/UK range |
| Gross et al. (2005) | 340 | 15.3% | 52/340 US exonerees |
| Garrett (2011) | 250 | 10.8% (27 cases) | DNA-confirmed innocent |
| National Registry of Exonerations (2023) | 3,300+ | ~12% | Juveniles = 42% |
| Gudjonsson (2018) | UK case review | Substantial | 40-year CCRC analysis |
| Scherr et al. (2020) | NRE registry | ~30% | Cumulative disadvantage |
| Gudjonsson (2003) — UK custodial | 509 | 11.3% | Self-reported prior false confession |
| Kassin et al. (2010) | Multiple | 15–25% | Reid technique as primary risk factor |

---

### 🟡 Garrett (2011): 10.8% falls below the stated 12% floor
27/250 = 10.8%. This looks like it contradicts the stated range floor of 12%.

The explanation is correct and present in the statistical appendix (Section 3.2): exoneration databases are undercounts — they only capture cases where conviction occurred, the defendant survived, exculpatory evidence was preserved, and exoneration succeeded. The 10.8% is a floor within an already filtered dataset.

**This explanation must travel with every citation of the 27/250 figure.** Without it, readers and critics will flag the contradiction.

---

### 🟡 14–26% in Institutional Negligence supplement
This is a narrower range drawing primarily from DNA-confirmed exonerations (Kassin & Gudjonsson, 2004 + Innocence Project). It is not wrong but conflicts with 12–30% used everywhere else.

**Fix:** Either standardise all documents to 12–30% (with 14–26% noted as the DNA-confirmed subset), or add one sentence explaining the difference in the Institutional Negligence supplement.

---

### 🔵 Linguistic distancing in false confessions — ORIGINAL RESEARCH
**Your analysis.** Dataset: Rizzelli et al. (2021) corpus, N=135 (37 false, 98 true confessions). Chi-square tests on word frequency per confession.

Key findings:
- "you": 7.6× higher in false confessions (χ²=3903.7, p<0.001)
- "that's": 11.7× higher in false confessions
- "it's": 12.2× higher in false confessions
- Impersonal pronoun total: 5.18× higher

**Interpretation:** Innocent false confessors orient toward the interrogator ("you said," "you told me") because the narrative was fed to them, not self-generated. They linguistically distance themselves from a crime they did not commit even while confessing to it.

**Standard citation:** *"Original analysis (this thesis), Study 2: reanalysis of Rizzelli et al. (2021) corpus (N=135; 37 false, 98 true confessions)"*

---
---

## PILLAR 4: Suggestibility & Pre-Interrogation

---

### 🟡 Compound elevation: +80–120% — derived, not a single study
**Components now fully sourced:**

| Condition | Increase | Source |
|---|---|---|
| Anxiety induction | +38% | Gudjonsson & Clark (1986) |
| Sleep deprivation | +56% | Harrison et al. (2014) |
| Extended detention | +29–44% | ⚠️ Author still missing — year 2010 |
| Custody vs neutral | Yield +31%, Shift +42% | ⚠️ Author still missing |
| **Compound** | **+80–120%** | Derived from above |

One author name (2010 detention study) and one custody comparison study are still unidentified in the uploaded files.

**Recommended standard phrasing for summaries:**
*"Cumulative pre-interrogation conditions produce a compound elevation in suggestibility of 80–120% above baseline — derived from Gudjonsson & Clark (1986), Harrison et al. (2014), and related custodial research"*

Do not present the 80–120% as a single study's finding in Executive Summary or Institutional Negligence without this note.

---
---

## PILLAR 5: Neurodivergence & Credibility

---

### ✅ Autistic speakers rated significantly more deceptive — now fully cited
**Source:** Lim, A., Young, R.L., & Brewer, N. (2021). Autistic Adults May Be Erroneously Perceived as Deceptive and Lacking Credibility. *Journal of Autism and Developmental Disorders, 52*(2), 490–507.
N=1,410 observers. Autistic speakers rated as more deceptive and less credible than neurotypical speakers when telling the truth.

This is the author that was missing from the main thesis documents. Add: **Lim et al. (2021)** wherever the d=0.65, N=1,410 finding appears.

---

### ✅ 37% of UK police received autism training
**Source:** Autistica (2024). *Autism, Deception and the Criminal Justice System.* Survey N=394 police officers.

---

### ✅ Autism prevalence: 1–2% general vs 2–18% forensic
**Source:** Autistica (2024) — same report.

The wide range (2–18%) reflects variation across different forensic sub-populations (e.g., remand vs sentenced; youth vs adult; different diagnostic thresholds across studies). This is not imprecision — it is the actual documented range. The Autistica (2024) source should be cited wherever this figure appears.

---

### ✅ Autism-typical behaviours diagnostically overlap with deception cues
**Source:** Haworth, K. et al. (2023). Police suspect interviews with autistic adults. *Frontiers in Psychology.*
Gaze aversion (#1 believed deception cue, 63.7% endorsement) and fidgeting (#3 believed cue) are diagnostic autism presentations.

---

### 🔵 Cultural variation in truthful speech — ORIGINAL RESEARCH
From cultural_analysis.txt — your analysis showing truthful speech patterns differ significantly by cultural background (India, US, Romania, Mexico):
- Hedging rate: Kruskal-Wallis H=383.64, p<.001
- Disfluency rate: H=141.16, p<.001
- First-person rate: H=430.82, p<.001

Large cross-cultural effect sizes (US vs Romania hedging: d=1.17).

**Implication for thesis:** Any deception-detection instrument calibrated on an Anglo baseline will generate structurally higher false-positive rates for minority and culturally-different speakers — not because they lie more, but because their truthful speech is linguistically different. Applied to Australia: Aboriginal witnesses are structurally disadvantaged before they speak.

**Standard citation:** *"Original analysis (this thesis), Study 5 [or appropriate study number]: cross-cultural corpus analysis"* — this needs dataset citation (what corpus was used?). Check and add.

---
---

## COUNTER-ARGUMENT TO NOTE: Mourtgos & Adams (risk_interrogation.txt)

This document is a published paper arguing that the risk of false confession from lawful interrogation tactics is "imprecisely estimated and likely overstated." It uses inverse-probability simulations and argues the empirical basis for declaring current techniques dangerously error-prone is thin.

**This is not in your thesis documents but it should be.** It is the strongest available counter-argument. Addressing it strengthens the thesis; ignoring it leaves it vulnerable. Key claims to address:
- Base rates matter: false confession rates depend heavily on assumed proportion of guilty suspects in the interrogated population
- Ecological validity of lab paradigms is disputed
- The paper explicitly states "false confessions are real, consequential, and worthy of sustained policy attention" — they are not dismissing the problem, they are disputing the magnitude of risk from *lawful* techniques specifically

---
---

## COMPLETE FLAGS SUMMARY

| Stat | Status | Action needed |
|---|---|---|
| 47% lie detection | ✅ resolved | Add "lie detection specifically" context |
| 54.1% overall accuracy | ✅ | Fix Institutional Negligence (wrong paper cited) |
| 91.3% inversion rate | 🔵 original | Mark as original; add method note |
| 78.6% inversion rate | 🔵 original (subset) | Only in Study 3 tables, not headline |
| Disfluency d=0.60 | 🔵 original | Mark as original; note vs DePaulo d=0.05 |
| Linguistic distancing in confessions | 🔵 original | Mark as original; cite Rizzelli corpus |
| Cultural speech variation | 🔵 original | Add dataset citation |
| ~23% false accusation rate | 🔴 | Mark as derived calculation, not empirical finding; add assumptions |
| 3 unnamed memory table studies | ✅ resolved | Add: Loftus et al. (1978), McCloskey & Zaragoza (1985), Belli (1989) |
| 32% broken glass | ✅ | No action |
| 22%, d=0.72 aggregate memory | ✅ | No action |
| 12–30% false confession range | ✅ | Add "aggregate across datasets" note in summaries |
| 14–26% (Institutional Negligence) | 🟡 | Standardise to 12–30% or explain DNA-subset distinction |
| Garrett 10.8% below 12% floor | 🟡 | Add undercount explanation wherever 27/250 cited |
| 80–120% compound suggestibility | 🟡 | Add derivation note; 2 author names still missing |
| Autism credibility d=0.65 | ✅ resolved | Author is Lim et al. (2021) — add everywhere |
| Autism 2–18% forensic prevalence | ✅ resolved | Source is Autistica (2024) |
| Haworth et al. (2023) | ✅ | Add to all neurodivergence sections |
| Mourtgos & Adams counter-argument | 🔴 not in thesis | Consider adding and addressing in thesis |
| 42% in two unrelated contexts | 🟢 cosmetic | Rename one for clarity |

---

## YOUR FOUR ORIGINAL RESEARCH CONTRIBUTIONS

| Study | Dataset | Key Stats | How to cite |
|---|---|---|---|
| Study 1: Disfluency in truthful speech | Pérez-Rosas et al. (2015), N=121 | d=0.60, p=0.004 | "Original analysis (this thesis), Study 1" |
| Study 2: Linguistic distancing in false confessions | Rizzelli et al. (2021), N=135 | "you" 7.6×, χ²=3903.7 | "Original analysis (this thesis), Study 2" |
| Study 3: Belief-Reality Inversion Matrix | GDRT (2006) × DePaulo (2003), 23 cues | 91.3%, p<0.0001 | "Original analysis (this thesis), Study 3" |
| Study 4: Algorithmic vs human detection | Pérez-Rosas corpus + Bond & DePaulo | 63.5% vs 54% | "Original analysis (this thesis), Study 4" |
| Study 5: Cultural variation in truthful speech | [Dataset TBC] | H=383.64 hedging | "Original analysis (this thesis), Study 5" |

---

*v3 — incorporates: signal_inversion_effect.txt, constructed_guilt_statistical_appendix.txt, risk_interrogation.txt, tables.txt, cultural_analysis.txt*
