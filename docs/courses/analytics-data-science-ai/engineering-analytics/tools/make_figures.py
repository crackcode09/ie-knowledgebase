"""make_figures.py - regenerate every figure in figures/.

    python tools/make_figures.py

License: MIT
"""
import os
import sqlite3
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import anlkit as ak  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, GREEN, RED = "#2b6cb0", "#dd6b20", "#a0aec0", "#2f855a", "#c53030"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_energy_scatter():
    e = ak.load("plant_energy.csv")
    fig, ax = plt.subplots(figsize=(6.5, 4))
    for s, c in ((2, GREY), (3, ORANGE)):
        d = e[e.shifts == s]
        ax.scatter(d.units_produced, d.kwh / 1000, s=10, alpha=0.6, color=c, label=f"{s} shifts")
    ax.set_xlabel("Units produced per day")
    ax.set_ylabel("Electricity (MWh per day)")
    ax.set_title("Third-shift days use more energy at every output level", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "01_energy_scatter.png")


def fig_small_multiples():
    with sqlite3.connect(ak.DB) as con:
        d = pd.read_sql("""SELECT p.family, d.month, SUM(f.qty * f.net_price) / 1000.0 AS rev
                           FROM fact_orders f JOIN dim_product p ON f.product_id = p.product_id
                           JOIN dim_date d ON f.date = d.date GROUP BY p.family, d.month""", con)
    fams = ["Valves", "Tees", "Elbows"]
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), sharey=True)
    for ax, fam in zip(axes, fams):
        for other in fams:
            g = d[d.family == other]
            ax.plot(g.month, g.rev, color=BLUE if other == fam else "#e2e8f0", lw=2 if other == fam else 1,
                    zorder=3 if other == fam else 1)
        ax.set_title(fam, loc="left")
        ax.set_xticks([1, 4, 7, 10])
        ax.set_xticklabels(["Jan", "Apr", "Jul", "Oct"])
    axes[0].set_ylabel("Revenue ($000 per month)")
    fig.suptitle("Small multiples: valves carry the revenue; no family shows a clear seasonal pattern", x=0.01, ha="left",
                 weight="bold")
    save(fig, "01_small_multiples.png")


def fig_clusters():
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    c = ak.load("customers.csv")
    X = c[["annual_revenue", "orders_per_year", "return_rate", "days_since_last_order"]].copy()
    X["annual_revenue"] = np.log10(X.annual_revenue)
    lab = KMeans(n_clusters=3, n_init=20, random_state=0).fit_predict(StandardScaler().fit_transform(X))
    med = pd.Series(c.annual_revenue).groupby(lab).median().sort_values(ascending=False)
    names = dict(zip(med.index, ["Key accounts", "Regular OEMs", "Occasional buyers"]))
    fig, ax = plt.subplots(figsize=(6.5, 4))
    for k, col in zip(med.index, (BLUE, ORANGE, GREY)):
        m = lab == k
        ax.scatter(c.orders_per_year[m], c.annual_revenue[m] / 1000, s=14, color=col, alpha=0.7, label=names[k])
    ax.set_yscale("log")
    ax.set_xlabel("Orders per year")
    ax.set_ylabel("Annual revenue ($000, log scale)")
    ax.set_title("k-means finds three customer segments", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "03_customer_clusters.png")


def fig_abc():
    s = ak.abc_table()
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(s.cum_sku_pct, s.cum_value_pct, color=BLUE, lw=2)
    for pct, lab in ((80, "A | B"), (95, "B | C")):
        x = s.cum_sku_pct[s.cum_value_pct >= pct].iloc[0]
        ax.axhline(pct, color=GREY, ls=":", lw=0.8)
        ax.axvline(x, color=GREY, ls=":", lw=0.8)
        ax.text(x + 1, pct - 6, f"{lab}\n{x:.0f}% of SKUs", fontsize=8)
    ax.set_xlabel("Cumulative % of SKUs (sorted by annual usage value)")
    ax.set_ylabel("Cumulative % of annual usage value")
    ax.set_title("ABC classification: 20% of SKUs carry 80% of value", loc="left", weight="bold")
    save(fig, "03_abc_curve.png")


