"""make_figures.py - regenerate every figure in figures/.

    python tools/make_figures.py

License: MIT
"""
import os
import sys
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import commkit as ck  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "font.size": 10})
BLUE, ORANGE, GREY, LIGHT = "#2b6cb0", "#dd6b20", "#a0aec0", "#e2e8f0"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def fig_scrap_bad():
    """Deliberately poor chart: rainbow bars, dual axis, heavy grid, no message."""
    df = ck.load("grinding_scrap_weekly.csv")
    fig, ax = plt.subplots(figsize=(7, 4))
    colors = plt.cm.rainbow(np.linspace(0, 1, len(df)))
    ax.bar(df.week, df.scrap_pct, color=colors, edgecolor="black")
    ax.grid(True, which="both", color="black", lw=0.6)
    ax.set_ylim(0, 6)
    ax2 = ax.twinx()
    ax2.plot(df.week, df.parts, "k--o", ms=3, label="Parts")
    ax2.set_ylabel("Parts")
    ax.set_xlabel("Wk")
    ax.set_ylabel("Scrap %")
    ax.set_title("Line 3 OD Grind Scrap % and Parts Produced by Week (WK1-WK26) - Data from MES Export")
    ax2.legend(loc="upper right")
    ax.title.set_fontsize(9)
    save(fig, "05_scrap_before_cleanup.png")


def fig_scrap_good():
    df = ck.load("grinding_scrap_weekly.csv")
    b, a = df[df.phase == "before"], df[df.phase == "after"]
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(df.week, df.scrap_pct, color=GREY, marker="o", ms=3, lw=1)
    ax.hlines(b.scrap_pct.mean(), 1, 13, color=ORANGE, lw=2.5)
    ax.hlines(a.scrap_pct.mean(), 14, 26, color=BLUE, lw=2.5)
    ax.axvline(13.5, color="black", lw=0.8, ls=":")
    ax.text(7, b.scrap_pct.mean() + 0.35, f"Before: {b.scrap_pct.mean():.1f}%", ha="center", color=ORANGE, weight="bold")
    ax.text(20, a.scrap_pct.mean() + 0.35, f"After: {a.scrap_pct.mean():.1f}%", ha="center", color=BLUE, weight="bold")
    ax.text(13.6, 5.6, "Fix in place\n(week 14)", fontsize=8, va="top")
    ax.set_ylim(0, 6)
    ax.set_xlabel("Week")
    ax.set_ylabel("Scrap (% of parts)")
    ax.set_title("Line 3 scrap fell by more than half and has stayed down", loc="left", weight="bold")
    clean(ax)
    save(fig, "05_scrap_after.png")


def fig_pareto():
    d = ck.load("scrap_defects_before.csv").sort_values("count")
    share = 100 * d["count"] / d["count"].sum()
    fig, ax = plt.subplots(figsize=(7, 3.6))
    colors = [BLUE if x in ("diameter oversize", "burn marks") else GREY for x in d.defect]
    ax.barh(d.defect, share, color=colors)
    for y, v in enumerate(share):
        ax.text(v + 0.8, y, f"{v:.0f}%", va="center", fontsize=9)
    ax.set_xlabel("Share of scrapped parts, 13 weeks before the fix (%)")
    ax.set_title("Oversize and burn made 70% of the scrap", loc="left", weight="bold")
    ax.set_xlim(0, 55)
    clean(ax)
    save(fig, "05_defect_pareto.png")


def fig_pie_vs_bar():
    d = ck.load("scrap_defects_before.csv")
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
    axes[0].pie(d["count"], labels=d.defect, colors=plt.cm.Set3(np.arange(len(d))), textprops={"fontsize": 7})
    axes[0].set_title("Pie: hard to compare slices")
    ds = d.sort_values("count")
    axes[1].barh(ds.defect, ds["count"], color=GREY)
    axes[1].set_title("Sorted bar: ranking is obvious")
    clean(axes[1])
    save(fig, "05_pie_vs_bar.png")


def fig_feedback_pareto():
    c = ck.load("rehearsal1_comments.csv")
    c = c[~c.comment.str.startswith("(positive)")].sort_values("count", ascending=False)
    cum = 100 * c["count"].cumsum() / c["count"].sum()
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.bar(range(len(c)), c["count"], color=BLUE)
    ax.set_xticks(range(len(c)))
    ax.set_xticklabels([textwrap.fill(t, 14) for t in c.comment], fontsize=8)
    ax.set_ylabel("Reviewer comments")
    ax2 = ax.twinx()
    ax2.plot(range(len(c)), cum, color=ORANGE, marker="o")
    ax2.set_ylim(0, 105)
    ax2.set_ylabel("Cumulative %")
    ax.set_title("Rehearsal 1: four issues drew three-quarters of the critical comments", loc="left", weight="bold")
    ax.spines["top"].set_visible(False)
    ax2.spines["top"].set_visible(False)
    save(fig, "06_feedback_pareto.png")


def fig_rehearsal():
    df = ck.load("rehearsal_feedback.csv")
    t = df.pivot_table(index="criterion", columns="rehearsal", values="score", aggfunc="mean").sort_values(2)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for y, (crit, row) in enumerate(t.iterrows()):
        ax.plot([row[1], row[2]], [y, y], color=LIGHT, lw=4, zorder=1)
        ax.scatter(row[1], y, color=GREY, s=50, zorder=2, label="Rehearsal 1" if y == 0 else None)
        ax.scatter(row[2], y, color=BLUE, s=50, zorder=2, label="Rehearsal 2" if y == 0 else None)
    ax.set_yticks(range(len(t)))
    ax.set_yticklabels(t.index)
    ax.set_xlim(1, 5)
    ax.set_xlabel("Mean reviewer score (1 = poor, 5 = excellent), 8 reviewers")
    ax.set_title("Every criterion improved; delivery and Q&A gained least", loc="left", weight="bold")
    ax.legend(frameon=False, loc="lower right")
    clean(ax)
    save(fig, "07_rehearsal_scores.png")


def _slide(ax, title, lines, title_size=11, body_size=8, bg="white"):
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.add_patch(plt.Rectangle((0, 0), 16, 9, fc=bg, ec="#4a5568"))
    ax.text(0.6, 8.2, title, fontsize=title_size, weight="bold", va="top")
    y = 6.9
    for ln in lines:
        wrapped = textwrap.fill(ln, 70)
        ax.text(0.8, y, wrapped, fontsize=body_size, va="top")
        y -= 0.62 * (wrapped.count("\n") + 1) + 0.15


def fig_slides():
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
    draft = ck.read_example("deck_draft.md").split("## Define")[1].split("<!--")[0].strip().splitlines()
    _slide(axes[0], "Define", [ln.lstrip("- ") for ln in draft], title_size=11, body_size=6.5)
    axes[0].set_title("Before: topic title, 76 words", fontsize=9, color="#c53030")
    _slide(axes[1], "Approve $38,000 to cut grinding\nscrap in half on Lines 1, 2 and 4",
           ["Line 3 scrap fell from 4.5% to 2.0%", "Same fix on three more lines: about $250,000 a year",
            "Payback in about two months"], title_size=12, body_size=10)
    axes[1].set_title("After: the takeaway is the title, 24 words", fontsize=9, color="#2f855a")
    save(fig, "07_slide_before_after.png")


if __name__ == "__main__":
    for f in (fig_scrap_bad, fig_scrap_good, fig_pareto, fig_pie_vs_bar, fig_feedback_pareto, fig_rehearsal, fig_slides):
        f()
    print("figures written to", os.path.abspath(FIG))
