# Module 1 — Lean and DMAIC; Kaizen Measurements and Baseline Performance

**Time:** 75 min

## Learning objectives

1. Map a kaizen event onto the DMAIC phases.
2. Choose kaizen metrics and establish baseline performance.
3. Compute lead time with Little's law and process cycle efficiency.

## 1. Kaizen inside DMAIC

| DMAIC | Kaizen equivalent |
|---|---|
| Define | Pre-work: charter, scope, SIPOC |
| Measure | Pre-work baseline + Day 1 current state |
| Analyze | Day 2 root causes |
| Improve | Days 3–4 implementation |
| Control | Day 5 standard work, control plan + 30/60/90 follow-up |

A kaizen compresses DMAIC into a week, which works only when pre-work has done the Define and much of the Measure. Lean asks "where is the waste and how does work flow?"; Six Sigma asks "what causes the variation?" Kaizen events use both.

## 2. Kaizen metrics

Pick 3–6 metrics that reflect the charter goal, are measurable before and after, and the team can affect during the week.

| Category | Metric |
|---|---|
| Flow | Lead time, WIP, process cycle efficiency |
| Productivity | Output per hour, output per operator, takt attainment |
| Quality | First-pass yield, defects |
| Equipment | Changeover time, OEE (Module 13) |
| Space and motion | Floor space, walking distance |
| Safety and people | Ergonomic risk score, team ideas implemented |

## 3. Baseline performance — case

```bash
python tools/kaizen.py baseline
```

| Measure | Value |
|---|---|
| Available time | 2 shifts × 450 min − 60 min = **840 min/day** |
| Customer demand | **560 units/day** |
| Takt time | 840 × 60 / 560 = **90 s** |
| Actual output (20-day average) | **465 units/day** — below demand |
| Total WIP + finished goods | **5,170 units** |
| Lead time (Little's law: WIP ÷ demand) | 5,170 / 560 = **9.2 days** |
| Value-added time per unit | **385 s** (sum of cycle times) |
| Process cycle efficiency (PCE) | 385 s / (9.2 days × 840 min × 60) = **0.08%** |

**Little's law** (lead time = WIP ÷ throughput) gives lead time from a WIP count, without tracking units. Using demand as the throughput is the usual value stream mapping convention; using actual output (465/day) gives 11 days.

A PCE well below 1% is typical in batch-and-queue manufacturing: a unit spends almost all its time waiting.

## 4. Getting a good baseline

- Use data from a normal period (several weeks); plot it in time order (Module 12).
- Measure the same way before and after (same definitions, same shifts).
- Photograph the area before the event.

## Check yourself

A process has 1,200 units of WIP and ships 300 units/day. Value-added time is 20 min. Lead time and PCE (8-hour day)?

<details><summary>Answer</summary>

Lead time = 1,200/300 = 4 days = 1,920 working min. PCE = 20/1,920 ≈ 1.0%.
</details>
