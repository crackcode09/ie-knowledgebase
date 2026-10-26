# Module 1 — Voice of the Customer

**Time:** 2.5 h · **Phase:** Define

## Learning objectives

1. Gather VOC from appropriate sources and segments.
2. Size and design a customer survey.
3. Organize raw VOC with an affinity diagram and classify needs with the Kano model.

## 1. Who is the customer?

Most designs have several customers with different needs. For an industrial component: the **design engineer** who specifies it, **purchasing** who buys it, the **assembler** who installs it, the **maintenance technician** who services it, and the **end user** whose machine depends on it.

**Market segmentation** groups customers whose needs are similar enough to serve with one design. Common bases: industry/application, size, geography, buying behavior, performance needs. A good segment is identifiable, large enough to matter, reachable, and responds differently from other segments.

## 2. VOC sources

| Reactive (already exists) | Proactive (you go get it) |
|---|---|
| Complaints, returns, warranty data | Interviews (one-on-one, 30–60 min) |
| Service and sales notes | Site visits / watching customers use the product (gemba) |
| Online reviews, forums | Focus groups |
| Lost-order reasons | Surveys |

Interviews and observation find needs customers can't articulate; surveys measure how widespread and important known needs are. Do qualitative work first, then quantify.

## 3. Surveys

### Sample size for estimating a proportion

  n = z² · p(1 − p) / E²  (use p = 0.5 if unknown; E = margin of error)

| Target | n |
|---|---|
| ±5%, 95% confidence | 385 |
| ±5%, 95%, population of only 800 customers (finite-population correction) | 260 |
| ±3%, 95% | 1,068 |

```bash
python tools/dfss.py survey
```

These are numbers of **completed** responses. With a 20% response rate, invite five times as many — and worry about non-response bias (the people who answer may differ from those who don't).

### Writing good questions

- One idea per question ("Is the guide quiet and smooth?" is two questions).
- Neutral wording ("How would you rate…" not "How much do you like our improved…").
- Balanced scales with a midpoint; label every point.
- Ask about behavior and needs, not solutions ("What happens when a guide fails?" not "Would you like a self-lubricating guide?").
- Pilot the survey with 5–10 people before sending.

## 4. Affinity diagram

Turns dozens of raw comments into a handful of need themes.

1. Write each verbatim comment on a card (keep the customer's words).
2. Team sorts cards silently into natural groups.
3. Name each group with a header that states the underlying need.
4. Group headers into a hierarchy if useful.

Example raw comments → themes:

| Raw comments | Theme (need) |
|---|---|
| "It sticks after sitting overnight" · "jerky at slow speed" · "takes too much force to push" | **Slides smoothly** |
| "Moves when the cutter hits" · "deflects under the gripper load" | **Holds position under load** |
| "We re-grease every month" · "seals wear out" | **Low maintenance** |
| "Operators complain about the whine" | **Quiet** |
| "Competitor quoted 20% less" | **Affordable** |

## 5. Kano model

Noriaki Kano's model (1984) classifies needs by how satisfaction responds to performance:

| Type | If missing | If present | Example |
|---|---|---|---|
| **Must-be (basic)** | Very dissatisfied | Not noticed | Guide doesn't corrode |
| **One-dimensional (performance)** | Dissatisfied | More is better | Lube interval, friction |
| **Attractive (delighter)** | Not missed | Delighted | Wear indicator visible without disassembly |
| Indifferent | — | — | Color of the end cap |

Must-be needs rarely come up in interviews (customers assume them) but failing one loses the customer. Delighters become must-bes over time.

## Check yourself

1. Why do interviews before a survey?
2. You need ±5% at 95% confidence and expect a 25% response rate from a large population. How many surveys do you send?

<details><summary>Answers</summary>

1. Interviews discover needs; surveys can only measure the needs you already thought to ask about.
2. 385 completed / 0.25 = 1,540 invitations.
</details>
