# Cheat Sheet

## Decide whether to use AI

1. Problem statement with a number? → if not, stop and write one.
2. Can the work be eliminated or simplified? → do that first.
3. Is a fixed rule enough? → rules-based automation.
4. Is it a repeated decision with labelled history, or a language task a human can check? → consider ML or GenAI.
5. Data ready (labels, quality, access)? → if not, a data or process fix first.
6. Are errors tolerable, or caught? → design human review and thresholds.

## Formulas

| Item | Formula |
|---|---|
| Annual value of an idea | volume × minutes ÷ 60 × % saved × loaded rate + avoidable waste |
| Feasibility (course) | (data readiness + (6 − complexity) + (6 − risk)) ÷ 3 |
| Precision | caught ÷ flagged |
| Recall | caught ÷ all actual positives |
| Net value of alerts | caught × prevented cost − flagged × intervention cost |
| Wilson 95 % interval | (p + z²/2n ± z√(p(1 − p)/n + z²/4n²)) ÷ (1 + z²/n), z = 1.96 |
| NPV | Σ cash flowₜ ÷ (1 + r)ᵗ |

## Data quality dimensions

Completeness · validity · consistency · uniqueness · timeliness · accuracy · **label availability** (for ML) · accessibility.
