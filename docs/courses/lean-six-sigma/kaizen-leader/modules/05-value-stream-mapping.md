# Module 5 — Value Stream Mapping

**Time:** 2 h

## Learning objectives

1. Draw a current-state value stream map (VSM) with data boxes and a timeline.
2. Calculate lead time and process cycle efficiency from the map.
3. Sketch a future state.

## 1. What a VSM shows

A value stream map (popularized by Rother and Shook's *Learning to See*, 1999) shows material flow **and** information flow on one page, with data for each process and a timeline that separates waiting from working.

## 2. Current state — carriage cell

```
 Production control ──(daily schedule to each step)──────────────────────────────►
                                                                                 
 [Kitting]   △   [Ball insert] △  [Preload set] △  [Seal & lube] △ [Friction test] △ [Pack] → Shipping
  C/T 40s  1800   C/T 75s     900  C/T 95s     650  C/T 60s     420  C/T 70s    300  C/T 45s  1100 FG
  C/O 0           C/O 35m          C/O 50m          C/O 10m          C/O 15m          C/O 5m
  Up 100%         Up 92%           Up 85%           Up 95%           Up 90%           Up 100%

 Timeline:  3.21 d | 40 s | 1.61 d | 75 s | 1.16 d | 95 s | 0.75 d | 60 s | 0.54 d | 70 s | 1.96 d | 45 s
```

(△ = inventory before the step, units. Inventory days = units ÷ 560/day.)

```bash
python tools/kaizen.py vsm
```

| Total | Value |
|---|---|
| Lead time | 3.21 + 1.61 + 1.16 + 0.75 + 0.54 + 1.96 = **9.23 days** |
| Value-added (processing) time | 40 + 75 + 95 + 60 + 70 + 45 = **385 s** |
| PCE | **0.08%** |

**Observations:** every step is pushed by its own schedule (no link to the customer); the biggest inventories are before kitting (released too early) and in finished goods (packed ahead of orders = overproduction); preload has the longest changeover and lowest uptime.

## 3. Future state — design questions

Rother and Shook's questions, applied:

1. **What is the takt?** 90 s.
2. **Build to a finished-goods supermarket or ship directly?** Small supermarket of fast runners; build slow runners to order.
3. **Where can we use continuous flow?** Ball insert → preload → seal & lube → test → pack in one U-cell (Module 8).
4. **Where do we need pull?** Kitting is replenished by kanban from the cell (Module 8).
5. **Single scheduling point?** The pack end of the cell (the pacemaker).
6. **How will we level the mix?** Small, repeating batches of each carriage size (enabled by quick changeover, Module 9).
7. **What process improvements are needed?** Preload changeover (SMED), preload uptime (TPM), layout.

**Future-state target:** WIP ≈ 1,800 units → lead time ≈ 3.2 days; output ≥ 560/day.

## Check yourself

Why does the timeline use inventory **days** rather than units?

<details><summary>Answer</summary>

Days of inventory equal how long a unit waits there (Little's law); adding them gives lead time, which the customer feels.
</details>
