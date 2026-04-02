# CONSTRUCTED GUILT — Master Stats Reference v2
### Key Claims · Sources · Flags
*Updated after review of original research files*

---

## HOW TO READ THIS DOCUMENT

Each stat is marked:
- ✅ **Consistent & sourced** — use as-is across all documents
- 🔵 **Original research** — your own analysis; needs method note when cited
- 🟡 **Needs clarification** — correct but presented inconsistently
- 🔴 **Needs fixing** — genuinely wrong or unsupported

---

## PILLAR 1: Deception Detection Failure

---

### Stat: 54.1% overall accuracy (chance = 50%)
**Source:** Bond & DePaulo (2006) — 206 studies, 24,483 judges
**Status:** ✅

Note: This is the *overall* rate combining truth and lie trials.
Within this same meta-analysis, the breakdown is:
- Truth detection: **61%** (people have a truth bias — tend to believe)
- Lie detection: **47%** (below chance — worse than guessing for lies specifically)

**← This explains the "47% figure" flagged in the previous audit.**
It is NOT a contradiction of 54.1%. It is a breakdown component of the same study.
The Nuremberg doc cites 47% without this context — it should read:
*"Lie detection specifically: 47% — below chance (Bond & DePaulo, 2006)"*

---

### Stat: DePaulo et al. (2003) — used elsewhere in documents
**Source:** DePaulo et al. (2003) — 158 cues, 120 samples, N > 10,000
**Status:** ✅ — but it is a DIFFERENT paper from Bond & DePaulo (2006)

These two papers serve different purposes:
- **Bond & DePaulo (2006)** → detection accuracy (how well people detect lies): gives the **54.1%** figure
- **DePaulo et al. (2003)** → which cues actually correlate with deception: gives the **effect sizes per cue**

⚠️ The Institutional Negligence supplement attributes "54.1% accuracy" to "DePaulo et al. (2003), 120+ studies, 2,000+ participants." This is wrong on two counts: wrong paper, wrong N. The 54.1% is from Bond & DePaulo (2006), N = 24,483. Fix this in Institutional Negligence.

---

### Stat: 91.3% of credibility cues are inverted (21/23)
**Source:** 🔵 Original research — inversion_matrix.csv + tables.txt
**Method:** 23 cues matched between GDRT (2006) belief data (N=11,227, 75 countries) and DePaulo et al. (2003) effect sizes. Binomial test p = 0.0000. 95% CI: [75.1%, 100%].
**Status:** 🔵 This is your finding — clearly documented and statistically sound.

Citation should read: *"Original analysis (this thesis): Belief-Reality Inversion Matrix, N=23 matched cues; Global Deception Research Team (2006) × DePaulo et al. (2003)"*

---

### Stat: 78.6% inversion rate (11/14)
**Source:** 🔵 Original research — full_statistical_output.txt, Study 3
**Status:** 🟡

This is from the same analysis but uses a 14-cue subset (Study 3), not all 23 matched cues. Both figures are valid — they represent different sized matched sets. The documents currently use both without explanation, which looks inconsistent.

**Recommendation:** Use **91.3% (21/23)** as the headline throughout. The 78.6% figure can appear in the detailed analysis tables with a note that it's the subset used in Study 3. Do not use both interchangeably as if they're the same claim.

---

### Stat: Disfluency is significantly HIGHER in truthful speech — d = 0.60, p = 0.004
**Source:** 🔵 Original research — Study 1, Pérez-Rosas et al. (2015) Michigan Real-Life Trial Corpus, N=121 (60 truthful, 61 deceptive). Mann-Whitney U test.
**Status:** 🔵 Your finding. Solid stats.

Context: d = 0.60 is 6x the median deception cue effect size (DePaulo et al. 2003 median = 0.10). This is the strongest single cue finding in your study.

Citation should read: *"Original analysis (this thesis), Study 1: Pérez-Rosas et al. (2015) corpus reanalysis, d = 0.60, p = 0.004"*

Note: DePaulo et al. (2003) shows speech hesitations d = 0.05 (no reliable link) — your finding extends this with a finer-grained "disfluency/filler" coding. The difference is real and should be explained briefly when citing.

---

## PILLAR 2: Memory Distortion

---

