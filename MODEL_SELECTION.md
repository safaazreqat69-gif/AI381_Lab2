\# Model Selection



\## The question



The model predicts whether a customer is likely to leave (churn). A false negative can cause the company to lose a customer, while a false positive can lead to unnecessary retention offers and costs.



\## Candidates



| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |

|---|---|---:|---:|---:|---:|---:|---|

| Logistic Regression | Simple, fast, and interpretable baseline | 0.7982 | 0.4948 | 0.2500 (one-year / two-year) | 2.6852 | 3.5479 | `e61ab8aff17a47ed9b3d8f46658b76fd` |

| Random Forest | Tests nonlinear patterns using multiple decision trees | 0.7589 | 0.4536 | 0.2222 (one-year) | 10.2498 | 3160.0957 | `65d1f6aa07a24fdb847179348bfd201a` |

| Gradient Boosting | Tests sequential boosting to improve predictive performance | 0.7476 | 0.4167 | 0.2222 (two-year) | 2.7025 | 141.6445 | `ab433316e3c047dab59cc911c01ee6e4` |



\## The champion



I selected \*\*Logistic Regression\*\* as the champion.



It achieved the highest overall AUC (0.7982) and F1 (0.4948). It also had the lowest p95 latency (2.6852 ms) and smallest model size (3.5479 KB).



I accepted that it did not achieve the best F1 for every contract slice. Gradient Boosting performed better on one-year contracts (0.4444), while Random Forest performed better on two-year contracts (0.3636). Logistic Regression achieved the best month-to-month F1 (0.5432).



I chose the best overall balance of predictive performance, speed, and model size.



\## My promotion rules



\*\*Latency budget (p95): 25 ms\*\*, because all three candidates were below this limit, leaving room for deployment and inference overhead.



\*\*Minimum gain to replace the champion (F1 points): 0.005\*\*, because a new model must improve overall F1 by at least 0.005 (absolute F1 improvement) to justify replacing the current champion.



\## What I would check next



I would investigate whether the one-year and two-year contract groups contain enough customers for reliable evaluation. Their low F1 scores could indicate that the model performs poorly on these customer groups. I would also monitor changes in customer behavior and data over time.
