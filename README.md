# Customer Churn Prediction

## 📌 Project Overview

This project develops a **Machine Learning model to predict customer churn** using the Telco Customer Churn dataset.

Customer churn occurs when customers stop using a company's services. Predicting customers who are likely to churn can help businesses take early retention actions such as providing offers, improving services, or contacting high-risk customers.

The project implements a complete machine learning workflow, including:

* Data loading and inspection
* Data cleaning and preprocessing
* Exploratory analysis
* Train-test splitting
* Feature scaling
* One-hot encoding
* Machine learning model development
* Model evaluation
* ROC-AUC analysis
* Hyperparameter tuning
* Cross-validation
* Feature importance and model interpretability
* Error analysis
* Final model selection
* Model artifact export
* Inference on new customers

---

## 🎯 Objective

The main objective is to build a classification model that can identify customers who are likely to **churn**.

The project prioritizes **Recall** because failing to identify a customer who is likely to churn can result in losing that customer.

---

## 📊 Dataset

The project uses the **Telco Customer Churn** dataset.

The target variable is:

* `Churn = Yes` → Customer churned
* `Churn = No` → Customer did not churn

The dataset contains customer information related to:

* Demographics
* Tenure
* Contract type
* Internet service
* Payment method
* Monthly charges
* Total charges
* Additional services

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine learning and evaluation
* **Matplotlib** – Data visualization
* **Joblib** – Saving and loading ML models
* **Jupyter Notebook** – Development environment

---

## 🤖 Machine Learning Models

Three classification algorithms were implemented:

### 1. Logistic Regression

Used as a linear classification model and baseline for comparison.

### 2. Decision Tree

A tree-based model capable of learning non-linear relationships between customer characteristics and churn.

### 3. Random Forest

An ensemble of decision trees designed to improve predictive performance and robustness.

All baseline models use:

```python
class_weight='balanced'
```

to account for the difference between churn and non-churn classes.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading & Inspection
   ↓
Data Cleaning
   ↓
Exploratory Analysis
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
One-Hot Encoding
   ↓
Baseline Models
   ↓
Model Evaluation
   ↓
ROC-AUC Analysis
   ↓
Hyperparameter Tuning
   ↓
Cross-Validation
   ↓
Feature Importance
   ↓
Final Model Selection
   ↓
Model Export
   ↓
New Customer Prediction
```

---

## 🧹 Data Preprocessing

The preprocessing pipeline includes:

1. Handling missing/blank values
2. Removing redundant columns
3. Converting the target variable into a machine-learning-friendly format
4. Splitting the dataset into training and testing sets
5. Scaling numerical features using `StandardScaler`
6. Encoding categorical features using `OneHotEncoder`
7. Combining numerical and categorical features

The train-test split is performed **before fitting preprocessing components** to help prevent data leakage.

---

## 📈 Model Evaluation

The models are evaluated using:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **ROC-AUC**
* **Confusion Matrix**

### Why Recall?

Recall is the primary model-selection metric because the main business objective is to identify as many potential churn customers as possible.

A false negative means that a customer who actually churns was incorrectly classified as a non-churn customer.

---

## 📊 Baseline Model Results

| Model               |   Accuracy |  Precision |     Recall |   F1-Score |
| ------------------- | ---------: | ---------: | ---------: | ---------: |
| Logistic Regression |          — |     0.5052 |     0.7834 |     0.6143 |
| Decision Tree       |     0.7346 |     0.5000 | **0.8075** |     0.6176 |
| Random Forest       | **0.7580** | **0.5299** |     0.7807 | **0.6314** |

The baseline Decision Tree achieved the highest Recall among the baseline models.

The Random Forest achieved the highest baseline Accuracy and F1-Score.

> Note: The final model is selected after hyperparameter tuning using Recall as the optimization metric.

---

## 🔧 Hyperparameter Tuning

`GridSearchCV` with **5-fold stratified cross-validation** is used to tune the three model families.

The optimization metric is:

```text
Recall
```

The tuned models include:

* Logistic Regression
* Decision Tree
* Random Forest

The final model is selected based on the highest Recall on the held-out test set.

---

## 🔁 Cross-Validation

A 5-fold stratified cross-validation check is performed on the selected model.

The following metrics are evaluated:

* Recall
* F1-Score

The mean and standard deviation across folds are calculated to check whether the model's performance is reasonably stable.

---

## 📉 ROC-AUC Analysis

ROC curves are generated for all trained models.

The ROC curve compares:

* **False Positive Rate (FPR)**
* **True Positive Rate (TPR)**

ROC-AUC measures the ability of a model to distinguish between churn and non-churn customers across different classification thresholds.

An AUC closer to **1** indicates stronger discrimination, while an AUC around **0.5** indicates performance close to random classification.

---

## 🔍 Feature Importance & Interpretability

Feature importance is analyzed for the selected model to understand which customer characteristics contribute most strongly to churn predictions.

Important churn-related patterns examined in the project include:

* Contract type
* Customer tenure
* Internet service type
* Payment method
* Monthly charges
* Customer service-related features

These insights can help convert machine-learning predictions into practical business actions.

---

## ❌ Error Analysis

The project identifies:

### False Negatives

Customers who actually churned but were predicted as non-churn.

These are particularly important because they represent potential customers that the business failed to identify as being at risk.

### False Positives

Customers predicted as churners who did not actually churn.

These predictions may result in unnecessary retention efforts.

The error records are exported for further analysis.

---

## 💾 Saved Model Artifacts

The project saves important machine-learning artifacts, including:

```text
models/
├── scaler.pkl
├── ohe.pkl
├── feature_names.json
└── <final_model>_final.pkl
```

Processed datasets are saved under:

```text
data/
└── processed/
    ├── X_train_final.npy
    ├── X_test_final.npy
    ├── y_train.npy
    ├── y_test.npy
    └── dataset_metadata.json
