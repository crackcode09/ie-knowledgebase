# Module 01 — Common Errors When Communicating

## Objectives

- Recognize the errors that most often sink technical presentations and reports.
- Diagnose them in a real draft.
- Know the fix for each.

## The common errors

| Error | What it looks like | Fix |
|---|---|---|
| **Burying the lead** | conclusion and ask on the last slide | answer first (Module 03) |
| **Chronological story** | "first we did… then we did…" | organize by the message, not the timeline |
| **No clear ask** | "consider rollout to other lines" | state the decision, amount, owner and date |
| **Wrong audience level** | DMAIC phase names, acronyms, p-values to executives | translate into impact; keep detail in an appendix |
| **Data dump** | every chart from the project | only evidence that supports the message |
| **Text-heavy slides** | paragraphs read aloud | one idea per slide; detail in the notes or a handout |
| **Topic titles** | "Analyze", "Results" | the takeaway as a sentence |
| **Misleading or unreadable charts** | dual axes, rainbow colors, truncated scales | Module 05 |
| **Hidden uncertainty** | "scrap is now 2 %" with no sense of spread | give ranges and how long it has held |
| **Overrunning time** | 20 minutes of content in a 10-minute slot | script and rehearse; leave time for questions |
| **Not listening** | answering the question you wanted, not the one asked | Module 04 |
| **Passive, inflated language** | "it was subsequently determined that…" | short sentences, active voice, plain words |

## Diagnose a real draft

Open `examples/deck_draft.md` and run:

```bash
python tools/commkit.py check examples/deck_draft.md
```

| Slide | Words | Bullets | Flags |
|---|---|---|---|
| Agenda | 14 | 8 | 8 bullets; topic title |
| Define | 76 | 7 | 76 words; 7 bullets; topic title |
| Measure | 58 | 5 | 58 words; topic title |
| Analyze | 50 | 6 | 50 words; topic title |
| Improve | 30 | 4 | topic title |
| Control | 21 | 5 | topic title |
| Next steps | 10 | 3 | topic title |

The checker sees crowded slides and topic titles. A human reviewer sees more:

- The **ask** ("consider rollout… approx. $38k") is on the last slide, phrased as an option, with no savings figure next to it.
- The **savings** ($86,000 a year on Line 3) appear **nowhere** in the deck.
- The audience gets **DMAIC phase names, Gauge R&R, multi-vari, Cpk** — useful to a quality engineer, noise to a plant manager.
- Seven slides and an agenda for a 10-minute slot that needs time for discussion.

And the written summary (`examples/summary_draft.md`):

```bash
python tools/commkit.py readability
```

| | Draft | Revised |
|---|---|---|
| Words per sentence | 39.0 | 24.6 |
| Flesch reading ease (higher = easier; 60–70 is plain English) | −35.6 | 73.2 |
| Flesch–Kincaid grade | 27.9 | 9.2 |
| Words of 3+ syllables | 42 % | 5 % |

The draft's one-paragraph summary scores beyond any school grade. It is not wrong — it is unreadable for a busy reader. The revised version says more (savings, the ask, payback) in fewer words.

Readability formulas measure sentence and word length only. They cannot tell whether text is accurate, logical or relevant. Use them to catch bloat, not to grade quality.

## Check yourself

1. Rewrite "Consideration should potentially be given to the replication of these countermeasures across the remaining grinding lines" as a clear ask.
2. Which error is worst for a decision meeting, and why?
3. Why might an engineer resist putting the conclusion first?

<details><summary>Answers</summary>

1. "Approve $38,000 to apply the same fix to Lines 1, 2 and 4." (Name who decides and by when if it isn't obvious.)
2. No clear ask (or burying it): the meeting can end without a decision even if everything else is perfect.
3. It can feel like skipping the proof, or like being presumptuous. In practice, the audience listens to the evidence *more* carefully when they know what it is supposed to support.

</details>
