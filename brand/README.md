# The IE Hub brand kit

Logo files, fonts and social image templates for The IE Hub. The design system (tokens, usage rules, previews) is the
reference for how to use them; this folder holds the files.

## Logo

| File | Use |
|---|---|
| `logo/the-ie-hub-A-on-dark.svg`, `…-on-light.svg` | **Primary logo**: the `>ie` mark beside the wordmark. `on-dark` on `#1f1d18`, `on-light` on `#faf6ee`. |
| `logo/the-ie-hub-B-on-dark.svg`, `…-on-light.svg` | Wordmark only, where the mark is already on screen. |
| `logo/mark-dark.svg` | The mark: tile `#d97757`, glyphs `#1f1d18`. 24 px and up. |
| `logo/mark-light.svg` | The mark on the light theme: tile `#b0532f`, **white** glyphs `#faf6ee`. |
| `logo/mark-white.svg` | Glyphs only, pure white, no tile: for photos and accent grounds. |
| `logo/favicon.svg` | The mark fitted to 16 px (every edge on a whole pixel), colours from `prefers-color-scheme`. Copied to `public/favicon.svg`. |
| `logo/*-1024.png`, `*-400.png`, `*@3x.png` | Rasters. `mark-*-400.png` is full-bleed (no rounded corners) for profile pictures, which platforms crop themselves. |

The mark is the large `>ie` design (32-unit grid, 3-unit strokes, tile corners 6/32). At 16 px those strokes fall on
half pixels and blur, so `favicon.svg` and `public/favicon-16.png` use a pixel-fitted drawing of the same mark; every
size from 32 px up uses the large design. The wordmark letters are outlined paths, so the files need no fonts.

The site header does not load these files: `tools/logo/header.svg.html` is the same logo as one inline SVG coloured
by the page's CSS variables, so it follows the theme toggle. `tools/roadmap_graph.py` puts it into every page.

## Fonts

`fonts/`: Space Grotesk 500/700, Inter 400 and 400 italic, JetBrains Mono 400/700 (Latin subset, Fontsource 5.2),
each under the SIL Open Font License 1.1 (licence files alongside). Used by the social templates; the site loads the
same families from Google Fonts.

## Social images

`social/template.html` draws every format from one layout family: the design-system cover blocks on the right (or in a
top band on tall formats), the words on the left, the logo at the bottom. `social/render.js` screenshots it with
Playwright:

```bash
node brand/social/render.js
```

renders the brand set and an example post into `social/out/`. For posts, write a JSON list and pass it:

```json
[{"name": "spc-launch-square", "format": "square", "theme": "dark",
  "eyebrow": "open course · draft, open for review", "headline": "Charting Process Behavior",
  "sub": "Chart a process over time, separate routine variation from signals, and judge whether it can meet its specifications."}]
```

```bash
node brand/social/render.js posts.json
```

| Format | Size (px) | Where | Size checked against |
|---|---|---|---|
| `og` | 1200 × 630 | Link previews for the site; LinkedIn and Facebook link posts | Widely cited Meta guidance (1.91:1); Meta's own page not opened |
| `x-header` | 1500 × 500 | X profile header | X Help Center (search result); the profile picture covers the bottom-left, so words sit right of it |
| `linkedin-cover` | 4200 × 700 | LinkedIn Page cover | LinkedIn Help snippet only; third-party guides say 1128 × 191 (same 6:1 shape). Check before uploading. |
| `square` | 1080 × 1080 | Feed posts (LinkedIn, Instagram) | Common guides, not a platform page |
| `portrait` | 1080 × 1350 | Feed posts, 4:5 | Common guides, not a platform page |
| `logo/mark-*-400.png` | 400 × 400 | Profile picture on LinkedIn and X | LinkedIn Help and X Help (search results) |

## Posting plan

One look everywhere: dark theme by default, light for variety, one accent, the logo bottom-left of every post.

| Post type | Eyebrow (mono, accent) | Headline | Formats |
|---|---|---|---|
| Course launch | `open course · draft, open for review` (or `verified` once reviewed) | Course title | square, portrait, og |
| Module explainer | `module · <course>` | The one idea, as a plain sentence | portrait (carousel cover), square |
| Insight | `insight` | A claim the course backs, with its source in the caption | square |
| Roadmap update | `roadmap` | What was added, in numbers taken from `ROADMAP.md` | og, square |
| Review call | `review wanted` | Course title + what needs a second pair of eyes | square |
| Profiles | none | Logo and tagline only | x-header, linkedin-cover, mark-400 |

Rules for the words: say what the thing is first; no hype, no exclamation marks, no emoji; never call a course
verified or certified before its review is recorded in the catalog.