### Stat: Loftus & Palmer (1974) — "smashed" vs "contacted"
- Speed estimate difference: **16 km/h**
- False memory of broken glass: **32% vs 14% controls**
- Effect size: d = 0.89
**Source:** Loftus & Palmer (1974) — published study
**Status:** ✅ Consistent across all documents

---

### Stat: Aggregate ~22% false memory rate, d = 0.72
**Source:** Loftus (2005) 30-year research review
**Status:** ✅ Consistent across all documents

---

### Other studies in the memory distortion table
Three rows in the table (d=0.72/17%, d=0.61/~25%, d=0.68/~22%) have no author names attached.
**Status:** 🟡 These appear to be from specific Loftus studies. Need to identify:
- The barn study (d=0.72, 17%) — likely Loftus, Miller & Burns (1978)
- The post-event narrative study (d=0.61, ~25%) — likely Loftus (1979)
- The memory substitution study (d=0.68, ~22%) — likely Loftus & Hoffman (1989)

Recommend checking these before publication. Even if the effect sizes are right, unnamed rows weaken the table.

---

## PILLAR 3: False Confessions

---

### The aggregate range: 12–30% of exonerations involve false confessions
**Status:** ✅ — correct as an aggregate, and the thesis explains this properly in the main body

The range comes from combining the datasets below. It is **not a single study's finding** — it is the span across multiple methodologies and jurisdictions. This needs to be stated consistently whenever the range is cited, especially in summary documents.

**Underlying datasets:**

| Study | N | False Confession % | Notes |
|---|---|---|---|
| Kassin & Gudjonsson (2004) | Review | 14–25% | Range across US/UK exoneration studies |
| Leo & Ofshe (2005) | 340 | 15.3% (52 cases) | US exonerations |
| Garrett (2011) — DNA exonerations | 250 | **10.8%** (27 cases) | DNA-confirmed innocent |
| National Registry of Exonerations (2023) | 3,300+ | ~12% | US; juveniles = 42% of these |
| Gudjonsson (2003) — UK custodial | 509 | 11.3% | UK detained suspects |
| Gross et al. (2020) | Registry | ~30% | Cumulative disadvantage analysis |

⚠️ **The Garrett figure (10.8%) falls below the stated floor of 12%.** The thesis handles this correctly in the main body — DNA exoneration databases undercount because only a fraction of wrongful convictions are ever overturned. This explanation must travel with the 27/250 citation every time it's used. Without it, it looks like the flagship example contradicts the range.

---

### Stat: 14–26% used in Institutional Negligence supplement
**Status:** 🟡

This narrower range comes from DNA-specific exoneration data (Kassin & Gudjonsson, 2004 + Innocence Project). It's not wrong — it's a subset. But it conflicts with "12–30%" used everywhere else. Pick one range for all documents, or note explicitly that 14–26% is the DNA-confirmed subset.

---

### Stat: ~23% false confession rate among those subjected to Reid Technique
**Status:** 🔴 Still no source found in any of the uploaded research files.

This appears twice in the main documents ("approximately 23%") stated as fact, with no citation. It does not match any figure in the false confession tables. This needs either:
1. A source citation
2. To be explicitly marked as original analysis with the calculation shown
3. To be removed

---

### Stat: False confessions — linguistic distancing markers
**Source:** 🔵 Original research — Study 2, reanalysis of Rizzelli et al. (2021) confession corpus
- "you" appears 7.6x more in false confessions (χ² = 3903.7, p < .001)
- "that's" appears 11.7x more
- "it's" appears 12.2x more
**Status:** 🔵 Strong finding, clearly documented.

Citation should read: *"Original analysis (this thesis), Study 2: reanalysis of Rizzelli et al. (2021) corpus (N=135; 37 false, 98 true confessions)"*

---

## PILLAR 4: Suggestibility & Pre-Interrogation

---

### Compound figure: +80–120% elevation in suggestibility
**Status:** 🟡 — correct, but needs a derivation note in every document that uses it

This is a calculated compound, not a single study finding. The components:

| Condition | Increase | Source |
|---|---|---|
| Anxiety induction | +38% | Gudjonsson & Clark (1986) |
| Sleep deprivation | +56% | Harrison et al. (2014) |
| Extended detention | +29–44% | ⚠️ Author missing — year 2010 only |
| Custody vs neutral | Yield +31%, Shift +42% | ⚠️ Author missing |
| **Compound** | **+80–120%** | Derived |

