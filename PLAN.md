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
