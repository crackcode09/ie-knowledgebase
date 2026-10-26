# Module 9 — Measuring Central Tendency

**Time:** 30 min · **Data:** `data/shaft_diameter.csv`, `data/lead_time.csv`

## Learning objectives

1. Compute the mean, median and mode.
2. Choose the right measure of center for the data's shape.
3. Locate the center of a process.

## 1. Three measures

| Measure | How | Strength | Weakness |
|---|---|---|---|
| **Mean** x̄ | Sum ÷ n | Uses every value; basis for most statistics | Pulled by skew and outliers |
| **Median** | Middle value of sorted data (average of the two middle values if n is even) | Robust to skew and outliers | Ignores the size of extreme values |
| **Mode** | Most frequent value | Only measure for nominal data | Unstable for continuous data |
| *Trimmed mean* | Mean after dropping the top and bottom x% | Compromise between mean and median | Less familiar |

## 2. Hand calculation

Five shaft diameters (mm): 12.717, 12.704, 12.700, 12.699, 12.692

- Mean = 63.512 / 5 = **12.7024**
- Sorted: 12.692, 12.699, **12.700**, 12.704, 12.717 → median = **12.700**
- Mode: none (all values differ)

## 3. Symmetric vs skewed data

```bash
python tools/describe.py summary data/shaft_diameter.csv mm
python tools/describe.py summary data/lead_time.csv days
```

| | Shaft diameter (100 parts) | Lead time (60 orders) |
|---|---|---|
| Shape | Roughly symmetric | Right-skewed |
| Mean | 12.7001 mm | **6.39 days** |
| Median | 12.699 mm | **5.35 days** |
| 10% trimmed mean | 12.6996 mm | 5.96 days |

For the shaft, mean ≈ median — either describes the center. For lead time the mean is about a day higher than the median because a few orders took 14–15 days.

**Which to report?** It depends on the question:

- "What does a typical customer experience?" → **median** (5.35 days: half of orders ship faster).
- "How many order-days of work are in the system?" or "What's the total cost?" → **mean** (totals = mean × n).
- Report both for skewed data, and show the histogram.

## 4. Locating the center of a process

The center is only meaningful for a **stable** process. If the process drifted during data collection, "the center" is an average of different processes. Plot the data in time order first (*Charting Process Behavior*).

## Check yourself

1. Repair costs: 120, 140, 150, 160, 2,900 USD. Mean and median? Which describes a typical repair?
2. Which measure of center works for "most common defect type"?

<details><summary>Answers</summary>

1. Mean = 694, median = 150. The median describes a typical repair; the mean is needed for the total budget (5 × 694 = 3,470).
2. The mode.
</details>
