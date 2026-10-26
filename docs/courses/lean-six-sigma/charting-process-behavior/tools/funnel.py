"""Deming's funnel experiment, simulated in one dimension.

A marble is dropped through a funnel aimed at a target (0). Where it lands
= funnel position + random noise (sd = 1). Four adjustment rules:

  Rule 1: never move the funnel.
  Rule 2: after each drop, move the funnel from its CURRENT spot by -error.
  Rule 3: set the funnel at -error measured from the TARGET.
  Rule 4: set the funnel over the spot where the last marble landed.

    python tools/funnel.py

License: MIT
"""
import numpy as np


def run(rule, n=1000, seed=7):
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, 1, n)
    funnel, out = 0.0, np.empty(n)
    for i in range(n):
        z = funnel + noise[i]
        out[i] = z
        if rule == 2:
            funnel -= z
        elif rule == 3:
            funnel = -z
        elif rule == 4:
            funnel = z
    return out


if __name__ == "__main__":
    for r in (1, 2, 3, 4):
        z = run(r)
        print(f"Rule {r}: sd of landing spots = {z.std():8.2f}   last 100 drops sd = {z[-100:].std():8.2f}"
              f"   mean of last 100 = {z[-100:].mean():8.2f}")
