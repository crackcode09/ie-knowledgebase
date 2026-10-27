## 2026-10-26 — Plan: Port the playbook "warm terminal" design and add an on-site course reader

### Status: COMPLETE (pending merge of PRs #4, #5, #6)

### What is being built or changed
- Restyle the site (catalog, learning path, mind map, drawer) with the design system from `D:\nidhin.dev\my-claude.md`: warm terminal palette, Space Grotesk / Inter / JetBrains Mono, editor-style top bar, hero with status pill, reading progress bar, reduced-motion support. Light and dark variants.
- Add a course reader so courses and modules are read on the site instead of on GitHub: sticky module TOC, prev/next, mark-done, Raw/Copy, "Open on GitHub".
- Polish: keyboard navigation, print styles, module-level progress feeding the path and mind map.

### Files to be created or modified
- `tools/roadmap_template.html` — theme, header, hero, theme toggle, progress bar (PR 1); reader wiring (PR 2)
- `tools/roadmap_graph.py` — copy course markdown and figures into `docs/courses/` and emit course/module pages (PR 2)
- `docs/index.html`, `docs/courses/**` — generated output
- `README.md` — regenerate instructions

### Implementation steps
1. PR `feat/warm-theme`: tokens, fonts, top bar, hero, cards, drawer, progress bar, light/dark toggle. Verify all three tabs and drawer in headless Chrome.
2. PR `feat/course-reader`: generator copies markdown and figures; reader page renders with marked (cdnjs) and lazy Mermaid; module pages with prev/next and done ticks.
3. PR `feat/reader-polish`: keyboard nav, print styles, module-level progress.

### Assumptions & decisions
- Light and dark both; dark follows the playbook palette, light is a derived warm cream palette.
- CDN use (cdnjs) is acceptable on GitHub Pages; Mermaid loads only on pages that contain a diagram.
- Warm theme, not PBC brand colours: the knowledgebase is a personal open-source site.

### Questions for user
- None outstanding; defaults above applied after "okay".

### Outcome (filled in after completion)
- PR #4 `feat/warm-theme`: tokens, fonts, top bar, hero, progress bar, light/dark toggle; all views restyled.
- PR #5 `feat/course-reader`: `docs/course.html` reader with module nav, pager, done ticks, Raw/Copy, Mermaid; generator copies courses into `docs/courses/`; drawer links to the reader.
- PR #6 `feat/reader-polish`: module-level progress on cards and in the drawer, `/` focuses search, arrow keys / `d` / `r` in the reader, print stylesheet.
- Deviation: print output was generated but not visually verified (no PDF renderer on this machine).


## [2026-10-27] — Plan: Legal pages and content verification gate

### Status: COMPLETE

### What is being built or changed
- Privacy Policy and Terms of Use pages on the site, generated from `tools/legal/*.html` through `tools/legal_template.html`, with footer links on every page.
- An originality and affiliation notice (site and `NOTICE.md`): not affiliated with IISE; only public course titles and topic outlines used as a coverage map; all content original and AI-assisted; trademarks descriptive only; takedown path.
- A verification gate: every course has a status cell (`draft` or `verified (Name, YYYY-MM-DD)`) read by the generator; draft courses show a badge on the catalog card, a pill in the drawer and a banner in the reader; the hero shows "n of N courses verified" and a preview-release notice. `REVIEW.md` is the checklist a reviewer signs.

### Files to be created or modified
- `tools/legal_template.html`, `tools/legal/privacy.html`, `tools/legal/terms.html` — page shell and bodies
- `tools/roadmap_graph.py` — status column, verified count, legal page rendering
- `tools/roadmap_template.html`, `tools/reader_template.html` — badges, banners, footer links
- `README.md`, `courses/*/README.md` — status cells `v1.0` → `draft`; README legal section
- `NOTICE.md`, `REVIEW.md`, `CONTRIBUTING.md` — notice, checklist, contributor rules

### Implementation steps
1. Generator reads the status cell and emits `verified`/`review` per course and a `verified` total.
2. Templates show the status; legal shell and bodies written; generator renders them into `public/`.
3. All status cells set to `draft`; docs updated; site regenerated and checked in headless Chrome.

### Assumptions & decisions
- Operator named as "IE Knowledgebase contributors" with GitHub issues as the contact channel; no governing-law clause.
- All 28 courses start as `draft`; none has been through the checklist yet.
- Plain-language wording with an explicit "not legal advice" line.

