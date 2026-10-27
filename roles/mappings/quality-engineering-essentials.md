# Role map: Quality Engineering Essentials

| | |
|---|---|
| Course | `courses/quality-operational-excellence/quality-engineering-essentials/` (mapped as it stands on `main` on 2026-10-27, before the board-run-1 fixes in PR #34; re-map after they merge) |
| Roles | 17-2112.00 Industrial Engineers (declared; "quality engineer" sample title), 17-2112.03 Manufacturing Engineers (declared) |
| O*NET release | 31.0, downloaded 2026-10-27 |
| Mapping run | 1 (two identical runs, consolidated) |
| Date | 2026-10-27 |
| State | proposed |
| Confirmed by | |

## Summary

- Elements with importance ≥ 3.0 across both profiles: 204 (IE 93, ME 111); technology rows carry no importance and are counted separately.
- Run 1: covered 27, touched 53, not reached 124. Run 2: covered 40, touched 48, not reached 116.
- Consolidated with the weaker call wherever the runs disagreed: **covered 25 · touched 62 · not reached 117**.
- Stability: the runs disagreed on 17 rows (listed under Differences). They agreed on the shape: the course serves the analysis, problem-solving and quality-control side of both roles and does not reach the design, planning, cost-estimation, supervision and communication side.
- High-importance gaps, top three by importance: Engineering and Technology knowledge (4.42 / 4.41), Communicating with Supervisors, Peers, or Subordinates (4.23 / 4.04), Mechanical knowledge (4.20 / 4.08). On tasks: Estimate production costs (IE 18607, 3.97) and Provide technical expertise related to manufacturing (ME 18183, 4.04).
- Technology: of the hot or in-demand rows (IE 28, ME 16) the course uses only Python, through the supplied scripts. Excel, Minitab, SQL, SAP, R and MATLAB are neither named nor used.
- Content the standard does not name: most of the course's specific methods (SPC, capability indices, gauge R&R, FMEA, DMAIC, error-proofing, ISO 9001, AI tooling). O*NET names outcomes, not methods, so this is expected and dated.

## Coverage

Weaker call kept where the runs differed. IE = 17-2112.00, ME = 17-2112.03. Evidence is the quote both runs agreed on, or run 1's where only one gave it.

| Element (profile, ID) | Importance | Coverage | Evidence | Status |
|---|---|---|---|---|
| Making Decisions and Solving Problems (ME 4.A.2.b.1; IE 4.41) | 4.50 | covers | M06 "Corrective action matrix": "score them on impact, cost, effort and risk"; M06 check 2 on the rollout decision | proposed |
| Production and Processing (ME 2.C.2.a; IE 4.28) | 4.42 | touches | M01 "Inputs determine output": "materials, machines, methods, measurement, people and environment"; quality slice only | proposed |
| Engineering and Technology (ME 2.C.3.b; IE 4.41) | 4.42 | touches (run 1: not reached) | M01 "Inputs determine output": "Inspecting Y finds problems; controlling the critical X's prevents them" | proposed |
| Troubleshoot product problems involving designs, materials, or processes (ME 18181) | 4.35 | covers (processes only) | M05 "The path to root cause": "Verify with data (stratification, graphs, regression, tests)" | proposed |
| Getting Information (ME 4.A.1.a.1; IE 4.21) | 4.35 | touches (run 2: covers) | M03 "Data collection and sampling plan": "what to measure, operational definition, gauge, who, when, how many, how recorded" | proposed |
| Working with Computers (IE 4.A.3.b.1; ME 4.28) | 4.32 | touches | M02 "Run it": "python tools/qekit.py cleanse"; learner runs supplied scripts | proposed |
| Investigate or resolve operational problems such as material use variances or bottlenecks (ME 18177) | 4.27 | touches (run 2: covers) | M05 "Verifying causes with data": "19 of 20 oversize parts are from M2 (chi-square p = 0.0001)"; quality variance only | proposed |
| Analyzing Data or Information (ME 4.A.2.a.4; IE 3.91) | 4.21 | covers | M05 "Simple and multiple regression": "OD vs tool age alone: slope 0.0051 mm per 1,000 parts, R² 0.23" | proposed |
| Processing Information (ME 4.A.2.a.2; IE 3.92) | 4.19 | covers | M02 "Data cleansing": "After cleansing: 40 rows, 38 usable OD values" on `dirty_export.csv` | proposed |
| Identify opportunities or implement changes to improve processes or reduce costs (ME 20960) | 4.19 | covers (improvement; cost reduction not practised) | M06 "Piloting a solution": "Test the change on a limited scale — one machine, a few shifts" | proposed |
| Apply continuous improvement methods, such as lean manufacturing (ME 18167) | 4.16 | covers (DMAIC; Lean tools explained only) | M07 Part A: "one page per DMAIC phase" | proposed |
| Identifying Objects, Actions, and Events (ME 4.A.1.b.1; IE 3.94) | 4.12 | touches (run 2: covers) | M04 "Trend charts and control charts": "so you can tell signals from noise" | proposed |
| Monitoring Processes, Materials, or Surroundings (ME 4.A.1.a.2; IE 3.87) | 4.08 | touches (run 2: covers) | M06 "Hold the gains": "keep X̄–R charts on OD for each machine, with a reaction plan" | proposed |
| Documenting/Recording Information (ME 4.A.3.b.6; IE 3.54) | 4.00 | touches | M02 "Data cleansing": "Document every change, never silently delete outliers" | proposed |
| Critical Thinking (IE 2.A.2.a; ME 3.75) | 4.00 | covers | M05 check 1: "Correlation can arise from a lurking variable"; "Regression shows association; the pilot confirms cause" | proposed |
| Mathematics, skill (ME 2.A.1.e; IE 3.25) | 4.00 | covers | M07 Part B answer 7: "Cp = 0.6 / 0.48 = 1.25; Cpk = (10.3 − 10.1) / 0.24 = 0.83"; M03 sample size | proposed |
| Complex Problem Solving (ME 2.B.2.i; IE 3.88) | 4.00 | covers | M07 Part A review criteria: "root causes are verified, not assumed" | proposed |
| Deductive Reasoning (IE and ME 1.A.1.b.4) | 4.00 | touches | M05 "The path to root cause": "Narrow with logic and process knowledge (5-Why)" | proposed |
| Inductive Reasoning (IE and ME 1.A.1.b.5) | 4.00 | touches | M05 "Effective problem statements": "Those contrasts point at causes" | proposed |
| Problem Sensitivity (ME 1.A.1.b.3; IE 3.88) | 4.00 | touches | M02 "Data cleansing": "Decimal slip (63.52 instead of 6.352)"; M05 FMEA severity override | proposed |
| Written Expression (IE 1.A.1.a.4; ME 3.62) | 4.00 | touches (run 2: not reached) | M01 check 2 answer: "what, where, when, how big, against what standard; no cause or solution" | proposed |
| Incorporate new manufacturing methods to improve existing operations (ME 20961) | 3.96 | touches (run 1: not reached) | M06 "Piloting a solution": "confirm it works and catch side effects before full rollout"; rollout not taught | proposed |
| Mathematics, knowledge (ME 2.C.4.a; IE 3.89) | 3.96 | touches (run 2: covers) | M03 "How many?": "n = (1.96 σ / E)²"; statistics only, no algebra, geometry or calculus | proposed |
| Determine root causes of failures using statistical procedures (ME 20962) | 3.92 | covers | M05: "Verified causes: M2's offset (≈ 0.008 mm high), tool wear without compensation, and coolant temperature" | proposed |
| Monitoring, skill (ME 2.A.2.d; IE 3.38) | 3.88 | touches | M04: "Common cause → improve the system; special cause → find and remove it"; O*NET defines the skill for people and organisations | proposed |
| Operations Monitoring (ME 2.B.3.g) | 3.88 | touches (run 2: covers) | M04: "Don't adjust a stable process for noise" | proposed |
| Judgment and Decision Making (ME 2.B.4.e; IE 3.12) | 3.88 | covers | M06 check 2: "Compare total cost: scrap, sorting, returns and customer risk saved vs extra tool cost" | proposed |
| Organizing, Planning, and Prioritizing Work (ME 4.A.2.b.6; IE 3.74) | 3.88 | touches | M01 charter timeline: "D 2 wks, M 4 wks, A 4 wks, I 4 wks, C 2 wks"; M05 FMEA priorities | proposed |
| Prepare reports summarizing manufacturing performance (ME 18182) | 3.87 | touches | M07 Part A: "Produce a short project storyboard (one page per DMAIC phase)" | proposed |
| Prepare documentation for new processes or procedures (ME 18178) | 3.83 | touches (run 2: covers) | M06 control plan table (`templates/control-plan.csv`); the capstone asks for one | proposed |
| Computers and Electronics (ME 2.C.3.a; IE 3.77) | 3.81 | touches | M03 "Run it": "python tools/qekit.py grr" | proposed |
| Analyze statistical data and specifications to establish quality and reliability objectives (IE 1391) | 3.80 | touches | M04 "Process capability": "Capability compares the voice of the process with the voice of the customer"; objectives are given in the charter, not derived | proposed |
| Writing (IE and ME 2.A.1.c) | 3.75 | touches | M01 check 2: "Rewrite as a proper problem statement" | proposed |
| Systems Analysis (ME 2.B.4.g; IE 3.25) | 3.75 | touches | M01 "Inputs determine output": "is a function of process inputs (X's)" | proposed |
| Systems Evaluation (ME 2.B.4.h; IE 3.25) | 3.75 | covers | M04 "Stage variables": "the new level is holding"; M06 pilot before/after with side effects | proposed |
| Mathematical Reasoning (ME 1.A.1.c.1; IE 3.12) | 3.75 | touches | M07 Part B 7 and 8 | proposed |
| Number Facility (ME 1.A.1.c.2; IE 3.12) | 3.75 | touches (run 1: not reached) | M07 Part B 2: "Five ODs: 6.352, 6.358, 6.349, 6.361, 6.355. Mean and standard deviation?" | proposed |
| Evaluate precision and accuracy of production and testing equipment to formulate corrective action (IE 1407) | 3.68 | covers (equipment; drawings not reached) | M03 "Variable gauge R&R": "Action: standard method (ratchet stop, measuring position), retrain, repeat the study" | proposed |
| Evaluating Information to Determine Compliance with Standards (IE 4.A.2.a.3; ME 3.54) | 3.67 | covers | M03: "10–30 % may be acceptable depending on the application and cost"; M04 capability against spec | proposed |
| Record information on engineering drawings and production problems (IE 1403) | 3.66 | touches (run 1: not reached; production problems only) | M05 "Effective problem statements": "8.3 % of inserts sampled from M1/M2 over 20 days were defective" | proposed |
| Estimating the Quantifiable Characteristics (ME 4.A.1.b.3; IE 3.62) | 3.65 | touches (run 1: not reached) | M02 "Center and spread": "95 % CI for the mean 6.36210 to 6.36337 mm" | proposed |
| Inspecting Equipment, Structures, or Materials (ME 4.A.1.b.2; IE 3.42) | 3.65 | touches (run 1: not reached) | M03 "Attribute agreement analysis": "Thread damage is judged visually (pass/fail)"; the learner analyses an inspection study | proposed |
| Evaluate manufactured products against specifications (ME 18175) | 3.62 | covers | M04 "Process capability": "Baseline OD capability by machine (spec 6.325–6.375 mm)" | proposed |
| Technology Design (ME 2.B.3.b) | 3.62 | touches | M06 "Error-proofing": "Bayline's tool-life counter that locks the cycle at 1,600 parts is a prevention device" | proposed |
| Judging the Qualities of Objects, Services, or People (ME 4.A.2.a.1; IE 3.26) | 3.62 | touches (run 1: not reached) | M03 "Attribute agreement analysis": "This inspection is not reliable" | proposed |
| Interpreting the Meaning of Information for Others (ME 4.A.4.a.1; IE 3.41) | 3.54 | touches (run 2: not reached) | M03: "marginal — acceptable for SPC (ndc 8) but using almost a quarter of the tolerance" | proposed |
| Troubleshooting (ME 2.B.3.k; IE 2.00) | 3.50 | covers | M05 "5-Why, 1-How": "drive one branch to a controllable cause, then ask how to fix it" | proposed |
| Design tests of products or process capabilities (ME 20963) | 3.48 | touches (run 2: covers) | M06 "Piloting a solution": "Plan the pilot: what will change, how success is measured, how long, and what would stop it" | proposed |
| Administration and Management (IE 2.C.1.a; ME 3.23) | 3.45 | touches | M00 "ISO 9001 in outline": "Top management owns the QMS, sets a quality policy and assigns responsibilities" | proposed |
| Coordinate and implement quality control objectives, activities, or procedures (IE 18608) | 3.42 | touches (run 2: covers) | M06 control plan reaction: "stop, check offset and tool; quarantine since last good subgroup" | proposed |
| Implement disposition of discrepant material and assess cost and responsibility (IE 1406) | 3.42 | touches | M06 control plan reaction: "100 % sort lot"; cost and responsibility not assessed | proposed |
| Apply statistical methods to determine processes, staff requirements, and production standards (IE 1395) | 3.37 | touches | M03 baseline and sample size; no staff or standards work | proposed |
| Study operations sequence, material flow, organization charts (IE 1404) | 3.28 | touches (run 1: not reached) | M00 "What a process map gives you": "Waiting, rework loops, inspection and transport appear as boxes that add no value" | proposed |
| Developing Objectives and Strategies (IE 4.A.2.b.4; ME 3.24) | 3.28 | touches | M01 charter: "Reduce defectives to < 1 % within 4 months, with oversize OD < 0.3 %" | proposed |
| Quality Control Analysis (ME 2.B.3.m; IE 2.25) | 3.25 | covers | M03 "Measurement is a process": "Observed variation = true part-to-part variation + measurement variation"; gauge R&R, capability and charts practised | proposed |
| Controlling Machines and Processes (ME 4.A.3.a.3; IE 3.17) | 3.23 | touches | M06 "Error-proofing": "the controller applies the wear offset automatically" | proposed |
| Science, skill (ME 2.A.1.f) | 3.12 | touches (run 1: not reached) | M06 "Piloting a solution": "Two-proportion test: z = 11.5, p < 0.001" | proposed |
| Formulate sampling procedures and forms for recording quality data (IE 1402) | 3.11 | covers | M03 "Data collection and sampling plan" with the four-row sample-size table and `data-collection-plan.md` | proposed |
| Python (IE technology, hot) | not rated | covers (see question 6) | README "Getting started": "python tools/qekit.py all"; "Run it" blocks in M02 to M06 | proposed |

## High-importance elements not reached

Neither run found the course reaching these (importance ≥ 3.0). Grouped; the nearest module is given where one comes close.

**Tasks, Industrial Engineers:** Estimate production costs and cost-saving methods (18607, 3.97; nearest M06, a qualitative comparison only) · Plan the sequence of operations (1394, 3.92) · Confer with clients, vendors, staff and management (18609, 3.78) · Communicate with management and users to develop standards (1400, 3.71) · Recommend methods for improving utilisation of personnel, material and utilities (1393, 3.67; M01 names the 8 wastes) · Draft and design layout of equipment and workspace (1398, 3.63) · Direct workers in measurement, inspection and testing (1405, 3.59; M03 actions) · Develop manufacturing methods, labour standards and cost analysis systems (1392, 3.50) · Review production schedules and specifications (1399, 3.47) · Complete production reports and purchase orders (1408, 3.43) · Regulate workflow schedules (1410, 3.19) · Schedule deliveries (1409, 3.11).

**Tasks, Manufacturing Engineers:** Provide technical expertise related to manufacturing (18183, 4.04) · Review product designs for manufacturability (18180, 3.92) · Design layout of equipment or workspaces (18168, 3.83) · Communicate manufacturing capabilities and schedules (18170, 3.81) · Supervise technicians and other engineers (18185, 3.63) · Design, install or troubleshoot manufacturing equipment (18172, 3.62; M05 reliability) · Estimate costs, times or staffing for new designs (18174, 3.58) · Train production personnel (18186, 3.56; M06 standard work) · Sustainability tasks (19649 3.37, 19650 3.32, 19651 3.09) · Purchase equipment and parts (18179, 3.25) · Read current literature to keep abreast (18184, 3.08; the reading list exists but there is no activity).

**Knowledge, both profiles:** Mechanical (4.20 / 4.08) · Design (4.08 / 4.00; M06 error-proofing is explained only) · English Language (3.96 / 3.77; problem-statement writing is too narrow) · Customer and Personal Service (IE 3.42; M00 customer focus) · Education and Training (3.34 / 3.15; M06 standard work) · Public Safety and Security (IE 3.12) · Physics (3.10 / 3.42) · Administrative (IE 3.01).

**Skills, both profiles:** Reading Comprehension (4.00 / 4.00) · Active Listening (4.00 / 3.88) · Speaking (3.88 / 3.88) · Active Learning (3.25 / 3.62) · Learning Strategies (ME 3.25) · Time Management (3.00 / 3.50) · Coordination (3.12 / 3.00) · Social Perceptiveness (3.00 / 3.00; M06 "listen to resistance", a mention) · Instructing (3.00 / 3.12) · Operations Analysis (ME 3.25) · Persuasion (ME 3.12; M06 leading change) · Negotiation (ME 3.00) · Service Orientation (ME 3.00) · Management of Material Resources (ME 3.00).

**Abilities, both profiles:** Oral Comprehension, Written Comprehension, Oral Expression (4.00 / 3.88 each) · Information Ordering (3.62 / 3.88; M05) · Near Vision (3.62 / 4.00) · Category Flexibility (3.38 / 4.00; M05 fishbone) · Selective Attention (3.38 / 3.12) · Fluency of Ideas (3.25 / 3.62; M05 fishbone) · Originality (3.25 / 3.62) · Speech Recognition and Speech Clarity (3.25 to 3.50) · Visualization (3.12 / 4.00; M02 reading graphs) · Flexibility of Closure (3.00 / 3.62) · Far Vision (3.00 / 3.25) · Perceptual Speed and Speed of Closure (ME 3.12, 3.00).

**Work activities, both profiles:** Communicating with Supervisors, Peers, or Subordinates (4.04 / 4.23) · Thinking Creatively (4.02 / 3.85; M05 fishbone) · Updating and Using Relevant Knowledge (3.86 / 3.73) · Drafting, Laying Out, and Specifying Technical Devices (3.70 / 4.04) · Establishing and Maintaining Interpersonal Relationships (3.58 / 3.88) · Developing and Building Teams (ME 3.44; the charter lists a team) · Communicating with People Outside the Organization (IE 3.33) · Providing Consultation and Advice (3.06 / 3.35) · Coordinating the Work of Others (ME 3.23) · Training and Teaching Others (3.11 / 3.23; M06) · Scheduling Work (ME 3.15) · Resolving Conflicts and Negotiating (ME 3.12) · Guiding, Directing and Motivating Subordinates (ME 3.08) · Coaching and Developing Others (ME 3.00).

**Technology, hot or in demand, not used:** IE 27 of 28 rows, ME all 16. Microsoft Excel, Office, PowerPoint, Word, Visio, Project, SharePoint, Access; SQL and SQL Server; SAP; R, MATLAB, SAS; shell scripting; AutoCAD, SolidWorks; Visual Basic. Minitab and "statistical software" are listed without a flag and are not used either; the course uses its own `qekit.py`.

## Content the standard does not name

All rows: not in O*NET 31.0 for 17-2112.00 or 17-2112.03. Information about the standard, dated; not a defect in the course.

| Module and section | What it teaches | Note |
|---|---|---|
| M00 "A short history"; "Quality control, quality assurance, quality improvement"; "Why continuous improvement is hard" | History from Shewhart to Lean Six Sigma; the QC/QA/QI split and the Juran trilogy; tampering, local optimisation, fear | not named; the IE quality-control tasks do not draw the distinction |
| M00 "ISO 9001 in outline" | QMS principles, clauses 4 to 10, certification, sector standards | not named |
| M01 "Learning and problem solving with AI tools" | AI assistants as a colleague to check; confidentiality | not named; no AI tooling in either profile's technology list |
| M01 "DMAIC"; "The project charter"; "The 99.9 % problem" | Six Sigma project structure and charter; rolled throughput yield | not named (ME names lean, not DMAIC; project management appears only as the Microsoft Project row) |
| M02 "Distribution identification"; "Data cleansing" | AIC and KS fits, lognormal percentiles; duplicates, placeholders, label standardisation | not named beyond "statistical methods" |
| M03 "Variable gauge R&R"; "Attribute agreement analysis"; "Cause-and-effect matrix"; "Baseline performance" | ANOVA gauge R&R, ndc, kappa; C&E matrix; DPU, DPMO, sigma level | only IE 1407 (equipment precision) is near; the methods are not named |
| M04, whole module | Control chart selection, I–MR, X̄–R, p charts, transformation, staged limits, Cp/Cpk/Pp/Ppk | not named; SPC appears only as the "quality control software" technology row |
| M05 "Generating causes"; "FMEA"; "Product and process reliability" | Fishbone, 5-Why/1-How, root cause tree; S, O, D and RPN; MTBF and series/redundant reliability | root causes are named in ME 20962 and reliability objectives in IE 1391; the tools are not |
| M06 "Error-proofing"; "Leading change"; "Hold the gains" | Error-proofing hierarchy; change management; control plan, visual management, 5S, standard work | ME 18167 names "lean manufacturing" generally; the tools are not named |
| Absent from the course | Cost of quality; production cost estimation; 8D; supplier quality; sustainability | listed so the gap against the standard is visible (IE 18607, ME 18174, ME 19649 to 19651) |

## Differences between run 1 and run 2

The consolidated table keeps the weaker call in every case.

| Row | Run 1 | Run 2 | Chair's reading |
|---|---|---|---|
| Engineering and Technology (knowledge) | not reached | touches | Y = f(X) is a one-paragraph mention; kept as touches on run 2's quote, flagged for the reviewer |
| Getting Information | touches | covers | the data collection plan is a template the learner fills in the capstone; touches until exercises exist (PR #34 adds them) |
| Investigate operational problems (ME 18177) | touches | covers | quality variance only; touches |
| Identifying Objects, Actions, and Events | touches | covers | chart reading is practised in check-yourself items only; touches |
| Monitoring Processes, Materials, or Surroundings | touches | covers | the learner interprets charts, does not monitor; touches |
| Written Expression | touches | not reached | one problem statement; kept as touches, thin |
| Incorporate new methods (ME 20961) | not reached | touches | the pilot is shown, rollout is not; touches |
| Mathematics (knowledge) | touches | covers | statistics only; touches |
| Operations Monitoring | touches | covers | same evidence as Monitoring Processes; touches |
| Prepare documentation (ME 18178) | touches | covers | an example control plan plus a capstone request; touches until the capstone is required work |
| Number Facility | not reached | touches | one skill-check item; touches |
| Record information on production problems (IE 1403) | not reached | touches | problem statements record production problems; touches |
| Estimating the Quantifiable Characteristics | not reached | touches | a confidence interval is an estimate; touches |
| Inspecting Equipment, Structures, or Materials | not reached | touches | analysing an inspection study is not inspecting; kept as touches, flagged |
| Judging the Qualities | not reached | touches | same evidence; flagged |
| Interpreting the Meaning of Information for Others | touches | not reached | the gauge R&R interpretation is a worked example; touches, thin |
| Design tests of process capabilities (ME 20963) | touches | covers | the pilot plan is shown; touches |
| Coordinate quality control activities (IE 18608) | touches | covers | the control plan is drafted from a template; touches |
| Study operations sequence (IE 1404) | not reached | touches | the process map section; touches |
| Science (skill) | not reached | touches | the two-proportion test; touches |

## Questions for the human reviewer

1. **Can a course cover an ability?** Both runs treated abilities (deductive reasoning, number facility, visualization and the like) as traits a course can only exercise, so none is marked covers. *Resolved by:* a project rule: abilities are mapped as touches at most, or they are left out of coverage counts altogether.
   - **Answer:**
2. **What counts as practice?** Run 2 counted worked examples plus check-yourself and skill-check items as practice; run 1 wanted a stated exercise. This single rule moves about a dozen rows between covers and touches. PR #34 adds a real exercise to every module, which settles most of these on the re-map. *Resolved by:* confirming that an exercise with the course data is the bar for covers.
   - **Answer:**
3. **Establishing objectives (IE 1391).** The course analyses data against specifications but the goal is given in the charter, never derived. *Resolved by:* deciding whether deriving a quality or reliability objective from data is in scope for this course or for the role profile only.
   - **Answer:**
4. **Lean inside "continuous improvement such as lean" (ME 18167).** DMAIC is practised end to end; Lean tools (wastes, 5S, standard work) are explained only. *Resolved by:* reading "such as" as an example (covers) or a requirement (touches).
   - **Answer:**
5. **Broad knowledge areas (Engineering and Technology, Production and Processing, Administration and Management).** The course covers the quality slice of each. *Resolved by:* how much of a knowledge area a course must reach before a touch counts.
   - **Answer:**
6. **Does running `qekit.py` count as using Python?** Both runs said yes under the "command or script" rule, but the learner writes no code. *Resolved by:* deciding whether the technology column means "uses" or "is competent in".
   - **Answer:**
7. **Monitoring (the skill).** O*NET defines it as assessing the performance of people and organisations; both runs stretched it to process monitoring. *Resolved by:* applying the standard's definition strictly (not reached) or loosely (touches).
   - **Answer:**
8. **Inspection and judging.** Analysing an attribute-agreement study is not inspecting parts. *Resolved by:* whether analysing inspection results counts as a touch.
   - **Answer:**
9. **Standards knowledge.** Module 00's ISO 9001 content maps to nothing in either profile; run 1 asked whether the standard's Administration and Management or Law and Government elements are meant to hold it. *Resolved by:* a project decision on where management-system knowledge sits in the map.
   - **Answer:**
10. **The role declaration itself.** The course declares 17-2112.00 with the quality-engineer sample title and 17-2112.03. The not-reached list is dominated by design, layout, scheduling, supervision and communication elements that belong to those roles in full but not to a quality engineer's slice of them. *Resolved by:* deciding whether a "quality engineer" profile should be a weighted subset of 17-2112.00 (which the map would then be scored against) rather than the whole occupation.
    - **Answer:**
