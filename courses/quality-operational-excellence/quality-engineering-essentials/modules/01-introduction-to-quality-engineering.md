# Module 01 — Introduction to Quality Engineering

**Time:** 3 h

## Objectives

- Explain the quality engineer's role and the idea that inputs determine outputs, Y = f(X).
- Relate Lean principles, the 3 M's and the 8 wastes to quality.
- Show why "99.9 % good" isn't good enough, and use the DMAIC improvement process.
- Write a project charter.

## Inputs determine output: Y = f(X)

Every output characteristic (Y) — a dimension, a defect rate, a delivery time — is a function of process inputs (X's): materials, machines, methods, measurement, people and environment. Inspecting Y finds problems; **controlling the critical X's prevents them**. Most of this course is about finding which X's matter and keeping them under control.

## Lean and quality

Lean focuses on flow and waste; Six Sigma on variation and defects. They reinforce each other.

**Five Lean principles** (as commonly stated): specify **value** from the customer's view; map the **value stream**; make value **flow**; let the customer **pull**; pursue **perfection**.

**The 3 M's** — *muda* (waste), *mura* (unevenness), *muri* (overburden). Unevenness and overburden create waste and defects.

**8 wastes** (often remembered as DOWNTIME): **D**efects, **O**verproduction, **W**aiting, **N**on-utilized talent, **T**ransportation, **I**nventory, **M**otion, **E**xtra processing. Defects are the waste quality engineers attack most directly — and every defect drags in others (rework motion, waiting, extra inspection).

## The 99.9 % problem

If every step in a process is 99.9 % right, the chance a unit passes **all** steps (rolled throughput yield) is 0.999ⁿ:

| Steps | Overall yield |
|---|---|
| 10 | 99.0 % |
| 100 | 90.5 % |
| 500 | 60.6 % |
| 1,000 | 36.8 % |

After 693 steps, fewer than half of the units are defect-free. Complex products and processes need far better than 99.9 % per step — which is why defect rates are tracked in parts per million.

## DMAIC

| Phase | Question | Typical tools (this course) |
|---|---|---|
| **Define** | What is the problem, for whom, and what is the goal? | charter, SIPOC, voice of the customer |
| **Measure** | How big is it? Can we trust the data? | basic statistics, MSA, baseline, capability, SPC (Modules 02–04) |
| **Analyze** | What are the root causes? | problem statement, fishbone, 5-Why, stratification, regression, FMEA (Module 05) |
| **Improve** | What fixes them? Do the fixes work? | error-proofing, pilots (Module 06) |
| **Control** | How do we keep the gain? | control plan, SPC, visual management, standard work (Module 06) |

## Running case: Bayline Fasteners

**Bayline Fasteners** (fictional) machines brass threaded inserts on two lathes (M1, M2) over three shifts. Critical characteristic: **outside diameter (OD) 6.350 ± 0.025 mm** — oversize inserts can't be pressed into the customer's plastic housings; undersize inserts pull out. A key customer has returned two shipments for oversize and damaged-thread inserts.

## The project charter

| Element | Bayline example |
|---|---|
| Business case | Two customer returns this quarter; risk of losing a $1.2M/yr account; internal scrap and sorting cost |
| Problem statement | In the last 20 production days, 8.3 % of inserts sampled were defective, mostly oversize OD and thread damage, vs a customer requirement of < 1 % |
| Goal | Reduce defectives to < 1 % within 4 months, with oversize OD < 0.3 % |
| Scope | In: OD turning, threading, final inspection on M1/M2. Out: raw material supplier selection, packaging |
| Team | Quality engineer (lead), process engineer, two machinists, quality inspector, maintenance tech |
| Sponsor | Plant manager |
| Timeline | D 2 wks, M 4 wks, A 4 wks, I 4 wks, C 2 wks |
| Metrics | Primary: % defective. Secondary (don't make worse): cycle time, tool cost |

A template is in `templates/project-charter.md`.

**Worked example: from the data to the charter.**

**Data:** `data/production_sample.csv`, the 480-insert sample that Modules 02 to 05 analyse: one row per insert with the day, machine, shift, OD and the inspector's defect call.

**Steps:** (1) count the defect calls and sort them by type; (2) split the count by machine; (3) set the goal against the customer's requirement, with a separate target for the largest defect type. Command: `python tools/qekit.py pareto`.

**Result:** 40 of 480 defective, 8.3 %; oversize OD 20 (4.2 % of inserts) and thread damage 11 are the two largest types; M2 has 30 of the 40 (12.5 % of its inserts) against M1's 10 (4.2 %). The customer requires under 1 %.

**What it means:** every number in the problem statement and the goal above is one of these counts. The 8.3 % and the defect mix are the problem; "oversize OD under 0.3 %" targets the largest type; the machine split tells the team where to look first (Module 05), and it is the baseline the pilot in Module 06 is measured against.

## Learning and problem solving with AI tools

AI assistants can help draft charters, suggest fishbone categories, explain statistical output or write code (the course's Python tools are an example). Use them as a **colleague to check**, not an authority: verify calculations, never paste confidential data into tools your company hasn't approved, and keep the team's process knowledge at the center.

## Exercise 1.1

Using `data/production_sample.csv` (one row per insert, with machine, shift, OD and the defect call):

1. Write the problem statement for machine M2 alone: count its defective inserts, its oversize inserts, and compare with M1.
2. The charter lists two secondary metrics that must not get worse. Where in the course are they checked?
3. Bayline's insert goes through 12 process steps. If each were 99.5 % right, what share of inserts would pass every step?

Answers in `solutions/README.md`.

## Check yourself

1. A product has 50 process steps, each 99.5 % right. What's the rolled throughput yield?
2. Rewrite as a proper problem statement: "The lathes are bad."
3. Which of the 8 wastes does sorting suspect inserts create?

<details><summary>Answers</summary>

1. 0.995⁵⁰ = 77.8 %.
2. "Over the last 20 days, 8.3 % of inserts from lathes M1 and M2 were defective (mainly oversize OD), against a customer requirement of < 1 %, causing two returned shipments." — what, where, when, how big, against what standard; no cause or solution.
3. Extra processing (the sorting), plus waiting, inventory (quarantined parts), motion and transportation.

</details>
