# Module 00 — Introduction: Finance for the Engineer-Manager

## Objectives

- Explain why an engineer running a profit center needs financial literacy.
- Distinguish accounting (recording what happened) from finance (deciding what to do with money).
- Meet the running case and the course roadmap.

## Why this matters

Engineers get promoted into running a cell, a department or a product line. The day they do, their performance is reported in dollars: margin, budget variance, return on capital. Engineering proposals — a new machine, an automation cell, a scrap-reduction project — are approved or rejected on financial criteria. Speaking the language is the difference between "good idea" and "funded."

## Accounting vs finance

| | Accounting | Finance |
|---|---|---|
| Question | What happened? | What should we do? |
| Time | Past, period by period | Future cash flows |
| Main output | Financial statements | Decisions: invest, borrow, price, budget |
| Basis | Accrual (revenue when earned, cost when incurred) | Cash, timed and risk-adjusted |
| Rules | Accounting standards (e.g. US GAAP, IFRS) | Economic logic; company policy |

**Profit is not cash.** A plant can report profit and still run out of cash (customers pay slowly, inventory piles up, a machine is bought). Module 04 shows exactly how.

## The accounting equation

**Assets = Liabilities + Equity**

Everything the business owns was funded by someone: lenders and suppliers (liabilities) or owners (equity). Every transaction keeps the equation in balance.

## Running case

**Riverbend Motion Components, Inc.** (fictional) makes linear-motion parts — shafts, bearings, slides — with about $48 million in annual revenue. You manage **Cell 7**, a precision-machining profit center. All figures are illustrative and simplified; the tax rate used throughout is a flat **25 %** for teaching, not any jurisdiction's actual rate.

| Module | Question about Riverbend |
|---|---|
| 01 | What kind of entity is it, and what is a "profit center"? |
| 02–04 | What do its balance sheet, income statement and cash flow say? |
| 05 | How healthy is it? Build a dashboard. |
| 06 | Did Cell 7 hit its budget, and why not? |
| 07 | How do we compare money at different times? |
| 08 | Where does capital come from and what does it cost? |
| 09–11 | Should we buy a $1.2M 5-axis machining center? Lease it? What if we're wrong? |
| 12 | How many parts must Cell 7 sell to break even? Should it automate? |
| 13 | What is the whole company worth? |

## Getting started

```bash
pip install -r requirements.txt
python tools/finkit.py all
```

A spreadsheet works for every calculation in the course; formulas are given alongside the Python.

## Check yourself

1. A customer order ships in December and is paid in February. In which month is the revenue recorded, and in which is the cash received?
2. Riverbend buys $500k of inventory on 60-day credit. Which two parts of the accounting equation change?

<details><summary>Answers</summary>

1. Revenue is recorded in December (when earned, under accrual accounting); cash arrives in February.
2. Assets (inventory) rise $500k and liabilities (accounts payable) rise $500k. Equity is unchanged.

</details>
