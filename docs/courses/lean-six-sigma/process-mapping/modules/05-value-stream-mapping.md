# Module 5 — Value Stream Mapping (Including Transactional Processes)

**Time:** 50 min

## Learning objectives

1. Draw a value stream map with process data and a timeline.
2. Use percent complete-and-accurate (%C&A) to show quality in information flow.
3. Sketch a future state.

## 1. Elements of a VSM

- **Process boxes** with data: process (work) time, lead time (elapsed), people, %C&A.
- **Inventory / queues** between boxes (parts on shelves, emails in inboxes).
- **Information flow** at the top (how work is triggered and scheduled).
- **Timeline** at the bottom: waiting above, work below; totals give lead time and process time.

Rother and Shook's *Learning to See* (1999) introduced VSM for manufacturing; Martin and Osterling's *Value Stream Mapping* (2013) adapted it for office and service processes and popularized **%C&A** — the share of work a step receives that it can use without correcting, adding missing information, or clarifying.

## 2. RMA current state (summary)

```
 Email / phone ──► Customer service ──► (spreadsheet) ──► everyone checks the spreadsheet

 [Request & authorize]  [Ship & receive]  [Diagnose & report]  [Approve]  [Repair & test]  [Ship & close]
  PT 23 min              PT 25 min         PT 70 min            PT 10 min  PT 80 min        PT 17 min
  %C&A 55% log,          %C&A 90%          %C&A 92%             %C&A 85%   %C&A 97%         %C&A 99%
       95% issue

 Timeline (wait):  30 h | 98 h | 34 h | 40 h | 32 h | 40 h        → lead time 277.8 h ≈ 11.6 days
 Timeline (work):  23 m | 25 m | 70 m | 10 m | 80 m | 17 m        → process time 3.75 h
```

```bash
python tools/pmap.py vsm
```

**Rolled %C&A** = product of each step's %C&A = 0.55 × 0.95 × 0.90 × 0.92 × 0.85 × 0.97 × 0.99 = **35%**. Only about one RMA in three flows through without someone correcting or chasing information. The worst step is the very first: **55%** of requests arrive incomplete.

## 3. Future state

| Problem | Future-state change |
|---|---|
| 55% of requests incomplete | Web RMA form with required fields and photo upload; RMA number issued automatically |
| 72 h for the customer to ship | Prepaid return label generated with the RMA |
| Parts moved between buildings | Triage at receiving; lab and repair co-located (Module 4) |
| 40 h waiting for engineering approval | Standard disposition rules; quality decides within rules; engineering reviews exceptions only |
| Close-out email nobody reads | Automatic status updates from the system |
| Spreadsheet tracking | Single RMA record visible to all lanes |

Target: lead time ≤ 6 days (Module 10 shows why), rolled %C&A ≥ 80%.

## Check yourself

Why multiply %C&A values rather than average them?

<details><summary>Answer</summary>

Each step's errors compound: a unit must be right at every step to flow through untouched, so the probabilities multiply (like rolled throughput yield).
</details>
