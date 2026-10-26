# Module 1 — SIPOC

**Time:** 30 min

## Learning objectives

1. Build a SIPOC to set the boundaries of a process.

## 1. How to build it

Work in this order — it's easiest:

1. **P**rocess: name it; write the start trigger and end point; list 5–7 high-level steps.
2. **O**utputs: what the process produces.
3. **C**ustomers: who receives each output (internal and external).
4. **I**nputs: what the process needs.
5. **S**uppliers: who provides each input.
6. Optional: add customer requirements next to outputs (links to Modules 6–10).

## 2. RMA process SIPOC

**Start:** customer requests a return. **End:** customer receives the repaired or replacement part and close-out.

| Suppliers | Inputs | Process | Outputs | Customers |
|---|---|---|---|---|
| Customer | Return request, failed part, failure description | 1. Request & authorize return | RMA number | Customer |
| Carrier | Shipping | 2. Receive part | Received-part record | Quality |
| Customer service | RMA form, customer data | 3. Diagnose failure | Failure report | Customer, Engineering, Supplier quality |
| Engineering | Repair/replace decision | 4. Approve disposition | Disposition | Repair, Customer service |
| Parts crib | Spare components | 5. Repair and re-test | Repaired part, test record | Customer |
| ERP / CRM | Order and warranty data | 6. Ship back and close | Shipment, credit or invoice, close-out | Customer, Finance |

**What the SIPOC already reveals:** six functions touch every RMA, and the customer is a supplier of inputs (a complete failure description) as well as the customer — a clue that incomplete requests could drive delay.

## Check yourself

Why limit the process column to 5–7 steps?

<details><summary>Answer</summary>

The SIPOC's job is scope and boundaries; detail belongs in the flow chart. Too many steps turns it into a flow chart without the logic.
</details>
