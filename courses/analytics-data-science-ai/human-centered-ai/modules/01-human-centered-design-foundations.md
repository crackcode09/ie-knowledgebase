# Module 01 — Human Centered Design Foundations

Core HCD principles, and why starting with people is essential for effective AI initiatives.

## Objectives

- Define the core principles of human-centered design (HCD).
- Explain why HCD is critical to AI readiness and adoption.
- Describe how user needs, behaviors and constraints shape AI solutions.

## What human-centered design is

**Human-centered design** is a way of solving problems that starts with the people who do the work and will use the solution. It understands their needs, behaviors and constraints first, then develops and tests solutions with them in short cycles.

Core principles (as commonly stated, for example in the ISO 9241-210 human-centred design standard; wording here is the course's):

1. **Start from an explicit understanding of users, their tasks and their environment.**
2. **Involve users** throughout, not only at the end.
3. **Let evaluation with users drive the design**, and refine it as you learn.
4. **Iterate.** Expect to be wrong at first; learn in small, cheap steps.
5. **Design for the whole experience**: the work around the tool, not only the screen.
6. **Use a multidisciplinary team**: frontline experts, engineers, IT, data, operations.

A common way to picture the flow is a "double diamond": first widen, then narrow, on the **problem**; then widen, then narrow, on the **solution**.

```
   Discover  ─►  Define      │   Develop  ─►  Deliver
   (diverge)     (converge)  │   (diverge)    (converge)
   ◄──── right problem ─────►│◄──── right solution ────►
```

## Why HCD matters for AI

AI tools succeed or fail on **adoption**. People use, trust, work around or reject them. The common reasons for rejection are human, not technical:

| What goes wrong | HCD counter |
|---|---|
| The tool solves a problem users don't have | Discover real needs before choosing a solution |
| It doesn't fit the work: gloves, noise, 30-second windows, no free hands | Observe the work environment; design for its constraints |
| Users don't trust outputs they can't trace | Learn what evidence users need in order to act |
| It adds steps or screens to an already busy job | Map the workflow; remove more work than you add |
| Users weren't involved, so feel it was done *to* them | Co-design and test with them from the start |

HCD complements the problem-first and Lean approach of the [Efficient AI](../../efficient-ai/README.md) course. Lean asks which problem creates the most waste; HCD asks what the problem is like for the people living it.

## How needs, behaviors and constraints shape AI solutions

At Halvorsen Components (fictional, the same company as in Efficient AI), the first idea was a chatbot on the office PCs. Eight interviews (Module 02) changed the design:

| Insight | Design implication |
|---|---|
| Operators wear gloves; the machine area is loud | No touch-only screen; no voice-only interface. Large-button rugged tablet; scan a job barcode to start |
| Technicians ask a specific question in the middle of a job | Answer at the machine, in seconds, scoped to the current machine and job |
| People don't trust numbers they can't trace | Show the source passage and revision with every answer |
| Know-how lives in a few experts | Add a way for experts to review and add answers |

## Check yourself

1. Name three HCD principles.
2. Why might an accurate AI tool still fail to be adopted?

<details><summary>Answers</summary>

1. Any three of: understand users, tasks and environment; involve users throughout; user evaluation drives the design; iterate; design the whole experience; multidisciplinary team.
2. It may not fit the work (environment, time, workflow), may not address a real need, may not show enough evidence to be trusted, or may add work. Accuracy is necessary but not enough.

</details>
