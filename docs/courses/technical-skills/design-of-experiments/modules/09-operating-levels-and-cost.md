# Module 09: Determining Operating Levels: Quality, Cost and Productivity

## Objectives

- Use a fitted model to predict every candidate setting.
- Add cost and productivity to the decision, not just the response.
- Build in a safety margin and confirm before you standardize.

## Concept

An experiment tells you how factors move the response. The operating decision also needs:

- **Specification:** what response is good enough.
- **Cost:** machine time, material, energy, scrap.
- **Productivity:** cycle time and throughput.
- **Uncertainty:** a prediction is a mean. Individual parts scatter around it with SD σ, and the model coefficients have error too.

A simple recipe:

1. Predict y at every candidate setting from the model.
2. Keep the settings that meet spec *with margin*.
3. Among those, pick the cheapest or fastest.
4. Run **confirmation runs** at the chosen setting and compare them with the prediction interval.

## Worked example: warpage vs cycle cost

The specification is warpage ≤ 110 µm. Use the Module 07 model:

ŷ = 119.35 + 6.53A − 13.68B − 10.78C − 8.51D + 7.18BC

The cost model below is **illustrative**; substitute your own plant's numbers.

- Cycle time (s) = 30 + 4·D + 1.5·B. Long cooling and a hot mold slow the cycle.
- Cost per part = cycle × $0.012/s machine rate, plus $0.30 expected scrap and rework if predicted warpage is above 110 µm.

| A | B | C | D | Predicted warpage (µm) | Cycle (s) | Cost ($) | Meets spec |
|---|---|---|---|---|---|---|---|
| − | + | + | + | **87.0** (lowest) | 35.5 | 0.426 | yes |
| − | + | − | + | 94.2 | 35.5 | 0.426 | yes |
| − | − | + | + | 100.0 | 32.5 | 0.390 | yes |
| + | + | + | + | 100.1 | 35.5 | 0.426 | yes |
| − | + | + | − | 104.1 | 27.5 | **0.330** (cheapest) | yes |
| + | + | − | + | 107.3 | 35.5 | 0.426 | yes |
| − | + | − | − | 111.3 | 27.5 | 0.630 | no |
| others | | | | 113 to 166 | | | no |

Six of the 16 settings meet spec.

- **Lowest warpage:** A−, B+, C+, D+ gives 87.0 µm at a 35.5 s cycle.
- **Cheapest compliant setting:** A−, B+, C+, D− gives 104.1 µm at a 27.5 s cycle. That is 8 s faster, about 29 % more parts per hour from the same press.

### Is 104.1 µm safe enough?

The margin to spec is 5.9 µm. The residual SD is 3.17 µm, so individual parts at that setting are spread roughly ±6 µm (2σ). Some parts would exceed 110 µm. Options:

- **Accept a middle setting:** A−, B−, C+, D+ predicts 100.0 µm at a 32.5 s cycle, for 10 µm of margin and a cost of $0.39.
- **Tighten σ:** look for the noise source.
- **Confirm first:** make about 10 parts at A−, B+, C+, D−. If their mean falls inside the prediction interval and the individual values stay under spec, standardize.

### Don't forget other responses

- High hold pressure (C+) also drives **flash** (Module 08).
- Low melt temperature can hurt fill and weld-line strength.

Overlay the constraints from every response before you choose. A common tool is a desirability function, or simply a table like the one above with one column per response.

## Run it

```bash
python tools/doekit.py optimize
```

## Check yourself

1. Why is "the setting with the lowest predicted warpage" often not the answer?
2. Why should you not extrapolate this model to a mold temperature of 100 °C?
3. Confirmation runs average 112 µm at the chosen setting. What now?

<details><summary>Answers</summary>

1. It ignores cost, cycle time, other responses and margin. Here it costs 29 % throughput for a quality gain the specification does not need.
2. The model is only supported between 70 and 90 °C. Curvature, flash and degradation risks outside that range are unknown.
3. Compare 112 with the prediction interval. If it falls outside, something has changed (a lurking variable, the measurement system or interactions the model omits): investigate before adjusting. If it is inside but over spec, move to a setting with more margin.

</details>