### Outcome (filled in after completion)
- Delivered as described in one PR. Course placement script now writes `draft` for new rows.

## [2026-10-27] — Plan: Site review and fixes (code, accessibility, layout)
## [2026-10-27] — Plan: Course review board

### Status: COMPLETE

### What is being built or changed
- Three independent reviews of the site build (generator, catalog page, reader page) plus a design pass at phone and laptop widths; every confirmed finding fixed in one branch.

### Files to be created or modified
- `tools/roadmap_template.html` — reset clears module progress; safe hash decoding; D3-missing guard; drawer hidden from the tab order when closed, focus moved in and restored; focus and collapsed categories survive re-renders; open drawer re-renders on ticks; cards are articles with a fixed header row (status tag left, tick right) and Enter/Space handling; tick `aria-pressed`; learning path grouped by category inside each level; mind map keyboard access, selection cleared on close, modules kept visible when a course is selected, colours follow the theme, search applied on first open; tabs with `aria-controls`, panels, arrow keys; shareable hash kept in sync; compact status pill under 1400px; phone layout; light palette darkened to pass AA; D3 with SRI.
- `tools/reader_template.html` — unknown slug handled; anchors kept on cross-course and GitHub links; GitHub-style heading ids with de-duplication; renderer and fetch errors separated; Mermaid with error handling and in-place theme re-render; print hides chrome and wraps code; shortcuts ignore repeats, modifiers and editable targets; un-marking a module un-marks the course; `aria-pressed`, `aria-current`, `role=status`, skip link; tables wrapped instead of `display:block`; query strings stripped from links; raw download for binaries; marked and Mermaid with SRI.
- `tools/roadmap_graph.py` — stray `##` sections no longer attach to a category; titles keep em dashes; folded items use the last link; SVG labels escaped; prerequisite lines matched only when they start with "Prerequisites"; links leaving the repo skipped; self-links dropped; missing course README or duplicate ids abort the run; LF output on Windows; template placeholders verified; `<!--` escaped in the JSON.
- `tools/legal_template.html`, `tools/legal/*.html` — nav semantics for the in-page contents; palette tokens.

### Implementation steps
1. Reviews (three agents) and screenshots at 360/1024/1280 in both themes.
2. Patch all three templates and the generator from the verified findings.
3. Regenerate; syntax-check the embedded scripts with node; re-screenshot every view, including phone width through a 360px iframe; recompute contrast ratios.

### Assumptions & decisions
- Node ids keep their current scheme (URLs stay stable); duplicates are now an error instead of a silent collision.
- The warm-terminal identity stays; only token values changed to meet contrast.
- Locked cards stay de-emphasised at 70% opacity rather than 55%.

### Outcome (filled in after completion)
- Delivered as one PR. Typography readability research runs separately and lands as its own PR.
- A multi-agent review board that runs REVIEW.md against one course: four specialist reviewers in parallel (originality, accuracy, trademarks and licences, structure and plain language), a chair that consolidates PASS / FAIL / QUESTION verdicts into `reviews/<slug>.md`, and a question round where the human reviewer answers doubts. Sign-off is a separate, human-gated step that flips the status cells and opens a `review:` PR.

### Files to be created or modified
- `.claude/agents/review-originality.md`, `review-accuracy.md`, `review-trademarks.md`, `review-structure.md` — reviewer definitions (read-only, evidence-based output format)
- `.claude/skills/review-course/SKILL.md` — the chair: locate, brief, run in parallel, consolidate, ask, sign off
- `reviews/README.md`, `reviews/_template.md` — report conventions and layout
- `REVIEW.md`, `README.md` — pointers to the board

### Implementation steps
1. Write reviewer agents with narrow checklists mapped to REVIEW.md sections, each returning the same table shape.
2. Write the chair skill with explicit preconditions for sign-off.
3. First run on one course the owner knows well, to judge the report format before running across all courses.

### Assumptions & decisions
- Reviewers never edit the repo; the chair edits only the report until sign-off.
- A FAIL in originality or trademarks blocks outright, mirroring REVIEW.md section 5.
- Based on the Karpathy guideline ideas (state assumptions, surface doubts, verifiable criteria), not on a specific framework.

### Outcome (filled in after completion)
- Delivered as one PR. First run pending the owner's choice of course.
