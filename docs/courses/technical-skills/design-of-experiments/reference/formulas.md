# Formula Sheet

## One-way ANOVA (CRD): k treatments, n_i runs each, N total

| Source | SS | df |
|---|---|---|
| Treatments | Σ n_i (ȳ_i − ȳ)² | k − 1 |
| Error | Σ Σ (y_ij − ȳ_i)² | N − k |
| Total | Σ Σ (y_ij − ȳ)² | N − 1 |

F = MS_treatment / MS_error.

Tukey HSD = q(α; k, df_E) × √(MS_E / n).

## Randomized complete block: a treatments, b blocks

- SS_trt = b Σ (ȳ_i· − ȳ)²
- SS_blk = a Σ (ȳ_·j − ȳ)²
- SS_E = SS_T − SS_trt − SS_blk, with df (a − 1)(b − 1)

## Latin square, p × p

Rows, columns and treatments each have p − 1 df. Error has (p − 1)(p − 2) df.

## Two-factor factorial: a × b levels, n replicates

| Source | SS | df |
|---|---|---|
| A | b·n Σ (ȳ_i·· − ȳ)² | a − 1 |
| B | a·n Σ (ȳ_·j· − ȳ)² | b − 1 |
| AB | n Σ Σ (ȳ_ij· − ȳ)² − SS_A − SS_B | (a − 1)(b − 1) |
| Error | Σ Σ Σ (y_ijk − ȳ_ij·)² | ab(n − 1) |
| Total | Σ Σ Σ (y_ijk − ȳ)² | abn − 1 |

## Power for comparing two means using ANOVA error

- δ = Δ / (σ √(2/n))
- power = P(|t′(df_E, δ)| > t(1 − α/2, df_E))

## 2^k factorials (coded ±1)

- Effect = ȳ(+) − ȳ(−). Coefficient = effect / 2.
- Interaction column = product of the factor columns.
- SS_effect = N × effect² / 4.
- Lenth: s₀ = 1.5 · median|e|; PSE = 1.5 · median{|e| : |e| < 2.5 s₀}; ME = t(0.975, m/3) · PSE.
- Curvature: t = (ȳ_center − ȳ_factorial) / (s_c √(1/n_f + 1/n_c)), with n_c − 1 df.

## Fractional factorials

- Generator, for example E = ABCD, gives the defining relation I = ABCDE.
- Alias of an effect = effect × defining word, with squared letters removed.
- Resolution = length of the shortest word in the defining relation.

## Coded and real units

- real = center + coded × (high − low)/2
- coded = (real − center) / ((high − low)/2)
