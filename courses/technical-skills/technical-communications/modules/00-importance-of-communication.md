# Module 00 — The Importance of Effective Communication

## Objectives

- Explain why good analysis fails without good communication.
- Describe the gap between how engineers and decision makers think about a project.
- Meet the running case and the course roadmap.

## Why it matters

An engineer can find the root cause, prove it with statistics and fix it — and the project still dies if leadership does not understand what was found, why it matters or what is being asked of them. The work is only finished when the right people **understand it and act on it**.

Poor technical communication shows up as:

- decisions delayed for "one more analysis";
- funding refused because the benefit was buried on slide 14;
- good fixes not spread to other lines because nobody outside the team understood them;
- credibility lost when a chart is misread or a number can't be explained;
- meetings that end without a decision.

## The engineer–audience gap

| The engineer tends to… | The decision maker wants… |
|---|---|
| tell the story in the order the work was done | the conclusion and the ask first |
| show method to prove rigor | confidence that the method was sound, not the method itself |
| use precise technical terms | plain words and business impact |
| show all the data | the few numbers that change the decision |
| treat uncertainty as a footnote | to know how sure you are and what could go wrong |

Neither side is wrong. Rigor matters — but the audience's job is to decide, not to repeat your analysis. Your job is to make the decision easy and safe.

## A working definition

**Effective technical communication** gets the right audience to understand the right message **well enough to act**, in the time they have, with an accurate sense of the uncertainty.

Four tests follow from that definition, and the course builds each one:

1. **Audience** — who must act, and what do they already know? (Modules 02, 04)
2. **Message** — can you state the point and the ask in one or two sentences? (Modules 02, 03)
3. **Evidence** — does the data support the point, shown so it can't be misread? (Module 05)
4. **Delivery** — is it clear, on time, and does it handle questions? (Modules 04, 07, 08)

## Running case

A process engineer at a fictional bearing plant led a project that cut scrap on **grinding Line 3** from 4.5 % to 2.0 %. She has a **10-minute slot** at the plant leadership meeting to ask for **$38,000** to apply the fix to three more lines. The `examples/` folder holds her first draft and her revised version of both the deck and the written summary; the course follows her from one to the other.

All data and people are fictional. The project's technical details (gauge study, capability numbers) are illustrative.

## Getting started

```bash
pip install -r requirements.txt
python tools/commkit.py all
python tools/commkit.py check examples/deck_draft.md
```

`commkit.py check <file>` scores the readability of any Markdown draft and flags crowded slides. It's a quick aid, not a judge.

## Check yourself

1. The engineer's first draft followed the order of her project (Define, Measure, Analyze, Improve, Control). Why might that order hurt her in a 10-minute leadership slot?
2. Think of the last technical presentation you attended. Did you leave knowing what the presenter wanted? If not, what was missing?

<details><summary>Answers</summary>

1. The ask (approve $38,000) arrives in the last minute — if at all. Leaders spend eight minutes not knowing why they are listening, and the discussion time runs out before the decision.
2. Usually missing: a clear statement of the ask, a reason it matters to the audience, or a summary at the start.

</details>
