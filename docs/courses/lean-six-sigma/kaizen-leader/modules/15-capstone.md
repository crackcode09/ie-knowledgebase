# Module 15 — Capstone: Plan and Lead a Kaizen Event

**Time:** 4–6 h (paper exercise) or a real event

## Option A — Real event

Plan and lead (or co-lead) a kaizen on a real process. Submit: charter, SIPOC, pre-work checklist, current-state VSM with timeline, takt and constraint analysis, root cause summary, A3, before/after metrics with a process behavior chart, standard work for one station, control plan, 30/60/90 plan.

## Option B — Paper case: order-entry kaizen (transactional)

**Situation.** Customer orders for configured linear guides go through: Receive (email) → Check configuration → Credit check → Enter in ERP → Engineering review (only for specials) → Confirm to customer. Demand: 120 orders/day, one 8-hour shift (450 min available).

| Step | C/T (min/order) | Staff | Queue before step (orders) | First-pass yield |
|---|---|---|---|---|
| Receive | 1.5 | 1 | 40 | 100% |
| Check configuration | 6.0 | 2 | 95 | 82% (rest returned to customer for clarification) |
| Credit check | 2.0 | 1 | 30 | 98% |
| Enter in ERP | 4.0 | 2 | 60 | 95% |
| Engineering review (25% of orders) | 20.0 | 1 | 70 | 100% |
| Confirm | 1.5 | 1 | 25 | 100% |

**Tasks**

1. Compute takt.
2. For each step compute the effective time per order per staff member and compare with takt. Remember engineering only sees 25% of orders. Which step is the constraint?
3. Compute total queue, lead time (Little's law) and PCE.
4. Draw the current-state VSM and identify the 3 biggest wastes (use DOWNTIME).
5. Propose a future state (e.g., configuration check at order entry with a configurator, standard specials, FIFO lanes, level release) and estimate the new lead time.
6. Write the A3 and a 30/60/90 plan.

Solutions: `solutions/README.md`.

## Rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope and charter | Vague | Clear but too big | Clear, achievable in a week, measurable goals |
| Current state | Opinions | Map without data | Map with data, takt, constraint, timeline |
| Root causes | Missing | Listed | Verified with data/observation |
| Solutions | Generic | Specific | Specific, tied to causes and constraint, error-proofed |
| Results and sustain | Missing | Before/after numbers | Chart-based evidence + control plan + follow-up |
