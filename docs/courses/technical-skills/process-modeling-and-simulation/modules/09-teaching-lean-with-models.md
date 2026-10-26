# Module 9 — Using Models to Teach Lean Concepts

**Time:** 40 min

## Learning objectives

1. Use small models to demonstrate core Lean and flow principles.

Simulations make abstract principles visible: people see queues grow and shrink. Four classic demonstrations, all reproducible with `procsim.py` or a few lines of code.

## 1. Utilization and waiting

Waiting grows sharply as utilization approaches 100% — the Kingman approximation:

  Wq ≈ [(CVa² + CVs²) / 2] × [u / (1 − u)] × service time

At u = 0.80 the factor u/(1 − u) is 4; at 0.90 it's 9; at 0.95 it's 19. **Lesson:** "keep everyone 100% busy" guarantees long lead times. Demonstrate by running `Design(arrival_scale=...)` from 0.8 to 1.3 (Module 5 chart).

## 2. Variability is a cost

Same averages, different variability: the repair center with repair-time CV × 1.5 drops ~4 points on time (Module 5). **Lesson:** standard work and stable processes reduce waiting as much as added capacity.

## 3. Batch vs one-piece flow

3 steps of 1 minute each, 20 units:

| | First unit done | Last unit done |
|---|---|---|
| Batch of 20 | 41 min | 60 min |
| One-piece flow | 3 min | 22 min |

The test-batching experiment (Module 6) shows the same effect inside the repair center. **Lesson:** batches create waiting.

## 4. Pooling and flexibility

Six cross-trained techs outperform 2 + 4 specialists, and even beat 2 + 5 (Module 4). **Lesson:** flexibility is capacity.

## Running a teaching session

1. Ask the group to predict the result (write it down).
2. Run the model live.
3. Discuss the gap between prediction and result.
4. Change one thing and repeat.

## Check yourself

A manager wants each technician at 98% utilization. Using the Kingman factor, what happens to waiting compared with 85%?

<details><summary>Answer</summary>

u/(1 − u) goes from 5.7 to 49 — roughly 8–9 times more waiting for the same variability.
</details>
