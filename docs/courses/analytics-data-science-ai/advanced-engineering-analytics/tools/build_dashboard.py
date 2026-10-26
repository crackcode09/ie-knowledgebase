"""build_dashboard.py - build an interactive operations dashboard (single HTML file) with Plotly.

    pip install plotly
    python tools/build_dashboard.py            # writes dashboard/corbin_operations_dashboard.html

The HTML loads the Plotly JavaScript library from its public CDN, so open it with an internet
connection (or change include_plotlyjs to True to embed the ~4 MB library and work offline).
The same layout can be built in any BI tool (Tableau, Power BI, etc.) from data/ - see module 10.
License: MIT
"""
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import aeakit as ak  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "dashboard", "corbin_operations_dashboard.html")


def build(path=OUT):
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    t = ak.analysis_table()
    t["week"] = t.date.dt.to_period("W").dt.start_time
    o = pd.read_csv(os.path.join(ak.D, "customer_orders.csv"), parse_dates=["promised", "shipped"])
    o["on_time"] = (o.shipped <= o.promised).astype(int)
    o["week"] = o.promised.dt.to_period("W").dt.start_time
    m = pd.read_csv(os.path.join(ak.D, "maintenance_log.csv"))
    b = m[m.type == "breakdown"]

    colors = {"L1": "#2b6cb0", "L2": "#2f855a", "L3": "#718096", "L4": "#dd6b20"}
    kpi = dict(avail=100 * t.availability.mean(), scrap=100 * t.scrap_rate.mean(), otd=100 * o.on_time.mean(),
               below=100 * (t.seal_min < ak.SPEC_MIN_SEAL).mean())
    fig = make_subplots(rows=3, cols=2, vertical_spacing=0.12, horizontal_spacing=0.1,
                        specs=[[{"type": "indicator"}, {"type": "indicator"}], [{}, {}], [{}, {}]],
                        subplot_titles=("", "", "Weekly availability by line (%)", "Weekly on-time delivery by line (%)",
                                        "Breakdown minutes by failure mode", "Seal strength vs temperature (run means)"))
    fig.add_trace(go.Indicator(mode="number", value=kpi["avail"], number={"suffix": " %", "valueformat": ".1f"},
                               title={"text": "Availability (all lines)"}), 1, 1)
    fig.add_trace(go.Indicator(mode="number", value=kpi["otd"], number={"suffix": " %", "valueformat": ".1f"},
                               title={"text": "On-time delivery"}), 1, 2)
    for line in ak.LINES:
        w = t[t.line == line].groupby("week").availability.mean() * 100
        fig.add_trace(go.Scatter(x=w.index, y=w.values, mode="lines", name=line, legendgroup=line,
                                 line=dict(color=colors[line])), 2, 1)
        d = o[o.line == line].groupby("week").on_time.mean() * 100
        fig.add_trace(go.Scatter(x=d.index, y=d.values, mode="lines", name=line, legendgroup=line,
                                 showlegend=False, line=dict(color=colors[line])), 2, 2)
    fm = b.groupby(["failure_mode", "line"]).downtime_min.sum().unstack(fill_value=0)
    for line in ak.LINES:
        if line in fm:
            fig.add_trace(go.Bar(x=fm.index, y=fm[line], name=line, legendgroup=line, showlegend=False,
                                 marker_color=colors[line]), 3, 1)
    fig.update_layout(barmode="stack")
    fig.add_trace(go.Scatter(x=t.seal_temp_c, y=t.seal_mean, mode="markers", marker=dict(size=4, opacity=0.5, color=t.line.map(colors)),
                             text=t.run_id + " " + t.line, name="runs", showlegend=False), 3, 2)
    fig.add_trace(go.Scatter(x=[t.seal_temp_c.min(), t.seal_temp_c.max()], y=[ak.SPEC_MIN_SEAL] * 2, mode="lines",
                             line=dict(color="red", dash="dash"), name="min 18 N", showlegend=False), 3, 2)
    fig.update_layout(title=f"Corbin Packaging (fictional) - operations dashboard, Jan-Jun 2026 | scrap {kpi['scrap']:.2f}% | "
                            f"runs with a seal test < 18 N: {kpi['below']:.1f}%",
                      height=1000, template="simple_white", legend_title_text="Line")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.write_html(path, include_plotlyjs="cdn")
    return os.path.abspath(path)


if __name__ == "__main__":
    print("written", build())
