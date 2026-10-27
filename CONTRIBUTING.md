# Contributing

Improvements are welcome: corrections, clearer explanations, new exercises, real (anonymized) datasets, translations.

## Rules

1. **Every number must be reproducible.** If you change a dataset or worked example, rerun that course's `tools/make_data.py`, `tools/make_figures.py` and its analysis script (`tools/spc.py`, `tools/htest.py`, …), and update the module text and `solutions/README.md` to match.
2. **Cite primary sources** for any non-obvious claim (see `reference/further-reading.md`). Where authorities disagree (e.g., transforming data before charting), present both positions.
3. **Original content only.** Don't paste text, figures or exercises from copyrighted courses or books. In particular, nothing from IISE course material: we use only the public catalog's course titles and topic lists as a map of what to cover (see [NOTICE.md](NOTICE.md)). No official MODAPTS or MTM data cards, no standards text; use a simplified teaching version and say so.
4. **Plain language.** Write for someone on the shop floor with no statistics background; put the math in tables.
5. **Each module keeps the same structure:** objectives → concept → worked example → exercise → check yourself.
6. **Every course starts as `draft`.** The status cell in the catalog tables stays `draft` until a reviewer who did not write the course completes [REVIEW.md](REVIEW.md) and changes it to `verified (Name, YYYY-MM-DD)` in a `review:` pull request. Nothing is distributed as final before that.

## Layout

Courses live under `courses/<category>/<course>/`. The categories mirror the IISE course catalog (Lean & Six Sigma, Quality & Operational Excellence, Work Design & Work Measurement, …), plus categories added for subjects the catalog does not cover (Operations Research & Decision Analysis); each category folder has a README listing its courses. A new course goes in the category that fits and gets a row in both that README and the root README.

## Site templates

One width per column: inside the reader document, the catalog page and the legal pages, prose, tables, code and figures share the same right edge. Set the width once on the column (`.doc`, `.page`, `main`) and never on the text inside it; `python tools/roadmap_graph.py` refuses to build if a rule narrows content inside a column.

## Workflow

Fork → branch → pull request. Run any checks the course ships (e.g. `python tools/check_constants.py` in Charting Process Behavior) before submitting changes to its tools.
