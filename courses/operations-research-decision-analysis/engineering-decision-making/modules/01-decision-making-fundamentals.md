# Module 01 — Decision-Making Fundamentals

Outline items: Contexts for decision making · Fundamental and means objectives · Measurement scales (nominal, ordinal, interval, and ratio)

## Objectives

- Recognize the context of a decision and what it demands.
- Separate fundamental objectives from means objectives, so you frame the decision well and find more alternatives.
- Use measurement scales correctly.

## Running case

**Corran Motion Systems** (fictional) is launching a new linear-axis product and must choose its drive technology:

| | A Belt drive | B Ball screw | C Linear motor | D Rack and pinion |
|---|---|---|---|---|
| Unit cost ($) | 410 | 520 | 880 | 450 |
| Accuracy (µm, lower is better) | 50 | 10 | 2 | 30 |
| MTBF (h) | 18,000 | 22,000 | 30,000 | 15,000 |
| Time to market (months) | 6 | 8 | 14 | 7 |

Later modules add an uncertain market, a rival, supplier selection, field-failure warnings and a post-launch review. All data is simulated with a fixed seed (2030).

## Contexts for decision making

| Dimension | Question | Corran example |
|---|---|---|
| Individual or group | Who decides; whose preferences count? | Product council of 7 (Module 02) |
| One-time or repeated | Can we learn and adjust? | Technology choice is one-time; pricing is repeated |
| Certainty, risk or uncertainty | Do we know the outcomes and probabilities? | Market demand uncertain (Modules 03–04) |
| Single or multiple objectives | Are there trade-offs? | Cost vs accuracy vs reliability vs speed |
| Static or sequential | Are there later decisions or other players? | Prototype test, then launch; rival responds (Module 05) |
| Time and budget pressure | How much analysis can we afford? | 6 weeks to decide |

The context determines the method: no single method fits every decision. Module 06 returns to this.

## Fundamental and means objectives

- **Fundamental objectives** are what you ultimately care about in this decision.
- **Means objectives** matter only because they help achieve fundamental ones.

Ask **"Why is that important?"** until the answer is "it just is". That gives a fundamental objective.

```
Fundamental: maximize product profit over 5 years    Maximize customer satisfaction
               ▲                     ▲                        ▲
Means:   minimize unit cost   reach market fast       maximize accuracy; maximize reliability (MTBF)
               ▲                     ▲                        ▲
         use existing suppliers   reuse the current controller   specify better bearings
```

Why the distinction matters:

- **Evaluation** uses fundamental objectives, or measurable means close to them. Otherwise you double-count: "use existing suppliers" and "unit cost" measure the same thing.
- **Creating alternatives** uses means objectives: each one suggests new options. For example, "reach market fast" suggests a hybrid: launch with B now, offer C later.

## Measurement scales (nominal, ordinal, interval, and ratio)

| Scale | Meaning | Example | Valid operations |
|---|---|---|---|
| Nominal | Categories, no order | Drive type (belt, screw…) | Count, mode |
| Ordinal | Order, but unequal or unknown gaps | Panel ranking; "Good / Very good" grades | Median, rank-based methods |
| Interval | Equal gaps, arbitrary zero | Temperature in °C; value scores 0–1 | Differences, means, linear transformations |
| Ratio | True zero | Cost, MTBF, months | All, including ratios ("twice as reliable") |

Common errors:

- Averaging ordinal grades as if they were interval numbers.
- Saying "C is 25 times as accurate as A" from a ratio of µm. Mathematically true, but is that the value of the difference? Module 02 uses value functions instead.
- Multiplying interval-scale value scores, for example "twice the value".

## Check yourself

1. Is "use existing suppliers" a fundamental or a means objective for Corran? Why?
2. A survey rates designs 1–5 (poor to excellent). Can you say design X (average 4) is twice as good as Y (average 2)?

<details><summary>Answers</summary>

1. A **means** objective. It matters because it lowers cost and risk and shortens time to market. Ask "why?" and you reach those.
2. No. The ratings are ordinal, or at best interval. With no true zero, ratios are meaningless. Even averages assume equal gaps between grades.

</details>
