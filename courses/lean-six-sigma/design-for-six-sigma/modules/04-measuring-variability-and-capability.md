# Module 4 — Measuring Process Variability and Capability in Design

**Time:** 3 h · **Phase:** Design

## Learning objectives

1. Express design performance as Cp, Cpk, DPMO and Z.
2. Explain the "sigma level" convention and its 1.5σ shift.
3. Use capability predictions to set tolerances and choose processes.

## 1. Capability indices (recap)

| Index | Formula | Meaning |
|---|---|---|
| Cp | (USL − LSL) / 6σ | Potential: does the spread fit the tolerance? |
| Cpk | min(USL − μ, μ − LSL) / 3σ | Actual: does it fit where it's centered? |
| DPMO | P(out of spec) × 10⁶ | Expected defects per million opportunities |
| Z_bench | Normal quantile of total P(out) | Single "distance to failure" in σ units |

Full treatment of capability on production data: *Charting Process Behavior*, Module 12. In design, you use the same indices **predictively** — from supplier process data, similar parts, or simulation — before the process exists.

## 2. Worked example — a bore for the carriage housing

Spec 20.000 ± 0.015 mm. The candidate machining process (from a similar part's data) has σ = 0.004 mm and tends to run 0.004 mm large.

| | μ = 20.004 | μ = 20.000 (recentered) |
|---|---|---|
| Cp | 1.25 | 1.25 |
| Cpk | **0.92** | **1.25** |
| DPMO | **2,981** | **177** |
| Z_bench | 2.75 | 3.57 |
| "Sigma level" (Z_bench + 1.5) | 4.25 | 5.07 |

Upper side when off-center: z = (20.015 − 20.004)/0.004 = 2.75 → 2,979 ppm; lower side z = 4.75 → ~1 ppm.

```bash
python tools/dfss.py capability
```

**Design decisions this supports:** recenter (offset the process), tighten the process (σ), or — if function allows — widen the tolerance. A design team that knows its process σ can set tolerances that are both functional and producible.

## 3. The 1.5σ shift convention

Six Sigma practice, originating at Motorola in the 1980s, reports a **sigma level** = Z (short-term) assuming the mean will drift up to 1.5σ over the long term. "Six sigma" = 3.4 DPMO is the one-sided tail beyond 4.5σ, not 6σ.

| Sigma level | DPMO (with 1.5σ shift) |
|---|---|
| 3 | 66,807 |
| 4 | 6,210 |
| 5 | 233 |
| 6 | 3.4 |

The 1.5σ figure is an empirical convention, not a law, and has been widely criticized (e.g., by Wheeler). Use it only to talk with people who use it; for engineering decisions use Cpk/DPMO computed from your actual data, and keep the process stable so the mean doesn't drift.

## Check yourself

1. Cp = 2.0, Cpk = 0.8. What's the design/process action?
2. Why is "sigma level 6" not the same as Z = 6?

<details><summary>Answers</summary>

1. Recenter — the spread is fine, the location isn't.
2. The convention subtracts a 1.5σ assumed long-term shift: sigma level 6 corresponds to a 4.5σ one-sided tail (3.4 DPMO).
</details>
