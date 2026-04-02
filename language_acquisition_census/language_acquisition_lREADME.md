# LaTeX Version of Language Acquisition Study

## Files

- `language_acquisition_study.tex` - Main manuscript file

## How to Compile

### Option 1: Overleaf (Recommended)

1. Go to: https://www.overleaf.com/latex/templates/template-for-gigascience-journal-manuscript-submissions/hwjctgpqtrhs
2. Click "Open as Template"
3. Replace the content with `language_acquisition_study.tex`
4. The template includes the `oup-contemporary.cls` class file

### Option 2: Local Compilation

You'll need the `oup-contemporary.cls` class file. Download it from Overleaf or CTAN.

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt-get install texlive-full

# Compile
pdflatex language_acquisition_study.tex
bibtex language_acquisition_study
pdflatex language_acquisition_study.tex
pdflatex language_acquisition_study.tex
```

### Option 3: Use Standard Article Class

If you don't have the OUP class, I've also created a standalone version using the standard article class:

See `language_acquisition_study_standalone.tex`

## Paper Summary

**Title**: Geographic Birthplace as a Predictor of Primary Language: A Cross-National Observational Study

**Key Findings**:
- N = 1,811,487,320 individuals across 8 countries
- Geographic environment predicts language with 72-97% accuracy
- Mean Cohen's h = 0.93 (above "large" threshold)
- All chi-square tests significant at p < .001

**Supplementary Evidence**:
- International adoption studies: 100% language replacement
- Twin studies: Genetics affects ability, not which language
- Generational studies: Complete shift within 3 generations

## Citation

```bibtex
@article{omxus2026language,
  title={Geographic Birthplace as a Predictor of Primary Language: A Cross-National Observational Study},
  author={{OMXUS Research Initiative}},
  journal={Preprint},
  year={2026}
}
```
