# Study 2: Linguistic Distancing in True vs False Confessions

## What This Proves
Innocent people who falsely confess use dramatically different language than guilty people who truly confess. False confessors orient toward the interrogator ("you said", "you told me" — 7.59x higher) and use impersonal distancing ("that's what happened" — 11.67x higher) because the narrative was fed to them, not self-generated.

## Dataset
- Source: Rizzelli, Kassin & Gales (2021), Appendix A raw word counts
- Published in: The Wrongful Conviction Law Review, 2(3), 205-225
- N = 135 confessions (37 proven false via DNA/Innocence Project, 98 presumed true from FBI files)
- Location: data/rizzelli_appendix_a.csv

## Method
- Per-confession word frequency rates
- Chi-square tests for each word
- Category analysis (impersonal pronouns, personal pronouns, conjunctions)

## Key Results
| Word | True (per conf.) | False (per conf.) | Ratio | chi2 | p |
|------|-----------------|-------------------|-------|-----|---|
| 'you' | 9.4 | 71.3 | 7.59x | 3903.7 | <.001 |
| 'that's' | 1.7 | 19.3 | 11.67x | 1288.6 | <.001 |
| 'it's' | 1.2 | 14.6 | 12.17x | 993.1 | <.001 |
| Impersonal total | 49.0 | 253.6 | 5.18x | 10701.9 | <.001 |

## How to Run
./run.sh

## Citation
Rizzelli, L., Kassin, S., & Gales, T. (2021). The language of criminal confessions: A corpus analysis. Wrongful Conviction Law Review, 2(3), 205-225.
