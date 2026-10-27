# Module 00 — Foundations of Quality

**Time:** 75 min

## Objectives

- Trace how quality practice developed, from inspection to statistical control to management systems, and name the people and ideas behind each step.
- Distinguish quality control, quality assurance and quality improvement, and say which tools in this course belong to each.
- Describe the main obstacles to continuous improvement and how a quality engineer works around them.
- Name the standards a quality engineer meets and what each is for; explain what ISO 9001 requires in outline, what certification does and does not prove, and where DMAIC projects fit inside it.
- State what a process map gives an improvement team before any data is collected.

## What "quality" means

Two definitions do most of the work in practice:

- **Fitness for use** (Juran): the product or service does what the customer needs it to do, in the customer's conditions.
- **Conformance to requirements** (Crosby): the output matches what was specified, every time.

They pull in different directions when the specification is wrong. A part can conform perfectly to a drawing and still fail in use; a part can work and still be rejected because it is out of tolerance. A quality engineer owns both halves: getting the requirement right (voice of the customer, specifications, critical-to-quality characteristics) and then meeting it consistently (measurement, control, capability).

At Bayline Fasteners, the running case for this course, the insert OD of 6.350 ± 0.025 mm is a conformance requirement. The customer's real need is that inserts press into a housing without stripping. The returns happened because conformance slipped, but a good investigation also asks whether the tolerance reflects the need.

## A short history

Quality practice changed each time somebody found a cheaper way to be right than inspecting everything afterwards.

| Period | Shift | People and ideas |
|---|---|---|
| Before 1900 | The craftsman judged their own work; quality was personal reputation. | Guilds, apprenticeship |
| 1900s–1920s | Mass production separated planning from doing. Inspection departments sorted good from bad at the end of the line. | Taylor's scientific management; the inspector as a job |
| 1924–1931 | Shewhart showed that variation has two kinds of cause and that a chart can tell them apart. Control replaced sorting. | Walter Shewhart at Bell Labs: the control chart, *Economic Control of Quality of Manufactured Product* (1931); Dodge and Romig's acceptance sampling tables |
| 1940s | Wartime production spread sampling and control charts across US industry. | War Standards Z1.1–Z1.3; training of thousands of engineers in statistical methods |
| 1950s–1960s | Japan rebuilt its industry around statistical methods and management responsibility for quality. | Deming's 1950 lectures; Juran's 1954 visits; the Deming Prize (1951); Ishikawa's cause-and-effect diagram and quality circles; Feigenbaum's *Total Quality Control* |
| 1970s–1980s | Western firms, losing share to Japanese competitors, adopted company-wide approaches. | Crosby's *Quality Is Free* (1979); Taguchi's loss function; total quality management; Toyota Production System studied abroad |
| 1986–1990s | Defect rates were restated in parts per million, and improvement became a managed project portfolio. | Six Sigma at Motorola (1986), scaled at GE (1995); ISO 9000 series first published (1987); Malcolm Baldrige Award (1987); *The Machine That Changed the World* names "Lean" (1990) |
| 2000s– | Lean and Six Sigma merged into one toolkit; management systems adopted a process approach and risk-based thinking. | Lean Six Sigma; ISO 9001:2000, ISO 9001:2015 and ISO 9001:2026; sector standards such as IATF 16949 and AS9100 |

Three ideas survive every fashion change, and this course is built on them:

1. **Variation is the enemy, and it has causes you can find.** Shewhart's distinction between common and special causes is still the basis of every control chart (Module 04).
2. **Prevention beats detection.** Inspection finds defects after the cost has been incurred. Controlling inputs (Y = f(X), Module 01) stops them.
3. **Quality is management's job, measured in data.** Deming argued that most problems belong to the system, which only management can change, and that decisions should rest on evidence rather than opinion. Those two claims became the "leadership" and "evidence-based decision making" principles in ISO 9001.

## Quality control, quality assurance, quality improvement

The words are used loosely on the shop floor, but the standards give them distinct meanings, and the distinction decides who does what.

| Term | Question it answers | Typical activities | Where in this course |
|---|---|---|---|
| **Quality control (QC)** | Is this output meeting requirements right now? | Measurement, inspection, control charts, reaction to out-of-control signals, containment | Modules 02–04, 06 |
| **Quality assurance (QA)** | Can we show, in advance and to others, that requirements will be met? | Procedures, audits, calibration records, supplier approval, management system, certification | Module 00 (ISO 9001), Module 03 (calibration), Module 06 (control plans) |
| **Quality improvement (QI)** | How do we raise the level the process can reach? | DMAIC projects, root cause analysis, error-proofing, capability improvement | Modules 01, 05, 06, 07 |

