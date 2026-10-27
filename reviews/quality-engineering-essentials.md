# Review: Quality Engineering Essentials

| | |
|---|---|
| Course | `courses/quality-operational-excellence/quality-engineering-essentials/` (8 modules, including the folded-in `00-foundations-of-quality.md` that covers the catalog's separate "Quality 101" topic) |
| Board run | 2, plus a targeted run-3 re-check of the run-2 findings (accuracy section) |
| Date | 2026-10-27 |
| State | open questions (no FAIL remains; questions 17 to 26 answered on 2026-10-27 and applied in PR #37, except the 7.1.5 / 7.5 / 10.2 confirmation under 17) |
| Verified by | |

## Verdict summary

| Item | Run 1 | Run 2 |
|---|---|---|
| 1.1 Nothing copied | PASS | PASS (39 searches over both runs, no hits) |
| 1.2 Only public titles and outlines used | FAIL | PASS (statement added to the README) |
| 1.3 No licensed data cards or standards text | PASS | PASS (standards map is names and one-line purposes only) |
| 1.4 Fictional, seeded data | PASS | PASS (one question on the company name) |
| 1.5 Quotations short and attributed | PASS | PASS |
| 2.1 Formulas match a primary source; every symbol defined | FAIL | PASS after #36 (run 2 found one Cpk/Ppk label slip and one attribution slip; both fixed and re-checked) |
| 2.2 Every number reproducible | FAIL | PASS (scripts rerun; data byte-identical; every number matches) |
| 2.3 Claims current and cited | FAIL | QUESTION (ISO 9001:2026 clause structure; one wrong sentence on Dee's kappa, counted under blocking finding 3) |
| 2.4 Exercises answered correctly | PASS | PASS after #36 (the Ben's-offset answer was corrected and re-checked against the data) |
| 2.5 Disagreements presented fairly | FAIL | PASS (Wheeler, Action Priority, kappa baseline all present) |
| 2.6 Sources table complete | not checked | PASS after #36 (entries added, Cited-in rebuilt and re-checked row by row, stale line removed) |
| 3.1 Marks used descriptively | PASS | PASS |
| 3.2 Belt names describe content | PASS | PASS |
| 3.3 Figures are the course's own | PASS | PASS |
| 3.4 Third-party material licensed and attributed | PASS | PASS |
| 3.5 Licence statements present | PASS | PASS |
| 4.1 Module structure complete, worked examples as dataset, steps, result, meaning | FAIL | PASS (two questions on modules 00 and 01) |
| 4.2 Syllabus complete with time and topics | FAIL | PASS (times sum to 39.25 h) |
| 4.3 Links and images resolve | FAIL | PASS |
| 4.4 Prerequisites line parses | PASS | PASS |
| 4.5 Readable without a statistics background | QUESTION | QUESTION (glosses added; a few long sentences and abbreviations remain) |
| 4.6 Figures and data files present | PASS | PASS |

## Blocking findings (run 2), all fixed in PR #36

The accuracy reviewer re-checked each one on the fixed branch (run 3, targeted): 1, 2 and 3 confirmed fixed; 4 confirmed except the ISO 9001:2026 row, which was corrected in a follow-up commit, and one further stale sentence in the facilitator notes ("the AIAG baseline passes Dee"), also corrected.

1. **2.1 and 2.4, Cpk versus Ppk label.** `modules/04` exercise 4.1 (1) and `solutions/README.md` call M1's 0.92 "Cpk", but it is computed with the overall standard deviation, which the course's own formula sheet defines as Ppk. The module's result table already says Ppk. Fix: say "Ppk = 0.92; if centred, Pp = 1.42". Also, `reference/formulas.md` credits the kappa formula to landis-koch-1977; the formula is Cohen (1960), Landis and Koch supply the bands. Fix: add a cohen-1960 entry and cite it.
2. **2.4, exercise 3.1 answer.** The answer says Ben's offset "grows with size". Per part, Ben's excess over the other two operators runs 0.0010 to 0.0043 mm with no trend (part 8 is 0.0010, part 6 is 0.0043). Fix: "Ben reads high on every part, by about 0.001 to 0.004 mm, with no clear trend with size", and point the diagnosis at technique rather than linearity.
3. **2.3, module 03 line 92.** "Dee's kappa of 0.71 passes the AIAG baseline comfortably" is wrong by the module's own stated baseline: AIAG calls above 0.75 good and below 0.40 poor, so 0.71 is in the conditional band. Fix: "Dee's kappa of 0.71 sits in AIAG's conditional band, and even so Dee disagreed with the expert on one part in five".
4. **2.6, `reference/sources.md`.** The "Cited in" column does not match the modules (montgomery-8e is cited in 00, not 02/04/07; crosby, womack, george and nist entries list modules that do not cite them by ID), the "general practice" list still names the deleted "+6 %" figure and the now-attributed kappa bar and change model, and two entries are missing: ISO 9001:2026 (cited in module 00) and Cohen 1960. Fix: add the two entries, rebuild the column from the actual citations, trim the list.

## Questions for the human reviewer (run 2)

Run 1's sixteen questions and their answers are kept below under "Run 1 record". New or still open:

17. **ISO 9001:2026 clause structure.** Module 00 says the 2026 edition keeps the 2015 structure; reachable sources say the architecture is retained but clause 6.1 is restructured with new sub-clauses, and the IAF transition rules were not yet published in them. The module already tells readers to check numbers against the auditor's edition. *Resolved by:* confirming from the standard or the IAF notice whether 7.1.5, 7.5 and 10.2 keep their numbers and the transition end date; otherwise soften "keeps" to "largely keeps".
    - **Answer:** (Nidhin, 2026-10-27) Research first; do not assume the structure. Chair's research the same day: DNV's revision summary and the Global ACI transition notice report that clauses 4 to 10 carry over, 6.1 is split into 6.1.1 to 6.1.3, 10.1 and 10.3 are consolidated into a new 10.1, 6.3 is strengthened and a quality-culture requirement is added under 5.1, 7.1.4 and 7.3; 2015 certificates end 30 September 2029. None of the reachable sources renumbers 7.1.5, 7.5 or 10.2, and none confirms them either. Applied: module 00 now says "largely keeps", lists those reported changes with two new source entries (dnv-iso9001-2026, global-aci-2026), keeps the "(2015 numbering)" caveat and adds the 2029 date. Still open for a reader with the published standard: confirm 7.1.5, 7.5 and 10.2 keep their numbers.
18. **Bayline name.** No company called Bayline Fasteners exists, but "Bay Fastening Systems" and "Bay Fasteners & Components" do, in the same industry. *Resolved by:* a ruling that the name is distinct enough, or a rename.
    - **Answer:** (Nidhin, 2026-10-27) Bayline is a fictional name made up for the case; distinct enough. No change.
19. **Change model attribution.** The four stages (awareness, understanding, acceptance, commitment) are the course's own; "condensation of Kotter" overstates the link. *Resolved by:* labelling the model as the course's own with Kotter cited as background.
    - **Answer:** (Nidhin, 2026-10-27) Yes, with research. Chair's research found no published model with the awareness, understanding, acceptance, commitment sequence (the nearest is Prosci's ADKAR, which differs). Applied: module 06 labels the three ideas as the course's own summary, not a published model, with Kotter's eight steps cited as the standard reference.
20. **Module 06 "growth inside about 0.004 mm".** The regression gives about 0.0024 mm of growth per 400-part offset step. *Resolved by:* stating the basis (two steps, or an allowance) or changing to 0.0025.
    - **Answer:** (Nidhin, 2026-10-27) Agreed. Applied: "about 0.0025 mm (0.0145 mm × 400 / 2,400)" per offset step.
21. **"Many customers now require the AP method"** (module 05) is plausible but unsourced. *Resolved by:* citing the AIAG-VDA handbook's adoption statement or softening to "some automotive customers".
    - **Answer:** (Nidhin, 2026-10-27) Where a standard or customer policy exists it overrides anything the course assumes. Chair's research: the AIAG-VDA handbook (2019) replaced RPN with AP; Ford's PPAP requirement has accepted the handbook format since 2024 (IATF Global Oversight notice, 17 October 2024); no OEM document reached says AP is mandatory across the board. Applied: module 05 now says AP is the required method where a customer applies the handbook, cites the Ford notice (iatf-ford-ppap-2024) as evidence of adoption, and says the customer's requirement overrides the course.
22. **Rolled throughput yield and the 1.5σ shift cited to montgomery-8e.** The reviewer could not confirm the book presents RTY. *Resolved by:* a reviewer with the book, or citing george-2005 for RTY.
    - **Answer:** (Nidhin, 2026-10-27) Reviewer supplied the standard definition (RTY = product of the first-pass yields of the sequential steps; step yield = 1 − DPU or e^−DPU), which matches module 01 and the formula sheet. Applied: rolled throughput yield, DPU and DPMO are now cited to george-2005 (The Lean Six Sigma Pocket Toolbook) in module 01 and the formula sheet; montgomery-8e keeps the sigma-level convention and the 1.5σ shift. Whether Montgomery also presents RTY no longer matters for the citation.
23. **Module 04 long sentences** (the Wheeler paragraph, the constants sentence, the staged-chart proof sentence) and **abbreviations** (UCL, LCL, p̄, σ_within, np, c, u, X̄–S used in the chart table without a gloss). *Resolved by:* a yes to splitting and glossing, or a ruling that the chart table is a pointer to the SQC course.
    - **Answer:** (Nidhin, 2026-10-27) Agreed. Applied: the Wheeler paragraph, the constants sentence, the staged-chart proof sentence, the run-rules sentence and the raw-scale meaning sentence are split; a "Reading the table" line under the chart table glosses X̄, R, S, p, np, c, u, UCL, LCL and p̄; σ_within is defined where Cp is introduced.
24. **Module 02:** skewness, Kolmogorov–Smirnov and Akaike are glossed functionally, not defined; two sentences near 40 words. *Resolved by:* accept or split.
    - **Answer:** (Nidhin, 2026-10-27) Split for readability. Applied: skewness, AIC and the KS statistic are defined in one sentence each; the two long sentences (statistic versus parameter; descriptive versus inferential) are split.
25. **Worked example in modules 00 and 01.** Module 00 is a concept module with an exercise and no worked example; module 01's worked example is the charter table with a one-sentence data link. *Resolved by:* a ruling that a concept module and a charter are exempt from the dataset-steps-result-meaning shape, or a short data-to-charter chain in module 01.
    - **Answer:** (Nidhin, 2026-10-27) Concept modules are not exempt; give them a layout that presents the example properly. Applied: module 00 gets a worked example in the course's shape (data: the production sample's defect calls and the calibration record; steps; a result table classifying three Bayline activities as control, assurance, improvement; meaning), and module 01's one-line data link becomes a short data-to-charter chain (data, steps, command, result, meaning) tying every charter number to the sample. Counts reproduced with `python tools/qekit.py pareto`.
26. **Module 05 step 2** (box and scatter plots) names no command; the figure comes from `tools/make_figures.py`. *Resolved by:* adding the command.
    - **Answer:** (Nidhin, 2026-10-27) Agreed. Applied: step 2 of module 05's worked example names `python tools/make_figures.py` and the file it writes.

## Follow-up after the question round (2026-10-27)

The answers to 17 to 26 were applied in PR #37 (modules 00, 01, 02, 04, 05, 06 and the sources table). Three source entries were added: dnv-iso9001-2026, global-aci-2026, iatf-ford-ppap-2024. Module 00 and module 01 now carry worked examples in the dataset, steps, command, result, meaning shape, so item 4.1 no longer has an open question. Items 2.3 and 4.5 move to PASS pending the board's next run; the chair has not marked them PASS here because no reviewer has re-read the changed text. Before sign-off the board should be re-run so the report reflects the changed modules.

## Not checked (run 2)

- Figure images against the printed numbers (scripts run; PNGs not compared). The AIAG MSA 4th edition 6σ multiplier was not confirmed against the manual itself. iso.org and nsf.org returned 403, so the ISO 9001:2026 publication date rests on the reviewer's confirmation in run 1. History-table claims (Taylor, Feigenbaum, Ishikawa, Taguchi) were sanity-checked, not sourced. Package licences not checked against metadata. IISE's own materials are not public and were not compared. The search tool returns summaries, so "no hit" is weaker than a full-text check.

## Originality (run 2)

| Item | Verdict | Evidence |
|---|---|---|
| 1.1 Nothing copied | PASS | 20 quoted-phrase searches this run (standards table, ISO section, modules 02 to 07, README, exercises) and 19 in run 1: no page carried the same or lightly paraphrased wording. Closest returns were generic topic pages (Minitab and AIAG kappa pages, Wheeler versus Breyfogle columns, RPN and Action Priority explainers). |
| 1.2 Only public titles and outlines used | PASS | README line 15 states the public-title-and-outline basis, that module 00 covers the catalog's "Quality 101" topic, originality, non-affiliation, and links NOTICE. |
| 1.3 No licensed data cards or standards text | PASS | The standards map lists 12 standards by number and name with one original line each; no clause or definition wording. Constants are public mathematical constants; AIAG figures are rules of thumb attributed by ID; the FMEA scale is in words; no Action Priority table. |
| 1.4 Fictional, seeded data | PASS | `make_data(seed=1924)` writes every CSV including `tooling_cost.csv` (labelled illustrative); hand-set pilot counts are disclosed in module 04; README names the seed and states Bayline and every person are fictional; first names only. |
| 1.5 Quotations short and attributed | PASS | No third-party prose quoted; Juran, Crosby, Deming, Shewhart, Wheeler, Landis and Koch paraphrased and attributed with entries in `sources.md`. |

## Accuracy (run 2)

Scripts rerun from a copy in a venv: `qekit.py data` (data byte-identical, including the new cost file), `qekit.py all`, `make_figures.py`, all exit 0. Exercise answers recomputed independently in pandas and scipy.

Run 1 fixes checked one by one: borderline count (fixed), ISO edition wording (fixed, one question), Wheeler and Action Priority (balanced), tooling cost (all five figures match the script: $0.010 to $0.015, +50 %, $0.390 to $0.395 and +1.28 %, $0.0417 avoided, $0.0367 net), KS labelling (fixed), kappa baseline (fixed).

| Item | Verdict | Evidence |
|---|---|---|
| 2.1 | FAIL (one label, one attribution) | Every formula correct against Montgomery 8e and AIAG MSA 4th ed.; every symbol defined; σ_within versus overall s stated; σ_total, pooled p̄, p-chart floor, R_sys = 1 − (1 − R_unit)² and the constant-λ assumption present. Slip: M1's 0.92 called "Cpk" in exercise 4.1 and its answer (it is Ppk). Slip: κ formula credited to landis-koch-1977; it is Cohen 1960. |
| 2.2 | PASS | All numbers in modules 00 to 07, solutions and the formula sheet match the script (describe, Pareto, distribution, cleanse, GRR, attribute, sample size, baseline, SPC, staged, capability, stratify, regression, FMEA, reliability, pilot). Rounding note: CI shown as 6.36210 where the script prints 6.3621. |
| 2.3 | QUESTION | Confirmed: Amd 1:2024; 2000 and 1987 dates; Shewhart 1931; Z1.1 to Z1.3; Deming 1950 and 1951; Juran 1954; Crosby 1979; Motorola 1986 and GE 1995; Baldrige 1987; Womack 1990; Kotter 1996; Shingo 1986; Landis and Koch 1977 with the quoted bands; AIAG kappa 0.75 and 0.40; AIAG-VDA 2019; the named ISO standards; the seven principles. Open: whether ISO 9001:2026 keeps the 2015 clause numbers (question 17). Wrong: "Dee's kappa of 0.71 passes the AIAG baseline comfortably" (blocking finding 3). Stale: `sources.md` still lists the deleted "+6 %" claim. |
| 2.4 | FAIL (one answer) | All exercise and skill-check answers recomputed correctly (94.2 %; 12.5 % and 4.2 %; machine means and SDs; M2 Pareto; CI; Dee's parts 3, 9, 15, 22, 23; n = 86; 0.92 and 1.42; 0.59 per day; shift means; 12 of 19 and 17 of 19; break-even 0.91 points; $60 edge gives $0.029 net; the ten capstone answers). Over-reach: exercise 3.1 (1) says Ben's offset grows with size; per-part excess is 0.0010 to 0.0043 mm with no trend. |
| 2.5 | PASS | Transform versus not (Wheeler); RPN versus Action Priority with the S ≥ 9 override; AIAG, Landis and Koch and the course bar on kappa; "check your customer" on GRR; the 1.5σ convention flagged; Cp versus Pp explained. |
| 2.6 | FAIL | Editions present for all 14 entries. "Cited in" out of step with the modules; stale "+6 %" line; ISO 9001:2026 and Cohen 1960 missing. Every Verified cell "no", as the rule requires until a person checks. |

## Trademarks and licences (run 2)

| Item | Verdict | Evidence |
|---|---|---|
| 3.1 | PASS | The standards map says it is descriptive and reproduces no text; each row is a number, a name and a one-line purpose. AIAG, AIAG-VDA, Landis and Koch and Kotter attributed by ID; two short guideline figures only. README states non-affiliation. No "official", "accredited", "approved" or "certified" wording about the project. |
| 3.2 | PASS | No belt names; certification language concerns ISO 9001 organisational certification only. |
| 3.3 | PASS (carried from run 1, figures unchanged) | 7 PNGs, all saved by `make_figures.py` and referenced from modules 02 to 05; no SVGs, logos or screenshots. |
| 3.4 | PASS | No copied tables or datasets; `sources.md` is a citation list; `tooling_cost.csv` is generated by the course script. |
| 3.5 | PASS | README ends with the licence line; requirements are permissively licensed (from general knowledge). |

## Structure and plain language (run 2)

Parser output: all 8 modules with a time (75 min, 3 h, 6 h × 5, 5 h) and a topic count; no hard prerequisites; 7 related courses resolved.

| Item | Verdict | Evidence |
|---|---|---|
| 4.1 | PASS | Exercises 1.1 to 6.1 present with answers in solutions; module 00 has exercise 0.1; module 07 has objectives, a project brief and a skill check. Worked examples in 02 to 06 each give dataset, steps, command, result and meaning; module 06 gives before, what changed, after; the tooling arithmetic recomputes by hand. Questions on modules 00 and 01 (question 25) and on the module 05 plot command (question 26). |
| 4.2 | PASS | README table has Time and Topics for all 8; every module has a matching Time line; sum 39.25 h. |
| 4.3 | PASS | Every link and image resolves; cross-course links use the full category form. |
| 4.4 | PASS | "Prerequisites: none." parses to no hard prerequisites. |
| 4.5 | QUESTION | Modules 02 and 04 read in full. Run 1's items fixed (USL and LSL, AIC, CI, quartiles, σ, x̄, μ glossed; Terms example; common and special cause defined before use; constants explained; "capable" before Cp). Remaining: questions 23 and 24. |
| 4.6 | PASS | 7 figures and 8 data files present with correct relative paths. |

## Run 1 record (2026-10-27)

Run 1 found 8 blocking findings, all fixed in PR #34: the README originality statement; the "12 deliberately borderline" count (now 9 of 30); the ISO 9001 edition wording plus a standards map; counter-positions on transforms (Wheeler) and FMEA (Action Priority) and the AIAG kappa baseline; exercises for modules 01 to 06; per-session times; the broken module 04 link and link form; the formula sheet with every symbol defined. Worked examples were rewritten as dataset, steps, command, result, meaning, with before, what changed, after for the pilot; the unsupported "+6 %" became a computation from `data/tooling_cost.csv`; KS values were labelled rough guides.

Run 1 questions and answers (Nidhin, 2026-10-27, numbers as in run 1):

1. ISO clause numbers and titles: acceptable; clause text stays out; add a map of the standards a quality engineer meets. Applied.
2. Kappa bands: state the AIAG baseline and why the course trains stricter. Applied.
3. ISO 9001:2026 published 16 September 2026: confirmed. Applied.
4. Tool cost: had no basis in any data; compute it from a cost table. Applied.
5. Before and after: tell the chain from dataset to steps to result to meaning. Applied; the rule is now in REVIEW.md 4.1.
6. KS p-values: name the dataset, walk the steps, label the values descriptive. Applied.
7. to 16. Chair's recommendations applied, pending confirmation: baseline measured before the MSA fixes (7); shift C wording (8); change model as the course's own condensation citing Kotter (9; see question 19); Bayline fictional, stated in the README (10; see question 18); real exercises with answers in solutions (11); full link form (12); glosses in modules 02 and 04 (13, 14); editions in the sources table (15); exercise answers in solutions, check-yourself answers inline (16).
