"""commkit.py - data and checks for the Technical Communications course.

Running case: a process engineer at a fictional bearing plant presents a scrap-reduction
project on a grinding line to the plant leadership team.

    python tools/commkit.py data                 # (re)write data/*.csv
    python tools/commkit.py all                  # every worked example
    python tools/commkit.py <name>               # results, readability, slides, timing, feedback
    python tools/commkit.py check <file.md>      # readability + slide density for your own draft

Requires numpy, pandas, scipy. License: MIT
"""
from __future__ import annotations

import os
import re
import sys

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
EXAMPLES = os.path.join(ROOT, "examples")


# ---------------------------------------------------------------- data
def make_data(seed=909):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    # weekly scrap % on grinding line 3: 13 weeks before, 13 weeks after the fix (week 14 onward)
    rows = []
    for w in range(1, 27):
        base = 4.6 if w <= 13 else 2.1
        rows.append(dict(week=w, phase="before" if w <= 13 else "after",
                         parts=int(rng.integers(19000, 22000)), scrap_pct=round(max(0.5, base + rng.normal(0, 0.45)), 2)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "grinding_scrap_weekly.csv"), index=False)
    # defect categories for the 13 weeks before (counts)
    cats = {"diameter oversize": 5160, "burn marks": 2880, "chatter / waviness": 1830, "taper": 720,
            "surface scratches": 510, "other": 360}
    pd.DataFrame([dict(defect=k, count=int(v + rng.integers(-60, 60))) for k, v in cats.items()]).to_csv(
        os.path.join(D, "scrap_defects_before.csv"), index=False)
    # rehearsal feedback: 8 reviewers score 6 criteria (1-5) at rehearsal 1 and rehearsal 2
    crit = {"clear objective": (2.6, 4.3), "audience fit": (2.4, 4.0), "structure": (3.0, 4.1),
            "data clarity": (2.2, 4.2), "delivery": (3.1, 3.6), "Q&A handling": (2.9, 3.9)}
    rows = []
    for rnd in (1, 2):
        for r in range(1, 9):
            for c, (m1, m2) in crit.items():
                m = m1 if rnd == 1 else m2
                rows.append(dict(rehearsal=rnd, reviewer=r, criterion=c, score=int(np.clip(round(m + rng.normal(0, 0.6)), 1, 5))))
    pd.DataFrame(rows).to_csv(os.path.join(D, "rehearsal_feedback.csv"), index=False)
    # coded written comments from rehearsal 1
    comments = {"too much text on slides": 9, "unclear what you want from us": 7, "jargon / acronyms": 6,
                "chart hard to read": 6, "ran over time": 4, "spoke too fast": 3, "other": 2, "(positive) clear root-cause story": 3}
    pd.DataFrame([dict(comment=k, count=v) for k, v in comments.items()]).to_csv(
        os.path.join(D, "rehearsal1_comments.csv"), index=False)
    return "data written"


def load(name):
    return pd.read_csv(os.path.join(D, name))


# ---------------------------------------------------------------- text checks
def syllables(word: str) -> int:
    """Heuristic English syllable count (vowel groups, silent e). Good enough for drafts, not exact."""
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))


def readability(text: str) -> dict:
    # sentence ends: . ! ? followed by space/end, or a line break (bullets and headings rarely end in a period)
    sentences = [s for s in re.split(r"[.!?]+(?:\s|$)|\n+", text.strip()) if re.search(r"[A-Za-z]", s)]
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    syl = sum(syllables(w) for w in words)
    ns, nw = max(1, len(sentences)), max(1, len(words))
    long_words = sum(1 for w in words if syllables(w) >= 3)
    return {"sentences": ns, "words": nw, "words per sentence": round(nw / ns, 1),
            "Flesch reading ease": round(206.835 - 1.015 * nw / ns - 84.6 * syl / nw, 1),
            "Flesch-Kincaid grade": round(0.39 * nw / ns + 11.8 * syl / nw - 15.59, 1),
            "% words of 3+ syllables": round(100 * long_words / nw, 1)}


def slide_density(md: str, max_words=40, max_bullets=6) -> list[dict]:
    """Split a Markdown deck on '## ' headings; count words and bullets per slide."""
    out = []
    for block in re.split(r"\n(?=## )", md.strip()):
        lines = block.strip().splitlines()
        if not lines or not lines[0].startswith("## "):
            continue
        title = lines[0][3:].strip()
        body = "\n".join(lines[1:])
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)          # speaker notes in comments are not on the slide
        words = len(re.findall(r"[A-Za-z0-9][\w%.'-]*", body))
        bullets = sum(1 for line in lines[1:] if re.match(r"\s*[-*] ", line))
        flags = []
        if words > max_words:
            flags.append(f"{words} words (> {max_words})")
        if bullets > max_bullets:
            flags.append(f"{bullets} bullets (> {max_bullets})")
        if len(title.split()) <= 2:
            flags.append("topic title: write the takeaway as a sentence")
        out.append(dict(slide=title, words=words, bullets=bullets, flags="; ".join(flags) or "ok"))
    return out


