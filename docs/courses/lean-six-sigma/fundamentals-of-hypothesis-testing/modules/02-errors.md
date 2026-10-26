# Module 2 — Decisions and the Two Types of Error

**Time:** 40 min

## Learning objectives

1. Assign the correct type of error given the outcome of a test.
2. Explain α, β and power.
3. Choose a significance level based on consequences.

## 1. The decision table

| | **H₀ is really true** | **H₀ is really false** |
|---|---|---|
| **Reject H₀** | **Type I error** (false alarm) — probability α | Correct — probability **power = 1 − β** |
| **Fail to reject H₀** | Correct — probability 1 − α | **Type II error** (missed effect) — probability β |

- **α (significance level):** the risk you accept of a false alarm. Chosen before the test.
- **β:** the risk of missing a real effect of a given size.
- **Power (1 − β):** the probability of detecting an effect of a given size. Depends on the effect size, the noise, n and α (Module 3).

## 2. Assigning error types — practice

| Situation | Truth | Decision | Error |
|---|---|---|---|
| You conclude a new coolant improved surface finish; it actually didn't | H₀ true | Reject | **Type I** |
| You conclude two suppliers are no different; supplier B really is harder | H₀ false | Fail to reject | **Type II** |
| A gauge study finds the new gauge biased; it really is | H₀ false | Reject | Correct |
| Incoming lot passes acceptance test; lot really is bad | H₀ (lot good) false | Fail to reject | **Type II** (consumer's risk) |
| Good lot is rejected | H₀ true | Reject | **Type I** (producer's risk) |

Acceptance sampling uses the same idea under different names: α = **producer's risk**, β = **consumer's risk**.

## 3. Choosing α

α = 0.05 is a convention (popularized by R. A. Fisher in the 1920s), not a law. Choose by consequences:

| If a false alarm is… | …and a miss is… | Consider |
|---|---|---|
| Expensive (capital equipment, requalification) | Cheap | α = 0.01 |
| Cheap (one more trial) | Expensive (safety, field failure) | α = 0.10, and plan for high power |
| Balanced | Balanced | α = 0.05 |

You cannot lower α and β together without more data or less noise.

## 4. Worked example: a real Type II error

`data/supplier_hardness.csv` was generated with a **true** difference of 1.4 HRC between suppliers (σ = 1.2 each, 15 bars each). The test (Module 11) gives p = 0.092 → fail to reject at α = 0.05.

That is a Type II error — and it wasn't bad luck from a badly planned study: the power to detect 1.4 HRC with this design is about 87% (`tools/htest.py`, noncentral t). One time in eight, a well-designed study misses a real effect. This is why "fail to reject" never means "proven equal."

## Check yourself

1. A test with α = 0.05 is run 100 times on a process where H₀ is true. About how many will reject H₀?
2. A study rejects H₀. Which error is now possible: Type I, Type II, or both?

<details><summary>Answers</summary>

1. About 5 (Type I errors).
2. Only Type I — you can't miss an effect you just detected.
</details>
