# Module 0 — Introduction to the Voice of the Customer

**Time:** 40 min

## Learning objectives

1. Explain what the voice of the customer (VOC) is and why it drives process and product design.
2. Identify who the customer is — including internal and indirect customers.
3. View an organization as a set of processes whose inputs determine its outputs.

## 1. What VOC is

The voice of the customer is the process of finding out what customers need — stated and unstated — and translating it into measurable requirements (CTQs), specifications and targets that the organization designs and runs its processes to meet.

Without VOC, teams optimize for what's easy to measure internally. With it, every process metric traces back to something a customer values.

## 2. Who is the customer?

> A customer is anyone who receives the output of your process.

| Type | Spare-parts ordering example |
|---|---|
| **External, paying** | Maintenance manager at a plant; distributor's purchasing; OEM buyer |
| **External, using** | Maintenance technician who installs the part |
| **External, influencing** | Plant reliability engineer who specifies brands |
| **Internal** | Warehouse (receives the order from customer service); finance (receives the shipment record) |
| **Regulatory / society** | Export control; packaging waste rules |

The person who pays, the person who uses and the person who decides are often different people with different needs. Map them before you ask anyone anything.

## 3. The organization as processes: Y = f(X)

Every output (Y) the customer experiences is the result of process inputs (Xs):

```
 Inputs (X)                         Process                  Outputs (Y)
 stock availability ─┐
 part-number data ───┤                                        delivered on time?
 order-entry method ─┼──► Quote → Order → Pick → Ship ──►     right part?
 carrier cut-off ────┤                                        status visible?
 picker training ────┘                                        easy to order?
```

You cannot manage the Ys directly — only the Xs. VOC defines which Ys matter and how much; the cause-and-effect matrix (Module 10) points to the Xs that drive them.

## 4. The running case

A bearing and linear-motion manufacturer sells spare parts to three segments: **end-user plants (MRO — maintenance, repair and operations)**, **distributors**, and **OEM machine builders**. Spare-parts sales are flat and the net promoter score is negative. The team runs a VOC study: interviews, a 300-response survey, and complaint data. All numbers come from `python tools/voc.py all`.

## 5. Course map

| # | Module |
|---|---|
| 1 | Obtaining VOC and listening to all the voices |
| 2 | Market segmentation and choosing target markets |
| 3 | Understanding customer requirements: two types; Kano; changing expectations |
| 4 | Where to go for customer requirements |
| 5 | Surveys: design and execution |
| 6 | Sampling uncertainty and margin of error |
| 7 | Affinity diagram |
| 8 | CTQ tree and operational definitions |
| 9 | VOC as specifications and targets |
| 10 | Cause-and-effect matrix |
| 11 | Skill check and capstone |

## Check yourself

For an internal IT help desk, name two customers with different needs.

<details><summary>Answers</summary>

E.g., the employee with the problem (wants it fixed fast) and their manager or the security team (want it fixed safely, with records) — and the help-desk staff of the next shift (internal customers of the ticket notes).
</details>
