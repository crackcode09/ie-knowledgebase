# Glossary

- **ANOVA:** analysis of variance. It tests whether the means of several groups differ.
- **Baseline model:** the simplest reasonable prediction (overall mean, majority class). Every model is compared against it.
- **Bootstrap:** resampling the data with replacement to estimate how much a statistic would vary.
- **Cross-validation:** repeatedly training on part of the data and testing on the rest.
- **Data dictionary:** documentation of each field: its meaning, unit, type and allowed range.
- **Effect size (η²):** the share of total variation explained by a factor.
- **Fan-out:** row duplication caused by joining to a table with many matching rows.
- **Feature engineering:** creating informative inputs from raw data, such as trends and ratios.
- **Grain:** what one row of a table represents.
- **Kruskal-Wallis / Mann-Whitney:** rank-based tests comparing three or more groups / two groups.
- **Leakage:** using information during training that would not be available at prediction time.
- **Noise floor:** the best accuracy any model can reach, given how precisely the outcome is measured.
- **Overfitting:** fitting noise, so the model performs worse on new data.
- **Primary / foreign key:** the unique row identifier / a reference to another table's key.
- **Spearman correlation:** rank-based correlation that measures monotonic association.
- **Threshold:** the probability cut-off that turns a model score into an action.
- **Tukey HSD:** pairwise comparisons after ANOVA that control the family-wise error rate.
- **VIF:** variance inflation factor. It measures multicollinearity among predictors.
