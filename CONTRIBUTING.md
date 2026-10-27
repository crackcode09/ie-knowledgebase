# Contributing

Improvements are welcome: corrections, clearer explanations, new exercises, real (anonymized) datasets, translations.

## Rules

1. **Every number must be reproducible.** If you change a dataset or worked example, rerun that course's `tools/make_data.py`, `tools/make_figures.py` and its analysis script (`tools/spc.py`, `tools/htest.py`, …), and update the module text and `solutions/README.md` to match.
2. **Cite primary sources** for any non-obvious claim (see `reference/further-reading.md`). Where authorities disagree (e.g., transforming data before charting), present both positions.
3. **Original content only.** Don't paste text, figures or exercises from copyrighted courses or books.
4. **Plain language.** Write for someone on the shop floor with no statistics background; put the math in tables.
5. **Each module keeps the same structure:** objectives → concept → worked example → exercise → check yourself.

## Layout

Courses live under `courses/<category>/<course>/`. The categories mirror the IISE course catalog (Lean & Six Sigma, Quality & Operational Excellence, Work Design & Work Measurement, …), plus categories added for subjects the catalog does not cover (Operations Research & Decision Analysis); each category folder has a README listing its courses. A new course goes in the category that fits and gets a row in both that README and the root README.

## Workflow

Fork → branch → pull request. Run any checks the course ships (e.g. `python tools/check_constants.py` in Charting Process Behavior) before submitting changes to its tools.