def read_example(name):
    with open(os.path.join(EXAMPLES, name), encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------- examples
def ex_results():
    df = load("grinding_scrap_weekly.csv")
    b, a = df[df.phase == "before"], df[df.phase == "after"]
    t = stats.ttest_ind(b.scrap_pct, a.scrap_pct, equal_var=False)
    diff = b.scrap_pct.mean() - a.scrap_pct.mean()
    se = np.sqrt(b.scrap_pct.var(ddof=1) / len(b) + a.scrap_pct.var(ddof=1) / len(a))
    weekly_parts = df.parts.mean()
    cost_per_part = 3.40                                   # illustrative scrap cost per part ($)
    annual = diff / 100 * weekly_parts * 50 * cost_per_part
    dfx = load("scrap_defects_before.csv").sort_values("count", ascending=False)
    top2 = dfx["count"].head(2).sum() / dfx["count"].sum()
    return {"mean scrap before / after %": (round(b.scrap_pct.mean(), 2), round(a.scrap_pct.mean(), 2)),
            "reduction (points)": round(diff, 2), "relative reduction %": round(100 * diff / b.scrap_pct.mean(), 1),
            "approx. 95% CI for reduction (points)": (round(diff - 1.96 * se, 2), round(diff + 1.96 * se, 2)),
            "Welch t-test p": float(f"{t.pvalue:.2g}"), "average parts per week": round(weekly_parts),
            "annualized savings at $3.40/part, 50 weeks ($)": round(annual, -3),
            "top-2 defect share before %": round(100 * top2, 1)}


def ex_readability():
    return {"draft summary": readability(read_example("summary_draft.md")),
            "revised summary": readability(read_example("summary_revised.md"))}


def ex_slides():
    return {"draft deck": slide_density(read_example("deck_draft.md")),
            "revised deck": slide_density(read_example("deck_revised.md"))}


def ex_timing():
    """Spoken pace ~130-150 words per minute (common planning range, not a standard)."""
    out = {}
    for name in ("deck_draft.md", "deck_revised.md"):
        md = read_example(name)
        notes = " ".join(re.findall(r"<!--(.*?)-->", md, flags=re.S))
        slides = len(slide_density(md))
        w = len(re.findall(r"[A-Za-z0-9][\w%.'-]*", notes))
        out[name] = {"slides": slides, "words in speaker notes": w,
                     "minutes at 130 / 150 wpm": (round(w / 130, 1), round(w / 150, 1))}
    out["rule of thumb"] = "plan 1-2 minutes per content slide; leave 1/3 of the slot for questions"
    return out


def ex_feedback():
    df = load("rehearsal_feedback.csv")
    tab = df.pivot_table(index="criterion", columns="rehearsal", values="score", aggfunc="mean").round(2)
    tab["change"] = (tab[2] - tab[1]).round(2)
    overall = df.groupby("rehearsal").score.mean().round(2).to_dict()
    c = load("rehearsal1_comments.csv")
    positive = c[c.comment.str.startswith("(positive)")]
    c = c[~c.comment.str.startswith("(positive)")].sort_values("count", ascending=False)
    c["cum %"] = (100 * c["count"].cumsum() / c["count"].sum()).round(1)
    return {"mean score by criterion (1-5)": tab.to_dict("index"), "overall mean": overall,
            "critical comments": int(c["count"].sum()), "positive comments (kept separately)": positive.to_dict("records"),
            "rehearsal-1 critical comments (Pareto)": c.to_dict("records")}


def check_file(path):
    with open(path, encoding="utf-8") as f:
        md = f.read()
    plain = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    plain = re.sub(r"^#+ ", "", plain, flags=re.M)            # keep heading text; it is read too
    plain = re.sub(r"!\[.*?\]\(.*?\)", "", plain)            # drop image links
    plain = re.sub(r"^\s*[-*] ", "", plain, flags=re.M)
    print("Readability:", readability(plain))
    rows = slide_density(md)
    if rows:
        print(pd.DataFrame(rows).to_string(index=False))


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"results": ex_results, "readability": ex_readability, "slides": ex_slides, "timing": ex_timing,
      "feedback": ex_feedback}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print(make_data())
        sys.exit()
    if which == "check":
        check_file(sys.argv[2])
        sys.exit()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            res = fn()
            for a, b in res.items():
                if isinstance(b, list):
                    print(f"  {a}:")
                    for row in b:
                        print(f"    {_clean(row)}")
                else:
                    print(f"  {a}: {_clean(b)}")
