# Module 09 — Classifying Movement Activities

## Objectives

- Decide which body member performs a movement.
- Separate movements from the terminal activity at their end.

## The classification question

For each movement, ask: **which is the largest body member that has to move to get the hand there?**

| If you see… | The body member is… | Teaching code |
|---|---|---|
| Only the fingers move (press a key, flick a switch) | Finger | A2 |
| The wrist bends; the forearm stays still | Hand | A3 |
| The elbow bends; the upper arm stays roughly still | Forearm | A4 |
| The shoulder moves the whole arm | Whole arm | A6 |
| The arm extends fully and the shoulder reaches forward | Extended arm | A8 |
| The trunk leans to extend reach (feet stay put) | Arm + trunk | A12 |

## Movement then terminal

Every movement ends in a **terminal activity**: a get (Module 15) or a put (Module 16). It may be a zero-time terminal (G0, P0), but it is always considered.

```
"Reach to bin and grasp a bolt"  →  A6 (movement)  G5 (get: selective)
"Move bolt to bag and drop it"   →  A6 (movement)  P0 (put: release)
```

## Loaded vs empty movements

A movement carrying an object is classified the same way as an empty one. **Weight** is handled separately with a load factor (auxiliary class, Module 19).

## Check yourself

Classify these movements:

1. Reaching to a part 40 cm away at bench height.
2. Pushing a button on the fixture 4 cm from the resting hand.
3. Leaning over a wide table to reach a part 80 cm away, without stepping.

<details><summary>Answers</summary>

1. Whole arm, **A6**.
2. Hand (wrist), **A3**. If only the finger moves, A2.
3. Arm plus trunk, **A12**. This is also an ergonomic flag (Module 20).

</details>
