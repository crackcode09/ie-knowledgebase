# Course review checklist

Every course is `draft` until a reviewer has worked through this list. The reviewer then changes the course's status cell in the root README and the category README from `draft` to `verified (Name, YYYY-MM-DD)` and opens a pull request titled `review: verify <course>`. The site reads that cell and switches the course's badge and banner from draft to verified.

Review one course per pull request. Do not verify a course you wrote.

## 1. Originality

- [ ] No sentence, paragraph, table, figure or exercise is copied or lightly paraphrased from IISE material or from any book, course, standard or website. Spot-check: search the web for three distinctive sentences from each module.
- [ ] The course uses only the public course title and topic list from the IISE catalog, and the README says so where it follows an outline's order.
- [ ] No licensed data cards, tables or standards text are reproduced (MODAPTS code card, MTM-1 data card, ANSI/ASQ sampling tables, ISO clause text). Where the course needs one, it uses its own simplified teaching version and says so.
- [ ] Every dataset is simulated with a fixed seed, and every company, product and person in a case is fictional. No real customer, employee, part or order data.
- [ ] Quotations, if any, are short, attributed and necessary.

## 2. Accuracy

- [ ] Definitions and formulas match a primary source (textbook, standard or peer-reviewed paper) listed in `reference/sources.md`. Check every formula in `reference/formulas.md` or the equivalent, and that every symbol is defined where it is used and means the same thing throughout the course.
- [ ] `reference/sources.md` exists, every entry has an edition or standard number, every ID cited in a module exists in the table, and each entry you have checked has Verified set to `yes`.
- [ ] Every number in the lessons and in `solutions/README.md` can be reproduced by running the course's own scripts (`tools/make_data.py`, `tools/make_figures.py`, the analysis script). Run them.
- [ ] Standards, regulations and historical claims are current and correctly cited (edition, year, clause). Anything uncertain is marked as such in the text or removed.
- [ ] Exercises have answers, and the answers are right.
- [ ] Where authorities disagree, the course presents both positions rather than picking one silently.

## 3. Trademarks and licences

- [ ] Names of organisations, methods, certifications and software are used only descriptively; no wording implies endorsement, affiliation or certification.
- [ ] Belt names describe content levels only; the course never says it certifies anyone.
- [ ] Figures made by contributors carry no third-party logos or screenshots of licensed software beyond what fair use allows.
- [ ] Any third-party material that is included is openly licensed, attributed, and compatible with CC BY 4.0.

## 4. Structure and plain language

- [ ] Each module has objectives, concept, worked example, exercise and a check-yourself section.
- [ ] The README syllabus table lists every module with its time and topics, and every link resolves.
- [ ] Written for a reader without a statistics background; the math is in tables, the prose explains it.

## Running the review board

The checklist above can be run by the course review board in Claude Code: `/review-course <slug>` launches four reviewers in parallel (originality, accuracy, trademarks and licences, structure and plain language), consolidates their PASS / FAIL / QUESTION verdicts into `reviews/<slug>.md`, and lists every doubt as a numbered question for you to answer. A FAIL in sections 1 or 3 blocks verification outright. The board never flips the status itself: once every question is answered and no FAIL remains, `/review-course <slug> --sign-off` records your name, updates the status cells and opens the `review:` pull request. See [reviews/README.md](reviews/README.md).

## 5. Sign-off

Add to the course README, under the title block:

```
**Status:** verified by <Name> on <YYYY-MM-DD>. <One line on scope, e.g. "All scripts rerun; formulas checked against Montgomery 8th ed.">
```

Then change the status cell in both catalog tables and run `python tools/roadmap_graph.py`.

If anything in sections 1 or 3 fails, do not verify. Open an issue describing the problem; if material may infringe, remove it in the same pull request.
