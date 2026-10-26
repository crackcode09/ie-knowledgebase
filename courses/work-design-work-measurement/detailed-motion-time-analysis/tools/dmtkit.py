"""dmtkit.py - teaching data card, analysis engine and lab problems for the Detailed Motion Time Analysis course.

IMPORTANT: the "Detailed Teaching Card" (DTC) in this file is ORIGINAL to this course. Its motion classes,
codes, formulas and values were written for teaching the method of a detailed, distance-based PMTS. It is NOT
the MTM-1 data card, does not reproduce MTM data, and is not validated for setting real standards.
Use the licensed system and certified analysts for real standards.

Unit: cs = centisecond = 0.01 s.

    python tools/dmtkit.py data            # write data/*.csv (card tables, lab keys)
    python tools/dmtkit.py all             # every worked example
    python tools/dmtkit.py lab L03         # print one coded lab analysis
    python tools/dmtkit.py code "R30b"     # value of one code

Requires pandas. License: MIT
"""
from __future__ import annotations

import os
import re
import sys

import pandas as pd

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
CS = 0.01                 # seconds per cs
PFD = 0.12

# ---------------------------------------------------------------- the teaching card (formulas, cs; d in cm)
REACH = {"a": (8, 0.9, "fixed, known location, or to the other hand"),
         "b": (9, 1.1, "location varies slightly from cycle to cycle"),
         "c": (12, 1.3, "object mixed with others: search and select"),
         "d": (12, 1.4, "very small object, or a precise grasp is needed")}
MOVE = {"a": (7, 0.8, "to the other hand or against a stop"),
        "b": (8, 1.0, "to an approximate location"),
        "c": (10, 1.2, "to an exact location")}
IN_MOTION = 3             # subtract when the hand is already moving at the start (code suffix m), min 2 cs
GRASP = {"Gc": (0, "contact grasp: touch, push, slide; no finger closure", False),
         "Gp": (3, "pick-up: easy, isolated object", False),
         "Gs": (8, "small or flat object: precise finger closure", True),
         "Gr": (6, "regrasp: change grip without letting go", False),
         "Gt": (6, "transfer to the other hand", False),
         "Gx": (14, "select from a jumble: search, separate, then grasp", True)}
POS_FIT = {"L": (9, "loose: no pressure, visible clearance"),
           "C": (20, "close: light pressure, small clearance"),
           "T": (45, "tight: heavy pressure or interference")}
POS_SYM = {"S": (0, "symmetric: any orientation fits"), "M": (4, "semi-symmetric: a few orientations fit"),
           "N": (10, "non-symmetric: one orientation fits")}
POS_HARD = 6              # suffix h: difficult to handle (flexible, slippery, small)
RELEASE = {"RL": (2, "normal release: open the fingers"), "RLc": (0, "contact release")}
DISENGAGE = {"DL": (4, "loose: no effort, little recoil", False), "DC": (10, "close: some effort, recoil", True),
             "DT": (30, "tight: high effort, marked recoil", True)}
DIS_CARE = 5              # suffix c: care needed to avoid damage or injury
TURN = {"L": 1.0, "M": 1.5, "H": 2.5}     # turn: (3 + 0.05*deg) x factor for light/medium/heavy
AP = {"AP": (30, "apply pressure"), "APR": (45, "apply pressure with regrasp")}
BODY = {"FM": (25, "foot motion"), "LM": (30, "leg motion"), "SS": (50, "sidestep"),
        "TBD": (55, "turn body"), "WK": (45, "walk, per step"), "BD": (90, "bend"), "ABD": (95, "arise from bend"),
        "SIT": (120, "sit"), "STD": (140, "stand from sitting"), "EF": (20, "eye focus")}
EYE_TRAVEL = (2, 0.3)     # ET<cm>: 2 + 0.3 x cm of travel at reading distance


def weight_terms(kg):
    over = max(0.0, kg - 1.0)
    return 1 + 0.015 * over, 1.5 * over