```

The final model metrics are saved in:

```text
outputs/
└── final_model_summary.json
```

False-positive and false-negative predictions are also exported for error analysis.

---

## 🧪 Inference Demo

The notebook reloads the saved:

* Scaler
* One-hot encoder
* Final trained model

and uses them to make predictions on new, previously unseen customer records.

The inference section produces:

* Churn probability
* Predicted churn status
* Selected customer characteristics

Example output concept:

```text
Customer → Churn Probability → Predicted Churn
```

This demonstrates that the saved artifacts can be reused for future predictions.

---

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── X_train_final.npy
│       ├── X_test_final.npy
│       ├── y_train.npy
│       ├── y_test.npy
│       └── dataset_metadata.json
│
├── models/
│   ├── scaler.pkl
│   ├── ohe.pkl
│   ├── feature_names.json
│   └── <final_model>_final.pkl
│
├── outputs/
│   ├── false_negatives.csv
│   ├── false_positives.csv
│   └── final_model_summary.json
│
├── notebooks/
│   └── churn_prediction_project.ipynb
│
├── README.md
└── requirements.txt
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd customer-churn-prediction
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Open the notebook:

```bash
jupyter notebook
```

Then open:

```text
churn_prediction_project.ipynb
```

Run the notebook cells from beginning to end.

---

## 💡 Business Recommendations

Based on the churn patterns identified in the project, businesses can:

* Target high-risk month-to-month customers with retention offers.
* Pay special attention to customers with short tenure.
* Investigate service or pricing issues among high-risk internet-service customers.
* Encourage customers to use automatic payment methods where appropriate.
* Use churn probability to prioritize retention efforts instead of relying only on Yes/No predictions.

---

## ⚠️ Limitations

* The dataset has a moderate class imbalance.
* Only three classical machine-learning model families are evaluated.
* Business costs of false positives and false negatives are not explicitly modeled.
* The current pipeline saves artifacts locally rather than exposing them through a production API.
* Model performance may change when applied to new real-world customer data.

---

## 🚀 Future Improvements

Possible improvements include:

* SMOTE or other class-imbalance techniques
* Classification threshold tuning
* Additional feature engineering
* More advanced boosting algorithms
* Larger datasets
* Automated model monitoring
* Deployment through an API
* Web-based prediction interface
* Data and concept drift monitoring
* Cost-sensitive model selection

---

## ✅ Conclusion

This project demonstrates a complete **end-to-end customer churn prediction workflow** using machine learning.

The workflow covers data preprocessing, feature engineering, model training, evaluation, ROC-AUC analysis, hyperparameter tuning, cross-validation, feature interpretation, error analysis, model export, and prediction on new customers.

Recall is used as the primary model-selection metric because identifying potential churners is the main business objective.

The resulting model can be used as a **decision-support tool** to help businesses identify customers who may be at higher risk of churn and prioritize appropriate retention strategies.

---

## 👤 Author

**Your Name**

B.Tech – Chemical Engineering

---

## 📄 License

This project is intended for educational and demonstration purposes.
