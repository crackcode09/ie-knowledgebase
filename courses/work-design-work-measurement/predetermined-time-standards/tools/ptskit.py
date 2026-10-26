"""ptskit.py - teaching code card and calculations for the Predetermined Time Standards course.

IMPORTANT: the code card below (the "Open Teaching Card", OTC) is ORIGINAL to this course and is for
learning the method only. It is NOT the MODAPTS code card, NOT MTM or MOST, and its values are not
validated for setting real work standards. Use a licensed system and trained analysts for real standards.

Running case: Kessler Components (fictional) assembles and packs small electromechanical parts.

    python tools/ptskit.py data          # (re)write data/*.csv
    python tools/ptskit.py all           # every worked example
    python tools/ptskit.py <name>        # card, units, tasks, improve, ergonomics, standard, practice

Requires pandas. License: MIT
"""
from __future__ import annotations

import os
import re
import sys

import pandas as pd

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")

U_SECONDS = 0.1          # one teaching unit (U) = 0.1 s at normal pace
PFD = 0.12               # allowance used in the examples, % of normal time

# code letter -> (class, meaning). The integer after the letter IS the time in U (modular coding).
CARD = [
    # movement class (body member that does the motion)
    ("A2", "movement", "finger movement (≈ up to 3 cm)"),
    ("A3", "movement", "hand / wrist movement (≈ 3-10 cm)"),
    ("A4", "movement", "forearm movement (≈ 10-25 cm)"),
    ("A6", "movement", "whole-arm movement (≈ 25-45 cm)"),
    ("A8", "movement", "extended arm with shoulder (≈ 45-65 cm)"),
    ("A12", "movement", "arm plus trunk lean (beyond ≈ 65 cm, feet stay in place)"),
    # terminal class: GET
    ("G0", "get", "contact get: touch, push or slide; no closing of the fingers"),
    ("G2", "get", "simple get: easy-to-grasp object, low conscious control"),
    ("G5", "get", "selective get: small, tangled, mixed or fragile object; eyes must guide the fingers"),
    # terminal class: PUT
    ("P0", "put", "toss or release: no alignment"),
    ("P3", "put", "put with one alignment, loose fit; low conscious control"),
    ("P6", "put", "put with two or more alignments or a tight fit; high conscious control"),
    ("C2", "put", "each additional correction during a high-control put"),
    # auxiliary class
    ("W6", "auxiliary", "walk, per step"),
    ("F4", "auxiliary", "foot or leg action (pedal), per action"),
    ("B22", "auxiliary", "bend and arise (or stoop to below knee height and return)"),
    ("S20", "auxiliary", "sit down"),
    ("U22", "auxiliary", "stand up from sitting"),
    ("E3", "auxiliary", "eye focus or eye travel, per occurrence"),
    ("R2", "auxiliary", "read, per word or number group"),
    ("D3", "auxiliary", "decide or judge (simple yes/no), per decision"),
    ("X5", "auxiliary", "apply pressure without movement (press, seat, snap)"),
    ("T2", "auxiliary", "transfer or regrasp between fingers or hands"),
    ("K6", "auxiliary", "crank or turn, per full revolution"),
    ("L1", "auxiliary", "load factor, per loaded move: 1 per 2 kg above 2 kg per hand"),
    ("PT", "process", "process time from the machine or tool, in U (e.g. PT18 = 1.8 s); not a motion"),
]
CODE_RE = re.compile(r"^(PT|[A-Z])(\d+)(?:x(\d+))?$")


def code_value(tok):
    """Return (code, units) for a token such as 'A6', 'W6x3', 'PT18'."""
    m = CODE_RE.match(tok.strip())
    if not m:
        raise ValueError(f"bad code: {tok}")
    letter, val, rep = m.group(1), int(m.group(2)), int(m.group(3) or 1)
    base = f"{letter}{val}" if letter != "PT" else "PT"
    valid = {c for c, _, _ in CARD}
    if base not in valid:
        raise ValueError(f"code not on the teaching card: {tok}")
    return base, val * rep


def units(codes):
    return sum(code_value(t)[1] for t in codes.split())