def code_value(tok):
    """Return (time_cs, high_control) for one token."""
    t = tok.strip()
    m = re.fullmatch(r"R(\d+(?:\.\d+)?)([abcd])(m?)", t)
    if m:
        d, case, mv = float(m.group(1)), m.group(2), m.group(3)
        a, b, _ = REACH[case]
        v = a + b * d - (IN_MOTION if mv else 0)
        return round(max(v, 2), 1), case in "cd"
    m = re.fullmatch(r"M(\d+(?:\.\d+)?)([abc])(m?)(?:/(\d+(?:\.\d+)?))?", t)
    if m:
        d, case, mv, kg = float(m.group(1)), m.group(2), m.group(3), float(m.group(4) or 0)
        a, b, _ = MOVE[case]
        f, s = weight_terms(kg)
        v = (a + b * d - (IN_MOTION if mv else 0)) * f + s
        return round(max(v, 2), 1), case == "c"
    m = re.fullmatch(r"T(\d+)([LMH])", t)
    if m:
        return round((3 + 0.05 * int(m.group(1))) * TURN[m.group(2)], 1), False
    if t in GRASP:
        return float(GRASP[t][0]), GRASP[t][2]
    m = re.fullmatch(r"P([LCT])([SMN])(h?)", t)
    if m:
        v = POS_FIT[m.group(1)][0] + POS_SYM[m.group(2)][0] + (POS_HARD if m.group(3) else 0)
        high = not (m.group(1) == "L" and m.group(2) == "S")
        return float(v), high
    if t in RELEASE:
        return float(RELEASE[t][0]), False
    m = re.fullmatch(r"(D[LCT])(c?)", t)
    if m:
        v = DISENGAGE[m.group(1)][0] + (DIS_CARE if m.group(2) else 0)
        return float(v), DISENGAGE[m.group(1)][2]
    if t in AP:
        return float(AP[t][0]), False
    m = re.fullmatch(r"WK(\d+)", t)
    if m:
        return float(BODY["WK"][0] * int(m.group(1))), False
    m = re.fullmatch(r"ET(\d+)", t)
    if m:
        return round(EYE_TRAVEL[0] + EYE_TRAVEL[1] * int(m.group(1)), 1), False
    if t in BODY:
        return float(BODY[t][0]), False
    m = re.fullmatch(r"PT(\d+)", t)
    if m:
        return float(m.group(1)), False
    raise ValueError(f"code not on the teaching card: {t}")


def side(codes):
    if not codes or codes.strip() in ("", "-", "H"):     # H = hold (no time)
        return 0.0, False
    vals = [code_value(c) for c in codes.split()]
    return round(sum(v for v, _ in vals), 1), any(h for _, h in vals)


def row_time(lh, rh, body=""):
    """Simultaneous-motion rule (course convention): the hands overlap unless BOTH sides contain
    a high-control motion, in which case they are done one after the other. Body/eye/process codes add."""
    tl, hl = side(lh)
    tr, hr = side(rh)
    tb, _ = side(body)
    simult = not (hl and hr)
    hands = max(tl, tr) if simult else tl + tr
    return dict(lh_cs=tl, rh_cs=tr, simultaneous=simult, hands_cs=round(hands, 1), body_cs=tb,
                row_cs=round(hands + tb, 1))


