# Module 0 — Drawing a Process Picture: Why Map, and Which Map

**Time:** 40 min

## Learning objectives

1. Explain what a process map is for.
2. Choose the right type of map for a purpose.

## 1. Why map?

Everyone who works in a process carries a different picture of it in their head. A process map puts one shared picture on the wall so a team can agree on **where the process starts and ends, who is involved, the steps, the inputs, and the methods** — and then see the waste, delays and handoffs that nobody sees from inside a single step.

A map is a communication tool first. Choose the format that answers your question for your audience.

## 2. Types of process maps

| Map | Shows | Best for | Module |
|---|---|---|---|
| **SIPOC** | Suppliers, inputs, 5–7 high-level steps, outputs, customers | Agreeing scope and boundaries at the start | 1 |
| **Flow chart** | Steps, decisions, loops | Understanding the sequence and logic | 2 |
| **Swim-lane (cross-functional) map** | Steps by role/department | Handoffs, ownership, waiting between groups | 2 |
| **Value-added flow chart** | Steps classified VA / business-required / waste, with times | Finding non-value-added work | 3 |
| **Spaghetti diagram** | Physical path of material, information or people on a layout | Transport and motion waste | 4 |
| **Value stream map** | Material + information flow, inventory, timeline | End-to-end flow and lead time | 5 |

**Choosing:** start broad (SIPOC), then go deeper only where the problem is. Map **as-is** first — what actually happens, verified by walking the process — before designing **to-be**.

## 3. Running case

A manufacturer's **RMA process** (return merchandise authorization: a customer returns a failed linear guide carriage for diagnosis and repair). Customers complain that it takes "two weeks and endless emails." All numbers come from `python tools/pmap.py all`.

## 4. Mapping tips

- Map with the people who do the work, at the place where it's done.
- Use sticky notes first; formalize later.
- Agree the start and end triggers before drawing steps.
- Use a verb + noun for each step ("Inspect part," not "Inspection").
- Record what you see, including rework loops and workarounds.

Diagrams in this course are written in Mermaid, which GitHub renders directly — copy them as starting templates.

## Check yourself

You need to show a plant manager why parts travel 500 m before shipping. Which map?

<details><summary>Answer</summary>

A spaghetti diagram on the floor layout.
</details>
