# Analytics Cheat Sheet

## SQL essentials

```sql
SELECT column, AGG(measure) AS name      -- AGG: SUM, AVG, COUNT, MIN, MAX
FROM fact f
JOIN dim d ON f.key = d.key              -- combine tables on keys
WHERE condition                          -- filter rows before grouping
GROUP BY column                          -- one row per group
HAVING AGG(measure) > x                  -- filter groups
ORDER BY name DESC
LIMIT 10;
```

## Accuracy measures for classification

| Measure | Formula | Question |
|---|---|---|
| Accuracy | (TP + TN) / all | How often is the model right overall? |
| Precision | TP / (TP + FP) | When it says "fail", how often is it right? |
| Recall (sensitivity) | TP / (TP + FN) | What share of real failures does it catch? |
| Specificity | TN / (TN + FP) | What share of healthy cases does it leave alone? |
| F1 | 2PR / (P + R) | Balance of precision and recall |
| AUC | area under the ROC curve | Ranking ability across all thresholds (0.5 = random guessing) |

## Regression

- R² = 1 − SS_residual / SS_total
- Adjusted R² penalizes extra predictors.
- Coefficient: the change in y per unit change in x, with the other predictors held constant.
- Prediction interval ≈ ŷ ± 1.96 × residual SD for large samples.

## Clustering

- Standardize the features and transform skewed ones (for example, with a log).
- Silhouette ranges from −1 to 1; higher means better-separated clusters.
- Profile each cluster and name it in business terms.

## ABC classification

- Sort items by annual usage value (units × cost).
- A: top ~80% of value. B: next ~15%. C: last ~5%.
- The cut-offs are a policy choice.

## Forecast accuracy

- MAPE = mean(|A − F| / A)
- MAE = mean(|A − F|)
- RMSE = √mean((A − F)²)
- Always compare against a naive or seasonal-naive benchmark on a holdout.

## PCA

- Standardize first.
- Eigenvalues give the variance explained; loadings show each original variable's weight.
- Check predictive value; don't assume the first PC matters most for y.

## Linear programming

- Maximize or minimize cᵀx subject to Ax ≤ b and bounds.
- A constraint is binding when it is used to capacity.
- A shadow price is the objective's change per extra unit of a resource, valid within a range.