The two missing author names need to be found. The compound figure itself is defensible — the thesis explains the derivation well in the main body. The issue is that the Executive Summary and Institutional Negligence cite it as if it's a single study's result.

**Recommended standard phrasing:** *"Cumulative pre-interrogation conditions (anxiety, sleep deprivation, extended detention, custody) produce a compound elevation in suggestibility of 80–120% above baseline (Gudjonsson & Clark, 1986; Harrison et al., 2014; [2010 source]; derived)"*

---

## PILLAR 5: Neurodivergence & Credibility

---

### Stat: Autistic speakers rated significantly more deceptive, N=1,410, d=0.65
**Status:** 🟡 — Year is 2021 but author name is missing across most documents

This is likely Hilviu & Roeyers (2021) or possibly Crompton et al. (2021) — needs to be confirmed and properly cited.

---

### Stat: Autism prevalence 1–2% general population vs 2–18% forensic
**Status:** 🟡 — No citation, very wide range (2–18%)

The wide range suggests this is an aggregate across multiple studies rather than a single finding. Needs sourcing. If it's drawn from multiple studies, list the key ones or cite a review.

---

### Stat: 37% of UK police received autism training
**Source:** Autistica (2024) survey, N=394 police officers
**Status:** ✅ — Source named, just needs proper reference format

---

## SUMMARY FLAGS TABLE

| Stat | Status | Action |
|---|---|---|
| 47% lie detection rate | ✅ Correct — breakdown of 54.1% | Add context "lie detection specifically" where cited |
| 54.1% overall accuracy | ✅ Consistent | Fix Institutional Negligence attribution (wrong paper cited) |
| 91.3% inversion rate | 🔵 Original research | Add method note; use as headline, not 78.6% |
| 78.6% inversion rate | 🔵 Original research (14-cue subset) | Only in detailed tables, not headline |
| Disfluency d=0.60 | 🔵 Original research | Mark as original; explain vs DePaulo d=0.05 |
| Linguistic distancing in false confessions | 🔵 Original research | Mark as original; cite Rizzelli corpus |
| 32% broken glass (Loftus & Palmer) | ✅ Consistent | No action needed |
| 22%, d=0.72 aggregate memory | ✅ Consistent | No action needed |
| 3 unnamed studies in memory table | 🟡 | Identify authors (likely Loftus 1978, 1979, 1989) |
| 12–30% false confession range | ✅ Correct as aggregate | Add "aggregate across datasets" note in summaries |
| 14–26% (Institutional Negligence) | 🟡 Narrower subset | Standardise to 12–30% or explain subset |
| 27/250 Garrett below 12% floor | 🟡 | Add undercount explanation wherever cited |
| ~23% Reid false confession rate | 🔴 No source found | Cite, show calculation, or remove |
| 80–120% compound suggestibility | 🟡 Derivation missing in summaries | Add derivation note; find 2 missing author names |
| Autism credibility study d=0.65 | 🟡 Author missing | Find: likely Hilviu & Roeyers (2021) |
| Autism 2–18% forensic prevalence | 🟡 No citation | Source or list contributing studies |
| 42% appears in two unrelated contexts | 🟢 Cosmetic | Rename one instance for clarity |

---

## WHAT'S ORIGINAL RESEARCH (YOUR WORK)

| Finding | Dataset Used | Key Stats |
|---|---|---|
| Disfluency higher in truthful speech | Pérez-Rosas et al. (2015) Michigan Trial Corpus, N=121 | d=0.60, p=0.004 |
| Linguistic distancing in false confessions | Rizzelli et al. (2021) corpus, N=135 | "you" 7.6x, χ²=3903.7 |
| Belief-Reality Inversion Matrix (91.3%) | GDRT (2006) × DePaulo et al. (2003), 23 cues | p<0.0001, CI [75.1%, 100%] |
| Algorithmic detection outperforms humans | Pérez-Rosas corpus + Bond & DePaulo | 63.5% vs 54% human |

These four are the novel contributions of the thesis. They need to be consistently described as original analyses, with the dataset and method named, every time they're cited across the documents.

---

*v2 — updated after review of: belief_reality_analysis.py, inversion_matrix.csv, depaulo_2003_effect_sizes.csv, cue_mapping.csv, gdrt_2006_beliefs.csv, full_statistical_output.txt, tables.txt, signal_inversion_effect.txt*
