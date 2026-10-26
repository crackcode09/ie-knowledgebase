# Module 05 — Structure of a Standard Data System

## Objectives

- Organize elements into a coded hierarchy with clear boundaries.
- Separate constant and variable elements and assign a frequency to each.
- Build a lot standard from setup, run and allowances.

## Building blocks

| Part | Meaning | Harlan example |
|---|---|---|
| **Element** | A defined piece of work with clear start and end points | "Position and form one bend": starts when the part leaves the die, ends when the ram returns |
| **Constant element** | Same time on every job | Base setup (clear, load program, first-piece check) |
| **Variable element** | Time depends on a feature | Tool change: time per tool segment |
| **Frequency** | How often an element occurs | Per lot, per piece, per bend, per kg |
| **Code** | A unique ID for each element | PB-21 |
| **Range** | The values the element was built from | bends 1–12 |
| **Method description** | How the work is done, with tools and layout | Brake with two-finger backgauge; parts on a cart at the operator's left |
| **Source** | The studies behind each value | S01–S40, U01–U24 |

## The structure

```
Press-brake standard data (PB)
├── Setup (frequency: per lot)
│   ├── PB-10 Base setup ............................... constant
│   ├── PB-11 Change tooling ........................... variable × tool segments
│   └── PB-12 Write and prove new backgauge program .... constant, only when new
└── Run (frequency: per piece)
    ├── PB-20 Get blank, load, unload, aside ........... constant
    ├── PB-21 Position and form one bend ............... variable × bends
    ├── PB-22 Flip part between bends .................. variable × flips
    ├── PB-23 Weight handling increment ................ variable × kg
    └── PB-24 Length handling increment ................ variable × metres
```

## The data sheet

| Code | Element | Type | Frequency | Normal min |
|---|---|---|---|---|
| PB-10 | Setup: base | constant | per lot | 6.78 |
| PB-11 | Setup: change tooling | variable | per lot | 2.71 × tool segments |
| PB-12 | Setup: new backgauge program | constant | per lot, if new | 9.62 |
| PB-20 | Run: get blank, load, unload, aside | constant | per piece | 0.186 |
| PB-21 | Run: position and form one bend | variable | per bend | 0.087 |
| PB-22 | Run: flip part | variable | per flip | 0.118 |
| PB-23 | Run: weight increment | variable | per kg per piece | 0.023 |
| PB-24 | Run: length increment | variable | per metre per piece | 0.054 |

Allowance: **12 % PF&D** on normal time, added once at the job level.

The coefficients from the regression become element values directly. The **intercept** is the constant run element, and each **slope** is a variable element. This only works if the intercept makes physical sense. A negative intercept, for example, is a warning (Module 07).

## Job standard build-up

```
Lot standard (h) = [ setup + qty × run ] × (1 + PF&D) / 60
setup = PB-10 + PB-11 × segments + PB-12 × new
run   = PB-20 + PB-21 × bends + PB-22 × flips + PB-23 × kg + PB-24 × m
```

Two standards come out of every job:

- **Setup** (per lot), which belongs to the order
- **Run** (per piece), which belongs to the part

ERP routings usually store these separately. Merging them into a per-piece time hides the effect of lot size.

## Design rules

1. **Consistent element boundaries.** Every study used for an element must start and end at the same points. Otherwise the data mixes different work.
2. **Separate machine time and manual time** wherever a machine change could alter one but not the other.
3. **Put allowances in one place.** Keep elements at normal time and add allowances once. Adding them twice (in the element and again at the job) is a common error.
4. **Keep the frequency explicit.** "0.087 per bend" is safe. A bare "0.087" will eventually be applied per piece by mistake.
5. **Make variables easy to read from the drawing.** Bends and flips can be read from a flat pattern and bend sequence. "Difficulty" can't be read from anything.
6. **Version the data sheet.** Record the date, the source studies and the approver, so any standard can be traced back.

## Run it

```bash
python tools/sdskit.py structure
```

## Check yourself

1. Compute the standard for a 3-bend, no-flip, 1.0 kg, 500 mm part with 2 tool segments and an existing program, at lots of 10 and 100.
2. Which share of the 10-piece lot is setup?
3. An estimator adds 12 % to each element and then 12 % to the job. What error does that cause?

<details><summary>Answers</summary>

1. Run = 0.1863 + 0.0873·3 + 0.0226·1.0 + 0.0535·0.5 = **0.497 min**. Setup = 6.785 + 2.712·2 = **12.21 min**. Lot of 10: (12.21 + 4.97) × 1.12 / 60 = **0.321 h** (1.92 min/piece). Lot of 100: (12.21 + 49.7) × 1.12 / 60 = **1.157 h** (0.69 min/piece).
2. 12.21 / (12.21 + 4.97) = **71 %**. For short lots, setup reduction (SMED) pays more than speeding up the run.
3. The allowance is applied twice: 1.12² = 1.254, so the standard is **12 % too loose**, which overstates cost and understates efficiency.

</details>
