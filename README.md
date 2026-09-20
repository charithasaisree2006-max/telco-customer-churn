# 📊 Telco Customer Churn Prediction

## 📌 Project Overview

This project uses **Machine Learning** to predict whether a telecom customer is likely to **churn (leave the company)** based on customer information such as tenure, contract type, monthly charges, payment method, and other service-related features.

The project includes a **Streamlit web application** that allows users to enter customer details and receive a churn prediction.

## 🚀 Live Demo

🔗 **Streamlit App:**
https://telco-customer-churn-bjboxtcwxagu5secvyvbxj.streamlit.app/

## 🎯 Objectives

* Predict whether a customer is likely to churn.
* Analyze customer characteristics related to churn.
* Apply Machine Learning for binary classification.
* Provide an easy-to-use web interface using Streamlit.
* Help telecom companies identify customers who may leave their services.

## 🧠 Machine Learning Workflow

```text
Customer Data
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Train-Test Split
      ↓
Machine Learning Model
      ↓
Model Evaluation
      ↓
Churn Prediction
      ↓
Streamlit Web Application
```

## 📂 Project Structure

```text
Telco-Customer-Churn/
│
├── churn prediction.ipynb
├── app.py
├── requirements.txt
├── README.md
└── dataset/
    └── WA_Fn-UseC_-Telco-Customer-Churn.csv
```

## 📊 Dataset

The project uses a **Telco Customer Churn dataset** containing customer information and whether the customer has churned.

Important features include:

* Customer tenure
* Gender
* Senior citizen status
* Partner
* Dependents
* Phone service
* Internet service
* Online security
* Online backup
* Device protection
* Tech support
* Streaming services
* Contract type
* Paperless billing
* Payment method
* Monthly charges
* Total charges

### Target Variable

```text
Churn
```

The target represents whether the customer left the telecom service.

* `Yes` → Customer churned
* `No` → Customer stayed

## 🔧 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Streamlit**
* **Jupyter Notebook**

## 🤖 Machine Learning

The notebook contains the complete machine learning workflow, including:

1. Loading the dataset
2. Understanding the data
3. Handling missing values
4. Data preprocessing
5. Encoding categorical variables
6. Exploratory Data Analysis
7. Feature selection
8. Splitting the dataset
9. Model training
10. Model evaluation
11. Making predictions

## 📈 Model Evaluation

The classification model can be evaluated using metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help measure how effectively the model identifies customers who are likely to churn.

## 🌐 Streamlit Application

The Streamlit application provides an interactive interface where users can enter customer information and obtain a churn prediction.

### Application Flow

```text
Enter Customer Details
        ↓
Input Preprocessing
        ↓
Trained ML Model
        ↓
Prediction
        ↓
Churn / No Churn
```

## 💻 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Navigate to the project folder

```bash
cd Telco-Customer-Churn
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📦 Requirements

Example `requirements.txt`:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
```

## 🔮 Future Enhancements

* Improve model accuracy through hyperparameter tuning.
* Compare multiple classification algorithms.
* Add probability-based churn prediction.
* Add interactive data visualizations.
* Add customer segmentation.
* Deploy the model using cloud platforms.
* Add explainable AI techniques to understand individual predictions.

## ✅ Conclusion

The **Telco Customer Churn Prediction** project demonstrates how Machine Learning can be used to identify customers who may leave a telecom service.

The Streamlit application makes the trained model accessible through an interactive web interface, allowing users to enter customer information and obtain a churn prediction.

## 👨‍💻 Project

**Project:** Telco Customer Churn Prediction
**Technology:** Machine Learning + Streamlit
**Application:** Customer Churn Prediction
**Deployment:** Streamlit Cloud

---

⭐ If you found this project useful, consider giving the repository a star!