def fig_roc():
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    from sklearn.metrics import roc_curve
    m = ak.load("machine_health.csv")
    feats = ["age_years", "vibration_mm_s", "bearing_temp_c", "motor_current_a", "hours_per_day"]
    Xtr, Xte, ytr, yte = train_test_split(m[feats], m.failed_within_30d, test_size=0.3, random_state=7,
                                          stratify=m.failed_within_30d)
    p = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr).predict_proba(Xte)[:, 1]
    fpr, tpr, thr = roc_curve(yte, p)
    fig, ax = plt.subplots(figsize=(5.2, 4.4))
    ax.plot(fpr, tpr, color=BLUE, lw=2, label="logistic regression")
    ax.plot([0, 1], [0, 1], color=GREY, ls="--", label="random guessing")
    for t, c in ((0.5, ORANGE), (0.25, GREEN)):
        pred = p >= t
        tp = (pred & (yte == 1)).sum() / (yte == 1).sum()
        fp = (pred & (yte == 0)).sum() / (yte == 0).sum()
        ax.scatter(fp, tp, color=c, zorder=3, label=f"threshold {t}")
    ax.set_xlabel("False-positive rate (healthy machines flagged)")
    ax.set_ylabel("True-positive rate (recall)")
    ax.set_title("ROC curve: failure-in-30-days model", loc="left", weight="bold")
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    save(fig, "03_roc_curve.png")


def fig_regression():
    import statsmodels.formula.api as smf
    e = ak.load("plant_energy.csv")
    e["temp_dev"] = (e.outdoor_temp_c - 15).abs()
    e["third_shift"] = (e.shifts == 3).astype(int)
    m = smf.ols("kwh ~ units_produced + third_shift + temp_dev", data=e).fit()
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    axes[0].scatter(m.fittedvalues / 1000, e.kwh / 1000, s=8, color=BLUE, alpha=0.5)
    lim = [e.kwh.min() / 1000, e.kwh.max() / 1000]
    axes[0].plot(lim, lim, color=ORANGE)
    axes[0].set_xlabel("Predicted MWh")
    axes[0].set_ylabel("Actual MWh")
    axes[0].set_title(f"Predicted vs actual (R² = {m.rsquared:.2f})", loc="left")
    axes[1].scatter(m.fittedvalues / 1000, m.resid / 1000, s=8, color=GREY)
    axes[1].axhline(0, color=ORANGE)
    axes[1].set_xlabel("Predicted MWh")
    axes[1].set_ylabel("Residual MWh")
    axes[1].set_title("Residuals: no pattern = model form is reasonable", loc="left")
    save(fig, "04_energy_regression.png")


def fig_pca():
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    d = ak.load("process_batches.csv")
    Z = StandardScaler().fit_transform(d.drop(columns="yield_pct"))
    ev = PCA().fit(Z).explained_variance_ratio_ * 100
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.bar(range(1, 11), ev, color=[BLUE] * 3 + [GREY] * 7)
    ax.plot(range(1, 11), np.cumsum(ev), color=ORANGE, marker="o", label="cumulative")
    ax.set_xticks(range(1, 11))
    ax.set_xlabel("Principal component")
    ax.set_ylabel("% of variance explained")
    ax.set_title("Scree plot: 10 sensors, 3 underlying sources of variation", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "05_pca_scree.png")


def fig_forecast():
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    s = ak.load("monthly_sales.csv")
    y = s.sales_k.values
    hw = ExponentialSmoothing(y[:48], trend="add", seasonal="mul", seasonal_periods=12).fit()
    f = hw.forecast(12)
    x = np.arange(60)
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.plot(x[:48], y[:48], color=GREY, label="training data")
    ax.plot(x[48:], y[48:], color="black", marker="o", ms=3, label="actual (holdout)")
    ax.plot(x[48:], f, color=BLUE, lw=2, label="Holt-Winters forecast")
    ax.plot(x[48:], y[36:48], color=ORANGE, ls="--", label="seasonal naive")
    ax.set_xticks(range(0, 60, 12))
    ax.set_xticklabels(s.month[::12])
    ax.set_ylabel("Sales ($000 per month)")
    ax.set_title("Forecast vs holdout: modeling trend and season pays off", loc="left", weight="bold")
    ax.legend(frameon=False, fontsize=8, ncol=2)
    save(fig, "05_forecast_holdout.png")


if __name__ == "__main__":
    for fn in (fig_energy_scatter, fig_small_multiples, fig_clusters, fig_abc, fig_roc, fig_regression, fig_pca,
               fig_forecast):
        fn()
    print("figures written to", os.path.abspath(FIG))
