# About As Good As A Coin Toss: Reproducible Analyses

**Companion repository for:** Ross, G.M. (2026). *About As Good As A Coin Toss: Credibility Under Scrutiny.* Omxus Research, Perth WA.

## Abstract

Courts, police, and juries assess witness credibility using behavioural cues — gaze aversion, fidgeting, speech hesitation — that are empirically inverted. The cues believed to indicate deception actually indicate truthfulness, and vice versa. This repository contains 10 reproducible studies proving this signal inversion operates at every level: individual testimony, confession analysis, cross-cultural communication, neurodivergent presentation, and environmental determination of behaviour itself.

## Results Summary

| Study | N | Method | Key Finding | Effect Size | p |
|-------|---|--------|-------------|-------------|---|
| 1. Trial Testimony | 121 | Mann-Whitney U, logistic regression | Disfluency indicates **truthfulness**, not deception | d = 0.60 | .004 |
| 2. Confession Linguistics | 135 | Chi-square word frequency | False confessors use "you" 7.59x more — narrative was fed | Ratio 7.59x | < .001 |
| 3. Belief-Reality Inversion | 23 cues (N=11,227 + 158 studies) | Binomial sign test, Spearman | 74% of believed deception cues are empirically wrong | WII = +0.506 | .017 |
| 4. Human vs Algorithmic | k=206, N=24,483 | Meta-analysis + CV | Humans 54% (chance), algorithms 63.5-83% | h = 0.08 | < .05 |
| 5. Four Pillars | 250 DNA exonerations + meta | Binomial, convergent validity | All 4 pillars reject null independently | d = 0.72–1.0 | < 10⁻³⁰ |
| 6. ASD Compounding | 1,410 observers, 100k MC | Monte Carlo simulation | Autistic truth-tellers trigger 4.5x more inverted cues | d = 3.18 | < .001 |
| 7. Cross-Cultural | 4 cultures | Kruskal-Wallis H | Truthful speech varies by culture; monocultural detectors fail | H = 95.83 | < .001 |
| 8. Language & Birthplace | 1,811,487,320 | Chi-square, Cohen's h | Language is 100% environmentally determined | h = 0.93 | < .001 |
| 9. Environmental Outcomes | ~390,000 (Census) | OLS regression | Language outpredicts ancestry for life outcomes | ΔR² sig. | < .001 |
| 10. Distillation Framework | Theoretical | Mathematical proof | Behaviour is distilled from environment, not rationally chosen | — | — |

## Quick Start

```bash
git clone https://github.com/[tbd]/omxus-credibility-research.git
cd omxus-credibility-research
./run_all.sh
```

Each study is self-contained. To run individually:

```bash
cd study_01_trial_testimony
./run.sh
```

## Studies

### Signal Inversion (Studies 1-3)
**Studies 1-3** establish that the cues courts use to assess credibility are empirically inverted. Disfluency marks truth (Study 1). False confessions have distinctive linguistic signatures that courts miss (Study 2). Of 23 commonly believed deception cues, 74% are wrong (Study 3).

### System-Level Failure (Studies 4-5)
**Study 4** shows humans achieve 54% accuracy at deception detection — barely above a coin toss — while algorithms using linguistic features (invisible to human perception) reach 63.5-83%. **Study 5** demonstrates convergent validity across four independent evidence pillars.

### Demographic Compounding (Studies 6-7)
**Study 6** proves autistic individuals trigger multiple inverted heuristics simultaneously (compound penalty d = 3.18). **Study 7** shows truthful speech patterns vary significantly across cultures, meaning any monocultural detection framework systematically misidentifies minority speakers.

### Environmental Determination (Studies 8-9)
**Study 8** proves language — the most complex human behaviour — is 100% environmentally determined (N = 1.8B, Cohen's h = 0.93). **Study 9** shows that within the same ancestry group, environmental factors (language) predict educational outcomes independently of genetics.

### Theoretical Framework (Study 10)
**Study 10** provides the mathematical framework: behaviour propagates through a process structurally identical to knowledge distillation in neural networks. The implications for the rational actor model in criminology are direct.

## Papers

- `paper/Credibility_Under_Scrutiny.pdf` — Main paper (Ross, 2026)
- `paper/Neurobiological_Safety_Signals.pdf` — Companion paper on system design alternatives

## Related Work

Ross, G.M. (2025). *The Zookeeper.* [Book]

## Citation

```bibtex
@article{ross2026cointoss,
  author  = {Ross, G. M.},
  title   = {About As Good As A Coin Toss: Credibility Assessment and the Inversion of Behavioural Evidence},
  year    = {2026},
  journal = {Preprint},
  address = {Perth, WA},
  note    = {Omxus Research}
}
```

## License

This work is licensed under [CC-BY-4.0](LICENSE). You are free to share and adapt this material for any purpose, provided you give appropriate credit.

## Requirements

Python 3.10+ with numpy, scipy, matplotlib, pandas. See `requirements.txt` for exact versions. Each study creates its own virtual environment when run via `./run.sh`.
