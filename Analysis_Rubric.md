# Evaluation Metrics for Language Model Comparative Analysis

This document defines the metrics used to evaluate the performance of different language models in generating Python game scripts. The metrics focus on three key areas: Accuracy, Bug Frequency, and Feature Completeness.

## 1. Accuracy

### Definition
Accuracy measures how closely the generated scripts align with the provided prompts or specifications.

### Measurement Criteria
- **Exact Match:** Check if the generated script exactly matches the prompt in terms of functionality and output.
- **Partial Match:** Assess if key components of the prompt are addressed in the script, even if not all details are perfectly aligned.
- **Scoring:** Assign a score based on the percentage of prompt requirements met by the script. For instance, a script meeting all requirements scores 100%, while partial alignment scores proportionally lower.

## 2. Bug Frequency

### Definition
Bug Frequency evaluates the number and severity of defects in the generated scripts.

### Measurement Criteria
- **Count of Bugs:** Record the total number of bugs in the initial script output before any fixes.
- **Bug Severity:** Classify each bug by its impact:
  - **Critical:** Bugs that prevent the script from running or cause major errors during execution.
  - **Major:** Bugs that cause incorrect operations or results but do not prevent overall execution.
  - **Minor:** Bugs that do not significantly affect the script's functionality or performance.
- **Complexity of Fixes:** Assess the effort required to fix the bugs (e.g., simple, moderate, complex).

## 3. Feature Completeness

### Definition
Feature Completeness measures the extent to which the generated scripts incorporate the requested game features and mechanics.

### Measurement Criteria
- **Feature List:** Create a checklist of all features specified in the prompt.
- **Implemented Features:** Mark which of the listed features are correctly implemented in the script.
- **Scoring:** Calculate the percentage of features successfully implemented. For example, if 8 out of 10 features are implemented, the score would be 80%.

