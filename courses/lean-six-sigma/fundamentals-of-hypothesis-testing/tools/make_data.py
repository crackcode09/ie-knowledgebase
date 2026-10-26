"""Regenerate every dataset in data/ (fixed seed, fully reproducible). All data are synthetic.

    python tools/make_data.py

License: MIT
"""
import csv
import os

import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(1931)


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# 1. One mean vs standard: bearing outer diameter, nominal 25.000 mm, 20 parts.
od = 25.000 + 0.004 + rng.normal(0, 0.006, 20)
write("bearing_od.csv", ["part", "od_mm"], [[i + 1, f"{v:.4f}"] for i, v in enumerate(od)])

# 2. Two independent means: hardness (HRC) from two steel suppliers, 15 bars each.
a = rng.normal(58.0, 1.2, 15)
b = rng.normal(59.4, 1.2, 15)
write("supplier_hardness.csv", ["supplier", "hrc"],
      [["A", f"{v:.1f}"] for v in a] + [["B", f"{v:.1f}"] for v in b])

# 3. Paired means: same 12 parts measured on the old and the new height gauge.
true = rng.normal(40.0, 0.05, 12)
old = true + rng.normal(0, 0.004, 12)
new = true + 0.006 + rng.normal(0, 0.004, 12)
write("gauge_paired.csv", ["part", "old_mm", "new_mm"],
      [[i + 1, f"{o:.4f}", f"{n:.4f}"] for i, (o, n) in enumerate(zip(old, new))])

# 4. Several means: coating thickness (um) on three plating lines, 10 parts each.
rows = []
for line, mu in (("L1", 25.0), ("L2", 25.4), ("L3", 26.6)):
    rows += [[line, f"{v:.2f}"] for v in rng.normal(mu, 0.9, 10)]
write("coating_thickness.csv", ["line", "um"], rows)

# 5. One proportion: incoming inspection, 400 parts, supplier claims <= 3% defective.
write("incoming_inspection.csv", ["inspected", "defective", "claimed_rate"], [[400, 21, 0.03]])

# 6. Two proportions: defectives on day vs night shift.
write("shift_defectives.csv", ["shift", "inspected", "defective"], [["day", 500, 17], ["night", 520, 35]])

# 7. Several proportions / contingency: defect type by machine.
write("defects_by_machine.csv", ["machine", "burr", "scratch", "dimension", "other"],
      [["M1", 22, 15, 8, 5], ["M2", 18, 21, 9, 4], ["M3", 12, 14, 26, 6]])

# 8. One variance: torque (N*m) on a fastening station, spec requires sigma <= 0.50.
tq = rng.normal(12.0, 0.62, 25)
write("torque.csv", ["sample", "nm"], [[i + 1, f"{v:.2f}"] for i, v in enumerate(tq)])

# 9. Two variances: cut length (mm) on an old vs a new saw.
old_saw = rng.normal(150.0, 0.40, 16)
new_saw = rng.normal(150.0, 0.22, 16)
write("saw_length.csv", ["saw", "mm"],
      [["old", f"{v:.3f}"] for v in old_saw] + [["new", f"{v:.3f}"] for v in new_saw])

# 10. Nonparametric, two groups: repair turnaround (hours), skewed, before/after a kanban change.
before = rng.lognormal(np.log(30), 0.55, 18)
after = rng.lognormal(np.log(19), 0.55, 18)
write("repair_turnaround.csv", ["period", "hours"],
      [["before", f"{v:.1f}"] for v in before] + [["after", f"{v:.1f}"] for v in after])

# 11. Nonparametric, paired: operator ergonomic discomfort score (0-10) before/after a fixture change.
pre = rng.integers(3, 9, 14)
post = np.clip(pre - rng.choice([0, 1, 1, 2, 2, 3, -1], 14), 0, 10)
write("discomfort_scores.csv", ["operator", "before", "after"],
      [[i + 1, int(p), int(q)] for i, (p, q) in enumerate(zip(pre, post))])

# 12. Treatment comparison with a process behavior chart: daily scrap rate (%) before/after a change.
s = np.r_[rng.normal(4.0, 0.5, 20), rng.normal(3.1, 0.5, 15)]
write("daily_scrap.csv", ["day", "phase", "scrap_pct"],
      [[i + 1, "before" if i < 20 else "after", f"{v:.2f}"] for i, v in enumerate(s)])

# ---- Capstone case files (Module 18) ----
# Case A: tool life (parts per edge) with old vs new coolant, 10 inserts each.
ta = rng.normal(420, 45, 10)
tb = rng.normal(470, 45, 10)
write("case_a_tool_life.csv", ["coolant", "parts"],
      [["old", int(v)] for v in ta] + [["new", int(v)] for v in tb])

# Case B: shipping damage by carrier.
write("case_b_carrier_damage.csv", ["carrier", "shipments", "damaged"],
      [["Carrier1", 240, 9], ["Carrier2", 260, 11], ["Carrier3", 230, 10]])

# Case C: inspection time (min) for 10 inspectors before/after a training course.
base = rng.normal(14.0, 2.5, 10)
cb = base + rng.normal(0, 0.6, 10)
ca = base - 1.1 + rng.normal(0, 0.6, 10)
write("case_c_inspection_time.csv", ["inspector", "before_min", "after_min"],
      [[i + 1, f"{x:.1f}", f"{y:.1f}"] for i, (x, y) in enumerate(zip(cb, ca))])

# Case D: 12 measurements of a 50.000 mm master block on a CMM.
md = 50.000 + 0.0003 + rng.normal(0, 0.0012, 12)
write("case_d_master_block.csv", ["reading", "mm"], [[i + 1, f"{v:.4f}"] for i, v in enumerate(md)])

print("datasets written to", os.path.abspath(OUT))
