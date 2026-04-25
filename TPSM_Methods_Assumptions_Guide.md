# TPSM Viva Quick Guide: Methods, Assumptions, and Why Not Multiple Linear Regression

## 1) Why each method was used

### Data Understanding (`head`, `info`, `describe`, `isnull`)
- Used to verify structure, datatypes, missing values, and general quality before analysis.
- Purpose: prevent invalid statistical/model outputs caused by bad input data.

### Data Cleaning (`to_numeric`, `dropna`)
- Used to ensure all model/test inputs are numeric and non-missing.
- `to_numeric(errors="coerce")` converts invalid values to `NaN`, then `dropna()` removes those rows.

### Descriptive Analysis (means, bar plot, countplot, group means)
- Used to summarize trends and class distribution.
- Helps explain data behavior before inferential and predictive analysis.

### Spearman Correlation
- Used because variables are ordinal rating-type values.
- Detects monotonic associations without strict normality or linearity assumptions.

### Kruskal-Wallis Test
- Used to compare factors across 3 satisfaction groups (Low/Medium/High).
- Appropriate non-parametric alternative to one-way ANOVA for ordinal/non-normal data.

### Train-Test Split with `stratify=y`
- Used to evaluate generalization on unseen data.
- Stratification keeps class proportions stable, important when class counts are imbalanced.

### Logistic Regression (multiclass)
- Used as a baseline interpretable classifier.
- Gives a simple benchmark for predictive performance.

### Random Forest Classifier
- Used to capture nonlinear relationships and feature interactions.
- Also provides feature importance for practical interpretation.

### Evaluation Metrics (accuracy, precision, recall, F1, confusion matrix)
- Used because accuracy alone can be misleading under class imbalance.
- Class-sensitive metrics and confusion matrix show where prediction errors occur.

---

## 2) Assumptions for each key method

### Spearman Correlation
1. Variables are at least ordinal.
2. Relationship is monotonic.
3. Observations are independent.

### Kruskal-Wallis
1. Outcome is at least ordinal/continuous-like.
2. Groups are independent.
3. Observations are independent.
4. Similar distribution shape across groups is preferred for median-focused interpretation.

### Logistic Regression (multiclass)
1. Categorical target variable.
2. Independent observations.
3. Approximate linear relationship between predictors and log-odds.
4. No severe multicollinearity.
5. Reasonable sample size per class.

### Random Forest
1. Independent observations.
2. Train and test data represent same process.
3. Sufficient data variety for robust tree splits.

---

## 3) Why we cannot use Multiple Linear Regression

### Main reason
`satisfaction in RM` is categorical/ordinal (1, 2, 3 classes), not a truly continuous dependent variable.
Multiple Linear Regression requires a continuous response.

### Assumption mismatch
Multiple Linear Regression expects:
- continuous dependent variable,
- linear relationship,
- normally distributed residuals,
- homoscedasticity (constant residual variance).

These do not hold properly for class labels (1/2/3 satisfaction levels).

### Practical issue
Linear regression can output values like 2.47 or 3.81, which are not meaningful class labels by themselves.
Classification methods are designed to output class decisions/probabilities.

### Best viva answer (short)
"We did not use Multiple Linear Regression because our target is categorical/ordinal, not continuous. This violates linear regression assumptions. Therefore, classification models such as Logistic Regression and Random Forest are more appropriate."

---

## 4) One-minute viva summary

"In this project, we used methods based on data type and objective. For ordinal satisfaction ratings, we selected non-parametric inferential methods: Spearman correlation and Kruskal-Wallis. For prediction, we used Logistic Regression as an interpretable baseline and Random Forest to capture nonlinear effects and feature interactions. We evaluated with accuracy plus precision, recall, F1, and confusion matrix to handle class imbalance properly. We did not use Multiple Linear Regression because the dependent variable is not continuous; it is a categorical/ordinal class variable, so linear regression assumptions are not satisfied."

