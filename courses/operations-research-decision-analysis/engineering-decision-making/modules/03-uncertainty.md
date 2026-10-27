# Module 03 — Uncertainty

Outline items: Aleatory and epistemic uncertainty · Assessing subjective probabilities

## Objectives

- Distinguish uncertainty you can reduce from uncertainty you can't.
- Elicit subjective probabilities, fit distributions to them, and check expert calibration.

## Aleatory and epistemic uncertainty

| | Aleatory | Epistemic |
|---|---|---|
| Source | Inherent randomness | Lack of knowledge |
| Reducible? | No, only describable | **Yes**, by gathering information |
| Corran example | Which week a given actuator fails; demand fluctuation from month to month | Size of the market next year; true MTBF of a new design |
| Response | Design margin, buffers, insurance | Tests, studies, prototypes (value of information, Module 07) |

Many quantities have both. For example, true average demand is epistemic, while monthly variation around it is aleatory. Separating them tells you **where information can help**.

## Assessing subjective probabilities

When data is scarce, **elicit** probabilities from experts with a structured process:

1. **Define** the quantity precisely ("units sold in the first 12 months after launch, all regions").
2. **Motivate and condition**: explain the use; ask the expert to think of reasons the value could be very high or very low (to counter anchoring).
3. **Encode extremes first**: ask for the P10 and P90 before the P50, to reduce anchoring on a central value.
4. **Check** with questions like "Is it equally likely to be above or below your P50?"
5. **Fit a distribution** and show it back to the expert.

Corran's sales lead gives demand **P10 3,000, P50 5,000, P90 9,000** units a year. A lognormal fits:

- σ(log) from the low side = 0.399, from the high side = 0.459; average **0.429**
- the fitted P10 and P90 are 2,887 and 8,660
- mean **5,481**; P(demand < 4,000) = **0.30**

The distribution is skewed right: upside beyond P90 is larger than downside below P10.

### Calibration

Experts are usually **overconfident**: their intervals are too narrow. Corran checked 24 of its past "80 % confident" intervals against what actually happened (`data/calibration.csv`):

- **9 of 24 (37.5 %)** contained the actual value, against the 80 % claimed.
- A binomial test gives p ≈ 0.00001. The overconfidence is clear.

Remedies:

- feedback and training on calibration
- widen intervals deliberately
- ask for extremes first
- combine several experts

## Run it

```bash
python tools/edmkit.py elicit
python tools/edmkit.py calibration
```

## Check yourself

1. Classify: (a) whether a specific fuse blows during a lightning storm; (b) the true failure rate of a new coating that has never been field-tested.
2. An expert's 80 % intervals contained the truth 9 times in 24. How many should they have contained?

<details><summary>Answers</summary>

1. (a) Aleatory (random event). (b) Epistemic (reducible by testing).
2. 0.8 × 24 = **19.2**, so about 19. Nine is far short: the expert is overconfident.

</details>
