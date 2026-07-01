# Project 2: Data Classification Using AI
**DecodeLabs AI Internship — Batch 2026**

## Overview
This project implements a supervised learning pipeline to classify iris flowers into
three species (Setosa, Versicolor, Virginica) based on four physical measurements.
It demonstrates the full machine learning workflow: data loading, preprocessing,
model training, and evaluation using the K-Nearest Neighbors (KNN) algorithm.

## Dataset
- **Source:** Iris dataset (built into scikit-learn)
- **Samples:** 150 (50 per class, balanced)
- **Features:** 4 — sepal length, sepal width, petal length, petal width (all in cm)
- **Classes:** 3 — Setosa, Versicolor, Virginica

## Approach
1. **Data Loading & Exploration** — loaded via `sklearn.datasets.load_iris()`,
   inspected shape, feature names, and class distribution.
2. **Preprocessing** — applied `StandardScaler` to normalize features (mean=0,
   variance=1), since KNN is distance-based and sensitive to feature scale.
3. **Train-Test Split** — 80/20 split with shuffling (`random_state=7`) to
   ensure a fair, unbiased evaluation.
4. **Model Selection** — tested K values from 1 to 20, tracked error rate for
   each, and selected the K with the lowest test error.
5. **Training & Prediction** — trained `KNeighborsClassifier` on the scaled
   training set, predicted on the held-out test set.
6. **Evaluation** — assessed performance using accuracy, F1 score (macro-averaged),
   confusion matrix, and a full classification report.

## Results
- **Best K:** 7
- **Accuracy:** ~93%
- **F1 Score (macro):** ~0.93
- Misclassifications occurred only between Versicolor and Virginica, which is
  expected since these two classes have some feature overlap; Setosa was
  classified with 100% accuracy across all K values, as it is linearly
  separable from the other two species.

## Key Concepts Applied
- Supervised learning (classification)
- Feature scaling and its effect on distance-based algorithms
- Train-test split and generalization
- K-Nearest Neighbors algorithm and hyperparameter tuning (choosing K)
- Confusion matrix, precision, recall, and F1 score as evaluation metrics
- Why accuracy alone can be misleading on imbalanced data (not an issue here,
  since Iris is balanced, but considered as best practice)

## Libraries Used
- `scikit-learn` — dataset, preprocessing, model, metrics
- `pandas` — data exploration
- `matplotlib` — visualizing error rate vs. K

## How to Run
```bash
pip install scikit-learn pandas matplotlib
jupyter notebook project2_iris_classification.ipynb
```
Run all cells top to bottom. Console output prints dataset overview, K-tuning
results, and final evaluation metrics. A plot window displays the error-rate-vs-K
curve.

## Author
Raja Moiz Khalid — AI Intern, DecodeLabs
