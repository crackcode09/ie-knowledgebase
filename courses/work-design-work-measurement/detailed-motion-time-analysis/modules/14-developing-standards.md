# Module 14 — Developing Standards

## Objectives

- Convert an analysis into a standard time with allowances, process times and frequencies.
- Document, validate and maintain motion-based standards.

## From analysis to standard

```
Normal time  = Σ steps (hands + body/eye) + process time + prorated occasional elements
Standard     = manual normal time × (1 + allowance) + process time        (convention A)
           or  total normal time × (1 + allowance)                          (convention B)
```

Agree the convention, and use it consistently.

**Lab 6 (press load and unload)** illustrates the difference:

| Item | cs |
|---|---|
| Manual motions | 332.5 |
| Press cycle (process) | 180 |
| Total normal | 512.5 |
| Standard, allowance on manual only | (332.5 × 1.12 + 180) = 552.4 cs = **5.52 s** (652/h) |
| Standard, allowance on everything | 512.5 × 1.12 = 574 cs = **5.74 s** (627/h) |

Allowances for personal needs, fatigue and delay are set by policy and are **not** part of the PMTS data. See the [Work Measurement](../../work-measurement/README.md) course.

## Documentation

A standard is only as good as its records. Keep together:

- the method description, layout sketch and photos
- the analysis sheet (all codes, distances and frequencies)
- the allowance convention and the date
- the analyst, and the reviewer

## Validation and audit

- **Spot-check** the analysis against video or a time study of a trained operator using the method. The trained operator should reach the PMTS time after learning.
- **Re-analyse** whenever the method, layout, parts or tools change.
- **Audit** a sample of standards on a schedule.

## Element data from analyses

Repeated element analyses (e.g. "get washer from magazine and place in fixture") can be stored as **standard elements** and reused. That is the step from detailed motion data toward [Standard Data Systems](../../standard-data-systems/README.md).

## Run it

```bash
python tools/dmtkit.py standard
```

## Check yourself

The Lab 6 operator also changes the finished-parts tote every 100 parts (an element of 300 cs). Add it and recompute the standard under convention A.

<details><summary>Answers</summary>

Manual = 332.5 + 300/100 = 335.5 cs. Standard = 335.5 × 1.12 + 180 = 555.8 cs = **5.56 s** (≈ 648 per hour).

</details>
