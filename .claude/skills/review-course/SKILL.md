---
name: review-course
description: Run the course review board on one course - four specialist reviewers (originality, accuracy, trademarks, structure) in parallel, a chair that consolidates their findings into reviews/<slug>.md, and a question round where the human reviewer rides along and answers doubts. Never flips a course's status by itself. Use when asked to review, verify or audit a course, or when someone types /review-course <slug>.
---

# Course review board

You are the chair. The argument is a course slug (the folder name under `courses/<category>/`), optionally followed by `--sign-off` once the human reviewer has answered every question. Work from the repository root.

The board exists because every course was written with AI assistance and is `draft` until a person has verified it against [REVIEW.md](../../../REVIEW.md). The board does the legwork; the person decides. You never change a status cell unless the human reviewer has said, in this conversation, that the course is verified and under what name.

## 1. Locate and brief

1. Find the course: `courses/*/<slug>/README.md`. If it does not exist, say so and stop.
2. Read `REVIEW.md` and the course README so the brief is accurate. Note the course's category, module count, scripts under `tools/` and whether `reviews/<slug>.md` already exists (a re-review builds on it; read it).
3. State in one line what you are about to run and the absolute path of the course folder.

## 2. Run the four reviewers in parallel

In one response, launch four `Agent` calls with `subagent_type` set to `review-originality`, `review-accuracy`, `review-trademarks` and `review-structure`. Each brief must contain:

- the absolute course folder path and the README path relative to the repo root;
- the scratchpad directory for any scratch files (never the repo);
- the line "Read-only. Return only the output format in your agent definition.";
- for a re-review, the previous report's open questions and the human's answers, so the reviewer can confirm what changed.

Do not run the checks yourself while they run, and do not summarise results before all four have returned. If a reviewer fails or returns nothing, say so in the report under "Not checked" rather than filling in.

## 3. Consolidate into the report

Write `reviews/<slug>.md` from `reviews/_template.md`:

- Header: course title, path, date, board run number, overall state (`open questions`, `blocked`, or `ready for sign-off`).
- The four sections exactly as the reviewers returned them (their tables, questions and "Not checked" lists), under the headings Originality, Accuracy, Trademarks and licences, Structure and plain language.
- **Verdict summary:** one table, one row per checklist item, PASS / FAIL / QUESTION / NOT CHECKED.
- **Blocking findings:** any FAIL in Originality or Trademarks blocks verification outright (REVIEW.md section 5). Any FAIL in Accuracy or Structure blocks until fixed. List them with the fix each needs.
- **Questions for the human reviewer:** every QUESTION from every reviewer, numbered, each with the reviewer's evidence and the answer that would resolve it. This is the ride-along section.
- **Not checked:** merged list.

Then, in the conversation, give the human a short summary (state, number of blocking findings, number of questions) and ask the questions one at a time or as a numbered list. Record each answer in the report under the question, with the date. Do not argue with an answer; if an answer contradicts evidence, say so once with the evidence and record the human's final decision.

If there are blocking findings, the state is `blocked`. Fixing content is a separate task: offer it, but keep the fix in its own `fix:` pull request, and re-run the board afterwards (`/review-course <slug>` again) so the report reflects the fixed course.

## 4. Sign-off (only with `--sign-off`, and only when the human has said so)

Preconditions, all required: no FAIL remains, every question has a recorded answer, the human reviewer has given their name in this conversation, and the human did not write the course. If any is missing, say which and stop.

Then:

1. Add to the course README, under the title block: `**Status:** verified by <Name> on <YYYY-MM-DD>. <one line on scope from the report>`.
2. Change the status cell from `draft` to `verified (<Name>, <YYYY-MM-DD>)` in the root `README.md` and the category `README.md`.
3. Set the report's state to `verified` with the name and date.
4. Run `python tools/roadmap_graph.py`.
5. On a branch `review/<slug>` from `main`, commit the course README, both catalog READMEs, `public/`, and `reviews/<slug>.md`, push, and open a pull request titled `review: verify <course title>` whose body is the verdict summary table and the list of answered questions. Never commit directly to `main`.

## Rules

- Reviewers are read-only; the chair edits only `reviews/<slug>.md` until sign-off.
- Never mark PASS for something no reviewer checked.
- Keep the report in plain language; a future reader should understand why the course was verified without re-running the board.
- One course per run. For several, run them one after another and keep separate reports.
