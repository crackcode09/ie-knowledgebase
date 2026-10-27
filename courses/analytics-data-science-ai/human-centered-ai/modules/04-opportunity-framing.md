# Module 04 — Opportunity Framing

Translating themes into clear opportunity statements that focus teams on the right problems.

## Objectives

- Write "How might we…" opportunity statements from themes.
- Check statements for the right scope.
- Prioritize opportunities on desirability, feasibility, viability and AI fit.

## How might we…

A **"How might we" (HMW)** statement turns a theme into an invitation to solve, without fixing the solution:

> Theme: *Finding the right information takes too long.*
> HMW: *How might we help technicians get the right information for this job, at the machine, in seconds?*

Good statements:

- name the **user** and the **situation**
- describe the **outcome**, not the technology ("…in seconds", not "…with a chatbot")
- are **neither too broad** ("How might we improve operations?") **nor too narrow** ("How might we add a search box to the ERP?")
- respect known **constraints** (T6: gloves, noise, time)

## Halvorsen's opportunities

| ID | How might we… | Theme |
|---|---|---|
| O1 | help technicians get the right information for this job, at the machine, in seconds? | T1 |
| O2 | capture and share experts' know-how so that anyone on shift can handle unfamiliar jobs? | T2 |
| O3 | stop people re-keying the same data between systems? | T3 |
| O4 | show the reasons behind system numbers so people can trust and act on them? | T4 |
| O5 | protect planned work from daily firefighting? | T5 |
| O6 | design tools that work with gloves, noise and seconds to spare? | T6 |

## Prioritizing

Scores are 1–5. Weights: desirability 0.35, feasibility 0.25, viability 0.20, AI fit 0.20.

| ID | Desirability | Feasibility | Viability | AI fit | Score |
|---|---|---|---|---|---|
| **O1** | 5 | 3 | 4 | 4 | **4.10** |
| O2 | 5 | 3 | 4 | 3 | 3.90 |
| O3 | 4 | 4 | 4 | 2 | 3.60 |
| O4 | 4 | 3 | 3 | 4 | 3.55 |
| O5 | 4 | 2 | 3 | 2 | 2.90 |
| O6 | 3 | 3 | 3 | 2 | 2.80 |

- **Desirability:** do users want it? (breadth, workarounds)
- **Feasibility:** can we build it with our data and skills?
- **Viability:** is it worth it for the business?
- **AI fit:** does it need prediction or language understanding? O3 (re-keying) scores low on AI fit. It is better solved by integration or rules, as in the "fix the process first" lesson of Efficient AI.

O1 goes forward to a design sprint (Module 05). O6 is not dropped: it becomes a **design constraint** for O1.

## Run it

```bash
python tools/hcdkit.py opportunities
```

## Check yourself

1. Improve: "How might we use AI to improve maintenance?"
2. Score O2 with weights 0.25 / 0.25 / 0.25 / 0.25.

<details><summary>Answers</summary>

1. For example: "How might we help a maintenance technician fix an unfamiliar breakdown right the first time, without waiting for the one expert?" It names the user, the situation and the outcome, and no technology.
2. (5 + 3 + 4 + 3) / 4 = **3.75**.

</details>
