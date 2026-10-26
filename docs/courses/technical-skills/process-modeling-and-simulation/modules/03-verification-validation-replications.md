# Module 3 — Verification, Validation and Replications

**Time:** 50 min

## Learning objectives

1. Verify that a model works as intended.
2. Validate it against reality.
3. Use replications and confidence intervals to report results honestly.

## 1. Verification — is the model built right?

- Run with **no variation**: does it match hand calculations?
- Trace a few jobs step by step through the event list.
- Check conservation: arrivals = completions + jobs still in system.
- Check extremes: zero demand → zero waiting; huge demand → queues grow.
- Check utilizations against the static calculation (Module 0): simulated diag 0.80, repair 0.88, test 0.59 match static 0.80, 0.89, 0.60.

## 2. Validation — is it the right model?

Compare model outputs with real history over the same conditions:

```bash
python tools/procsim.py validate
```

| | Units/day | Mean lead (h) | p90 lead (h) | On time |
|---|---|---|---|---|
| Model v1 (no parts waits) | 49.2 | 4.13 | 6.94 | 95.2% |
| **Model v2 (25% wait ~3 h for parts)** | 49.8 | **4.80** | **8.19** | **88.7%** |
| History, last 3 months (illustrative) | 50 | 4.9 | 8.4 | 88% |

Version 1 was too optimistic. Asking "what's missing?" led to the parts waits found in job records; version 2 matches history within a few percent. **A model that disagrees with reality is information**: it shows something you didn't understand about the process.

Also validate **face validity**: walk technicians through the animation or the event trace — "does this look like your day?"

## 3. Replications and confidence intervals

One simulated day is one random sample. Run many independent days (replications) and report the mean with a confidence interval:

  CI = mean ± t × s / √n

The baseline's daily on-time rate over 200 simulated days: **88.1% to 91.1%** (95% CI of the daily mean; the job-weighted overall rate is 88.7%).

**When comparing designs**, use the same random-number seed (common random numbers) so differences come from the design, not luck — `procsim.py` does this by default — and check that differences are larger than the CI widths.

**Terminating vs steady-state:** this model restarts empty each day (terminating), so no warm-up period is needed. Models of continuously running processes need a warm-up period discarded before collecting statistics.

## Check yourself

Design X gives 92.1% on time and design Y 91.6%, each from 20 simulated days with CIs of ±1.5 points. Is X better?

<details><summary>Answer</summary>

Not demonstrably — the difference is smaller than the uncertainty. Run more replications (with common random numbers) before deciding.
</details>
