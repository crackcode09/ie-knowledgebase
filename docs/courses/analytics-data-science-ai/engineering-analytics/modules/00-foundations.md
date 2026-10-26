# Module 00 — Foundations: Engineering Analytics and the Strategic Role of Data

## Objectives

- Define engineering analytics and the four types of analytics.
- Describe a repeatable analytics process from question to decision.
- Explain how analytics creates business impact — and where it fails.

## What is engineering analytics?

**Engineering analytics** turns operational, product and customer data into insights that lead to better decisions. It combines engineering knowledge (how processes and products behave), statistics and modeling, and data technology.

| Type | Question | Example at Ridgeway | Module |
|---|---|---|---|
| **Descriptive** | What happened? | revenue by product family; energy per unit | 01, 02 |
| **Diagnostic** | Why did it happen? | third-shift days use 2,400 kWh more | 04 |
| **Predictive** | What will happen? | which machines will fail in 30 days; next quarter's sales | 03, 05 |
| **Prescriptive** | What should we do? | best weekly product mix | 07 |

Value usually rises from descriptive to prescriptive — and so do data and skill requirements. Most organizations get large gains from getting descriptive analytics right first.

## A process from question to decision

A widely used framework (CRISP-DM, the Cross-Industry Standard Process for Data Mining) has six phases; in plain terms:

1. **Understand the business question** — what decision will this inform, and what is it worth?
2. **Understand the data** — what exists, where, how good is it?
3. **Prepare the data** — clean, join, reshape, create features. Often 60–80 % of the effort (a commonly quoted estimate).
4. **Model** — the analytics technique.
5. **Evaluate** — does it answer the question accurately enough? Test on data the model hasn't seen.
6. **Deploy** — put it into a dashboard, a work process or a system, and monitor it.

The loop matters: evaluation often sends you back to the question or the data.

## Business impact and the strategic role of data

Analytics creates value only when a **decision or action changes**:

| Area | Analytics | Decision changed |
|---|---|---|
| Customers | segmentation | different service levels and pricing per segment |
| Operations | performance tracking, energy regression | shift scheduling, energy contracts |
| Maintenance | failure prediction | inspect flagged machines first |
| Inventory | ABC classification | review frequency and safety stock by class |
| Sales | forecasting | production and purchasing plans |
| Planning | optimization | product mix, capacity investment |

Data becomes a **strategic asset** when it is reliable, shared, and used repeatedly — when the same clean customer, product and equipment data feeds many decisions. That needs data ownership, definitions and quality standards (Module 06).

**Common failure modes of analytics projects:** a question nobody owns; data too poor to trust; a model nobody understands; a dashboard nobody looks at; no plan to change the process.

## Running case and tools

**Ridgeway Industrial** (fictional) makes and distributes industrial fittings — elbows, tees and valves. Datasets in `data/`:

| File | Used in |
|---|---|
| `ridgeway.db` (SQLite: orders star schema, 4,000 order lines from the distributor channel, 2026) | 01, 02 |
| `customers.csv` (300 customers) | 02, 03 |
| `skus.csv` (500 stocked items) | 03 |
| `machine_health.csv` (1,200 machine snapshots) | 03 |
| `plant_energy.csv` (522 workdays) | 01, 02, 04 |
| `process_batches.csv` (400 batches, 10 sensors) | 05 |
| `monthly_sales.csv` (company-wide, 60 months) | 05 |
| `ridgeway.xlsx` (the main tables, for spreadsheet users) | all |

All data is simulated with a fixed seed. Every technique is shown in Python with free, open-source libraries (pandas, scikit-learn, statsmodels, SciPy, SQLite), and each module notes how to do the same in a spreadsheet.

```bash
pip install -r requirements.txt
python tools/anlkit.py all
```

## Check yourself

1. Classify each as descriptive, diagnostic, predictive or prescriptive: (a) a monthly scrap Pareto, (b) a model of next month's demand, (c) why scrap rose in March, (d) a schedule that minimizes changeovers.
2. Why does an analytics project need a decision owner before it starts?

<details><summary>Answers</summary>

1. (a) descriptive, (b) predictive, (c) diagnostic, (d) prescriptive.
2. Without someone who will act on the result, even a good model changes nothing; the owner also defines what accuracy is "good enough."

</details>