# ---------------------------------------------------------------- labs: (description, LH, RH, body/eye/process)
LABS = {
    "L01": ("Pick a bolt from a bin and place it in a fixture hole (loose, symmetric)", [
        ("Reach to bin, select bolt", "", "R40c Gx", ""),
        ("Move bolt to fixture, place, release", "", "M35c PLS RL", ""),
        ("Return hand toward bin", "", "R10a", "")]),
    "L02": ("Insert a dowel pin into a close-fit hole", [
        ("Reach to pin tray, pick up pin", "", "R25b Gs", ""),
        ("Move pin to hole", "", "M25c", ""),
        ("Position close, semi-symmetric (chamfered pin), release", "", "PCM RL", "")]),
    "L03_current": ("Assemble washer on bolt, one hand holds", [
        ("LH reach and pick bolt; RH idle", "R30b Gp", "", ""),
        ("LH move bolt in front of body and hold", "M30b", "", ""),
        ("RH reach to washer tray, pick small washer", "H", "R30b Gs", ""),
        ("RH move washer to bolt", "H", "M30c", ""),
        ("RH position washer on bolt (loose, symmetric), release", "H", "PLS RL", ""),
        ("LH move assembly to chute, release", "M35b RL", "", "")]),
    "L03_improved": ("Assemble washer on bolt in a fixture, both hands", [
        ("Both hands reach: LH to bolt tray, RH to washer magazine", "R20a Gp", "R20a Gp", ""),
        ("LH move bolt into fixture (loose, symmetric); RH moves washer toward fixture", "M20b PLS RL", "M20b", ""),
        ("RH position washer on bolt in fixture, release", "", "PLS RL", ""),
        ("LH push assembly off fixture into chute", "R5a Gc M10a RLc", "", "")]),
    "L04": ("Fold a letter in thirds and insert into an envelope (office task)", [
        ("Both hands reach to letter, pick up", "R30a Gp", "R30a Gp", ""),
        ("Move letter to folding position, fold first third", "M20b", "M15a Gr M15b", ""),
        ("Fold second third, crease", "Gr M15b", "AP", ""),
        ("LH reach to envelope, pick up (flat)", "R25b Gs", "H", ""),
        ("Insert letter into envelope (close, semi-symmetric, flexible)", "H", "M15c PCMh RL", ""),
        ("Aside envelope to tray", "M30b RL", "", "")]),
    "L05": ("Stamp a document", [
        ("Reach to stamp handle, grasp", "", "R25a Gp", ""),
        ("Move stamp to document, press", "", "M25c AP", ""),
        ("Lift stamp from paper, return to pad, release", "", "DL M25a RL", ""),
        ("Look at the impression", "", "", "EF")]),
    "L06": ("Load a press, two-hand palm buttons, unload", [
        ("RH reach to blank stack, grasp flat blank", "", "R45b Gs", ""),
        ("Move blank into die nest (two locating pins)", "", "M45c PLN RL", ""),
        ("Both hands reach to palm buttons and press", "R20a Gc AP", "R30a Gc AP", ""),
        ("Press cycle", "", "", "PT180"),
        ("RH reach into die, grasp part, disengage from pins", "", "R40b Gp DC", ""),
        ("Move part to tote, release", "", "M40b RL", "")]),
    "L07": ("Pack six bottles into a divided carton (two at a time)", [
        ("Both hands reach to conveyor, pick a bottle each", "R30a Gp", "R30a Gp", ""),
        ("Both move bottles to carton cells, place loose and release", "M30b PLS RL", "M30b PLS RL", ""),
        ("Repeat twice more", "R30a Gp M30b PLS RL R30a Gp M30b PLS RL",
         "R30a Gp M30b PLS RL R30a Gp M30b PLS RL", "")]),
    "L08": ("Operate a lever then turn a handwheel one turn", [
        ("RH reach to lever, grasp, pull through 90 degrees (medium)", "", "R30a Gp T90M RL", ""),
        ("RH reach to handwheel rim, grasp", "", "R20a Gp", ""),
        ("Turn handwheel 180 degrees, regrasp, 180 degrees (light)", "", "T180L Gr T180L RL", "")]),
    "L09": ("Visually inspect a part for three features", [
        ("Pick up part from tray", "", "R30b Gp", ""),
        ("Move part to viewing position", "", "M30b", ""),
        ("Eye travel and focus on three features", "", "H", "ET15 EF ET15 EF ET15 EF"),
        ("Aside to pass or fail chute", "", "M30b RL", "")]),
    "L10": ("Get a box from the floor and put it on a bench 3 steps away", [
        ("Walk 3 steps to box", "", "", "WK3"),
        ("Bend, both hands grasp box", "R20a Gp", "R20a Gp", "BD"),
        ("Arise with box (6 kg)", "", "", "ABD"),
        ("Walk 3 steps back", "", "", "WK3"),
        ("Move box onto bench against stop, release", "M30a/3 RL", "M30a/3 RL", "")]),
    "C01_current": ("Capstone: assemble a connector (housing, 2 pins, cover), current method", [
        ("LH reach to housing bin, select housing", "R40c Gx", "", ""),
        ("LH move housing in front of body; RH reach into mixed pin bin, select pin", "M35b", "R35c Gx", ""),
        ("RH move pin to hole, position (close, non-symmetric), release", "H", "M30c PCN RL", ""),
        ("RH reach into pin bin, select second pin", "H", "R35c Gx", ""),
        ("RH move pin to hole, position, release", "H", "M30c PCN RL", ""),
        ("RH reach to cover stack, pick flat cover", "H", "R30b Gs", ""),
        ("RH move cover to housing, position (loose, semi-symmetric), snap", "H", "M30c PLM AP", ""),
        ("Look: pins and cover seated?", "H", "", "EF"),
        ("LH move assembly to tote, release", "M40b RL", "", "")]),
    "C01_improved": ("Capstone: connector in a fixture, oriented pins, cover magazine", [
        ("LH get housing from tray, place in fixture; RH get pin from strip feeder", "R30b Gp M30b PLS RL", "R20a Gp", ""),
        ("LH get second pin; RH insert first pin (chamfered, symmetric, close)", "R20a Gp", "M20c PCS RL", ""),
        ("LH insert second pin; RH get cover from magazine", "M20c PCS RL", "R20a Gp", ""),
        ("RH place cover in guided nest, snap", "", "M20b PLS AP", ""),
        ("Look: pins and cover seated?", "", "", "EF"),
        ("RH push assembly off fixture into chute", "", "R5a Gc M10a RLc", "")]),
}


