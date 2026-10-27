---
name: map-course
description: Map one course onto the O*NET occupation profiles it declares and write roles/mappings/<slug>.md - which rated elements of the role the course covers or touches, with quoted evidence, which high-importance elements it does not reach, and which content the standard does not name. Runs the mapping twice and reports the differences. Advisory only; rows stay "proposed" until a person confirms them. Use when asked to map a course to a role, check a course against O*NET, or when someone types /map-course <slug>.
---

# Map a course to its roles

You are the chair. The argument is a course slug (the folder name under `courses/<category>/`). Work from the repository root. This command is advisory: it never changes a course, never blocks the review board, and never puts anything on the site. It produces the proposed course-to-role map that a person confirms, which stage 3 of the roadmap (role profiles) is built from.

## 1. Locate and brief

1. Find the course: `courses/*/<slug>/README.md`. If it does not exist, say so and stop.
2. Read the README's `**Roles:**` line. Each code there must have a profile at `roles/onet/<code>.md`; if one is missing, run `python tools/onet_refresh.py <code>` (it needs network access) or say it is missing and continue without it. If there is no Roles line, use `17-2112.00` and record that it was the default.
3. Read `roles/README.md` so the brief matches the rules there. Note whether `roles/mappings/<slug>.md` exists (a re-map builds on it; read it and carry confirmed rows forward unchanged).
4. State in one line what you are about to run, the course folder and the profiles.

## 2. Run the mapping twice

Launch two `Agent` calls in one response, both with `subagent_type: map-relevance`, identical briefs: the absolute course folder, the absolute paths of the profile files, the O*NET version and download date from the profile headers, and the line "Read-only. Return only the output format in your agent definition." Two runs with the same brief show how stable the judgments are; do not merge them yourself before both return.

## 3. Consolidate

Write `roles/mappings/<slug>.md` from `roles/mappings/_template.md`:

- Header: course, roles (and whether the default was used), O*NET release and date, mapping run number, date, state `proposed` (or `partly confirmed` on a re-map that kept confirmed rows), confirmed by (blank).
- **Coverage:** the union of both runs' coverage rows. Where the runs agree, one row, status `proposed`. Where they disagree on the coverage call, take the weaker call (touches over covers), status `proposed`, and list the row under Differences. A row that appears in only one run is kept with the weaker reading and listed under Differences.
- **High-importance elements not reached:** elements of importance 3.0 or higher that neither run covered or touched.
- **Content the standard does not name:** union of both runs, each line dated with the O*NET version.
- **Differences:** every row where the runs disagreed, with the chair's reading in one line.
- **Summary** counts, with stability as the number of differing rows.
- **Questions for the human reviewer:** every question from either run, plus one for each difference that the chair could not settle from the evidence.

Then tell the human, in a short message: the counts, the stability, the top three high-importance gaps, and the questions as a numbered list. Record their answers in the file with the date; when they confirm rows, change those rows' status to `confirmed` and the file's state accordingly, and add their name under "Confirmed by".

## Rules

- Advisory only. A gap is information about the course's scope, not a defect; "not in the standard" is information about the standard, dated.
- Every coverage row carries a quote; drop any row without one.
- Nothing from a mapping goes to the site, the course, the catalog tables or the review report. Confirmed maps are the input to stage 3 of the roadmap, which has its own plan.
- Commit maps on a branch named `map/<slug>` and open a pull request titled `map: <course title>`; never commit to `main`.
