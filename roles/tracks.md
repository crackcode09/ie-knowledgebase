# Tracks

Curated routes through the catalog, one per occupation. The learning path page reads this file: each track becomes a rail of stations in the order listed, with the time per station and the reader's local progress.

Two sources anchor every track, and the page shows both:

- **O*NET** names the occupation (the code and title are the ones vendored under `roles/onet/`; the parenthetical is the O*NET sample title the track aims at). Nothing here changes the O*NET profile; the role map for each course (`roles/mappings/`) is where coverage is judged.
- **BLS Occupational Outlook Handbook** gives the outlook: median pay, growth over the projection decade and the number of jobs, with the year BLS states. BLS content is U.S. government work; the entry is linked as the source. Refresh these lines when BLS updates the Handbook (it did on 2026-08-27).

Rules the generator enforces: every numbered item is a course folder name under `courses/*/`, and a track has at least two courses. Keep the goal to one sentence. Order courses so that each one's prerequisites come earlier. The Outlook and Source lines are optional but go together.

## Industrial engineer

**Goal:** Get the tools industrial engineers use to improve processes, facilities, methods and work, in the order they build on each other.
**Role:** 17-2112.00 Industrial Engineers
**Outlook:** $102,440 median pay (2025) · 12% growth 2025–35, much faster than average · 365,100 jobs (2025)
**Source:** <https://www.bls.gov/ooh/architecture-and-engineering/industrial-engineers.htm> (BLS Occupational Outlook Handbook, Industrial Engineers, modified 2026-08-27)

1. introduction-to-industrial-engineering
2. measurement-and-basic-statistics
3. process-mapping
4. work-measurement
5. facilities-and-workplace-design
6. cost-of-quality

## Quality engineer

**Goal:** Measure a process you can trust, find what causes defects, fix it and keep it fixed.
**Role:** 17-2112.00 Industrial Engineers (sample title: quality engineer)
**Outlook:** $102,440 median pay (2025) · 12% growth 2025–35, much faster than average · 365,100 jobs (2025)
**Source:** <https://www.bls.gov/ooh/architecture-and-engineering/industrial-engineers.htm> (BLS Occupational Outlook Handbook, Industrial Engineers, modified 2026-08-27)

1. measurement-and-basic-statistics
2. process-mapping
3. charting-process-behavior
4. fundamentals-of-hypothesis-testing
5. root-cause-analysis
6. quality-engineering-essentials

## Manufacturing engineer

**Goal:** Design and improve the production process itself: flow, layout, changeover, and quality built in from the start.
**Role:** 17-2112.03 Manufacturing Engineers (BLS reports this specialty under Industrial Engineers)
**Outlook:** $102,440 median pay (2025) · 12% growth 2025–35, much faster than average · 365,100 jobs (2025), reported for industrial engineers as a whole
**Source:** <https://www.bls.gov/ooh/architecture-and-engineering/industrial-engineers.htm> (BLS Occupational Outlook Handbook, Industrial Engineers, modified 2026-08-27)

1. process-mapping
2. work-measurement
3. lean-methods-accelerator
4. facilities-and-workplace-design
5. process-modeling-and-simulation
6. design-for-six-sigma

## Operations research analyst

**Goal:** Turn operational data into decisions, from first charts to designed experiments, models and decision analysis.
**Role:** 15-2031.00 Operations Research Analysts
**Outlook:** $88,940 median pay (2025) · 12% growth 2025–35, much faster than average · 113,100 jobs (2025)
**Source:** <https://www.bls.gov/ooh/math/operations-research-analysts.htm> (BLS Occupational Outlook Handbook, Operations Research Analysts, modified 2026-08-27)

1. engineering-analytics
2. applied-statistics
3. fundamentals-of-hypothesis-testing
4. design-of-experiments
5. engineering-decision-making
6. advanced-engineering-analytics

## Management analyst

**Goal:** Find where an organisation loses time and money, prove the cause, and make the case for the fix to people who are not engineers.
**Role:** 13-1111.00 Management Analysts
**Outlook:** $101,860 median pay (2025) · 10% growth 2025–35, much faster than average · 1,077,100 jobs (2025)
**Source:** <https://www.bls.gov/ooh/business-and-financial/management-analysts.htm> (BLS Occupational Outlook Handbook, Management Analysts, modified 2026-08-27)

1. process-mapping
2. voice-of-the-customer
3. root-cause-analysis
4. cost-of-quality
5. engineering-decision-making
6. technical-communications

## Industrial production manager

**Goal:** Run a production operation: staff it, keep it reliable, hold quality, and read its finances.
**Role:** 11-3051.00 Industrial Production Managers
**Outlook:** $126,060 median pay (2025) · 3% growth 2025–35, as fast as average · 252,100 jobs (2025)
**Source:** <https://www.bls.gov/ooh/management/industrial-production-managers.htm> (BLS Occupational Outlook Handbook, Industrial Production Managers, modified 2026-08-27)

1. work-measurement
2. staffing-models
3. kaizen-leader
4. statistical-quality-control
5. reliability-engineering-excellence
6. financial-management-for-engineers
