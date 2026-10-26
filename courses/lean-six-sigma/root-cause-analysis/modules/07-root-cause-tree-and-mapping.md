# Module 7 — Root Cause Tree Analysis and Comprehensive Root Cause Mapping

**Time:** 75 min

## Learning objectives

1. Build a root cause tree for problems with several interacting causes.
2. Use AND/OR logic to show how causes combine.
3. Apply the tree to a case study.

## 1. When 5-Why isn't enough

Real failures often need **several** conditions at once, and several independent routes can produce the same failure. A root cause tree (similar in spirit to fault tree analysis) shows this structure:

- **OR** branch: any one of the causes below produces the event.
- **AND** branch: all causes below must be present together.

## 2. Case study — leaking valves reached the customer

```
Leaking valve reached customer
└── AND
    ├── Valve was a leaker
    │   └── OR
    │       ├── Seal seat too rough
    │       │   └── AND
    │       │       ├── Finishing insert worn         ← no tool-life limit (ROOT)
    │       │       └── Roughness not checked in-process ← no Ra gauge/plan (ROOT)
    │       ├── Casting porosity at seat                (tested: 12 porosity rejects, not seat-related → ruled out as main cause)
    │       └── Gasket out of tolerance                 (tested: not significant, Module 11 → ruled out)
    └── Leak test didn't stop it
        └── OR
            ├── Marginal part passed on retest          ← "retest until pass" practice (ROOT)
            └── Tester not repeatable at the limit      (to verify: gauge study on LT-1)
```

**Reading:** to reach the customer, a leaker had to be made **and** escape. Fixing either branch reduces escapes; fixing both makes recurrence very unlikely. The tree also shows branches that were **tested and ruled out** — that record matters as much as the root causes.

## 3. Comprehensive root cause mapping

For larger events (major quality escapes, safety incidents), map every contributing factor across levels:

| Level | Question | Valve case |
|---|---|---|
| Physical | What failed physically? | Rough seat surface |
| Human | What decisions or actions contributed? | Continuing to run after noticing finish; retesting failures |
| Latent / system | What policies, designs or management systems allowed it? | No tool-life standard; launch checklist had no in-process controls; retest practice never questioned |

Fix at the latent/system level, because those causes produce many future problems, not only this one.

## 4. Tips

- Each box is a fact or hypothesis — label which, and attach evidence.
- Stop a branch when you reach a cause the organization controls and can change.
- Review the tree with people who do the work.

## Check yourself

Why does the "escape" branch need its own analysis even if the "made" branch is fixed?

<details><summary>Answer</summary>

Other causes will eventually create leakers (new tool, new material); an effective detection barrier protects the customer from causes you haven't found yet.
</details>