def lab_table(name):
    rows = []
    for i, (desc, lh, rh, body) in enumerate(LABS[name][1], 1):
        rows.append(dict(step=i, description=desc, LH=lh, RH=rh, body=body, **row_time(lh, rh, body)))
    return pd.DataFrame(rows)


def lab_total(name):
    t = lab_table(name)
    cs = float(t.row_cs.sum())
    return dict(lab=name, steps=len(t), total_cs=round(cs, 1), normal_s=round(cs * CS, 2),
                standard_s=round(cs * CS * (1 + PFD), 2), per_hour=round(3600 / (cs * CS * (1 + PFD)), 1))


def card_tables():
    dists = [5, 10, 15, 20, 30, 40, 50, 60, 70, 80]
    reach = pd.DataFrame([{**{"case": c, "meaning": REACH[c][2]}, **{f"{d}cm": code_value(f"R{d}{c}")[0] for d in dists}}
                          for c in REACH])
    move = pd.DataFrame([{**{"case": c, "meaning": MOVE[c][2]}, **{f"{d}cm": code_value(f"M{d}{c}")[0] for d in dists}}
                         for c in MOVE])
    grasp = pd.DataFrame([dict(code=k, cs=v[0], meaning=v[1], high_control=v[2]) for k, v in GRASP.items()])
    pos = pd.DataFrame([dict(code=f"P{f}{s}", fit=POS_FIT[f][1], symmetry=POS_SYM[s][1],
                             cs=code_value(f"P{f}{s}")[0], cs_if_difficult=code_value(f"P{f}{s}h")[0],
                             high_control=code_value(f"P{f}{s}")[1]) for f in POS_FIT for s in POS_SYM])
    other = pd.DataFrame([dict(code=k, cs=v[0], meaning=v[1]) for k, v in {**RELEASE, **AP, **BODY}.items()] +
                         [dict(code=k, cs=v[0], meaning=v[1]) for k, v in DISENGAGE.items()] +
                         [dict(code="T<deg>L/M/H", cs="(3 + 0.05 x deg) x 1.0/1.5/2.5", meaning="turn"),
                          dict(code="ET<cm>", cs="2 + 0.3 x cm", meaning="eye travel"),
                          dict(code="WK<n>", cs="45 x n", meaning="walk n steps"),
                          dict(code="PT<cs>", cs="as measured", meaning="process time")])
    return reach, move, grasp, pos, other


