# Constructed Guilt: How Systems Designed to Detect Deception Systematically Construct It

**Alex Applebee & L. N. Combe** | OMXUS Research, 2026

---

## Abstract

This thesis examines the mechanisms through which guilt is produced -- not discovered -- by the criminal justice system. Drawing on semiotics, philosophy of language, critical legal theory, cognitive psychology, and empirical criminology, the analysis proceeds across seven institutional sites: pre-interrogation detention, police interrogation, legislative language, courtroom proceedings, media framing, jury processes, and the specific position of neurodivergent populations.

### Key Findings

1. **91.3% of deception cues are inverted.** The behaviours that investigators and lay observers interpret as indicators of deception are more strongly associated with truthful communication (21/23 cues inverted, p < 0.0001).

2. **Detection accuracy is at chance.** Bond & DePaulo (2006) meta-analysis: 54.1% accuracy across 24,483 participants and 247 studies.

3. **Memory is altered by questioning.** Post-event linguistic manipulation distorts witness memory in ~22% of cases (d = 0.72, Loftus 30-year programme).

4. **False confessions are routine.** 12--30% of documented exonerations involved false confessions. Pre-interrogation detention elevates suggestibility by 80--120% above baseline.

5. **Neurodivergent people are structurally illegible.** Individuals with autism, FND, PTSD, and CPTSD present authentically in ways that systematically trigger credibility-reducing inferences under instruments calibrated to neurotypical baselines.

6. **The system produces these outcomes through ordinary operation.** The architecture serves institutional interests in conviction rates. The presumption of innocence operates as doctrine, not as practice.

**The system doesn't fail sometimes. It's structurally inverted.**

---

## Quick Start

Run the reproducible analysis:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the full analysis pipeline
./run.sh

# Or step by step:
python src/run_analysis.py
```

Results are written to `results/`.

---

## Project Structure

```
.
├── CONSTRUCTED_GUILT_FULL_THESIS.md   # Full 9-chapter thesis (~25,000 words)
├── CONSTRUCTED_GUILT_UNIFIED.md       # Unified compilation
├── Executive Summary.pdf              # PDF executive summary
├── cover.jpg                          # Thesis cover image
│
├── manuscript/                        # Primary manuscript files
│   ├── EXECUTIVE_SUMMARY.md           # Start here (150 lines)
│   ├── CONSTRUCTED_GUILT_FULL_THESIS.md
│   ├── COMPLETE_THESIS_WITH_FIGURES.md
│   ├── CREDIBILITY_ASSESSMENT_THESIS_FINAL.md
│   ├── 11_signal_inversion.md         # Signal Inversion Effect standalone paper
│   ├── 15_they_dont_believe_you.md    # "They Don't Believe You" standalone
│   ├── SENTENCING.md                  # Thought experiment: the system judged by its own tools
│   └── ...supplements and chapter files
│
├── data/                              # Raw and processed data
│   ├── raw/                           # Source datasets
│   │   ├── cue_mapping.csv            # Belief-reality cue mapping
│   │   ├── depaulo_2003_effect_sizes.csv
│   │   └── gdrt_2006_beliefs.csv
│   └── thesis_research/               # Background studies and analysis design
│
├── src/                               # Analysis code
│   ├── run_analysis.py                # Main analysis runner
│   ├── belief_reality_analysis.py     # Belief-reality inversion matrix
│   ├── crop_all_images.py             # Image processing
│   └── CROP_AND_COMPILE.py            # Compilation utility
│
├── figures/                           # 16 statistical and neuroimaging figures (PNG)
├── results/                           # Analysis output
│   ├── tables/                        # Inversion matrix, signal inversion tables
│   └── full_statistical_output.txt
│
├── references/                        # Bibliography and source materials
│   ├── MASTER_STATS_REFERENCE_v3.md   # Full statistics audit with confidence flags
│   ├── bibliography.md
│   └── *.pdf                          # Reference papers
│
├── compiled/                          # LaTeX compilation and PDF outputs
│   ├── latex/                         # LaTeX build system
│   └── *.pdf                          # Compiled papers
│
├── justice_compiled/                  # Full compiled thesis book (PDF + source docs)
├── master_thesis/                     # Thesis template structure
├── long_form_md/                      # Extended markdown versions
├── constructed_guilt_original_thesis_latex/  # Original LaTeX source
├── overleaf/                          # Overleaf-compatible LaTeX
│
├── 0-Config/                          # LaTeX configuration (memoir, biblatex, cover)
├── 1-FrontMatter/                     # Abstract, acknowledgements, dedication
├── 2-MainMatter/                      # Chapter LaTeX files
├── 3-BackMatter/                      # Appendices
├── 4-Bibliography/                    # BibTeX references
│
├── THESIS_FULL_CONTENT/               # Complete chapter content
├── paste-cache/                       # Working cache (intermediate text fragments)
├── 99_archive/                        # Archived earlier versions
├── tools/                             # Build utilities
│
├── *.mdx                             # Standalone chapter/essay files
├── requirements.txt                   # Python dependencies
└── run.sh                            # One-command analysis runner
```

---

## Epistemic Notes

- The **91.3% inversion** finding proves beliefs about deception cues are backwards. It does NOT prove we can detect truth.
- The **23% false accusation rate** is derived from 54.1% accuracy assuming 50/50 base rates. It is not independently measured. Always mark as derived.
- **Bond & DePaulo (2006)** = detection accuracy. **DePaulo et al. (2003)** = deception cues. Different papers, different purposes.

## Integrated Studies

This thesis synthesises five original studies:

| Study | Key Finding |
|-------|-------------|
| Disfluency in Truthful Speech | d = 0.60 |
| Linguistic Distancing in False Confessions | "you" pronoun at 7.6x rate |
| 91.3% Belief-Reality Inversion | 21/23 cues inverted, p < 0.0001 |
| Algorithmic vs. Human Detection | Machines look at different features |
| Cross-Cultural Variation | Wrong cues are culturally contaminated; right ones are stable |

---

## Citation

```
Applebee, A. & Combe, L. N. (2026). Constructed Guilt: How Systems Designed
to Detect Deception Systematically Construct It. OMXUS Research.
```

---

## License

This work is shared for research and public interest purposes. Please cite appropriately.
