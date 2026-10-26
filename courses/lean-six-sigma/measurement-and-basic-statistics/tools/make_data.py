"""Regenerate every dataset in data/ (fixed seed). All data are synthetic.

    python tools/make_data.py

License: MIT
"""
import csv
import os

import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(1924)


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# 1. Customer complaints by category, last quarter (Pareto), with cost per complaint.
cats = [("Late delivery", 64, 120), ("Wrong part shipped", 31, 450), ("Damaged in transit", 22, 300),
        ("Dimension out of tolerance", 14, 1800), ("Missing paperwork", 9, 60),
        ("Surface finish", 6, 900), ("Invoice error", 5, 80), ("Other", 4, 150)]
rows = []
for c, n, cost in cats:
    rows += [[c, cost] for _ in range(n)]
order = rng.permutation(len(rows))
write("complaints.csv", ["category", "cost_usd"], [[i + 1] + rows[j] for i, j in enumerate(order)])
# add header fix: complaint id first
with open(os.path.join(OUT, "complaints.csv")) as f:
    body = f.read().splitlines()[1:]
with open(os.path.join(OUT, "complaints.csv"), "w") as f:
    f.write("complaint_id,category,cost_usd\n" + "\n".join(body) + "\n")

# 2. Shaft diameter, 100 parts (mm): roughly normal, nominal 12.700.
d = 12.700 + rng.normal(0.002, 0.010, 100)
write("shaft_diameter.csv", ["part", "mm"], [[i + 1, f"{v:.3f}"] for i, v in enumerate(d)])

# 3. Order lead time (days), 60 orders: right-skewed.
lt = np.round(rng.lognormal(np.log(5), 0.5, 60), 1)
write("lead_time.csv", ["order", "days"], [[i + 1, v] for i, v in enumerate(lt)])

# 4. Two suppliers, same average, different spread (why averages mislead). Spec 10.00 +/- 0.30.
a = rng.normal(10.00, 0.06, 30)
b = rng.normal(10.00, 0.16, 30)
a += 10.00 - a.mean()
b += 10.00 - b.mean()
write("supplier_thickness.csv", ["supplier", "mm"],
      [["A", f"{v:.3f}"] for v in a] + [["B", f"{v:.3f}"] for v in b])

# 5. Accuracy vs precision: four gauges each measure a 25.000 mm reference block 10 times.
g = {"G1": (0.000, 0.002), "G2": (0.000, 0.012), "G3": (0.015, 0.002), "G4": (0.015, 0.012)}
rows = []
for k, (bias, sd) in g.items():
    rows += [[k, f"{25.000 + bias + v:.4f}"] for v in rng.normal(0, sd, 10)]
write("gauge_reference.csv", ["gauge", "mm"], rows)

# 6. Fill weight from two filling heads mixed together (bimodal histogram).
fa = rng.normal(498.0, 1.0, 50)
fb = rng.normal(503.0, 1.0, 50)
rows = [["A", f"{v:.1f}"] for v in fa] + [["B", f"{v:.1f}"] for v in fb]
rows = [rows[i] for i in rng.permutation(100)]
write("fill_weight.csv", ["sample", "head", "g"], [[i + 1] + r for i, r in enumerate(rows)])

# 7. Daily output for a week, 3 shifts (averages hide a struggling shift).
write("shift_output.csv", ["day", "shift1", "shift2", "shift3"],
      [[d, int(s1), int(s2), int(s3)] for d, s1, s2, s3 in zip(
          ["Mon", "Tue", "Wed", "Thu", "Fri"],
          rng.normal(410, 8, 5), rng.normal(405, 8, 5), rng.normal(330, 25, 5))])

print("datasets written to", os.path.abspath(OUT))
