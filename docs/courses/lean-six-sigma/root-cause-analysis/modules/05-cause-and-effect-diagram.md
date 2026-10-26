# Module 5 — Cause-and-Effect (Fishbone) Diagram

**Time:** 45 min

## Learning objectives

1. Build a cause-and-effect diagram to identify and organize potential causes.
2. Separate potential causes from verified causes.

## 1. The tool

Kaoru Ishikawa popularized the cause-and-effect diagram in the 1940s–60s. The effect (problem statement) is the "head"; major categories are the "bones"; brainstormed causes hang off each bone. In manufacturing, the **6M** categories are a common start: Machine, Method, Material, Measurement, Man/People, Mother Nature (environment). For services, use e.g. Policies, Procedures, People, Place, Systems.

## 2. Valve leaks — fishbone

```
Machine                    Method                      Material
  │ worn finishing tool       │ no tool-life limit         │ casting porosity
  │ spindle runout (MC3?)     │ clamp torque not specified │ gasket thickness variation
  │ coolant concentration     │ retest-until-pass          │ insert grade change
  └──────────────┬────────────┴──────────────┬────────────┘
                 ├──────────────────────────────────────────►  Valve bodies fail
  ┌──────────────┴────────────┬──────────────┴────────────┐     helium leak test
  │ leak tester repeatability │ new operators on nights    │ ambient temperature
  │ Ra not measured in-process│ setter response time       │ humidity
Measurement                 People                      Environment
```

## 3. Using it well

- Brainstorm causes; don't evaluate during brainstorming.
- Keep going to specific, testable causes ("worn finishing tool", not "machine problems").
- Mark each cause: **verified by data**, **ruled out**, or **to test**. A fishbone lists *possible* causes; only data verify them.
- Prioritize what to test with the team's knowledge plus the Is/Is-Not clues (Module 1): MC3-heavy, seat area, varies over time → tool wear and spindle condition rise to the top. Humidity is a popular suspect — Module 11 tests it.

## Check yourself

The fishbone has 40 causes. What next?

<details><summary>Answer</summary>

Prioritize using evidence (Is/Is-Not, stratification, team voting on likelihood), then test the top few with data — don't try to fix all 40.
</details>
