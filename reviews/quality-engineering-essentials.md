# Review: Quality Engineering Essentials

| | |
|---|---|
| Course | `courses/quality-operational-excellence/quality-engineering-essentials/` (8 modules, including the folded-in `00-foundations-of-quality.md` that covers the catalog's separate "Quality 101" topic) |
| Board run | 1 |
| Date | 2026-10-27 |
| State | blocked |
| Verified by | |

## Verdict summary

| Item | Verdict |
|---|---|
| 1.1 Nothing copied | PASS (19 quoted-sentence searches, no hits; module 07 and README not searched) |
| 1.2 Only public titles and outlines used | FAIL (documentation gap: the course README lacks the statement) |
| 1.3 No licensed data cards or standards text | PASS |
| 1.4 Fictional, seeded data | PASS |
| 1.5 Quotations short and attributed | PASS |
| 2.1 Formulas match a primary source | FAIL (formulas correct; symbols undefined, three ambiguities; raised by the human reviewer) |
| 2.2 Every number reproducible | FAIL (one mismatch) |
| 2.3 Claims current and cited | FAIL (ISO 9001 edition) |
| 2.4 Exercises answered correctly | PASS |
| 2.5 Disagreements presented fairly | FAIL |
| 3.1 Marks used descriptively | PASS |
| 3.2 Belt names describe content | PASS |
| 3.3 Figures are the course's own | PASS |
| 3.4 Third-party material licensed and attributed | PASS |
| 3.5 Licence statements present | PASS |
| 4.1 Module structure complete | FAIL (no exercises in modules 01 to 06) |
| 4.2 Syllabus complete with time and topics | FAIL (no per-module time) |
| 4.3 Links and images resolve | FAIL (one broken cross-course link) |
| 4.4 Prerequisites line parses | PASS |
| 4.5 Readable without a statistics background | QUESTION |
| 4.6 Figures and data files present | PASS |

## Blocking findings

Nothing copied, no licensed material, no trademark problem: the originality and trademark substance is clean. The one originality FAIL is a missing sentence, and the rest are content fixes. Each needs a `fix:` pull request and a re-run of the board.

1. **1.2, course README.** Add the statement REVIEW.md asks for where a course follows an outline's order: that only the public IISE course title and topic list were used, that module 00 covers the catalog's "Quality 101" topic the same way, and that the project is not affiliated with IISE.
2. **2.2, `modules/03-measurement-system-analysis.md:56`.** "30 inserts (12 deliberately borderline)": the generator (`tools/qekit.py:73`) draws borderline parts at random and seed 1924 gives 9. Say "about a quarter (9 of 30)" or make the generator deliberate.
3. **2.3, `modules/00-foundations-of-quality.md` and README.** "The current edition is ISO 9001:2015" is out of date: certification bodies (LRQA, NSF, DNV) report ISO 9001:2026 published 16 September 2026 with a three-year transition. Say that 9001:2015 (with Amd 1:2024) is the edition most organisations are certified to, that 9001:2026 is published, and re-check whether clauses 7.1.5, 7.5 and 10.2 keep their numbers. See question 3.
4. **2.5, modules 04 and 05.** Present the other side: (a) module 04 teaches a log transform for the individuals chart without Wheeler's position that XmR limits are robust and should not be transformed; (b) module 05 teaches RPN only while `further-reading.md` itself notes AIAG-VDA 2019 replaced RPN with Action Priority; (c) kappa bands are given without the competing AIAG figures (question 2).
5. **4.1, modules 01 to 06.** No exercise sections; 02 to 06 have only "Run it" command blocks and 01 has neither. Add a task per module that uses the data, or decide the "Run it" block is the exercise and say so (question 11).
6. **4.2, README sessions table.** No time column, and only module 00 has a `**Time:**` line. Add per-session times (the course total is 39 hours) so the syllabus and the site show them.
7. **4.3, `modules/04-process-behavior-and-capability.md:10`.** `../../charting-process-behavior/README.md` does not exist; the course is in `lean-six-sigma`, so the target is `../../../lean-six-sigma/charting-process-behavior/README.md`.

8. **2.1, `reference/formulas.md` (raised by the human reviewer on 2026-10-27).** The formulas are right but the sheet defines almost none of its symbols, and three lines are ambiguous without them. Add a symbol table or a definition line under each formula: MS_E, MS_PO, MS_O, MS_P (ANOVA mean squares for error, part-by-operator interaction, operator, part); MR̄, X̿, R̄ (average moving range, grand mean, average range); E, σ, z, p in the sample-size formulas; b₀, b₁ (intercept, coefficients); S, O, D with their 1 to 10 scales; p₁, p₂, n₁, n₂; Φ⁻¹ (inverse standard normal) and t(0.975, n − 1). Give σ_total = √(σ²_GRR + σ²_part) for %Study variation, p̄ = (x₁ + x₂)/(n₁ + n₂) for the z-test, n as the subgroup size and the zero floor for the p chart's lower limit. State that σ in Cp and Cpk is the within-subgroup (short-term) estimate and that Pp and Ppk use the overall s. Write the parallel formula as R_sys = 1 − (1 − R_unit)², and state that R(t) = e^(−t/MTBF) assumes a constant failure rate λ = 1/MTBF. The same check applies to formulas stated inside the modules.

## Questions for the human reviewer

1. **ISO 9001 clause titles.** `modules/00-foundations-of-quality.md:84-106` lists clause numbers and titles (4 to 10, 7.1.5, 7.5, 10.2) with paraphrased descriptions, and names the seven principles. Both the originality and trademark reviewers judged this fair descriptive use. *Resolved by:* a ruling that clause numbers and titles are allowed and clause text is not.
   - **Answer:** (2026-10-27, Nidhin) Name the dataset (`quote_turnaround.csv`, 120 quotes) and walk the steps: fit four candidate distributions, compare by AIC, treat the KS value as a rough check only (it is computed after fitting to the same data), then show what the choice does to the 95th percentile. Label the p-values as descriptive in the module and in the script output. (2026-10-27, Nidhin) The numbers are real and traceable (`production_sample.csv` for the problem, `pilot_results.csv` and `qekit.py pilot` for the proof, `pilot_daily.csv` and `qekit.py staged` for stability), but the module never tells the chain. Expand the worked example into: the situation before and the dataset that showed it; what changed (chiller, tool change at 1,600 parts, automatic wear offset); the dataset that measured the change; the command that computes the proof; what the result means; the staged chart as the picture of stability, with the small-count caveat. State that the after-phase daily counts in the generator are constructed for teaching. (2026-10-27, Nidhin, after the chair traced the number) The 6 % has no basis in any dataset or in `qekit.py`; `pilot_results.csv` holds only inspected and defective counts. Fix: add a small tooling-cost table to the data (cost per tool, parts per tool at 2,400 and 1,600, tooling share of cost per part) and compute the figure in the script, or state the assumption in the text. Preferred: in the data, so it is reproducible like everything else. (2026-10-27, Nidhin) Confirmed: ISO 9001:2026 was published on 16 September 2026. Module 00 and the README are to be reworded accordingly (blocking finding 3); the clause-number check for 7.1.5, 7.5 and 10.2 against the 2026 edition is part of that fix. (2026-10-27, Nidhin) Switch to the industry standard as the baseline: state the AIAG MSA figures and why that standard is the reference, then explain why this course trains at the stricter 0.9 / 0.7 bands. Both sets stay visible so the learner knows the standard and the course's reason for the tighter target. (2026-10-27, Nidhin) Yes: clause numbers and titles with paraphrased descriptions are acceptable; clause text stays out. Go further: college teaching rarely tells a new quality practitioner which standards they will actually meet, so module 00 should add a descriptive map of the standards a quality engineer encounters (ISO 9000 vocabulary, ISO 9001 requirements, ISO 19011 auditing, ISO/IEC 17025 laboratories, ISO 10012 measurement management, the sector schemes IATF 16949, AS9100 and ISO 13485, the statistical standards for sampling, control charts and capability, and ISO 31000 risk), each with one line on what it is for and when it applies. No clause text.
2. **Kappa bands.** `modules/03-measurement-system-analysis.md:66` gives ≥ 0.9 excellent, 0.7 to 0.9 acceptable, < 0.7 improve, attributed to "quality-practice convention". AIAG MSA 4th ed. is usually quoted as > 0.75 good and < 0.4 poor; Landis and Koch use 0.61 to 0.80 "substantial". *Resolved by:* a named source for the bands, or switching to AIAG's figures.
   - **Answer:**
3. **ISO 9001:2026.** The accuracy reviewer could not reach iso.org (403) and relied on LRQA, NSF and DNV. *Resolved by:* confirming the publication and transition dates at iso.org or the IAF, and whether clauses 7.1.5, 7.5 and 10.2 survive.
   - **Answer:**
4. **Tool cost +6 %.** `modules/06-corrective-actions.md:45` and `:84`: tool-change interval drops from about 2,400 to 1,600 parts, which is 50 % more tool use per part, yet cost rises 6 %. *Resolved by:* stating the basis (for example tooling as a share of conversion cost) or correcting the figure.
   - **Answer:**
5. **Staged p chart as evidence.** `modules/04:171-180` says the chart "shows the change was real", but the after-stage has about 0.6 expected defectives per subgroup, where 3-sigma limits are unreliable. *Resolved by:* citing the two-proportion z-test as the evidence, or adding the small-count caveat.
   - **Answer:**
6. **KS p-values.** `qekit.py:146` reports KS p-values with parameters fitted from the same data, which inflates them. *Resolved by:* a "descriptive only" note, or a Lilliefors-type correction.
   - **Answer:**
7. **Baseline timing.** `modules/03:85` says the baseline is "after the MSA fixes", but the data still carries Ben's bias and the module says to repeat the GRR after fixes. *Resolved by:* a sentence saying which it is.
   - **Answer:**
8. **Shift wording.** `modules/05:79` says coolant is "hotter on later shifts", but only shift C is hotter in the data. *Resolved by:* confirming the wording or changing it to shift C.
   - **Answer:**
9. **Change model source.** `modules/06:181-183` ("awareness, understanding, acceptance, commitment") has no named source and the author's note flags it as unverified. *Resolved by:* a citation (Kotter, ADKAR or similar) or reframing as the course's own model.
   - **Answer:**
10. **Bayline is fictional.** The trademark reviewer found no real firm; the originality reviewer confirmed the README marks it fictional. *Resolved by:* your confirmation.
    - **Answer:**
11. **Template for modules 01 to 06.** Module 00 alone has a time line and an exercise. Were 01 to 06 written to a different template, and should they get exercises and times (blocking findings 5 and 6), or are the "Run it" blocks the intended exercise? *Resolved by:* your decision.
    - **Answer:**
12. **Same-category link shorthand.** README:41 and `modules/04:10` use `../statistical-quality-control/README.md` for a same-category course; it resolves but does not follow the `../../<category>/<course>/README.md` form. *Resolved by:* a ruling on whether the shorthand is allowed.
    - **Answer:**
13. **Plain language in module 02.** Undefined on first use: USL, AIC, KS test p, CI, Q1/Q3, skewness, sigma, x-bar, mu; the "Terms" section is two bullets of bare symbols; line 75 is a 46-word sentence with "95th percentile" unexplained. *Resolved by:* confirming the glossary is meant to carry these, or adding inline glosses and a split sentence.
    - **Answer:**
14. **Plain language in module 04.** Common cause and special cause used before definition (line 12); chart-type table with no gloss (19); constants A2, D3, D4 given with no explanation (48); four sentences over 35 words (14, 44, 65, 74); Cp and Cpk formulas before any intuition of "capable", and "voice of the process / voice of the customer" with no gloss (65); "lognormal" and "ln(hours)" with only a back-reference (31). *Resolved by:* your call on which to gloss or reorder.
    - **Answer:**
15. **Further reading editions.** `reference/further-reading.md` names no editions and says it is "from general knowledge" and "not verified". *Resolved by:* adding editions, or accepting the list as pointers only.
    - **Answer:**
16. **Exercise answers location.** Every check-yourself answer lives inline in the modules; `solutions/README.md` holds only script results and facilitator notes, and exercise 0.1 has no model answer. *Resolved by:* accepting the inline convention, or moving answers to `solutions/`.
    - **Answer:**

## Not checked

- Board gap found on this run (worked examples): modules give the result and the command but not the chain from dataset to steps to result to meaning. REVIEW.md item 4.1 is being extended so a worked example must name its dataset (file, rows, columns), list the steps and the command, give the result, say what it means, and for a change show before, what changed, after.
- Board gap found on this run: the accuracy reviewer checked that formulas match a source but not that every symbol is defined where used; REVIEW.md item 2.1 and the reviewer's instructions are being extended so later runs check it.
- Originality: module 07 and the README were not searched; fewer than three sentence searches for modules 00, 01, 02, 04 and 06; the search tool returns summaries, so absence of a hit is weaker than a full-text check; IISE's own materials are not public and were not compared.
- Accuracy: figure images were not compared to the printed numbers; iso.org was unreachable; the 39-hour length claim and the templates were not checked; sibling-course links were not followed.
- Trademarks: pip package licences beyond general knowledge; pixel-level figure provenance; root LICENSE, NOTICE.md and REVIEW.md not opened; `qekit.py`, CSVs and templates not read in full.
- Structure: plain-language read done in full only for modules 02 and 04; `qekit.py` not run by this reviewer; reference, templates and solutions scanned for links only.

## Originality

| Item | Verdict | Evidence |
|---|---|---|
| 1.1 Nothing copied | PASS (with a limit on coverage; see Not checked) | 19 quoted-sentence web searches across modules 00 to 06 found no verbatim or lightly paraphrased hit on any third-party page. Module 07 and the README were not searched. |
| 1.2 Only public titles and outlines used | FAIL (documentation gap) | The course README does not say that only the public IISE title and topic list were used. It says "organized along the DMAIC improvement process" and its session table follows an outline order (00 to 07). Module 00 covers the catalog's separate "Quality 101" course, but nothing says so. The repo-root README (line 101) has the disclaimer; REVIEW.md line 10 requires the statement in the course that follows an outline's order. No wording implies IISE endorsement or affiliation. |
| 1.3 No licensed data cards or standards text | PASS | No MODAPTS, TMU, Z1.4, AQL, Minitab or Excel matches. ISO 9001 content (`modules/00:82-106`) is original plain-language prose giving clause numbers and titles and the seven principle names, with no clause wording quoted. Control-chart constants are public mathematical constants. Gauge R&R 10/30 % and ndc ≥ 5 guidance is attributed generically with "check your customer's requirements"; no AIAG table. FMEA gives the 1 to 10 scale in words only. |
| 1.4 Fictional, seeded data | PASS | `tools/qekit.py:31-32` defines `make_data(seed=1924)`; all CSVs are generated there and `solutions/README.md` states the seed. "Bayline Fasteners" is marked fictional in the README and module 01; a web search found no such company. Names are first names only; no addresses or part numbers. |
| 1.5 Quotations short and attributed | PASS | No quoted third-party prose. Deming and Juran paraphrases are short and attributed; books and dates are bibliographic facts. |

Searches run (quoted, all returned no source): module 00: "Quality practice changed each time somebody found a cheaper way to be right than inspecting everything afterwards"; "if the activity's output is a decision about a unit or a batch, it is control"; "A kaizen week with no follow-up is a demonstration, not a system"; "Certification shows that a conforming system exists and is followed. It does not show that any particular shipment is good"; "A department improves its own metric and pushes the cost to the next one". Module 01: "After 693 steps, fewer than half of the units are defect-free"; "Use them as a colleague to check, not an authority". Module 02: "Using the wrong distribution understates how long the slow quotes take". Module 03: "Reproducibility dominates" with "Ben reads about 0.002 mm high on every part"; "Calibration ensures accuracy against traceable standards at set intervals; it does not prove the gauge is precise enough for the job"; "The 1.5 sigma shift in sigma-level tables is a convention, not a law"; the Ana/Ben/Cai 10-part, 3-operator, 3-trial example. Module 04: "Both machines have similar spread" with "The problem is centering". Module 05: "Jumping from step 1 to a solution is the most common failure"; "Act on the highest RPNs" with "review any severity" and "regardless of RPN". Module 06: "Make errors impossible or immediately obvious, rather than relying on inspection or memory"; "dress micrometer anvils before each check"; the change-leadership wording. Case name: "Bayline Fasteners". The closest results were Minitab and SAS gauge R&R example pages and sigma-shift explainers; none shared sentence-level wording.

## Accuracy

Scripts run from a copy of the course folder in the scratchpad, in a venv built from `requirements.txt` (the system Python lacked scipy):

- `python -I tools/qekit.py data`: exit 0, about 3 s; regenerated `data/*.csv` byte-identical to the committed files.
- `python -I tools/qekit.py all`: exit 0; all 17 examples ran.
- `MPLBACKEND=Agg python -I tools/make_figures.py`: exit 0, about 8 s; images not compared pixel by pixel.

| Item | Verdict | Evidence |
|---|---|---|
| 2.1 Formulas match a primary source | PASS, with a documentation gap | Checked against Montgomery, *Introduction to Statistical Quality Control* (8th ed.), AIAG MSA 4th ed. and standard textbooks: I-chart limits x̄ ± 2.66·MR̄, MR UCL 3.267, n = 5 constants A₂ 0.577, D₃ 0, D₄ 2.114, p-chart limits, Cp/Cpk/Pp/Ppk, ANOVA variance components (`formulas.md:30-34`), ndc = ⌊1.41·σ_part/σ_GRR⌋, %Tol with 6σ (AIAG 4th ed.), kappa, sigma level, sample sizes, series and 1-of-2 reliability, pooled two-proportion z. All 12 module 07 answers recomputed and correct. `further-reading.md` names no editions and says it is "not verified". |
| 2.2 Every number reproducible | FAIL (1 mismatch) | Every other number in modules 00 to 07 and `solutions/README.md` matches the script: describe, Pareto, distribution/AIC/KS, cleanse, GRR (9.5 / 13.5 / 16.5 / 98.6, 23.7 %, ndc 8, p 0.003, operator means), attribute table, sample sizes, baseline (DPMO 16,667, 3.63, Ppk 0.577), I-MR limits (3.2 to 102.9 h), staged p chart, capability, stratification, regression, FMEA, reliability, pilot (z 11.53, CI 6.5 to 8.75). Mismatch: `modules/03:56` says "30 inserts (12 deliberately borderline)"; `qekit.py:73` draws `rng.uniform(size=30) < 0.25`, giving 9 with seed 1924, and the count is random, not deliberate. |
| 2.3 Claims current and cited | FAIL (1) plus questions | FAIL: `modules/00` says "The current edition is ISO 9001:2015"; LRQA, NSF and DNV report ISO 9001:2026 published 16 Sept 2026 with a three-year transition (iso.org returned 403). Confirmed correct: Shewhart 1924 and 1931; Dodge and Romig; War Standards Z1.1 to Z1.3; Deming 1950 and the 1951 Deming Prize; Juran 1954; Crosby 1979; Motorola 1986 and GE 1995; ISO 9000 and Baldrige 1987; *The Machine That Changed the World* 1990; the seven QM principles; QC/QA/QI wording (matches ISO 9000:2015); PDCA across clauses 4 to 10; risk-based thinking replacing preventive action; clauses 7.1.5, 7.5 and 10.2; the three-year certification cycle; the 8 wastes. Unsourced: kappa bands, the change model, "tool cost +6 %". |
| 2.4 Exercises answered correctly | PASS with notes | All check-yourself answers (00 to 06) and capstone Part B (1 to 10) are right: 0.995⁵⁰ = 77.8 %; 0.99²⁰ = 81.8 %; mean 6.3550, s 0.004743; n = 61.5 → 62; DPU 0.03, DPMO 10,000; Cp 1.25, Cpk 0.833; z = 4.41; MTBF 1,714 h. Notes: answers live inline in the modules, not in `solutions/`; exercise 0.1 is open-ended with no model answer; Part B answer 4 ("kappa 0.45, moderately better than chance") sits oddly beside the 0.7/0.9 bands taught in module 03. |
| 2.5 Disagreements presented fairly | FAIL | (a) `modules/04:163` teaches a log transform for the individuals chart and says I-MR charts are sensitive to non-normality, without Wheeler's position that XmR limits are robust and should not be transformed, or distribution-specific limits. (b) `modules/05:83-93` teaches RPN only although `further-reading.md` notes AIAG-VDA 2019 replaced RPN with Action Priority. (c) Kappa guidance gives one set of bands. Handled well: the 1.5σ shift is flagged as a convention, the 10/30 % GRR bands carry a "check your customer" caveat, Cp versus Pp is explained. |

Sources for the ISO 9001:2026 finding: [LRQA](https://www.lrqa.com/en-au/latest-news/iso-90012026-is-live-the-transition-period-has-begun/), [NSF](https://www.nsf.org/knowledge-library/iso-90012026-published-on-september-16-2026-what-quality-leaders-need-to-know), [DNV](https://www.dnv.com/ca/news/2026/ba_new-edition-of-the-quality-management-system-standard-iso-9001-released/).

## Trademarks and licences

| Item | Verdict | Evidence |
|---|---|---|
| 3.1 Marks used descriptively, no implied endorsement | PASS | Marks found: ISO 9001/9000/13485, IATF 16949, AS9100, Six Sigma, Lean Six Sigma, Motorola, GE, Toyota Production System, AIAG, VDA; all descriptive (for example `modules/00:84` "ISO 9001 is the international standard for a quality management system"). No IISE, ASQ, Minitab, JMP, Excel, MODAPTS, MTM, SAP, OSHA, ANSI, Shingo or Baldrige hits. No "official", "accredited by", "endorsed" or "affiliated" wording about the project; "accredited certification body" at `:104` describes how ISO certification works. ISO 9001 content is a paraphrase with clause numbers and titles; nothing quoted. |
| 3.2 Belt names describe content, not certification | PASS | No belt names appear. The only certification language is about ISO 9001 organisational certification, not course completion. |
| 3.3 Figures are the course's own, no logos or licensed screenshots | PASS | All 7 PNGs opened: matplotlib charts on the course's fictional data, no logos, screenshots or photographs. Each is saved by `tools/make_figures.py` (lines 46, 61, 76, 97, 116, 136, 163) and referenced in modules 02 to 05. No SVGs. |
| 3.4 Included third-party material openly licensed and attributed | PASS | No "Source:", "Adapted from", "Courtesy of" or copyright markers. Data and templates are course-generated and fictional. `further-reading.md` lists citations only. The AIAG 10/30 % and ndc ≥ 5 guidelines and the kappa bands are rules of thumb cited by name only. |
| 3.5 Licence statements present | PASS | README ends with the content CC BY 4.0, code MIT line. `requirements.txt` lists numpy, scipy, pandas, statsmodels and matplotlib, all permissively licensed (not checked against package metadata). |

## Structure and plain language

Parser output (`course_info`):

```
Foundations of quality |  | topics 6
Introduction to quality engineering |  | topics 7
Measurement and basic statistics |  | topics 9
Measurement system analysis |  | topics 9
Process behavior and capability |  | topics 9
Analyzing root cause |  | topics 10
Corrective actions and control |  | topics 9
Capstone and skill check |  | topics 2
prereq []
related [7 courses, all resolved]
```

| Item | Verdict | Evidence |
|---|---|---|
| 4.1 Every module has objectives, concept, worked example, exercise, check yourself | FAIL | Exercise: only module 00 has one (`modules/00:108`, "Exercise 0.1"). Modules 02 to 06 have only a "Run it" block of `python tools/qekit.py` commands (02:91, 03:98, 04:76, 05:109, 06:74); module 01 has neither. Objectives: 07 has none (likely exempt as the capstone). Worked example: 00 has no worked case; 01 has the charter table; 02 to 06 embed the Bayline results under concept headings, which is acceptable. Check yourself: 07 has "Part B, Skill check". |
| 4.2 Syllabus lists every module with time and topics | FAIL | The README "Sessions" table (lines 38 to 47) has `# / Session / Topics` and no time column; the parser gives an empty time for all 8 rows. Only `modules/00:3` has a `**Time:** 75 min` line. README line 30 gives a 39-hour total only. All 8 module files are listed in order. |
| 4.3 Every link and image path resolves | FAIL | `modules/04:10` targets `../../charting-process-behavior/README.md`, which does not exist; the course lives in `courses/lean-six-sigma/`. Every other link and image resolves. |
| 4.4 Prerequisites line parses as intended | PASS | README:31 `**Prerequisites:** none.`; parser gives no hard prerequisites and 7 related courses from the "Related courses" section. |
| 4.5 Readable without a statistics background | QUESTION | Modules 02 and 04 read in full; see questions 13 and 14. No module is unreadable as a whole. |
| 4.6 Figures and data files present | PASS | All 7 referenced figures exist in `figures/` with `../figures/` paths; all 5 referenced data files exist in `data/`. |
