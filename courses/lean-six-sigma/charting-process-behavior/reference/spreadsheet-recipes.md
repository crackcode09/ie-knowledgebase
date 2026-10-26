# Spreadsheet Recipes (Excel / Google Sheets)

Data in column A starting at row 2 (A2:A31). Baseline = rows 2–21.

## XmR chart

| Cell | Formula | Meaning |
|---|---|---|
| B3 | `=ABS(A3-A2)` (fill down) | Moving range |
| E1 | `=AVERAGE(A2:A21)` | X̄ (baseline) |
| E2 | `=AVERAGE(B3:B21)` | mR̄ (baseline) |
| E3 | `=E1+2.66*E2` | UNPL |
| E4 | `=E1-2.66*E2` | LNPL |
| E5 | `=3.268*E2` | URL |
| C2 | `=IF(OR(A2>$E$3,A2<$E$4),"Rule 1","")` (fill down) | Flag |

Chart: line chart of A2:A31, add series for $E$1, $E$3, $E$4 repeated down columns.

## Rule 4 (8 in a row)

In D9: `=IF(OR(COUNTIF(A2:A9,">"&$E$1)=8,COUNTIF(A2:A9,"<"&$E$1)=8),"Rule 4","")` and fill down.

## X̄–R (subgroups across columns B:F)

| Cell | Formula |
|---|---|
| G2 | `=AVERAGE(B2:F2)` |
| H2 | `=MAX(B2:F2)-MIN(B2:F2)` |
| X̿ | `=AVERAGE(G2:G26)` |
| R̄ | `=AVERAGE(H2:H26)` |
| X̄ UCL / LCL | `=X̿ ± 0.577*R̄` (n = 5) |
| R UCL | `=2.114*R̄` |

## p chart

Columns: B = inspected, C = defective.
p̄: `=SUM(C:C)/SUM(B:B)`. Row p: `=C2/B2`. UCL: `=p̄+3*SQRT(p̄*(1-p̄)/B2)`. LCL: `=MAX(0, p̄-3*SQRT(p̄*(1-p̄)/B2))`.

## Capability

σ_within: `=mR̄/1.128` · Cpk: `=MIN(USL-X̄, X̄-LSL)/(3*σ_within)` · Ppk: same with `STDEV.S(A2:A21)`.
