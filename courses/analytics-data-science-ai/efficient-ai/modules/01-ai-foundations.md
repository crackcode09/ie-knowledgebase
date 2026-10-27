# Module 01 — AI Foundations

Plain-language overview of core AI concepts, including machine learning and generative AI, and where they are most effective.

## Objectives

- Explain what AI is and isn't.
- Distinguish rules-based automation, machine learning, generative AI and related tools.
- Judge when AI makes sense to apply.

## What AI is, and isn't

**Artificial intelligence** here means software that performs tasks that normally need human judgment by **learning patterns from data**, rather than following rules a person wrote line by line.

| AI is… | AI is not… |
|---|---|
| Pattern recognition at scale (text, numbers, images) | A substitute for knowing what problem you're solving |
| Probabilistic: it gives likely answers, with some error rate | Always right, or right in the same way every time |
| Only as good as the data and the feedback it gets | A fix for a broken or undefined process |
| A tool inside a process with people | Something you "turn on" and walk away from |

## The toolbox

| Tool | What it does | Typical use | Is it AI? |
|---|---|---|---|
| **Process fix / standard work** | Removes the cause of the problem | Approval limits, standard templates, SMED | No, and often the best answer |
| **Rules-based automation** (scripts, workflow, robotic process automation) | Follows fixed if-then rules | Copy data between systems; standard quotes | No: deterministic |
| **Classic analytics** | Reports, statistics, control charts | Trends, root cause | No, but often enough |
| **Machine learning (ML)** | Learns from labelled examples to **predict** or **classify** | Will this shipment be late? Which team should take this ticket? | Yes |
| **Unsupervised ML** | Finds groups or anomalies without labels | Unusual expense claims; customer segments | Yes |
| **Computer vision** | ML on images | Surface-defect inspection | Yes |
| **Generative AI (GenAI)**: large language models | **Generates** text (and code, images) from instructions and context | Draft replies, summarize, answer questions over documents | Yes |
| **Retrieval-augmented generation (RAG)** | GenAI that first **retrieves** relevant documents, then answers from them | Search work instructions and specs by question | Yes |
| **Optimization** | Finds the best plan under constraints | Scheduling, routing | Mathematical; often grouped with AI |

## Where each is most effective

- **ML:** a repeated decision, many historical examples **with outcomes** (labels), patterns too complex for simple rules, and errors that are tolerable or caught.
- **GenAI:** language-heavy work (reading, drafting, summarizing, searching), where a human reviews the output or the content can be checked against sources.
- **Neither:** when the rule is simple and stable (use rules), when the process itself is broken (fix it), or when errors are unacceptable and can't be caught.

## Three properties to remember

1. **Probabilistic.** Every model has an error rate. Design for the errors: thresholds, human review, fallbacks.
2. **Data-dependent.** Models learn the past, including its biases and mistakes. When the process changes, the model can go stale ("drift").
3. **GenAI can be fluent and wrong.** Language models can produce confident text that is incorrect or not supported by any source. Tie answers to sources and test them (Module 05).

## Check yourself

1. Classify: (a) "if the order is over $10,000, route it to a manager"; (b) predicting next month's demand per SKU from history; (c) drafting a customer reply from the ticket text.
2. Why is "AI will fix our late approvals" a warning sign?

<details><summary>Answers</summary>

1. (a) Rules-based automation, not AI. (b) Machine learning (forecasting). (c) Generative AI, with human review.
2. Late approvals are usually a **process** problem (unclear limits, no escalation rule). AI would automate the waste rather than remove it. Fix the process first (Module 04).

</details>
