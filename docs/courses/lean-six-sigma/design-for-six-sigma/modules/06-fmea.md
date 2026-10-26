# Module 6 — Failure Mode and Effects Analysis (FMEA)

**Time:** 4 h · **Phase:** Design

## Learning objectives

1. Build a design or process FMEA.
2. Rate severity, occurrence and detection; compute RPN.
3. Prioritize actions correctly — including when RPN misleads.

## 1. What FMEA does

A team systematically asks, for each function or process step: *How could it fail? What would happen? Why? How would we know?* — and acts on the biggest risks **before** they happen.

- **DFMEA** (design): failure modes of the product's functions.
- **PFMEA** (process): failure modes of manufacturing/assembly steps.

## 2. The columns

| Column | Question |
|---|---|
| Item / step | What function or process step? |
| Failure mode | How can it fail to do its job? |
| Effect | What does the customer (next step or end user) experience? |
| **Severity (S)** 1–10 | How bad is the effect? (9–10: safety/regulatory) |
| Cause | Why would the failure mode occur? |
| **Occurrence (O)** 1–10 | How likely is the cause? |
| Current controls | Prevention and detection in place today |
| **Detection (D)** 1–10 | How likely is it to escape? (10 = cannot detect) |
| RPN | S × O × D |
| Actions, owner, date | What will reduce the risk? |
| Revised S, O, D, RPN | After actions |

## 3. Worked example — carriage assembly PFMEA (extract)

| Failure mode | S | O | D | RPN |
|---|---|---|---|---|
| Preload too high | 7 | 5 | 5 | **175** |
| Wiper seal omitted | 6 | 4 | 7 | **168** |
| Wrong lubricant applied | 7 | 2 | 8 | 112 |
| Rail mounting holes mislocated | **8** | 3 | 4 | 96 |
| Carriage scratched in handling | 4 | 6 | 3 | 72 |

```bash
python tools/dfss.py fmea
```

## 4. Prioritizing — beyond RPN

RPN has known weaknesses: the same RPN can come from very different risks (S=10, O=1, D=10 → 100; S=2, O=5, D=10 → 100), and the scales are ordinal, so multiplying them is mathematically questionable. Good practice:

1. **Severity first:** any S ≥ 9 gets action regardless of RPN.
2. **Then S × O** (criticality).
3. **Then RPN.**

The AIAG & VDA FMEA Handbook (1st ed., 2019) replaced RPN with **Action Priority (AP)** tables (High/Medium/Low) based on S, O and D in that order of importance.

Here, the top RPNs (preload, wiper seal) are sensible priorities. "Wrong lubricant" has O = 2 but D = 8: a rare error that would almost certainly escape — a classic **error-proofing** target (Module 7).

## 5. Actions: prefer prevention

| Action type | Lowers | Example |
|---|---|---|
| Design change | S or O | Asymmetric seal geometry so it can't be omitted without visible gap |
| Process change / error-proofing | O | Dedicated lube dispenser that only accepts the correct cartridge |
| Better detection | D | 100% automated friction-force check (catches high preload) |

Detection improvements are the weakest — they catch defects after they're made.

## Check yourself

1. Two failure modes: S=10, O=2, D=2 (RPN 40) and S=4, O=6, D=6 (RPN 144). Which first?
2. Why is reducing occurrence preferred to improving detection?

<details><summary>Answers</summary>

1. The S = 10 mode — safety-level severity takes priority regardless of RPN.
2. Prevention avoids making the defect at all; detection still produces it (scrap, rework, and escapes when inspection fails).
</details>
