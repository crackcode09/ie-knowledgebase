# Module 9 — Job Evaluation

**Time:** 60 min

## Learning objectives

1. Compare job evaluation methods.
2. Apply the point-factor method to rank jobs by relative worth.

## 1. Methods

| Method | How | Pros / cons |
|---|---|---|
| **Ranking** | Order whole jobs from most to least demanding | Simple; subjective, no distances between jobs |
| **Classification (grading)** | Fit jobs into predefined grade descriptions | Common in government; broad |
| **Factor comparison** | Compare jobs factor by factor against benchmark jobs' pay | Detailed; complex |
| **Point-factor** | Score each job on weighted compensable factors | Most widely used; transparent; needs good factor definitions |

Job evaluation rates the **job**, not the person or their performance.

## 2. Point-factor method — case

**Compensable factors and weights:**

| Factor | Weight |
|---|---|
| Knowledge & skill | 35% |
| Responsibility | 25% |
| Effort (mental & physical) | 20% |
| Working conditions | 20% |

Each factor is rated on degrees 1–5 with written definitions. Points = Σ (weight × degree) → range 100–500.

| Job | Skill | Resp. | Effort | Cond. | **Points** |
|---|---|---|---|---|---|
| Kit packer | 2 | 2 | 3 | 2 | **220** |
| Material handler | 2 | 2 | 4 | 3 | 260 |
| Inspector | 3 | 3 | 2 | 2 | 260 |
| Machine operator | 3 | 3 | 3 | 3 | 300 |
| Setup technician | 4 | 4 | 3 | 3 | 360 |
| Team leader | 4 | 5 | 3 | 2 | 365 |
| Maintenance technician | 5 | 4 | 3 | 4 | 415 |

Example: kit packer = 35×2 + 25×2 + 20×3 + 20×2 = **220**.

```bash
python tools/ie.py jobeval
```

**Good practice:** a committee (not one person) rates jobs from up-to-date job descriptions; factor and degree definitions are written down; results are reviewed for consistency (similar jobs, similar scores) and for bias (comparable-worth checks across job groups).

## Check yourself

The team leader and setup technician score almost the same points. Should they be paid the same?

<details><summary>Answer</summary>

They should fall in the same or adjacent pay grade; pay within the grade can then vary with experience or performance. Module 10 shows the team leader is currently paid well below the line.
</details>
