# Terminal Financial Variance Calculator

A command-line tool written in Python to calculate, evaluate, and report cost variances across key accounting categories (*Material Cost*, *Labor Cost*, and *Overhead Cost*). 

The application evaluates whether cost performance is **FAVORABLE** or **UNFAVORABLE** based on standard managerial cost accounting principles and displays a formatted summary report.

---

## Features

- **Sequential Terminal Prompts:** Interactively collects `Actual Cost` and `Budgeted Cost` for each expense category.
- **Automated Variance Calculation:** Computes cost differences using $\text{Variance} = \text{Actual Cost} - \text{Budgeted Cost}$.
- **Performance Classification:**
  - **FAVORABLE:** Assigned when $\text{Actual Cost} \le \text{Budgeted Cost}$ ($\text{Variance} \le 0$).
  - **UNFAVORABLE:** Assigned when $\text{Actual Cost} > \text{Budgeted Cost}$ ($\text{Variance} > 0$).
- **Structured Data Storage:** Utilizes native Python lists and dictionaries for record handling.
- **Formatted Financial Output:** Prints a clean terminal report with currency formatting (commas and two decimal places).

---

## Requirements

- **Python:** 3.8 or higher
- **Dependencies:** None (uses standard library only)

---

## File Structure

```text
├── main.py            # Main application execution script
├── REQUIREMENTS.txt   # Project requirements specification
└── README.md          # Project documentation