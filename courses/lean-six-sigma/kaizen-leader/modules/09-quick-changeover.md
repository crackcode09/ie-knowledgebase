# Module 9 — Quick Changeover (SMED)

**Time:** 75 min

## Learning objectives

1. Analyze a changeover into internal and external elements.
2. Apply the SMED steps to cut changeover time.

## 1. SMED

Shigeo Shingo's **Single-Minute Exchange of Die** (*A Revolution in Manufacturing: The SMED System*, 1985) aims for changeovers under 10 minutes ("single-digit minutes").

- **Internal** elements: can only be done with the machine stopped.
- **External** elements: can be done while the machine is running.

## 2. The steps

1. **Observe and record** the whole changeover (video it); list every element with its time.
2. **Separate** internal from external — do external work before or after the stop.
3. **Convert** internal to external (pre-heat, pre-set, duplicate fixtures).
4. **Streamline** what remains: quick clamps, locating pins, eliminate adjustments, parallel work, standard tools at point of use.
5. **Standardize** the new method and train.

## 3. Case — preload station changeover

```bash
python tools/kaizen.py smed
```

| Element | Time (min) | Before | After |
|---|---|---|---|
| Find next fixture and gauge | 9 | internal (done after stopping) | **external** (pre-staged on a cart) |
| Remove old fixture | 5 | internal | internal |
| Clean locating surfaces | 4 | internal | internal |
| Fetch shims from crib | 7 | internal | **external** (shim kit on cart) |
| Mount new fixture (8 bolts) | 10 | internal | **2** (quick clamps + locating pins) |
| Set preload, trial parts | 15 | internal | **6** (preset gauge; first-part standard) |
| **Machine stopped** | | **50 min** as practised | **17 min** |

The 50-minute stop in the VSM included 16 minutes of fetching that is really external. Separating alone gets to 34 minutes; converting and streamlining get to **17 minutes** — a 50% cut on the 34 and 66% on the 50 actually experienced.

**Effect:** with one changeover per shift, preload gains ~66 minutes per day of running time; uptime rises; smaller, more frequent batches become affordable (level mix, smaller supermarket).

## Check yourself

Name one way to convert "set preload" further toward external.

<details><summary>Answer</summary>

Use a second fixture that is pre-set and verified offline on a gauge while the machine runs the current size, so only a swap is internal.
</details>
