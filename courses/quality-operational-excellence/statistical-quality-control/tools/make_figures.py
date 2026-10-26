"""make_figures.py - regenerate every figure in figures/.

    python tools/make_figures.py

License: MIT
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import sqckit as sk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def chart(ax, x, y, center, ucl, lcl, flag=None, title="", ylabel=""):
    ax.plot(x, y, color=BLUE, marker="o", ms=4, lw=1)
    ax.plot(x, np.broadcast_to(center, np.shape(x)), color="black", lw=1)
    ax.step(x, np.broadcast_to(ucl, np.shape(x)), where="mid", color=RED, ls="--", lw=1)
    ax.step(x, np.broadcast_to(lcl, np.shape(x)), where="mid", color=RED, ls="--", lw=1)
    if flag is not None:
        f = np.asarray(flag)
        ax.scatter(np.asarray(x)[f], np.asarray(y)[f], color=RED, s=45, zorder=3)
    ax.set_title(title, loc="left")
    ax.set_ylabel(ylabel)


def fig_histogram():
    x = sk.load("capability_study.csv").diameter
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.hist(x, bins=12, color=GREY, edgecolor="white")
    ax.axvline(x.mean(), color=BLUE, lw=2, label=f"mean {x.mean():.4f}")
    ax.axvline(x.median(), color=ORANGE, ls="--", label=f"median {x.median():.4f}")
    ax.set_xlabel("Pin diameter (mm)")
    ax.set_ylabel("Pins")
    ax.set_title("100 pins: location, spread and shape at a glance", loc="left")
    ax.legend(frameon=False)
    save(fig, "01_histogram.png")


def fig_variation():
    rng = np.random.default_rng(3)
    common = 10 + rng.normal(0, 1, 40)
    special = common.copy()
    special[25:] += 3
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.2), sharey=True)
    for ax, y, t in ((axes[0], common, "Common cause only: predictable, within limits"),
                     (axes[1], special, "A special cause shifts the process at point 26")):
        ax.plot(range(1, 41), y, color=BLUE, marker="o", ms=3, lw=1)
        ax.axhline(10, color="black", lw=1)
        ax.axhline(13, color=RED, ls="--", lw=1)
        ax.axhline(7, color=RED, ls="--", lw=1)
        ax.set_title(t, loc="left", fontsize=10)
    save(fig, "02_common_vs_special.png")


def fig_xbar_r():
    df = sk.load("pin_diameter_subgroups.csv")
    xb, r, L = sk.xbar_r_limits(df, phase_end=18)
    sg = xb.index.values
    flag = np.isin(sg, [19, 21, 22, 25])
    fig, axes = plt.subplots(2, 1, figsize=(8, 5.6), sharex=True)
    chart(axes[0], sg, xb.values, L["xbarbar"], L["UCLx"], L["LCLx"], flag, "X-bar chart (limits from subgroups 1-18)", "Mean diameter (mm)")
    axes[0].axvline(18.5, color=GREY, ls=":")
    chart(axes[1], sg, r.values, L["rbar"], L["UCLr"], L["LCLr"], None, "R chart", "Range (mm)")
    axes[1].set_xlabel("Subgroup (5 pins each)")
    save(fig, "03_xbar_r.png")


def fig_imr():
    h = sk.load("daily_hardness.csv").hardness_hrc.values
    mr = np.abs(np.diff(h))
    xbar, mrbar = h.mean(), mr.mean()
    fig, axes = plt.subplots(2, 1, figsize=(8, 5.2), sharex=True)
    d = np.arange(1, 31)
    chart(axes[0], d, h, xbar, xbar + 2.66 * mrbar, xbar - 2.66 * mrbar, h > xbar + 2.66 * mrbar, "Individuals chart", "Hardness (HRC)")
    chart(axes[1], d[1:], mr, mrbar, 3.267 * mrbar, 0, mr > 3.267 * mrbar, "Moving range chart", "MR (HRC)")
    axes[1].set_xlabel("Day")
    save(fig, "04_imr.png")


def fig_p():
    d = sk.load("valve_final_inspection.csv")
    pbar = d.defective.sum() / d.inspected.sum()
    p = d.defective / d.inspected
    ucl = pbar + 3 * np.sqrt(pbar * (1 - pbar) / d.inspected)
    lcl = (pbar - 3 * np.sqrt(pbar * (1 - pbar) / d.inspected)).clip(lower=0)
    fig, ax = plt.subplots(figsize=(8, 3.6))
    chart(ax, d.day.values, 100 * p.values, 100 * pbar, 100 * ucl.values, 100 * lcl.values, (p > ucl).values,
          "p chart: limits move with each day's sample size", "% defective")
    ax.set_xlabel("Day")
    save(fig, "05_p_chart.png")


def fig_c():
    c = sk.load("casting_defects.csv").defects.values
    cb = c.mean()
    fig, ax = plt.subplots(figsize=(8, 3.4))
    chart(ax, np.arange(1, 31), c, cb, cb + 3 * math.sqrt(cb), 0, c > cb + 3 * math.sqrt(cb), "c chart: surface defects per casting",
          "Defects")
    ax.set_xlabel("Casting")
    save(fig, "05_c_chart.png")


def fig_short_run():
    d = sk.load("short_run_lathe.csv")
    d["dev"] = d.diameter - d.nominal
    g = d.groupby("run").agg(part=("part_number", "first"), x=("dev", "mean"))
    r = sk.ex_short_run()
    c, u, l = r["DNOM chart: center, UCL, LCL (mm from nominal)"]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.plot(g.index, 1000 * g.x, color=GREY, lw=1, zorder=1)
    for part, col in (("P-120", BLUE), ("P-095", ORANGE), ("P-150", GREEN)):
        m = g.part == part
        ax.scatter(g.index[m], 1000 * g.x[m], color=col, s=30, label=part, zorder=2)
    for v, st in ((c, "-"), (u, "--"), (l, "--")):
        ax.axhline(1000 * v, color="black" if st == "-" else RED, ls=st, lw=1)
    ax.set_xlabel("Run (3 pins each), in production order")
    ax.set_ylabel("Mean deviation from nominal (µm)")
    ax.set_title("DNOM chart: three part numbers on one chart", loc="left")
    ax.legend(frameon=False, ncol=3)
    save(fig, "06_dnom_chart.png")


def fig_capability():
    x = sk.load("capability_study.csv").diameter
    c = sk.ex_capability()
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.hist(x, bins=12, density=True, color=GREY, edgecolor="white")
    t = np.linspace(11.96, 12.04, 300)
    ax.plot(t, stats.norm.pdf(t, x.mean(), x.std(ddof=1)), color=BLUE)
    for v, lab in ((11.970, "LSL"), (12.030, "USL"), (12.000, "target")):
        ax.axvline(v, color=RED if lab != "target" else "black", ls="--" if lab != "target" else ":")
        ax.text(v, ax.get_ylim()[1] * 0.92, f" {lab}", fontsize=8)
    ax.set_xlabel("Pin diameter (mm)")
    ax.set_yticks([])
    ax.set_title(f"Capability: Cp {c['Cp']:.2f}, Cpk {c['Cpk']:.2f} (mean is off-target)", loc="left")
    save(fig, "07_capability.png")


def fig_oc():
    p = np.linspace(0, 0.12, 300)
    single = [sk.pa_single(v, 80, 2) for v in p]
    dbl = [sk.double_plan_pa_asn(v)[0] if v > 0 else 1.0 for v in p]
    tight = [sk.pa_single(v, 110, 3) for v in p]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(100 * p, single, color=BLUE, lw=2, label="single n=80, c=2")
    ax.plot(100 * p, dbl, color=ORANGE, ls="--", label="double n1=40,c1=0,r1=2; n2=80,c2=4")
    ax.plot(100 * p, tight, color=GREEN, label="designed n=110, c=3")
    ax.axvline(1, color=GREY, ls=":")
    ax.axvline(6, color=GREY, ls=":")
    ax.text(1.1, 0.05, "AQL 1%", fontsize=8)
    ax.text(6.1, 0.85, "LTPD 6%", fontsize=8)
    ax.set_xlabel("Incoming lot quality (% defective)")
    ax.set_ylabel("Probability of acceptance")
    ax.set_title("Operating characteristic (OC) curves", loc="left")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "08_oc_curves.png")


def fig_aoq():
    N, n, c = 2000, 80, 2
    p = np.linspace(0.0005, 0.12, 400)
    pa = stats.binom.cdf(c, n, p)
    aoq = 100 * pa * p * (N - n) / N
    ati = n + (1 - pa) * (N - n)
    asn = [sk.double_plan_pa_asn(v)[1] for v in p]
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    axes[0].plot(100 * p, aoq, color=BLUE, lw=2)
    i = int(np.argmax(aoq))
    axes[0].axhline(aoq[i], color=RED, ls="--")
    axes[0].text(7, aoq[i] + 0.04, f"AOQL ≈ {aoq[i]:.2f}%", color=RED)
    axes[0].set_xlabel("Incoming quality (% defective)")
    axes[0].set_ylabel("Average outgoing quality (%)")
    axes[0].set_title("AOQ curve (rectifying inspection)", loc="left")
    axes[1].plot(100 * p, ati, color=BLUE, label="ATI, single plan (lot N=2000)")
    axes[1].plot(100 * p, asn, color=ORANGE, ls="--", label="ASN, double plan")
    axes[1].axhline(80, color=GREY, ls=":", label="single-plan sample = 80")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("Incoming quality (% defective)")
    axes[1].set_ylabel("Units inspected per lot (log)")
    axes[1].set_title("Inspection effort: ATI and ASN", loc="left")
    axes[1].legend(frameon=False, fontsize=8)
    save(fig, "09_aoq_ati_asn.png")


if __name__ == "__main__":
    for f in (fig_histogram, fig_variation, fig_xbar_r, fig_imr, fig_p, fig_c, fig_short_run, fig_capability, fig_oc, fig_aoq):
        f()
    print("figures written to", os.path.abspath(FIG))
