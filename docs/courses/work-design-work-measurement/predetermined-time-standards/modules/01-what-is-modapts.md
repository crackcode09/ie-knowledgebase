# Module 01 — What Is MODAPTS?

## Objectives

- Describe MODAPTS in one sentence and place it among work measurement methods.
- Explain what this open course teaches, and what only the licensing body provides.

## In one sentence

**MODAPTS** is a **predetermined motion time system (PMTS)**. You describe a manual task as a sequence of coded body motions, and the codes add up to the task's normal time, with no stopwatch and no performance rating ([Eisbrenner PG, "About MODAPTS"](https://eisbrennerpg.com/about-modapts/)).

## Where it sits among work measurement methods

| Method | Time comes from | Needs the job to exist? | Rating needed? |
|---|---|---|---|
| Time study | A stopwatch or video of a worker | Yes | Yes |
| Work sampling | Random observations | Yes | Usually |
| Standard data | Earlier studies of similar work | No | Already built in |
| **PMTS (e.g. MODAPTS, MTM, MOST)** | **Tables of motion times** | **No** | **No** |

A PMTS can set a standard **before** a workstation is built. That makes it a design tool as well as a measurement tool: you can compare layouts and methods on paper.

## About this course

The topics follow a MODAPTS practitioner course outline, item by item. MODAPTS is a trademark of the International MODAPTS Association, Inc. ([trademark record](https://trademark.justia.com/owners/international-modapts-association-inc-399044)). Its code card, rules and manual are the Association's material. This course therefore:

- explains **what MODAPTS is and how it is organized**, using only facts from public sources, which are cited;
- teaches the **method**, meaning how body-motion systems classify and code work, with an **original teaching code card** (`data/teaching_code_card.csv`). The card is built on the same principles but **is not the MODAPTS card**. Its values are for practice, not for real standards;
- points you to the **International MODAPTS Association (IMA)** for the official card, practitioner training and certification. Those are needed before you set real standards.

This course is not affiliated with or endorsed by the IMA.

## Running case

**Kessler Components** (fictional) kits fasteners, assembles small pinned housings and packs cartons. The IE team wants to:

- set standards for new jobs before they launch
- find faster methods
- reduce bending and over-reaching

## Run it

```bash
python tools/ptskit.py card
```

## Check yourself

1. What two things does a PMTS remove compared with time study?
2. Why is a PMTS useful before a workstation exists?

<details><summary>Answers</summary>

1. The stopwatch (timing) and the performance rating. Times come from tables that are already at a defined normal pace.
2. You can code the planned method from a layout drawing or mock-up, get a standard and compare alternatives, all before you spend money building the station.

</details>