# ---------------------------------------------------------------- practice tasks (analyses)
# Each step: (description, codes for the limiting hand / whole body). Simultaneous low-control motions of the
# other hand are noted but not coded (the limiting member governs).
TASKS = {
    "A_kit_current": [
        ("Reach to bolt bin, get one bolt from mixed bin", "A6 G5"),
        ("Move bolt to bag held open by left hand, release", "A6 P0"),
        ("Reach to washer bin, get one washer (small, flat)", "A6 G5"),
        ("Move washer to bag, release", "A6 P0"),
        ("Reach to nut bin, get one nut", "A6 G5"),
        ("Move nut to bag, release", "A6 P0"),
        ("Grasp bag top with both hands, press seal closed", "A3 G2 X5"),
        ("Move bag to tote, release", "A6 P0"),
        ("Reach for next empty bag, get from stack (selective: thin film)", "A8 G5"),
        ("Move bag to opening position, open bag (fingers)", "A6 P3 A2"),
    ],
    "A_kit_improved": [
        ("Reach both hands to gravity trays (bolt RH, nut LH, pre-oriented), get both at once", "A4 G2"),
        ("Move both to bag on holder, release (low control: simultaneous)", "A4 P0"),
        ("Reach to washer tray (pre-singulated), get washer", "A4 G2"),
        ("Move washer to bag, release", "A4 P0"),
        ("Press seal: both hands", "A3 G0 X5"),
        ("Slide bag off holder into chute", "A4 P0"),
        ("Pull next bag from roll on holder (perforated, self-opening)", "A3 G0 A3"),
    ],
    "B_pin_assembly": [
        ("Reach to tote, get housing", "A6 G2"),
        ("Move housing to fixture, place on two locating pins", "A6 P6"),
        ("Reach to pin tray, get one dowel pin", "A4 G5"),
        ("Move pin to bore, insert (tight fit, one correction)", "A4 P6 C2"),
        ("Seat pin with thumb", "X5"),
        ("Reach to hanging power driver, get", "A4 G2"),
        ("Move driver to screw 1, engage (bit to recess)", "A4 P6"),
        ("Drive screw 1 (tool time)", "PT18"),
        ("Move driver to screw 2, engage", "A3 P6"),
        ("Drive screw 2 (tool time)", "PT18"),
        ("Release driver to balancer", "A4 P0"),
        ("Look at assembly, decide: pin flush and screws seated?", "E3 D3"),
        ("Get assembly from fixture", "A2 G2"),
        ("Move to outgoing conveyor, place", "A6 P3"),
    ],
    "C_pack_current": [
        ("Walk to carton pallet (3 steps)", "W6x3"),
        ("Bend to pallet (floor level) and arise with carton", "B22"),
        ("Get carton with both hands (8 kg)", "G2"),
        ("Walk back to bench (3 steps), carrying", "W6x3"),
        ("Move carton to bench, place against stop (loaded move: 4 kg per hand)", "A6 L1 P3"),
        ("Read label: part number and quantity (4 groups)", "R2x4"),
        ("Decide: label matches order?", "D3"),
        ("Reach to tape gun, get", "A6 G2"),
        ("Move tape gun to carton seam, place", "A6 P3"),
        ("Pull tape across lid (whole arm)", "A8"),
        ("Aside tape gun", "A6 P0"),
        ("Slide carton to outgoing roller", "A8 G0 A8 P0"),
    ],
    "C_pack_improved": [
        ("Turn to carton lift table at bench height (no walking), get carton (8 kg)", "A6 G2"),
        ("Move carton to bench, place against stop (loaded)", "A6 L1 P3"),
        ("Scan label with fixed scanner (look, decide on beep/light)", "E3 D3"),
        ("Reach to tape gun on holder at seam start, get", "A4 G2"),
        ("Pull tape across lid", "A8"),
        ("Return tape gun to holder", "A4 P3"),
        ("Push carton to outgoing roller", "A8 G0 A8 P0"),
    ],
    "D_cable_capstone": [
        ("Reach to cable pile on bench, get one cable end (tangled)", "A8 G5"),
        ("Move cable end to coiling jig, hook on peg", "A6 P3"),
        ("Turn coiling crank 4 revolutions", "K6x4"),
        ("Reach to twist-tie dispenser, get one tie", "A4 G2"),
        ("Move tie around coil, align both ends", "A4 P6"),
        ("Twist tie ends with fingers (3 twists)", "A2x3"),
        ("Get coil off jig", "A3 G2"),
        ("Move coil to bag on holder, drop in", "A6 P0"),
        ("Read cable label (2 groups) and decide: right length code?", "R2x2 D3"),
    ],
}


