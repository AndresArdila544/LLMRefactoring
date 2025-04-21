# LLMRefactoring: Evaluating Large Language Models for Automated Code Refactoring

This repository contains the code, data, and evaluation pipeline for our study on the effectiveness of Large Language Models (LLMs) in automated code refactoring tasks. We benchmark and compare the performance of CodeLlama-7B, StarCoder2-7B, and WizardCoder-7B using a dataset of 420 Python programs sourced from Aizu Online Judge.

---

## Abstract

*Code refactoring is a critical yet time-consuming software engineering task aimed at improving readability, maintainability, and performance without altering a program’s functionality. Recent advancements in Large Language Models (LLMs) offer new opportunities for automating refactoring, but their effectiveness across different prompting strategies and quality metrics remains underexplored. In this study, we conduct a comprehensive evaluation of three state-of-the-art, code-focused LLMs—CodeLlama-7B, StarCoder2-7B, and WizardCoder-7B—on a curated dataset of 420 functionally correct Python programs. Each model is tested under zero-shot, one-shot, and few-shot prompting configurations. To measure refactoring success, we employ a custom offline judge for functional correctness (Pass@k) and compute structural quality metrics including Lines of Code (LOC), Cyclomatic Complexity (CC), Halstead Complexity, Maintainability Index (MI), and Levenshtein Distance. Our findings show that CodeLlama, especially under few-shot prompting, achieves the highest correctness (Pass@5 = 0.70), while also producing more concise and maintainable code. Prompt engineering significantly impacts model performance, with few-shot prompting leading to better structural outcomes and reduced complexity. In contrast, StarCoder2 consistently underperforms across all metrics and prompt types. Complementing our automated analysis, a developer survey reveals that human preferences align with models that improve both readability and maintainability. We conclude that while LLMs show strong potential for automated refactoring, especially with well-designed prompts, they still require post-validation and oversight before integration into production workflows.*

---

## Authors

- **Andres Ricardo Ardila Agudelo** — Concordia University — [a_ardil@live.concordia.ca](mailto:a_ardil@live.concordia.ca)  
- **Diego Palacios Escalera** — Concordia University — [di_pala@live.concordia.ca](mailto:di_pala@live.concordia.ca)  
- **Ahkil Dhim** — Concordia University — [ak_dhim@live.concordia.ca](mailto:ak_dhim@live.concordia.ca)

---

## Project Structure

```bash
.
├── input/                      # Original dataset (AOJ solutions)
│   └── filtered_problems/     # Cleaned, sampled submissions per problem
├── output/                    # LLM refactored code results by model and prompt type
├── correct_refactorings/     # Accepted outputs (Pass@k)
├── metrics/                   # Code quality metrics (LOC, CC, MI, etc.)
├── virtual_judge/            # Offline evaluation system (test case runner)
├── Human_survey/             # Developer evaluation screenshots and CSV logs
└── results/                  # Aggregated Pass@k scores and error reports
```


---

## Key Metrics

- **Pass@k** — Correctness across top-*k* outputs  
- **LOC** — Lines of Code (conciseness)  
- **Cyclomatic Complexity** — Number of control flow paths  
- **Halstead Metrics** — Cognitive complexity based on tokens  
- **Maintainability Index** — Composite readability and maintainability score  
- **Levenshtein Distance** — Edit distance from original code  

---

## Citation

If you use this work in your research, please cite this repository and/or contact the authors directly:
