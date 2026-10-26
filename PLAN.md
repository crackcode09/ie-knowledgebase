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

