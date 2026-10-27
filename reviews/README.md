# Course review reports

One report per course, written by the course review board (`/review-course <slug>` in Claude Code, defined under `.claude/skills/review-course/` with the four reviewer agents under `.claude/agents/`). The board checks a course against [REVIEW.md](../REVIEW.md) in four parallel passes (originality, accuracy, trademarks and licences, structure and plain language), consolidates the findings here, and lists every doubt as a numbered question for the human reviewer.

The board never verifies a course by itself. A course becomes `verified` only when a named person has answered the questions, no FAIL remains, and they sign off; the board then opens a `review: verify <course>` pull request that flips the status cells.

| State | Meaning |
|---|---|
| `open questions` | the board ran; the human reviewer has questions to answer |
| `blocked` | at least one FAIL; fix the content in its own PR, then re-run |
| `ready for sign-off` | no FAIL, every question answered; waiting for the human's name and go |
| `verified` | signed off; the status cells in the catalog tables carry the name and date |

Reports are plain Markdown so they can be read on GitHub. Use `_template.md` for the layout. Do not edit a report by hand except to record an answer to a question.