def task_table(name):
    rows = []
    for i, (desc, codes) in enumerate(TASKS[name], 1):
        u = units(codes)
        rows.append(dict(step=i, description=desc, codes=codes, units=u, seconds=round(u * U_SECONDS, 1)))
    return pd.DataFrame(rows)


def task_summary(name):
    t = task_table(name)
    toks = " ".join(t.codes).split()
    by = {"movement": 0, "get": 0, "put": 0, "auxiliary": 0, "process": 0}
    cls = {c: k for c, k, _ in CARD}
    for tok in toks:
        base, u = code_value(tok)
        by[cls[base]] += u
    total = int(t.units.sum())
    return dict(task=name, steps=len(t), units=total, normal_s=round(total * U_SECONDS, 1),
                standard_s=round(total * U_SECONDS * (1 + PFD), 2), by_class=by)


def make_data():
    os.makedirs(D, exist_ok=True)
    pd.DataFrame([dict(code=c, cls=k, meaning=m, units=(int(c[1:]) if c != "PT" else "per code"),
                       seconds=(round(int(c[1:]) * U_SECONDS, 1) if c != "PT" else "per code")) for c, k, m in CARD]
                 ).to_csv(os.path.join(D, "teaching_code_card.csv"), index=False)
    rows = []
    for name, steps in TASKS.items():
        for i, (desc, codes) in enumerate(steps, 1):
            rows.append(dict(task=name, step=i, description=desc, codes=codes))
    pd.DataFrame(rows).to_csv(os.path.join(D, "practice_analyses.csv"), index=False)
    # practice exercises for learners (codes left blank)
    ex = [("P1", "Get a pencil from a desk 30 cm away and put it in a cup (loose)", "A6 G2 A6 P3"),
          ("P2", "Get one paper clip from a box of loose clips 20 cm away and toss it onto a tray", "A4 G5 A4 P0"),
          ("P3", "Push a button 10 cm away with the index finger", "A4 G0"),
          ("P4", "Get a nut from a bowl 40 cm away and start it on a bolt (two alignments, one correction)",
           "A6 G5 A6 P6 C2"),
          ("P5", "Walk 4 steps to a shelf, read a 3-group label, decide if it is the right bin", "W6x4 R2x3 D3"),
          ("P6", "Press a pedal once while holding a part in place", "F4"),
          ("P7", "Get a 6 kg casting with one hand from a shelf 50 cm away and place it loosely on a bench",
           "A8 G2 A8 L1x2 P3"),
          ("P8", "Sit down at a workstation, then stand up again", "S20 U22"),
          ("P9", "Turn a crank handle 5 full revolutions", "K6x5"),
          ("P10", "Transfer a screw from the left hand to the right hand", "T2")]
    pd.DataFrame([dict(id=i, task=t, codes="") for i, t, _ in ex]).to_csv(
        os.path.join(D, "practice_exercises.csv"), index=False)
    pd.DataFrame([dict(id=i, task=t, codes=c, units=units(c)) for i, t, c in ex]).to_csv(
        os.path.join(D, "practice_exercises_key.csv"), index=False)
    return {"teaching_code_card": len(CARD), "practice_analyses": len(rows), "practice_exercises": len(ex)}


# ---------------------------------------------------------------- examples
def ex_card():
    by = {}
    for c, k, _ in CARD:
        by.setdefault(k, []).append(c)
    return {"classes": by, "unit": f"1 U = {U_SECONDS} s", "codes": len(CARD)}