def make_data():
    os.makedirs(D, exist_ok=True)
    for name, t in zip(["card_reach", "card_move", "card_grasp", "card_position", "card_other"], card_tables()):
        t.to_csv(os.path.join(D, f"{name}.csv"), index=False)
    rows = []
    for lab, (title, steps) in LABS.items():
        for i, (desc, lh, rh, body) in enumerate(steps, 1):
            rows.append(dict(lab=lab, title=title, step=i, description=desc, LH=lh, RH=rh, body=body))
    pd.DataFrame(rows).to_csv(os.path.join(D, "lab_keys.csv"), index=False)
    pd.DataFrame([dict(lab=r["lab"], title=r["title"], step=r["step"], description=r["description"], LH="", RH="",
                       body="") for r in rows]).to_csv(os.path.join(D, "lab_worksheets.csv"), index=False)
    return {"card_tables": 5, "lab_rows": len(rows), "labs": len(LABS)}


# ---------------------------------------------------------------- examples
def ex_units():
    s = 1.8
    return {"seconds": s, "cs": s / CS, "TMU (0.036 s)": round(s / 0.036, 1), "hours": round(s / 3600, 6),
            "TMU_per_hour": 100000}


def ex_card():
    return {"R30a": code_value("R30a")[0], "R30c": code_value("R30c")[0], "R30cm(in motion)": code_value("R30cm")[0],
            "M30b": code_value("M30b")[0], "M30b/5": code_value("M30b/5")[0], "T90L": code_value("T90L")[0],
            "T90H": code_value("T90H")[0], "PLS": code_value("PLS")[0], "PCN": code_value("PCN")[0],
            "PTNh": code_value("PTNh")[0], "Gx": code_value("Gx")[0], "DTc": code_value("DTc")[0]}


def ex_labs():
    return {"labs": [lab_total(n) for n in LABS]}


def ex_simo():
    t = lab_table("L03_current")
    i = lab_table("L03_improved")
    a, b = lab_total("L03_current"), lab_total("L03_improved")
    idle_rh = float(t[t.RH == ""].row_cs.sum())
    idle_lh = float(t[t.LH.isin(["", "H"])].row_cs.sum())
    return {"current_cs": a["total_cs"], "improved_cs": b["total_cs"],
            "saving_pct": round(100 * (1 - b["total_cs"] / a["total_cs"]), 1),
            "current_rh_idle_cs": idle_rh, "current_lh_idle_or_hold_cs": idle_lh,
            "current_per_h": a["per_hour"], "improved_per_h": b["per_hour"],
            "rows_simultaneous_improved": int(i.simultaneous.sum())}


def ex_standard():
    t = lab_table("L06")
    pt = float(t[t.body.str.startswith("PT")].row_cs.sum())
    tot = float(t.row_cs.sum())
    man = tot - pt
    return {"total_cs": tot, "process_cs": pt, "manual_cs": round(man, 1),
            "standard_s_allow_all": round(tot * CS * (1 + PFD), 2),
            "standard_s_allow_manual": round((man * (1 + PFD) + pt) * CS, 2),
            "per_hour_manual_convention": round(3600 / ((man * (1 + PFD) + pt) * CS), 1)}


def ex_rules():
    cases = [("R30b Gp", "R30b Gp"), ("R30b Gx", "R30b Gp"), ("R30c Gx", "R30b Gs"), ("M20b PLS RL", "M20b PLS RL"),
             ("M20c PCS RL", "M20c PCS RL")]
    return {"cases": [dict(LH=l, RH=r, **row_time(l, r)) for l, r in cases]}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if hasattr(o, "item"):
        return o.item()
    return o


EX = {"units": ex_units, "card": ex_card, "rules": ex_rules, "labs": ex_labs, "simo": ex_simo, "standard": ex_standard}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print(make_data())
        sys.exit()
    if which == "lab":
        print(LABS[sys.argv[2]][0])
        print(lab_table(sys.argv[2]).to_string(index=False))
        print(lab_total(sys.argv[2]))
        sys.exit()
    if which == "code":
        print(code_value(sys.argv[2]))
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
