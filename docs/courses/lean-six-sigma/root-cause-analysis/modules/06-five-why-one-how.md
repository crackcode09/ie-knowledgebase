# Module 6 — 5-Why, 1-How Analysis

**Time:** 40 min

## Learning objectives

1. Drill from a symptom to a root cause by asking "why" until cause connects to effect.
2. Check the chain in both directions and attach a "how" (countermeasure).

## 1. The method

Associated with Taiichi Ohno and the Toyota Production System: ask "why?" repeatedly — usually about five times, but stop when you reach a cause you can act on that prevents recurrence. Then ask **one "how"**: how will we remove that cause?

## 2. Valve leaks

| Why? | Answer | Evidence |
|---|---|---|
| 1. Why did the valve leak? | The seal seat was too rough to seal | Failure probability rises steeply with seat Ra (Module 12); leak rate tracks Ra (Module 11) |
| 2. Why was the seat rough? | The finishing insert was worn | Ra rises with tool hours (Module 9) |
| 3. Why was a worn insert in use? | Inserts are changed only when the finish "looks bad" | Process walk (Module 4) |
| 4. Why is there no tool-life rule? | The finishing operation was never given a tool-life limit when the part was introduced | Process documents |
| 5. Why wasn't it caught? | Ra isn't measured in-process; leak test catches it only at the end — and the retest lets marginal parts through | Flow chart (Module 4) |

**Root causes:** no tool-life control on the finishing operation, and no in-process roughness check (plus a retest practice that lets marginal parts escape).

**1-How:** set a tool-life limit from data (Module 10), add an in-process Ra check, stop "retest until pass." Then ask *how* to prevent the same gap on other operations (preventive action).

## 3. Check the logic

- **Forward test:** read it bottom-up using "therefore." *No tool-life rule → therefore worn inserts stay in → therefore rough seats → therefore leaks.* If it doesn't read naturally, a step is missing or wrong.
- **Evidence at each step:** every answer should be backed by data or observation, not opinion.

## 4. Pitfalls

- Stopping at "operator error" or "machine failure."
- Following a single chain when several causes combine (use a root cause tree — Module 7).
- Answers based on opinion. If you don't know, the answer is "we need to check."

## Check yourself

A 5-Why ends with "the operator didn't follow the procedure." Continue it.

<details><summary>Answer</summary>

Why? (procedure unclear, not trained, not practical at takt, no feedback when wrong). Why was that possible? (no error-proofing, no standard work check). The root cause is in the system that allowed the deviation.
</details>
