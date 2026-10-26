# Module 5 — Graphical Summaries

**Time:** 25 min

## Learning objectives

1. Choose the right chart for the question and the data type.
2. Explain why you should always plot data before computing statistics.

## 1. Plot first

Two data sets can share the same mean and standard deviation and look completely different. Anscombe's quartet (1973) is the classic demonstration: four data sets with nearly identical means, variances and correlations, but one is a line, one a curve, one has an outlier, and one is a single extreme point. Numbers summarize; pictures reveal.

## 2. Which chart?

| Question | Data | Chart | Module |
|---|---|---|---|
| Which categories matter most? | Nominal counts or costs | **Pareto chart** | 6 |
| What's the shape, center and spread? | Continuous, ≥ ~30 values | **Histogram** | 7 |
| Same, small sample | Continuous, < ~30 values | **Dot plot** | 7 |
| Compare groups' center and spread | Continuous by group | **Box plot** or dot plot by group | 8 |
| How does it change over time? | Any, time-ordered | **Run chart** / process behavior chart | *Charting Process Behavior* |
| Are two variables related? | Two continuous | **Scatter plot** | — |
| Share of a whole, few categories | Nominal | Bar chart (preferred over pie) | — |

## 3. Box plot anatomy

```
   ┌─────────┬─────────┐
───┤         │         ├─────────    •
   └─────────┴─────────┘
  min    Q1  median  Q3      max   outlier
whisker                    whisker
```

The box holds the middle 50% of the data (the IQR, Module 10). Whiskers extend to the most extreme points within 1.5 × IQR of the box (Tukey's convention); points beyond are drawn individually.

## 4. Good chart habits

- Label axes with units; title says what and when.
- Start bar charts at zero; don't for line/run charts if it hides the variation.
- Show the specification limits on histograms of individual values.
- Avoid 3-D effects and dual axes that distort (the Pareto's cumulative line is a deliberate exception).

## Check yourself

Which chart? (a) Downtime minutes by cause; (b) daily scrap rate for the last 60 days; (c) comparing diameter from four lathes.

<details><summary>Answers</summary>

(a) Pareto. (b) Run chart or process behavior chart. (c) Box plots or dot plots by lathe.
</details>
