# Module 10: Computer Applications

## Objectives

- Generate, randomize and analyze designs in free software (Python).
- Reproduce the same analysis in a spreadsheet for small designs.
- Know what to look for in any commercial DOE package's output.

## 1. Generating a design and a randomized run sheet

```python
import itertools, numpy as np, pandas as pd

# 2^4 full factorial in standard order, plus 4 center points
runs = pd.DataFrame(list(itertools.product([-1, 1], repeat=4)), columns=list("DCBA"))[list("ABCD")]
runs = pd.concat([runs, pd.DataFrame([[0, 0, 0, 0]] * 4, columns=list("ABCD"))], ignore_index=True)
runs["std_order"] = range(1, len(runs) + 1)

rng = np.random.default_rng(2026)          # record the seed in the plan
runs["run_order"] = rng.permutation(len(runs)) + 1
runs.sort_values("run_order").to_csv("run_sheet.csv", index=False)
```

Half fraction, 2^(5−1) with E = ABCD:

```python
runs["E"] = runs.A * runs.B * runs.C * runs.D      # on the 16 factorial rows
```

To convert to real units, use real = center + coded × half-range. For example, melt temperature = 280 + 10 × A.

## 2. ANOVA for any of the designs

```python
import statsmodels.formula.api as smf, statsmodels.api as sm

m = smf.ols("strength ~ C(supplier)", data=crd).fit()                     # CRD
m = smf.ols("force ~ C(agent) + C(mold)", data=rbd).fit()                  # RCBD
m = smf.ols("cycle ~ C(program) + C(machine) + C(day)", data=latin).fit()  # Latin square
m = smf.ols("shrinkage ~ C(melt_temp) * C(hold_pressure)", data=fac).fit() # two-factor
print(sm.stats.anova_lm(m, typ=2))
```

For unbalanced data with Type III SS, use sum-to-zero coding: `C(melt_temp, Sum) * C(hold_pressure, Sum)` with `typ=3`.

Tukey HSD:

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd
print(pairwise_tukeyhsd(crd.strength, crd.supplier))
```

## 3. Effects for a 2^k design

Effects are just differences of means, so no special software is needed:

```python
effect_A = df[df.A == 1].y.mean() - df[df.A == -1].y.mean()
df["BC"] = df.B * df.C
effect_BC = df[df.BC == 1].y.mean() - df[df.BC == -1].y.mean()
```

`tools/doekit.py` has `effects_2k()` (all interactions at once) and `lenth_pse()`.

## 4. Diagnostics: always look at the residuals

```python
import matplotlib.pyplot as plt, scipy.stats as st
r = m.resid
st.probplot(r, plot=plt)                    # normality
plt.figure(); plt.scatter(m.fittedvalues, r)   # constant variance
plt.figure(); plt.plot(run_order, r, "o-")     # independence / drift over time
```

Watch for:

- a funnel shape (consider transforming y, for example with a log);
- a trend with run order (drift, or randomization not followed);
- one wild point (check the run notes before deleting anything).

## 5. Spreadsheet version (small designs)

For a 2^k design, put the ±1 columns and y in a sheet. Then:

- Effect of a column: `=AVERAGEIF(B:B,1,Y:Y)-AVERAGEIF(B:B,-1,Y:Y)`
- Interaction column: `=B2*C2`, filled down
- One-way ANOVA: most spreadsheet programs have an ANOVA tool (single factor and two-factor with replication) in a data-analysis add-in. Two-factor *with replication* requires a balanced layout.

## 6. Reading any DOE package's output

Whatever tool you use, find these items:

1. The **design table** with standard order and run order. Was it randomized?
2. **Effects or coefficients.** Are they in coded or uncoded units?
3. **The ANOVA table:** which SS type, and what was pooled into error?
4. **Alias structure** for fractions.
5. **Residual plots.**
6. **The prediction and its interval** at the chosen settings.

## Check yourself

1. Your software reports a coefficient of 6.53 for A, and a colleague reports an effect of 13.05. Do you disagree?
2. Why save the random seed in the experiment plan?

<details><summary>Answers</summary>

1. No. Coefficient = effect / 2 in coded units.
2. So the run order can be reproduced and audited, and so anyone can check the analysis used the order actually run.

</details>
