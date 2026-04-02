# Study 10: Consensus, Distillation, and Trust — Mathematical Framework

## What This Proves

Behavioural patterns propagate environmentally through a process structurally identical to **knowledge distillation** in neural networks. A child doesn't learn explicit rules from caregivers — they learn the *distribution over behavioural responses* (including which wrong answers are "almost right"). This is formally equivalent to a student network learning soft probability distributions from a teacher.

This connects Studies 1-9 to a theoretical foundation: if behaviour is distilled from environment (not rationally chosen), then the entire credibility assessment framework — which assumes behavioural cues reflect internal states — is structurally flawed.

## Structure

This is a **mathematical** study, not a computational one. It contains:

1. **LaTeX source** (`src/consensus_distillation_trust.tex`) — Full paper with proofs
2. **Theorem table** (`data/theorems_table.csv`) — All 16 theorems/definitions/propositions
3. **Validation script** (`src/run.py`) — Validates theorem table, computes Bitcoin double-spend probabilities, generates comparison figures

## Key Theorems

| # | Name | Statement | Rigor |
|---|------|-----------|-------|
| 3.1 | Mining Time Distribution | Block times ~ Exp(p/τ₀) | Rigorous |
| 3.2 | Double-Spend Probability | P(z) = I_{4pq}(z, 1/2) | Rigorous |
| 6.1 | Knowledge Distillation | KL-divergence loss formalises behavioural learning | Rigorous |
| 6.2 | Dark Knowledge Transfer | High-T limit reveals uncertainty structure | Rigorous |
| 11.3 | Linear Sybil Cost | C(n) ≥ n·k·c_vouch | Conditional |

## How to Run

```bash
./run.sh
```

This validates the theorem table and generates visualizations. To compile the LaTeX:

```bash
cd src && pdflatex consensus_distillation_trust.tex
```

## Output

- `results/study_10_results.txt` — Framework summary and validation
- `results/tables/study_10_double_spend.csv` — Bitcoin double-spend probability table
- `results/figures/study_10_consensus_mechanisms.png` — Comparison figure
