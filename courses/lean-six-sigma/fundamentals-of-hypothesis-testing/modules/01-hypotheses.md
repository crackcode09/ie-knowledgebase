# Module 1 — Hypotheses: The Process on Trial

**Time:** 45 min

## Learning objectives

1. Formulate a hypothesis statement from a practical question.
2. Differentiate the null and alternative hypotheses.
3. Choose between one-sided and two-sided alternatives.

## 1. The courtroom analogy

A criminal trial and a hypothesis test share the same logic:

| Courtroom | Hypothesis test |
|---|---|
| Defendant is presumed innocent | Null hypothesis H₀ is presumed true |
| Prosecution must prove guilt | Data must provide strong evidence against H₀ |
| "Beyond reasonable doubt" | Significance level α (e.g., 0.05) |
| Verdict: guilty | Reject H₀ |
| Verdict: **not guilty** (not "innocent") | **Fail to reject** H₀ (not "accept H₀") |
| Convicting an innocent person | Type I error |
| Acquitting a guilty person | Type II error |

The verdict "not guilty" doesn't prove innocence; it means the evidence wasn't strong enough. Likewise, failing to reject H₀ does not prove there is no difference.

## 2. Null and alternative

- **H₀ (null):** the status quo, "no difference," "no effect." It always contains the equals sign (=, ≤ or ≥).
- **Hₐ (alternative):** what you suspect or want to show. It never contains equality.

The burden of proof is on Hₐ. Put the claim you want evidence for into Hₐ.

## 3. From question to statement

| Practical question | H₀ | Hₐ | Sides |
|---|---|---|---|
| Is the machine off nominal 25.000 mm? | μ = 25.000 | μ ≠ 25.000 | Two |
| Is the defect rate above the 3% promised? | p ≤ 0.03 | p > 0.03 | One (upper) |
| Did the change *reduce* cycle time? | μ_after ≥ μ_before | μ_after < μ_before | One (lower) |
| Do the three lines differ? | μ₁ = μ₂ = μ₃ | At least one differs | — |
| Is torque σ more than 0.50? | σ ≤ 0.50 | σ > 0.50 | One (upper) |

**Template:** "We will test whether [parameter] of [process] is [different from / greater than / less than] [value or other group], using [data], at α = [level]."

## 4. One-sided or two-sided?

- **Two-sided** is the default. Use it unless a difference in one direction is impossible or genuinely irrelevant to the decision.
- **One-sided** tests have more power in the stated direction, but you must choose the direction **before** looking at the data. Choosing after seeing the data doubles your real Type I error rate.

## Exercise 1.1

Write H₀ and Hₐ for: (a) "Is the new supplier's fill weight different from 500 g?" (b) "Does the new fixture reduce the setup scrap rate?" (c) "Do the four operators measure the same way?"

<details><summary>Answers</summary>

(a) H₀: μ = 500, Hₐ: μ ≠ 500. (b) H₀: p_new ≥ p_old, Hₐ: p_new < p_old. (c) H₀: all four operator means equal; Hₐ: at least one differs.
</details>

## Check yourself

1. Which hypothesis always contains the equals sign?
2. Why is "accept H₀" the wrong conclusion?

<details><summary>Answers</summary>

1. H₀.
2. A non-significant result may just mean too little data (low power). Absence of evidence is not evidence of absence.
</details>