Juran framed the same three as a trilogy: **plan** (design the process and its controls), **control** (hold the gains), **improve** (break through to a new level). A control chart is a QC tool; the project that moved the center line was QI; the control plan that keeps it there is QA.

A practical test: if the activity's output is a decision about a unit or a batch, it is control. If its output is confidence held by someone else, it is assurance. If its output is a process that performs better than before, it is improvement.

## Why continuous improvement is hard

The tools in this course are not difficult. What makes improvement fail is usually one of these:

- **Tampering.** Adjusting a process in response to common-cause variation makes it worse (the funnel experiment, covered in Charting Process Behavior). Teams that cannot tell the two kinds of variation apart "fix" noise and create signals.
- **Measurement you cannot trust.** If gauge error is a large share of the tolerance, the data say nothing. Module 03 exists because this is the most common hidden failure.
- **Local optimization.** A department improves its own metric and pushes the cost to the next one. Process maps and value-stream thinking expose this.
- **Gains that evaporate.** Without a control plan, standard work and an owner, a process drifts back within months. Module 06 is about sustainment, not just fixes.
- **Fear and blame.** People hide defects when reporting them is punished. Deming's advice to drive out fear is still the precondition for honest data.
- **Opinion over evidence.** Experienced people are often right about causes, and sometimes wrong. The discipline of stating a hypothesis and testing it (Module 05) protects the project either way.
- **Improvement as an event.** A kaizen week with no follow-up is a demonstration, not a system. ISO 9001's clause on improvement (10) exists to make it routine.

## What a process map gives you

Before a single measurement is taken, a process map produces four things an improvement team cannot get any other way:

1. **One shared picture.** Operators, engineers and managers usually hold different mental models of the same process. Drawing it exposes the differences.
2. **Boundaries.** Where the project starts and stops, and which inputs come from outside it (the SIPOC view).
3. **Handoffs and non-value-added steps.** Waiting, rework loops, inspection and transport appear as boxes that add no value, and they are where most of the lead time hides.
4. **A frame for measurement.** Every box is a place to put a metric; the map tells you where the data in Modules 02–04 should be collected.

This course uses maps as a starting point; the [Process Mapping](../../../lean-six-sigma/process-mapping/README.md) course covers SIPOC, flow charts, swim lanes, value-added flow charts and value stream maps in depth.

## The standards a quality engineer meets

College courses rarely say which standards a working quality engineer will actually be asked about. This map names them, with one line each on what the standard is for and when it applies. It is descriptive only; the standards themselves are copyrighted documents bought from ISO or the national body, and this course reproduces none of their text.

| Standard | What it is for | When you meet it |
|---|---|---|
| ISO 9000 | The vocabulary and principles behind the 9000 family: what "quality", "nonconformity", "corrective action" and the rest mean (iso-9000-2015) | Whenever a definition is disputed in an audit or a contract |
| ISO 9001 | The requirements for a quality management system; the one an organization is certified to (iso-9001-2015, iso-9001-2026) | Any certified plant, every supplier questionnaire |
| ISO 19011 | How to audit management systems: auditor competence, planning, evidence, reporting | Internal audits and supplier audits |
| ISO/IEC 17025 | Competence of testing and calibration laboratories | When your calibration certificates must be traceable, and when a lab's results are challenged |
| ISO 10012 | Measurement management systems: managing measuring equipment and processes | The calibration programme behind Module 03 |
| IATF 16949 | ISO 9001 plus the automotive industry's additional requirements; brings in the AIAG core tools (APQP, PPAP, FMEA, MSA, SPC) | Automotive supply chains |
| AS9100 | ISO 9001 plus aerospace requirements (configuration, counterfeit parts, product safety) | Aerospace and defence supply chains |
| ISO 13485 | Quality management for medical devices, tied to regulatory approval | Medical device makers and their suppliers |
| ISO 2859 and ISO 3951 | Acceptance sampling by attributes and by variables; the ANSI/ASQ Z1.4 and Z1.9 equivalents | Incoming and outgoing inspection sampling plans |
| ISO 7870 series | Control charts: general guidance and the standard chart types | When a customer asks whether your SPC follows a standard |
| ISO 22514 series | Process capability and performance indices (Cp, Cpk, Pp, Ppk) and how to compute them | Capability reports to customers |
| ISO 31000 | Risk management principles and guidelines | Risk-based thinking in ISO 9001, enterprise risk registers |

