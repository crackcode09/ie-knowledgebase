# Contributing

Improvements are welcome: corrections, clearer explanations, new exercises, real (anonymized) datasets, translations.

## Rules

1. **Every number must be reproducible.** If you change a dataset or worked example, rerun `tools/make_data.py`, `tools/make_figures.py` and the relevant `tools/spc.py` command, and update the module text and `solutions/README.md` to match.
2. **Cite primary sources** for any non-obvious claim (see `reference/further-reading.md`). Where authorities disagree (e.g., transforming data before charting), present both positions.
3. **Original content only.** Don't paste text, figures or exercises from copyrighted courses or books.
4. **Plain language.** Write for someone on the shop floor with no statistics background; put the math in tables.
5. **Each module keeps the same structure:** objectives → concept → worked example → exercise → check yourself.

## Workflow

Fork → branch → pull request. Run `python tools/check_constants.py` before submitting changes to `tools/spc.py`.
