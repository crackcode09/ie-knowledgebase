# Model Evaluation Checklist

Model: ____________  Version: ____  Studies (n): ____  Date: ________

## Data

- [ ] Every study measures the same element boundaries and method
- [ ] Study files checked for keying errors (spot-check at least 10 %, and all flagged points)
- [ ] Exclusions documented with a reason (foreign element, different method, unqualified operator)
- [ ] Ranges of every variable recorded

## Fit

- [ ] Scatter plots of time vs each variable reviewed
- [ ] Every coefficient significant (|t| > ~2) **and** physically sensible in sign and size
- [ ] Intercept makes sense as a constant element
- [ ] Standard error of estimate: ____ min (____ % of a typical job)
- [ ] VIF of every predictor below ~5 (list): ________
- [ ] Leave-one-out RMSE close to the SE (not much larger)

## Residuals

- [ ] No |studentized residual| > 3 left uninvestigated
- [ ] No single study dominates (Cook's distance reviewed)
- [ ] Residuals vs fitted: no curve, no funnel
- [ ] Normal probability plot roughly straight

## Validation

- [ ] Hold-out studies (n = ____) collected after the model was built
- [ ] Per-job mean absolute error ____ %; within target: ____ of ____
- [ ] Aggregate error ____ %
- [ ] Hold-out jobs outside the range flagged
- [ ] Accuracy target agreed with users: ________

## Release

- [ ] Data sheet published with version, ranges, accuracy and use rules
- [ ] Calculator or ERP formula checked against the model on 3 test jobs
- [ ] Owner, audit frequency and review triggers set
