"""Regenerate every dataset in data/ (fixed seed). All data are synthetic.

Case: a valve-body cell (machining + leak test) has rising scrap and customer leak complaints.

    python tools/make_data.py

License: MIT
"""
import csv
import os

import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(1950)


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# 1. Scrap log, 8 weeks: defect type x machine x shift, with unit cost.
types = {"Leak at test": 85, "Bore oversize": 40, "Burr": 30, "Thread damage": 18,
         "Porosity": 12, "Scratch": 9, "Wrong marking": 6}
cost = {"Leak at test": 140, "Bore oversize": 95, "Burr": 20, "Thread damage": 95,
        "Porosity": 140, "Scratch": 15, "Wrong marking": 10}
rows = []
for t, n in types.items():
    for _ in range(n):
        if t == "Leak at test":
            m = rng.choice(["MC1", "MC2", "MC3"], p=[0.16, 0.18, 0.66])  # MC3 dominates leaks
        else:
            m = rng.choice(["MC1", "MC2", "MC3"])
        s = rng.choice(["Day", "Night"])
        wk = int(rng.integers(1, 9))
        rows.append([wk, t, m, s, cost[t]])
rows.sort()
write("scrap_log.csv", ["week", "defect", "machine", "shift", "cost_usd"], rows)

# 2. Seal seat surface roughness vs spindle hours since tool change (scatter + simple regression).
hrs = np.round(rng.uniform(0, 40, 35), 1)
ra = np.round(0.35 + 0.018 * hrs + rng.normal(0, 0.08, 35), 3)
write("tool_wear.csv", ["hours_since_tool_change", "seat_ra_um"], list(zip(hrs, ra)))

# 3. Leak rate (continuous) vs process inputs, 60 valves (multiple regression).
n = 60
ra_seat = rng.uniform(0.3, 1.2, n)
torque = rng.uniform(18, 26, n)
temp = rng.uniform(18, 32, n)
humidity = 0.6 * temp + rng.normal(0, 2.5, n) + 20  # correlated with temperature (a trap)
gasket = rng.uniform(1.90, 2.10, n)
leak = 2.0 + 3.2 * ra_seat - 0.12 * (torque - 22) + 0.02 * (temp - 25) + rng.normal(0, 0.45, n)
write("leak_rate.csv", ["valve", "seat_ra_um", "torque_nm", "ambient_c", "humidity_pct", "gasket_mm", "leak_ccm"],
      [[i + 1, f"{a:.2f}", f"{b:.1f}", f"{c:.1f}", f"{d:.1f}", f"{e:.3f}", f"{f:.2f}"]
       for i, (a, b, c, d, e, f) in enumerate(zip(ra_seat, torque, temp, humidity, gasket, leak))])

# 4. Leak test pass/fail (binary) vs seat roughness and torque, 200 valves (logistic regression).
n = 200
ra_b = rng.uniform(0.3, 1.3, n)
tq_b = rng.uniform(18, 26, n)
logit = -6.0 + 6.5 * ra_b - 0.25 * (tq_b - 22)
p = 1 / (1 + np.exp(-logit))
fail = rng.binomial(1, p)
write("leak_test.csv", ["valve", "seat_ra_um", "torque_nm", "fail"],
      [[i + 1, f"{a:.2f}", f"{b:.1f}", int(c)] for i, (a, b, c) in enumerate(zip(ra_b, tq_b, fail))])

print("datasets written to", os.path.abspath(OUT))
