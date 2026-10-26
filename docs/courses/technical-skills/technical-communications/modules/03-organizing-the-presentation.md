# Module 03 — Organizing the Presentation

## Objectives

- Structure a presentation answer-first, using a pyramid or situation–complication–resolution outline.
- Storyboard with action titles before opening the slide software.
- Fit the structure to the time, and plan the appendix.

## Answer first

Lead with the conclusion and the ask. Then give the supporting points, then the evidence for each. This is often called the **pyramid principle**: one governing idea at the top, a small number of supporting points below it, and evidence below those.

```
Approve $38,000 to cut grinding scrap in half on Lines 1, 2 and 4
├── It worked on Line 3: scrap 4.5% → 2.0%, held 13 weeks
│     └── weekly scrap chart
├── We know why: coolant drift and inconsistent dressing caused 70% of scrap
│     └── defect Pareto; coolant and dressing data
├── The fix is robust: three automatic controls, no reliance on memory
└── It will transfer: same machines and causes on 1, 2, 4; Line 4 piloted first
      └── savings math; risk and owner
```

Supporting points should be **mutually exclusive** (no overlap) and together **collectively exhaustive** (they cover the case a skeptic needs).

## Situation – Complication – Resolution

A short opening that frames why the audience should care:

- **Situation:** Grinding scrap has run around 4.5 % on all four lines.
- **Complication:** That costs roughly $86,000 a year per line, and assembly has stopped for oversize parts.
- **Resolution:** We fixed it on Line 3; we want to fix the other three.

Then go straight to the ask.

## Storyboard with action titles

Before building any slides, write the **title of every slide as a full sentence that states its takeaway** ("action title"). Read the titles alone, top to bottom — they should tell the whole story.

**Draft deck titles:** Agenda · Define · Measure · Analyze · Improve · Control · Next steps
→ tells you the project method, not the message.

**Revised deck titles:**

1. Approve $38,000 to cut grinding scrap in half on Lines 1, 2 and 4
2. Line 3 scrap has stayed near 2 % for 13 weeks
3. Two defects made 70 % of the scrap: oversize and burn
4. Both came from coolant drift and too-infrequent wheel dressing
5. Three changes now hold the process steady
6. The same parts and causes exist on Lines 1, 2 and 4
7. Decision needed today: approve $38,000
8. Appendix A / B — statistics, capability, savings math

That is the whole argument in seven lines. `templates/storyboard.md` has a blank version.

## Fit the time

| Slot | Content slides | Questions |
|---|---|---|
| 5 min | 2–3 | 2 min |
| 10 min | 4–6 | 3–4 min |
| 20 min | 8–12 | 6–8 min |

Rule of thumb: 1–2 minutes per content slide and about one-third of the slot for discussion. The revised Line 3 script is about 340 words — roughly 2.5 minutes of speech at 130–150 words per minute (`python tools/commkit.py timing`) — leaving most of the 10 minutes for questions and the decision. Speaking pace varies widely between people; time yourself.

## The appendix is not a dumping ground — it's insurance

Put the detail **some** of the audience will ask for — statistics, capability, savings math, assumptions — in labeled backup slides. Then you can answer "how do you know?" in five seconds without making everyone sit through it.

## Written documents use the same structure

- **Executive summary first** (one paragraph: finding, impact, ask).
- **Headings that state conclusions** ("Coolant drift caused most oversize scrap"), not topics ("Analysis").
- **Details and methods** in later sections or an appendix.
- An **A3** (one large page) is a compact form of the same structure: background, current condition, analysis, countermeasures, plan, follow-up.

## Check yourself

1. Write the situation–complication–resolution opening for a proposal to add a second shift on a bottleneck machine.
2. Read the draft deck's titles only. What do you learn?
3. A director interrupts on slide 2: "So what do you want?" What went wrong?

<details><summary>Answers</summary>

1. Example: *Situation:* Machine 12 runs two shifts and feeds three assembly lines. *Complication:* Orders are up 18 % and it is now the bottleneck; we're late on 9 % of orders. *Resolution:* Add a third-shift operator for six months while we qualify a second machine.
2. Only the project's method and order. Nothing about the result, the savings or the ask.
3. The ask wasn't on slide 1 — or wasn't stated plainly enough to be heard.

</details>
