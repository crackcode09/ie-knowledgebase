# Module 04 — Reliability-Centered Maintenance and Total Productive Maintenance

## Objectives

- Apply the RCM decision process to choose a maintenance strategy for each failure mode.
- Explain the core elements of TPM and how operators share ownership of reliability.
- Combine RCM and TPM in a practical program.

## Reliability-Centered Maintenance (RCM)

RCM asks, for each asset in its operating context, a fixed sequence of questions (the classic formulation has seven; a widely referenced SAE standard, JA1011, sets criteria for what counts as RCM — check the current version):

1. What are the **functions** and performance standards?
2. In what ways can it **fail to fulfil** them (functional failures)?
3. What **causes** each functional failure (failure modes)?
4. What **happens** when each failure occurs (effects)?
5. In what way does each failure **matter** (consequences: hidden, safety/environment, operational, non-operational)?
6. What can be done to **predict or prevent** each failure (proactive tasks and intervals)?
7. What should be done if no suitable proactive task is found (**default actions**: failure-finding, redesign, run-to-failure)?

### Task selection logic (simplified)

| If the failure mode… | Then consider… | Only if… |
|---|---|---|
| gives a detectable warning (a P-F interval, Module 10) | **condition-based task** (inspect, PdM) | the P-F interval is long enough and consistent enough to act on |
| has a clear wear-out age (β well above 1, Module 06) | **scheduled restoration or replacement** | most units survive to that age and it's cost-effective (Module 09) |
| is hidden (e.g. a standby pump, a safety switch) | **failure-finding task** (test it) | testing is practical and safe |
| has safety/environmental consequences and no task works | **redesign** | (mandatory) |
| has only economic consequences and no task pays | **run to failure** | the cost of failure is acceptable |

### Mini RCM: Line A coolant system

| Function | Functional failure | Failure mode | Consequence | Task |
|---|---|---|---|---|
| Deliver coolant at ≥ 40 L/min, 5 % concentration | No flow | Pump bearing failure | operational (grinder stops) | redundancy (standby pump) + monthly vibration route |
| | Low flow | Filter clogged | operational, quality | condition-based: differential pressure gauge, change at set Δp (replaces fixed weekly change) |
| | Wrong concentration | Concentrate pump fault | quality (burn, oversize) | online concentration monitor with alarm |
| Alarm on low level | Alarm fails to sound (hidden) | Level sensor stuck | multiple failure: pump runs dry | failure-finding: monthly functional test of the level alarm |

Notice the coolant pump: its failures are random (Module 05: exponential), so **a fixed-interval pump replacement would not help**. The right answers are redundancy, condition monitoring and faster restoration.

## Total Productive Maintenance (TPM)

TPM makes equipment care everyone's job, especially operators', and targets the losses measured by OEE. It is commonly described by eight pillars:

| Pillar | What it means on Line A |
|---|---|
| Autonomous maintenance | operators clean, inspect, lubricate and tighten; spot abnormalities early |
| Planned maintenance | maintenance focuses on PM, PdM and improvement, not fire-fighting |
| Focused improvement | cross-functional teams attack the biggest losses (Pareto from Module 05) |
| Quality maintenance | equipment conditions that guarantee zero defects (e.g. coolant concentration) |
| Early equipment management | design-for-reliability lessons fed into new equipment (Module 02) |
| Training and education | precision skills for technicians; equipment knowledge for operators |
| Safety, health and environment | zero accidents as part of equipment care |
| Office / administrative TPM | efficient support processes (parts, planning) |

**Autonomous maintenance steps** usually start with an initial clean-and-inspect ("cleaning is inspecting"), eliminating contamination sources and hard-to-reach areas, and writing standards for daily checks — then build toward operators owning routine care.

## RCM + TPM together

- RCM decides **what** must be done to each failure mode and **why**.
- TPM decides **who** does it and builds the culture and skills to keep it done.
- Many simple condition checks found by RCM (look, listen, feel, gauge readings) are ideal operator tasks.

## Check yourself

1. Why is a monthly test of the low-level alarm called a "failure-finding" task?
2. An RCM review finds a PM "replace coolant pump every 12 months". What would you recommend, and why?
3. Name two autonomous maintenance tasks for the hydraulic press.

<details><summary>Answers</summary>

1. The alarm's failure is hidden — nobody knows it's failed until the pump runs dry. The test doesn't prevent failure; it finds it so it can be fixed before the second failure happens.
2. Drop it. The pump's failures are random (constant hazard), so age-based replacement spends money without reducing risk. Use vibration monitoring, a standby pump, and fast changeover instead.
3. Daily: check oil level and temperature gauge, look for leaks at fittings and seals, check for unusual noise. Weekly: clean the area around the power unit so leaks are visible; check filter indicator.

</details>
