# Standard Data Sheet — [Process / machine family]

| Field | Entry |
|---|---|
| Data family code | e.g. PB |
| Version / date | v1.0, YYYY-MM-DD |
| Owner | |
| Approved by | |
| Method description | Machine(s), tooling, layout, material handling, operator count. Attach photos or a sketch |
| Source studies | IDs, dates, analysts |
| Allowance | % PF&D, applied once at job level on normal time |
| Accuracy (validation) | Per-job mean abs. error, % within target, aggregate error, number of hold-out studies |

## Elements

| Code | Element (start → end) | Type (constant / variable) | Frequency | Normal min | Driving variable | Valid range |
|---|---|---|---|---|---|---|
| | | | | | | |

## Job standard

```
setup = ...
run   = ...
lot standard (h) = (setup + qty × run) × (1 + PF&D) / 60
```

## Use rules

- Inputs come from: (drawing / routing / ERP attribute)
- Outside the valid range: provisional standard + time study of the first lot
- Method differs from the description: time study, not standard data
- Review triggers: new equipment or tooling, method change, audit bias > __ %, ...

## Change log

| Version | Date | Change | Studies added | Approved by |
|---|---|---|---|---|
