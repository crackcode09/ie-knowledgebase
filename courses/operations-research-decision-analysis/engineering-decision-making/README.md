# Engineering Decision Making & Risk Management

Learn to make better engineering decisions under time, budget and uncertainty constraints. It covers framing, multicriteria and group decisions, uncertainty and risk attitude, game theory, decision processes and search, the value of information, risk management with warning systems, and learning from failures. It follows the topic outline of a three-day course: every outline item appears as a section heading, in the same order.

**Length:** about 3 days (21 contact hours), or self-paced.  
**Prerequisites:** comfort with logical reasoning, probability and basic optimization. No advanced mathematics.

## What you will be able to do

- Identify and organize decision objectives to frame decisions and uncover more alternatives.
- Evaluate and select alternatives in multi-objective decisions with uncertainty.
- Apply group decision-making and game theory techniques to multi-person decisions.
- Choose a decision-making process suited to the context.
- Assess the value of information, and when gathering more is worthwhile.
- Describe risk management processes and mitigation options.
- Identify decision-making failures and learn from them.

## Running case

**Corran Motion Systems** (fictional) must choose the drive technology for a new product:

- belt drive, ball screw, linear motor, or rack and pinion
- decide whether to buy a market study first
- price against a rival
- search for a supplier
- set alarm thresholds for field failures

The ball screw emerges as the robust choice:

- best by MAUT
- the Condorcet winner in the council vote
- first-order dominant over two alternatives
- preferred at any realistic risk tolerance

The market study is worth $1.4 M against a $0.2 M cost. All data is simulated with a fixed seed.

## Modules

| # | Module (outline section) | Outline items |
|---|---|---|
| 01 | [Decision-making fundamentals](modules/01-decision-making-fundamentals.md) | Contexts for decision making; Fundamental and means objectives; Measurement scales (nominal, ordinal, interval, and ratio) |
| 02 | [Multicriteria decision making](modules/02-multicriteria-decision-making.md) | Analytic Hierarchy Process; Multiattribute utility theory; Swing weighting; Group decision making; Borda count; Kemeny-Young method; Majority judgement |
| 03 | [Uncertainty](modules/03-uncertainty.md) | Aleatory and epistemic uncertainty; Assessing subjective probabilities |
| 04 | [Decision making under uncertainty](modules/04-decision-making-under-uncertainty.md) | Stochastic dominance; Decision trees; Modeling risk aversion; Expected utility |
| 05 | [Sequential decision making — Game theory](modules/05-game-theory.md) | Two-player zero-sum games; Mixed strategies for a zero-sum game; Mixed motive games |
| 06 | [Decision-making processes](modules/06-decision-making-processes.md) | The incremental decision-making process; The contingency decision-making framework; Search; The secretary problem |
| 07 | [Value of information](modules/07-value-of-information.md) | Expected value of perfect information; Expected value of imperfect information |
| 08 | [Risk management](modules/08-risk-management.md) | Risk treatment strategies; Potential problem analysis; Precursors, warnings; Receiver operating characteristic (ROC) curves; Risk communication |
| 09 | [Learning from failures](modules/09-learning-from-failures.md) | Types of failures; Transforming failure information into knowledge; Sensitivity analysis |
| 10 | [Capstone](modules/10-capstone.md) | Integrated decision memo; skill check |

The source outline has two apparent typos:

- "SGroup decision making" is used here as "Group decision making".
- One line reads "Transforming failure information into knowledge sensitivity analysis". It is treated as two topics.

Both are noted in the modules.

**Suggested schedule:**

- Day 1: modules 01–03
- Day 2: modules 04–07
- Day 3: modules 08–10

## Related courses

- [Fundamentals of Hypothesis Testing](../../lean-six-sigma/fundamentals-of-hypothesis-testing/README.md) and [Applied Statistics](../../technical-skills/applied-statistics/README.md): probability and statistics background
- [Financial Management for Engineers](../../technical-skills/financial-management-for-engineers/README.md): NPV, sensitivity and Monte Carlo
- [Reliability Engineering Excellence](../../technical-skills/reliability-engineering-excellence/README.md): failure data and FMECA
- [Root Cause Analysis & Problem Solving](../../lean-six-sigma/root-cause-analysis/README.md): learning from failures

## Getting started

```bash
pip install -r requirements.txt
python tools/edmkit.py all          # every worked example
python tools/edmkit.py data         # regenerate data/*.csv
python tools/make_figures.py        # regenerate figures/
```

## Folder map

```
modules/     lessons (outline items as section headings)
tools/       edmkit.py (AHP, MAUT, voting, elicitation, calibration, dominance, trees, utility, games, search, VOI, ROC, sensitivity), make_figures.py
data/        alternatives, panel rankings and grades, calibration record, vibration data
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   formulas, glossary, further reading
templates/   objectives hierarchy, decision matrix, potential problem analysis, decision journal
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
