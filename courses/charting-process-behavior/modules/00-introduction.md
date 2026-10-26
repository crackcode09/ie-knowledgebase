# Module 0 — Introduction: Why Chart Process Behavior?

**Time:** 30 min · **Prerequisites:** none

## Learning objectives

By the end of this module you can:

1. Explain what a process behavior chart (control chart) is for, in one sentence.
2. Describe where charting fits in a structured improvement cycle (DMAIC / PDSA).
3. Set up the course tools on your computer.

## 1. The one-sentence version

A process behavior chart separates **routine variation** (the noise every process makes) from **exceptional variation** (a signal that something changed), so you react to the second and stop reacting to the first.

Walter Shewhart developed the idea at Bell Telephone Laboratories in the 1920s and published it in *Economic Control of Quality of Manufactured Product* (1931). W. Edwards Deming spread it; Donald Wheeler renamed "control charts" to **process behavior charts** because the chart does not control anything — it describes how a process behaves and tells you when that behavior changes. This course uses both names.

## 2. Two mistakes the chart prevents

| Mistake | What it looks like on the floor | Cost |
|---|---|---|
| **Type 1: reacting to noise** | Operator adjusts the machine after every slightly high reading; supervisor asks "what happened Tuesday?" about an ordinary Tuesday | Tampering adds variation (Module 10), wasted investigations |
| **Type 2: missing a signal** | A real shift is waved off as "normal scatter" | Scrap, escapes, customer complaints |

You cannot drive both risks to zero. Shewhart's three-sigma limits are an *economic* compromise that keeps Type 1 errors rare while still catching changes that matter.

## 3. Where charting fits in an improvement cycle

The most common structured improvement roadmap is **DMAIC**:

| Phase | Question | Charting role |
|---|---|---|
| **Define** | What problem, for whom? | — |
| **Measure** | How does the process behave today? | Baseline run chart / XmR chart, capability |
| **Analyze** | What drives the variation? | Stratified charts, rational subgroups |
| **Improve** | Did the change work? | Before/after charts with revised limits |
| **Control** | Will the gain hold? | Ongoing chart with a reaction plan |

Shewhart's own cycle (later Deming's **PDSA**: Plan–Do–Study–Act) uses charts in the *Study* step. Either way, the chart is the evidence that a change happened — or didn't.

## 4. Course map

| # | Module | You will be able to… |
|---|---|---|
| 1 | Measurement & metrics | Pick a metric and judge whether the data are trustworthy |
| 2 | Distributions & histograms | Read shape, center and spread from a histogram |
| 3 | Quantifying variability | Compute range, standard deviation, within vs overall sigma |
| 4 | Run (trend) charts | Plot data in time order and apply run rules |
| 5 | Introduction to process behavior charts | Explain where limits come from and why they are not specs |
| 6 | XmR chart | Build and interpret an individuals & moving range chart |
| 7 | Detection rules | Identify common vs special cause signals |
| 8 | Rational subgrouping & X̄–R | Design subgroups and build an X̄–R chart |
| 9 | Attribute charts | Build p, np, c and u charts |
| 10 | Tampering: Deming's funnel | Show why adjusting to noise makes things worse |
| 11 | Stratification | Split data by machine, shift, cavity, etc. to reveal hidden structure |
| 12 | Process capability | Compute and interpret Cp, Cpk, Pp, Ppk |
| 13 | Non-normal data & transformations | Decide when shape matters and what to do |
| 14 | Advanced charts | Know when to use X̄–S, EWMA, CUSUM, short-run charts |
| 15 | Capstone | Run a full study on your own data |

## 5. Set up the tools

```bash
git clone <this-repo-url>
cd open-ie-courses/courses/charting-process-behavior
pip install numpy matplotlib scipy
python tools/make_data.py        # regenerates data/*.csv
python tools/spc.py xmr data/shaft_diameter.csv value
```

No Python? Every calculation in this course is shown by hand and works in a spreadsheet. `reference/spreadsheet-recipes.md` has the formulas.

## Check yourself

1. A chart's purpose is to (a) keep the process inside spec, (b) tell signal from noise, (c) prove the process is normal.
2. Name the two kinds of mistakes a chart helps you balance.
3. In which DMAIC phase do you first build a baseline chart?

<details><summary>Answers</summary>

1. (b). Specs are the customer's voice; the chart is the process's voice (Module 5). Normality is not required (Module 13).
2. Reacting to noise as if it were a signal; missing a real signal.
3. Measure.
</details>

