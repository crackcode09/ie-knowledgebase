# Roles

The evidence and the working files for stage 3 of the site roadmap: turning a target position into what to train, grounded in the official occupational standard. Nothing here is advice yet; it is the data and the proposed mappings the advisor (stage 4) will be built on.

## Layout

```
roles/
  onet/            vendored O*NET occupation profiles, one .md and one .json per code, version-stamped
  onet/codes.txt   which codes are vendored; python tools/onet_refresh.py rebuilds them from the official CSV files
  mappings/        proposed course-to-role maps written by /map-course, one file per course; rows are "proposed" until a person confirms them
```

## The O*NET profiles

Each `roles/onet/<code>.md` lists the occupation's tasks, knowledge, skills, abilities, work activities and technology, with O*NET's importance ratings (1 to 5) and level ratings (0 to 7), and the hot and in-demand technology flags. The release version and download date are stamped at the top. O*NET publishes quarterly; refresh with `python tools/onet_refresh.py` and review the diff, since changed ratings change the maps.

> The profiles include information from the O*NET Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA), used under the CC BY 4.0 licence. O*NET is a trademark of USDOL/ETA. The IE Knowledgebase is not affiliated with or endorsed by USDOL/ETA.

Known limit: the standard lags the market. The Industrial Engineers profile lists no AI tools, so "not in the standard" is information with a date on it, never a defect in a course. The market signal (to be chosen) is the second column that corrects this.

## How a course declares its roles

A line in the course README, under the length and prerequisites:

```
**Roles:** 17-2112.00 (quality engineer), 17-2112.03
```

The first code is the primary role; a parenthetical names the O*NET sample title the course is closest to. Courses that serve no O*NET occupation directly (for example Technical Communications) declare the codes of the roles they support and say so in the parenthetical. A course without a Roles line is mapped against 17-2112.00 and the map says that was the default.

## Mapping a course

`/map-course <slug>` in Claude Code reads the course and the declared profiles and writes `roles/mappings/<slug>.md`: for each profile element the course teaches, the module and section that teach it, quoted, with a coverage call (covers, touches) and the element's importance. It also lists the high-importance elements the course does not reach, and the parts of the course that the standard does not name (dated). Every row is **proposed** until a person changes it to **confirmed**; the chair runs the mapping twice and reports the differences, so unstable judgments are visible. Nothing from a mapping appears on the site until it is confirmed.

The mapping is advisory. It never blocks verification; the review board (`/review-course`) decides whether a course is right, the map says what it is for.
