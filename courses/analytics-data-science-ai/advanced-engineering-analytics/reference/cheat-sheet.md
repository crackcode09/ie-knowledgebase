# Cheat Sheet

## pandas: merging and preparing

```python
df.drop_duplicates()
df["line"] = df["line"].str.strip().str.upper()
lab_run = lab.groupby("run_id").value.agg(mean="mean", min="min", n="count").reset_index()
t = runs.merge(lab_run, on="run_id", how="left", validate="one_to_one")
t = t.merge(lines, on="line", how="left", validate="many_to_one")
pd.read_excel("file.xlsx", sheet_name="runs")
df["trend"] = df.groupby("line")["x"].transform(lambda s: s - s.rolling(14, min_periods=3).mean().shift(1))
```

## statsmodels and SciPy

```python
smf.ols("y ~ C(line) * C(supplier)", data=t).fit()      # two-way ANOVA via anova_lm
pairwise_tukeyhsd(t.y, t.line)
smf.ols("y ~ x + I(x**2) + C(line)", data=t).fit()
stats.kruskal(*groups); stats.mannwhitneyu(a, b); stats.spearmanr(x, y)
```

## scikit-learn: honest accuracy

```python
cross_val_score(model, X, y, cv=KFold(5, shuffle=True, random_state=0), scoring="neg_mean_squared_error")
cross_val_score(clf, X, y, cv=StratifiedKFold(5, shuffle=True), scoring="roc_auc")
```

## Choosing a method

| Question | Data | Method |
|---|---|---|
| Do group means differ? | continuous, roughly normal | ANOVA + Tukey |
| Do groups differ? | skewed or ordinal | Kruskal-Wallis / Mann-Whitney |
| How does y depend on x's? | continuous y | multiple regression |
| Association | monotonic, any shape | Spearman |
| Uncertainty of a median or ratio | any | bootstrap |
| What causes y? | factors you can set | designed experiment |
| Predict y for new cases | any | cross-validated model compared with a baseline |

## Accuracy measures

- **RMSE** = √mean((y − ŷ)²)
- **AUC**: 0.5 = random guessing, 1 = perfect
- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN)
- **η²** = SS_factor / SS_total

## Join validation checklist

1. State the grain of each table.
2. Check that keys are unique where they should be.
3. Aggregate the many-side first.
4. Compare row counts and totals before and after the join.
5. Count unmatched rows.
