# Module 02 — Time Units and System Levels

## Objectives

- Convert between TMU, seconds, hours and the course's teaching unit.
- Choose between detailed and higher-level systems.

## Units

| Unit | Seconds | Notes |
|---|---|---|
| **TMU** (MTM) | 0.036 | 1 TMU = 0.00001 h; **100,000 TMU = 1 hour** |
| **cs** (this course) | 0.01 | Teaching unit for the DTC |
| Second | 1 | |

Conversion example: 1.8 s = **180 cs = 50 TMU** = 0.0005 h.

TMU values are small, so detailed analyses add many motions. A 2-second operation can have 10–20 motion codes.

## Detailed vs higher-level systems

Detailed systems (such as MTM-1) analyse every basic motion. Higher-level systems combine motions into larger units for faster analysis ([Wikipedia](https://en.wikipedia.org/wiki/Methods-time_measurement); see also the [Predetermined Time Standards](../../predetermined-time-standards/README.md) course).

| Use a detailed system when… | Use a higher-level system when… |
|---|---|
| Cycles are short and repeated many times (seconds, thousands per day) | Cycles are long, with more variety |
| Small savings matter (0.1 s × 1 M cycles = 28 h) | Analysis speed matters more than precision |
| You are designing tooling, fixtures and workplace detail | You are planning capacity or staffing |
| You need to explain every element of a method | A good-enough standard is needed quickly |

## Check yourself

1. Convert 250 TMU to seconds and to cs.
2. A detailed redesign saves 0.15 s per cycle on 2 million cycles a year. How many hours is that?

<details><summary>Answers</summary>

1. 250 × 0.036 = **9.0 s** = **900 cs**.
2. 0.15 × 2,000,000 = 300,000 s = **83.3 h**.

</details>
