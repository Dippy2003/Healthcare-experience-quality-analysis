# Healthcare Experience Quality Analysis

Statistical analysis project that examines how comfort-related healthcare factors are associated with overall patient satisfaction.

## Project Overview

This project analyzes patient survey data to evaluate relationships between comfort and service factors (for example, waiting time, doctor quality, diagnosis accuracy, and hospital facilities) and overall healthcare experience quality.

The work includes:

- Data loading and cleaning
- Descriptive statistics and visualization
- Correlation analysis (Spearman)
- Inferential testing (Kruskal-Wallis)
- Predictive modeling (Logistic Regression and Random Forest)

## Main Files

- `Healthcare_Experience_Quality_Analysis.ipynb` - complete analysis notebook
- `datasetsatisfaction.csv` - input dataset used by the notebook

## Research Hypothesis

- `H0`: Comfort-related factors have no significant relationship with overall satisfaction.
- `H1`: Comfort-related factors have a significant relationship with overall satisfaction.

## Key Inferential Result

Based on the current notebook outputs (alpha = 0.05):

- Spearman significant factors: `3/16`
- Kruskal-Wallis significant factors: `3/16`
- Decision: reject global `H0`

Significant factors in both tests:

- Quality/experience of doctor
- Exact diagnosis
- Modern equipment

## Tools and Libraries

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- scikit-learn

## How to Run

1. Open `Healthcare_Experience_Quality_Analysis.ipynb` in Jupyter or Cursor.
2. Ensure required Python packages are installed.
3. Set the notebook kernel to your working Python environment.
4. Run all cells from top to bottom.

## Notes

- The derived variable `satisfaction_group` is excluded from inferential testing to avoid leakage.
- Always use the wording **"fail to reject H0"** (not "prove H0") when `p >= 0.05`.

## Author

TPSM coursework project (SLIIT).