For the sampling, control-chart and capability standards the course teaches the methods from textbooks (montgomery-8e); the standards formalise the same methods and are what a customer may cite.

## ISO 9001 in outline

ISO 9001 is the international standard for a quality management system (QMS): the set of processes an organization uses to meet customer and regulatory requirements and to improve. ISO 9001:2015 (with Amendment 1 of 2024) is the edition most organizations hold certificates to; ISO 9001:2026 was published on 16 September 2026 with a three-year transition, so certificates move to the new edition through 2029. The outline below follows the 2015 structure, which the 2026 edition keeps; check clause numbers against the edition your auditor uses. It does not specify product quality; it specifies how the organization manages quality.

**Seven quality management principles** sit under the standard: customer focus, leadership, engagement of people, process approach, improvement, evidence-based decision making, and relationship management. Every clause can be traced back to one of them.

**Structure.** Clauses 4 to 10 follow Plan–Do–Check–Act:

| Clause | Title | What it asks for, in plain terms |
|---|---|---|
| 4 | Context of the organization | Who your interested parties are, what affects you, and what the QMS covers |
| 5 | Leadership | Top management owns the QMS, sets a quality policy and assigns responsibilities |
| 6 | Planning | Risks and opportunities are identified; quality objectives are measurable and planned |
| 7 | Support | People, infrastructure, calibrated measuring equipment, competence, documented information |
| 8 | Operation | How products and services are planned, designed, purchased, produced, released and handled when nonconforming |
| 9 | Performance evaluation | Monitoring and measurement, customer satisfaction, internal audit, management review |
| 10 | Improvement | Nonconformity and corrective action, continual improvement |

**Risk-based thinking** replaced the older "preventive action" clause: the organization is expected to think about what could go wrong in each process and act in proportion. FMEA (Module 05) is the quality engineer's usual tool for doing this formally.

**Documented information** is the standard's term for procedures and records. The 2015 edition requires fewer mandatory documents than earlier editions; the organization decides what it needs to control its processes, and must keep evidence that it did.

**Certification.** An accredited certification body audits the organization against the standard and issues a certificate, typically on a three-year cycle with surveillance audits between. Certification shows that a conforming system exists and is followed. It does not show that any particular shipment is good, and a certified supplier can still ship defects, as Bayline did. Customers in regulated or high-consequence sectors add their own requirements on top: IATF 16949 (automotive), AS9100 (aerospace), ISO 13485 (medical devices).

**Where this course fits.** A DMAIC project is how clause 10 gets done. The customer returns at Bayline are nonconformities under clause 10.2 (2015 numbering); the root cause analysis in Module 05 and the corrective actions in Module 06 are the evidence an auditor would ask for; the control plan is documented information under clause 7.5; gauge R&R and calibration (Module 03) satisfy clause 7.1.5 on monitoring and measuring resources.

## Exercise 0.1

List five activities your own organization does in the name of quality (for example incoming inspection, supplier audits, a monthly scrap review). Classify each as control, assurance or improvement using the test in the table above. Which of the three has the fewest entries? That is usually where the next project is.

## Check yourself

1. A supplier is ISO 9001 certified. A customer receives a shipment with 4 % defective parts. Is this a contradiction?
2. Which of the three terms, QC, QA or QI, describes each of the following: an out-of-control signal on an X̄ chart; an internal audit of calibration records; a project that reduced thread damage from 3 % to 0.4 %?
3. Shewhart's chart distinguishes two kinds of variation. Name them and say which one a DMAIC project usually targets.
4. Name two obstacles to improvement that a process map helps with, and one it does not.
5. Which ISO 9001 clause would an auditor cite when asking for evidence that a gauge R&R study was done?

<details><summary>Answers</summary>

1. No. Certification shows a conforming management system exists and is followed, not that every shipment is good. The defects should appear as a nonconformity under clause 10.2, with corrective action; a system that does not catch and act on them would be the audit finding.
2. QC (a decision about current output); QA (confidence for others, supported by records); QI (a process that now performs better).
3. Common-cause and special-cause variation. Special causes are removed first to make the process stable; a DMAIC project usually targets common-cause variation, which requires changing the process itself.
4. Helps with local optimization and with unclear boundaries or handoffs. Does not help with untrustworthy measurement, which needs a measurement system analysis.
5. Clause 7.1.5, monitoring and measuring resources, which covers the fitness of measuring equipment and calibration.

</details>
