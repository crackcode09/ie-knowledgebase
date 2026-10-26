# Spreadsheet Recipes (Excel / Google Sheets)

Data in A2:A101.

| Task | Formula |
|---|---|
| Mean / median / mode | `=AVERAGE(A2:A101)` · `=MEDIAN(A2:A101)` · `=MODE.SNGL(A2:A101)` |
| Trimmed mean (10% total) | `=TRIMMEAN(A2:A101, 0.2)` (the argument is the *total* fraction trimmed) |
| Range | `=MAX(A2:A101)-MIN(A2:A101)` |
| Standard deviation / variance | `=STDEV.S(A2:A101)` · `=VAR.S(A2:A101)` |
| Quartiles, IQR | `=QUARTILE.INC(A2:A101,1)`, `=QUARTILE.INC(A2:A101,3)`, difference |
| CV | `=STDEV.S(A2:A101)/AVERAGE(A2:A101)` |
| z-score | `=(x-AVERAGE(A2:A101))/STDEV.S(A2:A101)` |
| P(below x), normal | `=NORM.DIST(x, mean, sd, TRUE)` |
| Histogram counts | `=FREQUENCY(A2:A101, bin_upper_edges)` or Insert → Chart → Histogram |
| Pareto | Pivot table (category, sum/count) → sort descending → cumulative % column → combo chart (bars + line on secondary axis). Excel also has Insert → Chart → Pareto. |
| DPMO | `=defects/(units*opportunities)*1000000` |

Quartile conventions differ between software (`QUARTILE.INC` vs `.EXC`, Python, Minitab); small differences in Q1/Q3 are expected.
