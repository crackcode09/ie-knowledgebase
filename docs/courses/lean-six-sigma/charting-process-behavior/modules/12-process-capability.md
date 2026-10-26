# Module 12 — Process Capability

**Time:** 60 min · **Data:** `data/shaft_diameter.csv`

## Learning objectives

1. Compute Cp, Cpk, Pp and Ppk and explain what each one measures.
2. State the preconditions for a meaningful capability study.
3. Translate a capability index into expected nonconforming parts — and know when not to.

## 1. Preconditions

A capability index predicts what the process **will** do. That prediction only makes sense if the process is **predictable**. So:

1. Measurement system is adequate (Module 1).
2. Process behavior chart shows no signals over the study period (Modules 6–8).
3. Enough data — at least ~25 subgroups or ~50 individuals for a reasonably stable estimate; with 20 points, treat the result as preliminary.
4. Distribution shape is known well enough if you will quote ppm (Module 13).

**No stable chart → no capability index.** For an unpredictable process, Pp/Ppk describe the past only.

## 2. The indices

| Index | Formula | Sigma used | Answers |
|---|---|---|---|
| **Cp** | (USL − LSL) / 6σ_within | Within | Could the process fit in the tolerance if perfectly centered? |
| **Cpk** | min(USL − μ, μ − LSL) / 3σ_within | Within | Does it fit, given where it's actually centered? |
| **Pp** | (USL − LSL) / 6σ_overall | Overall s | Same as Cp, long-term |
| **Ppk** | min(USL − μ, μ − LSL) / 3σ_overall | Overall s | Same as Cpk, long-term |

- Cpk ≤ Cp always; the gap is lost to off-centering.
- Pp ≈ Cp when the process is stable; Pp much lower than Cp means the process shifted/drifted during the study.
- One-sided spec: use only the side that exists (e.g., Cpu = (USL − μ)/3σ).

### Typical targets

Common customer requirements (e.g., automotive PPAP practice) are Cpk ≥ 1.33 for ongoing processes and ≥ 1.67 for new or critical characteristics. Your customer's requirement governs.

| Cpk (normal, centered on the closer side) | Expected out-of-spec on that side |
|---|---|
| 1.00 | ≈ 1,350 ppm |
| 1.33 | ≈ 33 ppm |
| 1.50 | ≈ 3.4 ppm |
| 2.00 | ≈ 0.001 ppm |

(One-tail normal probabilities beyond 3·Cpk sigma, computed with `scipy.stats.norm`. These numbers assume normal tails — see Module 13.)

## 3. Worked example — shaft diameter

Spec 12.70 ± 0.04 (LSL 12.66, USL 12.74). Baseline hours 1–20 (stable per Module 6).

```bash
python tools/spc.py capability data/shaft_diameter.csv value 12.66 12.74 --first 20
```

| Statistic | Value |
|---|---|
| Mean | 12.6992 |
| σ_within (mR̄ / 1.128) | 0.00570 |
| σ_overall (s) | 0.00593 |
| Cp = 0.08 / (6 × 0.00570) | **2.34** |
| Cpk = (12.6992 − 12.66) / (3 × 0.00570) | **2.30** |
| Pp | 2.25 |
| Ppk | 2.21 |

**Interpretation:** a highly capable, well-centered process; Pp ≈ Cp confirms stability.

**After the shift (hours 21–30):** mean ≈ 12.7165. With the same within sigma, Cpk = (12.74 − 12.7165) / (3 × 0.00570) ≈ **1.38**. Still above 1.33 — but the special cause took away 40% of the capability margin. And since hours 21–30 are not stable, this number is a description, not a prediction.

## 4. Common mistakes

- Computing Cpk from an unstable process (the number changes every time you look).
- Using overall s and calling it Cpk.
- Quoting ppm from Cpk on clearly skewed data.
- Using capability on a sorted/inspected population (the tails were cut off).
- Comparing Cpk across suppliers who compute sigma differently. Ask how it was calculated.

## Exercise 12.1

Spec for fill weight (`data/fill_weight.csv`) is 495–505 g. Compute Cpk for the combined data (using the combined mR̄), then for head A and head B separately. Which number is meaningful?

## Check yourself

1. Cp = 1.8, Cpk = 0.9. What's the problem and the fix?
2. Cp = 1.5, Pp = 0.9. What does this tell you?

<details><summary>Answers</summary>

1. Process is capable in spread but badly off-center. Recenter.
2. The process is not stable over the study period — long-term variation is much larger than short-term. Find the special causes first.
</details>
