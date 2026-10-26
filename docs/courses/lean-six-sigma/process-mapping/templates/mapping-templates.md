# Mapping Templates

Copy these into your own Markdown (GitHub renders Mermaid diagrams) or onto a whiteboard.

## SIPOC

| Suppliers | Inputs | Process (5–7 steps) | Outputs | Customers |
|---|---|---|---|---|
| | | Start trigger: | | |
| | | 1. | | |
| | | 2. | | |
| | | 3. | | |
| | | 4. | | |
| | | 5. | | |
| | | End point: | | |

## Flow chart

```mermaid
flowchart TD
    S([Start trigger]) --> A[Step 1]
    A --> D{Decision?}
    D -- Yes --> B[Step 2]
    D -- No --> R[Rework] --> A
    B --> E([End])
```

## Swim lanes

```mermaid
flowchart LR
    subgraph Role_A[Role A]
      A1([Start]) ; A2[Step]
    end
    subgraph Role_B[Role B]
      B1[Step] ; B2{Decision}
    end
    subgraph Role_C[Role C]
      C1[Step] ; C2([End])
    end
    A1 --> B1 --> A2 --> B2 --> C1 --> C2
```

## Value-added flow chart worksheet

| # | Step | Owner | Work (min) | Wait before (h) | VA / BVA / NVA | Why this class? |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

Totals: work by class; total wait; lead time; VA ÷ lead time; handoffs.

## Spaghetti worksheet

| Move # | From | To | Distance (m) | Why? |
|---|---|---|---|---|
| 1 | | | | |

## CTQ tree

```mermaid
flowchart LR
    N[Customer need, in their words] --> D1[Driver] --> C1[CTQ: metric, target, limit]
    N --> D2[Driver] --> C2[CTQ: metric, target, limit]
```

| CTQ | Operational definition | Target | Limit | Data source |
|---|---|---|---|---|
| | | | | |
