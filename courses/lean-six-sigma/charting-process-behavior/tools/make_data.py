"""Regenerate every dataset in data/ (fixed seeds, fully reproducible).

    python tools/make_data.py

All data are synthetic. License: MIT
"""
import csv
import os

import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT, exist_ok=True)


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


rng = np.random.default_rng(2026)

# 1. Shaft diameter (mm), one part per hour. Spec 12.70 +/- 0.04.
#    Points 1-20 stable; from point 21 the process mean shifts up 0.015 mm.
x = 12.700 + rng.normal(0, 0.008, 30)
x[20:] += 0.015
write("shaft_diameter.csv", ["hour", "value"], [[i + 1, f"{v:.4f}"] for i, v in enumerate(x)])

# 2. Bore diameter (mm), 25 subgroups of 5 consecutive parts every 2 hours.
#    Subgroup 17: tool chip -> wider spread and higher mean.
s = 25.000 + rng.normal(0, 0.006, (25, 5))
s[16] += rng.normal(0.012, 0.012, 5)
write("bore_subgroups.csv", ["subgroup", "x1", "x2", "x3", "x4", "x5"],
      [[i + 1] + [f"{v:.4f}" for v in r] for i, r in enumerate(s)])

# 3. Daily final-inspection defectives (variable lot size). Day 14: bad material lot.
n = rng.integers(180, 320, 22)
p = np.full(22, 0.04)
p[13] = 0.11
d = rng.binomial(n, p)
write("daily_defectives.csv", ["day", "inspected", "defective"],
      [[i + 1, int(a), int(b)] for i, (a, b) in enumerate(zip(n, d))])

# 4. Surface blemishes per painted panel (same panel size), 25 panels.
c = rng.poisson(4.0, 25)
c[19] = rng.poisson(13)
write("panel_blemishes.csv", ["panel", "defects"], [[i + 1, int(v)] for i, v in enumerate(c)])

# 5. Blemishes on sheets of varying area (u-chart).
area = np.round(rng.uniform(1.5, 4.0, 20), 2)
cu = rng.poisson(1.8 * area)
write("sheet_blemishes.csv", ["sheet", "area_m2", "defects"],
      [[i + 1, a, int(v)] for i, (a, v) in enumerate(zip(area, cu))])

# 6. Order-to-ship cycle time (days), 40 orders, for run-chart practice.
ct = np.round(rng.lognormal(np.log(4.0), 0.25, 40), 1)
ct[25:] = np.round(ct[25:] * 0.8, 1)  # improvement implemented after order 25
write("cycle_time.csv", ["order", "days"], [[i + 1, v] for i, v in enumerate(ct)])

# 7. Surface roughness Ra (um): skewed, one-sided spec USL = 1.6.
ra = np.round(rng.lognormal(np.log(0.6), 0.35, 60), 3)
write("roughness_ra.csv", ["part", "value"], [[i + 1, v] for i, v in enumerate(ra)])

# 8. Two-machine stratification: fill weight (g) from two filler heads, interleaved.
w = []
for i in range(40):
    head = "A" if i % 2 == 0 else "B"
    mu = 500.0 if head == "A" else 503.0
    w.append([i + 1, head, f"{mu + rng.normal(0, 1.0):.2f}"])
write("fill_weight.csv", ["sample", "head", "value"], w)

print("datasets written to", os.path.abspath(OUT))