def ex_units():
    s = 2.4
    return {"seconds": s, "U (this course, 0.1 s)": round(s / U_SECONDS, 1),
            "TMU (0.036 s)": round(s / 0.036, 1), "MOD (0.129 s)": round(s / 0.129, 2),
            "minutes": round(s / 60, 4), "hours": round(s / 3600, 6),
            "pieces_per_hour_at_this_cycle": round(3600 / s, 1)}


def ex_tasks():
    return {"summaries": [task_summary(n) for n in TASKS]}


def ex_improve():
    out = {}
    for a, b in [("A_kit_current", "A_kit_improved"), ("C_pack_current", "C_pack_improved")]:
        sa, sb = task_summary(a), task_summary(b)
        out[a.split("_")[0] + "_" + a.split("_")[1]] = dict(
            current_s=sa["normal_s"], improved_s=sb["normal_s"],
            saving_pct=round(100 * (1 - sb["units"] / sa["units"]), 1),
            current_per_h=round(3600 / (sa["normal_s"] * (1 + PFD)), 1),
            improved_per_h=round(3600 / (sb["normal_s"] * (1 + PFD)), 1))
    return out


def ergonomic_flags(name, cycles_per_shift):
    t = task_table(name)
    toks = " ".join(t.codes).split()
    count = lambda pref: sum(int(m.group(3) or 1) for m in (CODE_RE.match(x) for x in toks)
                             if m and f"{m.group(1)}{m.group(2)}" in pref)
    return dict(task=name, bends=count({"B22"}), extended_reaches=count({"A8", "A12"}),
                loaded_moves=count({"L1"}), high_control_puts=count({"P6"}), selective_gets=count({"G5"}),
                steps_walked=count({"W6"}),
                per_shift={"bends": count({"B22"}) * cycles_per_shift,
                           "extended_reaches": count({"A8", "A12"}) * cycles_per_shift,
                           "steps": count({"W6"}) * cycles_per_shift})


def ex_ergonomics(demand={"C_pack": 600, "A_kit": 1500}):
    """Exposure per shift at the SAME daily demand, so current and improved methods compare fairly."""
    out = {}
    for n in ["C_pack_current", "C_pack_improved", "A_kit_current", "A_kit_improved"]:
        cyc = demand["_".join(n.split("_")[:2])]
        f = ergonomic_flags(n, cyc)
        busy_h = cyc * task_summary(n)["standard_s"] / 3600
        out[n] = dict(cycles_per_shift=cyc, busy_hours=round(busy_h, 2),
                      **{k: v for k, v in f.items() if k != "task"})
    return out


def ex_standard():
    s = task_summary("B_pin_assembly")
    t = task_table("B_pin_assembly")
    pt = sum(code_value(x)[1] for x in " ".join(t.codes).split() if x.startswith("PT"))
    manual = s["units"] - pt
    return {"total_U": s["units"], "manual_U": manual, "process_U": pt, "normal_s": s["normal_s"],
            "standard_s_allowance_on_all": round(s["units"] * U_SECONDS * (1 + PFD), 2),
            "standard_s_allowance_manual_only": round((manual * (1 + PFD) + pt) * U_SECONDS, 2),
            "pieces_per_hour": round(3600 / (s["units"] * U_SECONDS * (1 + PFD)), 1),
            "high_control_share_pct": round(100 * s["by_class"]["put"] / s["units"], 1)}


def ex_practice():
    k = pd.read_csv(os.path.join(D, "practice_exercises_key.csv"))
    return {"key": k.assign(seconds=(k.units * U_SECONDS).round(1)).to_dict("records")}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if hasattr(o, "item"):
        return o.item()
    return o


EX = {"card": ex_card, "units": ex_units, "tasks": ex_tasks, "improve": ex_improve, "ergonomics": ex_ergonomics,
      "standard": ex_standard, "practice": ex_practice}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print(make_data())
        sys.exit()
    if which == "show":
        print(task_table(sys.argv[2]).to_string(index=False))
        sys.exit()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list) and b and isinstance(b[0], dict):
                    print(f"  {a}:")
                    for row in b:
                        print(f"    {_clean(row)}")
                else:
                    print(f"  {a}: {_clean(b)}")
