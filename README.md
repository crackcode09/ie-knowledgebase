# IE Knowledgebase

Free, open courses on industrial engineering, quality and continuous improvement. Courses are grouped into the same categories used by the IISE professional course catalog, under `courses/<category>/<course>/`.

## Courses

See [ROADMAP.md](ROADMAP.md) for a checklist of what is built and what is still open in each category.

[![Roadmap graph](docs/roadmap.svg)](docs/roadmap.svg)

Suggested order: Measurement & Basic Statistics, Process Mapping and Voice of the Customer, then Charting Process Behavior, then Fundamentals of Hypothesis Testing, then Design for Six Sigma, then Root Cause Analysis. Kaizen Leader and Lean Methods Accelerator have no prerequisites and can be taken at any point.

### [Analytics, Data Science & AI](courses/analytics-data-science-ai/README.md)

_No courses yet._

### [Ergonomics & Safety](courses/ergonomics-safety/README.md)

_No courses yet._

### [Healthcare Process Improvement](courses/healthcare-process-improvement/README.md)

_No courses yet._

### [Leadership & Project Management](courses/leadership-project-management/README.md)

_No courses yet._

### [Lean & Six Sigma](courses/lean-six-sigma/README.md)

| Course | Topic | Length | Status |
|---|---|---|---|
| [Measurement & Basic Statistics](courses/lean-six-sigma/measurement-and-basic-statistics/README.md) | Data types, accuracy vs precision, Pareto charts, histograms, center, spread, the normal distribution | ~6 h | v1.0 |
| [Process Mapping](courses/lean-six-sigma/process-mapping/README.md) | SIPOC, flow charts, swim lanes, value-added flow charts, spaghetti diagrams, VSM, VOC, affinity diagrams, CTQ trees, VOC as specifications | ~6 h | v1.0 |
| [Voice of the Customer](courses/lean-six-sigma/voice-of-the-customer/README.md) | Customers and segments, Kano, surveys and margin of error, affinity and CTQ trees, operational definitions, VOC as specifications, cause-and-effect matrix | ~7 h | v1.0 |
| [Lean Methods Accelerator](courses/lean-six-sigma/lean-methods-accelerator/README.md) | Standalone Lean toolkit: COPQ, VSM, takt, balancing, heijunka, benchmarking, flow and cells, SMED, TOC, pull (kanban, CONWIP), 5S, visual management, TPM, standard work | ~18 h | v1.0 |
| [Charting Process Behavior](courses/lean-six-sigma/charting-process-behavior/README.md) | Statistical Process Control: run charts, XmR, X̄–R, attribute charts, capability | ~12 h + capstone | v1.0 |
| [Fundamentals of Hypothesis Testing](courses/lean-six-sigma/fundamentals-of-hypothesis-testing/README.md) | Hypotheses, errors, power, CIs; t, ANOVA, proportion, chi-square, variance and nonparametric tests | ~14 h + capstone | v1.0 |
| [Design for Six Sigma](courses/lean-six-sigma/design-for-six-sigma/README.md) | DCDOV: VOC, QFD, Pugh, FMEA, error-proofing, scorecards, DOE, tolerance stack-up, flow simulation, line balancing, reliability | ~45 h incl. capstone | v1.0 |
| [Root Cause Analysis & Problem Solving](courses/lean-six-sigma/root-cause-analysis/README.md) | Problem statements, Pareto, process maps, fishbone, 5-Why, root cause trees, stratification, regression, logistic regression, corrective actions | ~14 h | v1.0 |
| [Kaizen Leader](courses/lean-six-sigma/kaizen-leader/README.md) | Planning and leading kaizen events: charter, VSM, takt, TOC, flow, balancing, kanban, SMED, 5S, TPM, standard work, A3; includes a one-day team-member track | ~22 h | v1.0 |

### [Logistics & Supply Chain](courses/logistics-supply-chain/README.md)

_No courses yet._

### [Quality & Operational Excellence](courses/quality-operational-excellence/README.md)

_No courses yet._

### [Technical Skills](courses/technical-skills/README.md)

_No courses yet._

### [Work Design & Work Measurement](courses/work-design-work-measurement/README.md)

_No courses yet._

### [Microlearning Refreshers](courses/microlearning-refreshers/README.md)

_No courses yet._

## Adding a course

1. Pick the category folder under `courses/` that fits, and create `courses/<category>/<course-name>/` (lowercase, hyphenated).
2. Include `README.md` (objectives + syllabus), `modules/`, and `solutions/`, `data/`, `tools/` as needed.
3. Follow the module structure in [CONTRIBUTING.md](CONTRIBUTING.md), then add a row to the category README and to the table above.

## License

Content: CC BY 4.0. Code: MIT. See [LICENSE](LICENSE).
