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

## [2026-10-27] — Plan: Sources tables and the Sources page
## [2026-10-27] — Plan: Quality Engineering Essentials, fixes from board run 1
## [2026-10-27] — Plan: Role profiles data and the /map-course command

### Status: COMPLETE

### What is being built or changed
- One source of truth per course, `reference/sources.md` (columns ID, Source, Used for, Cited in, Verified), cited from modules by ID; a reviewer flips Verified. The generator reads every table into the model, shows a verified count in the course drawer, and builds `public/sources.html`: a site-level section (IISE catalog as a map only, O*NET, BLS, Bootstrap Icons, CDN libraries, fonts) followed by every course's table. Footer link on every page.

### Files to be created or modified
- `tools/roadmap_graph.py` — `course_sources`, `SITE_SOURCES`, `sources_page`, course node `sources`
- `tools/roadmap_template.html`, `tools/reader_template.html`, `tools/legal_template.html` — drawer count, footer links, table code style
- `courses/quality-operational-excellence/quality-engineering-essentials/reference/sources.md` — first converted course (replaces further-reading.md)
- `CONTRIBUTING.md`, `REVIEW.md`, `.claude/agents/review-accuracy.md` — citation rule, checklist items for the table and for symbol definitions

### Implementation steps
1. Define the table format and convert Quality Engineering Essentials.
2. Parse tables in the generator; render the global page through the legal shell; add the drawer count and footer links.
3. Extend REVIEW.md and the accuracy reviewer so every run checks the table and symbol definitions.

### Assumptions & decisions
- Courses without a table keep their further-reading list; the Sources page says so. Conversion of the other 31 happens as each goes through the board.
- Verified stays `no` until a human reviewer checks an entry; the board reports what it could confirm but does not flip it.

### Outcome (filled in after completion)
- Delivered as one PR; QEE shows 14 entries, 0 verified, pending its review.
- Every blocking finding and every chair recommendation from `reviews/quality-engineering-essentials.md` applied to the course: originality statement and fictional-data line in the README; corrected borderline count; ISO 9001:2026 wording and a descriptive map of the standards a quality engineer meets; AIAG baseline beside the course's stricter kappa bar; Wheeler's position on transforms and Action Priority beside RPN; real exercises for modules 01 to 06 with answers in solutions; per-session times; fixed and standardised cross-course links; formula sheet with every symbol defined; worked examples rewritten as dataset, steps, command, result, meaning, with before, what changed, after for the pilot; tooling cost computed from a new data file instead of an unsupported figure; KS values labelled as rough guides; shift-C coolant wording; Kotter cited for the change model.

### Files to be created or modified
- `courses/quality-operational-excellence/quality-engineering-essentials/` README, modules 00 to 07, `reference/formulas.md`, `solutions/README.md`, `tools/qekit.py`, `data/tooling_cost.csv`
- `tools/roadmap_graph.py` — syllabus header detection requires a separator row and a module link (reviewer finding 12b surfaced by the new datasets table)

### Implementation steps
1. Rewrite modules 02 to 06 and the formula sheet; patch 00, 01, 03, 07; extend the script and regenerate data.
2. Rerun `qekit.py all` and `make_figures.py`, check every number in the text against the output, check links and the site parser.
3. Open the fix PR; re-run the review board on the merged result.

### Assumptions & decisions
- Chair recommendations for questions 7 to 16 applied as answered, pending the owner's confirmation after the re-run.
- Figure PNGs left as committed (regeneration is byte-different but visually identical).

### Outcome (filled in after completion)
- Delivered as one PR; board re-run pending.
- Versioned O*NET occupation profiles vendored under `roles/onet/` (eight codes around industrial engineering), built from the official 31.0 CSV files by `tools/onet_refresh.py` with the release version, download date and CC BY 4.0 attribution stamped on each file.
- A `/map-course <slug>` command (chair skill plus a read-only `map-relevance` agent) that maps a course onto the profiles its README declares: covered and touched elements with quoted evidence, high-importance elements not reached, content the standard does not name (dated), run twice with the differences reported. Output to `roles/mappings/<slug>.md`, every row proposed until a person confirms it. Advisory only: not a review-board gate and nothing reaches the site.
- Courses declare roles with a `**Roles:**` line in the README; Quality Engineering Essentials is the first.

### Files to be created or modified
- `tools/onet_refresh.py`, `roles/onet/codes.txt`, `roles/onet/<code>.md|.json`, `roles/README.md`, `roles/mappings/_template.md`
- `.claude/agents/map-relevance.md`, `.claude/skills/map-course/SKILL.md`
- `courses/.../quality-engineering-essentials/README.md` (Roles line), `NOTICE.md` (O*NET attribution)

### Implementation steps
1. Download the 31.0 CSV files, extract the listed codes, write the profiles.
2. Write the agent and the chair skill with the double-run stability check.
3. First map on Quality Engineering Essentials.

### Assumptions & decisions
- Decided after a three-pass red team: separate command rather than a fifth board member, so verification keeps moving; evidence-quoted, human-confirmed rows; "not in the standard" is dated information, never a defect; data from the official bulk files, never scraped.
- O*NET 31.0 at the time of writing; refresh quarterly and review the diff.

### Outcome (filled in after completion)
- Delivered. First map run on Quality Engineering Essentials (two runs, consolidated, 17 differing rows, 10 questions) at `roles/mappings/quality-engineering-essentials.md`, state proposed.

## [2026-10-28] — Plan: Fix site review findings 1–4 and 6–9

### Status: COMPLETE

### What is being built or changed
- Eight bugs from a code review of the two site templates: mind-map springs, drawer focus, repeated D3 notice, search on the Learning path tab, a reader error on an unknown course, course-done rules that disagreed between the two pages, in-course link resolution, and repeated Mermaid failure notices.

### Files to be created or modified
- `tools/roadmap_template.html` — fixes 1–4 and the catalog half of 7
- `tools/reader_template.html` — fixes 6–9
- `public/index.html`, `public/course.html` — regenerated

### Implementation steps
1. Patch both templates; regenerate with `python tools/roadmap_graph.py`.
2. Syntax-check the embedded scripts with node.
3. Exercise each fix in the browser pane at 1280 px.

### Assumptions & decisions
- One course-done rule on both pages: ticking the last module marks the course done; unticking a module from a full set un-marks it; a course marked done by hand otherwise stays done.
- Findings 5 (sanitise reader HTML), 10 (SRI for anime.js), 11 (icon placeholders inside the data) and 12 (track source URL scheme) are left for a later change.

### Questions for user
- None.

### Outcome (filled in after completion)
- All eight fixed. Verified in the browser: drawer focus and course-done rule (2, 7), search switches to the catalog (4), one D3 notice after repeated tab clicks and resizes (3), no error on an unknown course (6), reader course-done rule in all three cases (7), one Mermaid notice per diagram after four theme switches (9). Fix 8 checked in node against the template's own `resolve()`. Fix 1 (animation springs) could not be checked in the browser: the pane was hidden, so animation frames did not run.
