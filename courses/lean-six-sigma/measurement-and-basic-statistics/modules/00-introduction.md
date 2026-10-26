# Module 0 — Introduction: Solving Problems with Statistics

**Time:** 25 min · **Prerequisites:** none

## Learning objectives

1. Explain why measurement and statistics matter in process improvement.
2. Describe the practical-problem → statistical-problem → statistical-solution → practical-solution loop.

## 1. Why bother?

Opinions about a process are cheap and often wrong. "Late deliveries are our biggest complaint" may be true by count but false by cost (Module 6). "Supplier A and B are the same — both average 10.00 mm" may hide that one of them will eventually ship bad parts (Module 8). Measurement turns opinions into facts; statistics turns piles of facts into information you can act on.

## 2. The four-step loop

```
 Practical problem  ──►  Statistical problem
 "Customers complain        "What is the distribution of lead
  orders are late"           time, and what drives its spread?"
        ▲                               │
        │                               ▼
 Practical solution  ◄──  Statistical solution
 "Fix the two biggest       "Lead time is skewed; 7 of 60 orders
  causes of long waits"      exceed 10 days, mostly one category"
```

Most improvement methods, including Lean Six Sigma's DMAIC (Define, Measure, Analyze, Improve, Control), follow this loop. This course covers the **Measure** toolkit: getting good data and summarizing it honestly.

## 3. Course map

| # | Module | Time |
|---|---|---|
| 1 | Basic statistical and Lean Six Sigma terms | 30 min |
| 2 | Descriptive vs inferential statistics | 20 min |
| 3 | Measurement and data types; discrete vs continuous | 30 min |
| 4 | Selecting the best measurement; accuracy vs precision | 35 min |
| 5 | Graphical summaries | 25 min |
| 6 | Pareto charts | 35 min |
| 7 | Histograms | 35 min |
| 8 | Understanding variation; why averages mislead | 35 min |
| 9 | Measuring central tendency | 30 min |
| 10 | Quantifying variability | 35 min |
| 11 | The normal distribution | 35 min |
| 12 | Wrap-up skill check | 30 min |

## 4. Setup

```bash
cd ie-knowledgebase/courses/lean-six-sigma/measurement-and-basic-statistics
pip install -r requirements.txt
python tools/make_data.py
python tools/describe.py summary data/shaft_diameter.csv mm
```

No Python? Every calculation works in a spreadsheet — see `reference/spreadsheet-recipes.md`.

## Where to go next

This course is the foundation for the other two in this repository: *Charting Process Behavior* (data over time) and *Fundamentals of Hypothesis Testing* (deciding with data).
