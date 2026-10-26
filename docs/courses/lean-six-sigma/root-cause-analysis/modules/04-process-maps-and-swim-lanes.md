# Module 4 — Process Flow Charts and Swim Lanes

**Time:** 40 min

## Learning objectives

1. Map a process to see where problems can enter.
2. Use swim lanes to show handoffs between people and departments.

## 1. Why map?

Most problems occur at steps nobody thinks about — handoffs, rework loops, decision points, informal workarounds. Walk the process (go to the gemba) and map what **actually** happens, not what the procedure says.

## 2. Symbols

| Symbol | Meaning |
|---|---|
| Oval | Start / end |
| Rectangle | Activity |
| Diamond | Decision |
| Arrow | Flow |
| D-shape / triangle | Delay / storage |

## 3. Valve cell — flow chart

```
(Start) → Load casting → Rough bore (MC1/2/3) → Finish seal seat → Deburr
        → Wash → Leak test ──◇ Pass? ──Yes──► Mark & pack → (End)
                                 │
                                 No
                                 ▼
                           Retest once ──◇ Pass? ──Yes──► Mark & pack
                                               │
                                               No → Scrap bin → (End)
```

Observations from walking it: (1) tool changes on the finish operation happen "when the finish looks bad" — no rule; (2) failed parts are retested once, so marginal leakers can pass on retest and reach the customer; (3) nobody records which machine made a scrapped part. Each is a lead for the investigation.

## 4. Swim-lane map — tool change process

| Lane | Steps |
|---|---|
| Operator | Notices rough finish → calls setter → waits |
| Setter | Arrives (avg 25 min) → changes insert → runs first part → asks quality |
| Quality | Measures first part Ra → approves |
| Tool crib | Issues insert (only if old one returned) |

Swim lanes expose handoffs and waits: the operator keeps running while waiting for the setter, producing rough parts.

## Check yourself

Why map the process as it is, not as the procedure says?

<details><summary>Answer</summary>

Problems often come from differences between the documented and actual process (workarounds, skipped steps, informal retests).
</details>
