# Module 0 — Introduction: Deciding with Data

**Time:** 30 min · **Prerequisites:** none (the *Charting Process Behavior* course in this repo helps for Module 6)

## Learning objectives

1. Explain what a hypothesis test is for, in one sentence.
2. Recognize improvement questions that call for a test.
3. Set up the course tools.

## 1. The one-sentence version

A hypothesis test tells you whether a difference you see in a **sample** is large enough, relative to the noise, that it is unlikely to be chance — so you can make a decision about the **process** the sample came from.

## 2. Questions a test answers

| Question on the floor | Test (module) |
|---|---|
| Is this machine running on nominal? | One-sample t (10) |
| Is supplier B's steel harder than supplier A's? | Two-sample t (11) |
| Does the new gauge read the same as the old one on the same parts? | Paired t (11) |
| Do the three plating lines produce the same thickness? | ANOVA (12) |
| Is the incoming defect rate above what the supplier promised? | One proportion (7) |
| Does night shift make more defectives than day shift? | Two proportions (8) |
| Does defect type depend on which machine made the part? | Chi-square (9) |
| Is torque variation within the requirement? | One variance (13) |
| Does the new saw cut more consistently? | Two variances (14) |
| Did repair turnaround (skewed data) improve? | Mann-Whitney (16) |
| Did the change work — over time? | Process behavior chart (6) |

## 3. Where testing fits

In a DMAIC project, tests live mostly in **Analyze** (is this factor really related to the problem?) and **Improve** (did the change make a real difference?). A test is a tool for a decision, not a substitute for knowing the process: always plot the data first, and always ask whether a difference is big enough to matter (Module 4).

## 4. Course map

| # | Module |
|---|---|
| 1 | Hypotheses: the process on trial |
| 2 | Decisions and the two types of error |
| 3 | Power and sample size |
| 4 | The test procedure, p-values, statistical vs practical significance |
| 5 | Confidence intervals |
| 6 | Treatment comparisons with process behavior charts |
| 7 | One proportion vs a standard |
| 8 | Two proportions |
| 9 | Several proportions: chi-square |
| 10 | One mean vs a standard: one-sample t |
| 11 | Two means: two-sample and paired t |
| 12 | Several means: ANOVA |
| 13 | One variance vs a standard: chi-square |
| 14 | Two variances: F and Levene |
| 15 | Parametric vs nonparametric tests |
| 16 | Nonparametric toolset |
| 17 | Choosing the right test |
| 18 | Capstone: four case files |

## 5. Setup

```bash
cd ie-knowledgebase/courses/lean-six-sigma/fundamentals-of-hypothesis-testing
pip install -r requirements.txt
python tools/make_data.py
python tools/htest.py all      # every worked example in the course
```

Every test is also shown with the formula, so you can do it by hand or in a spreadsheet (`reference/spreadsheet-recipes.md`).

## Check yourself

1. A test makes a statement about (a) the sample, (b) the process or population the sample came from.
2. Name the DMAIC phases where tests are used most.

<details><summary>Answers</summary>

1. (b). We already know the sample; the test is about what generated it.
2. Analyze and Improve.
</details>
