📊 Telco Customer Churn Prediction Using Machine Learning

🔗 Live Demo

🚀 Deployed Streamlit Application:
https://telco-customer-churn-bjboxtcwxagu5secvyvbxj.streamlit.app/

📌 Project Overview

Customer churn is an important problem for telecommunications companies. Customers may stop using a service because of pricing, contract type, service quality, payment methods, or other factors.

This project develops a Machine Learning-based Telco Customer Churn Prediction System that predicts whether a customer is likely to churn based on their personal, service, contract, and billing information.

The trained machine learning model is integrated with a Streamlit web application, allowing users to enter customer details and receive an immediate churn prediction.

The application is deployed online using Streamlit Community Cloud and can be accessed through a web browser.

🎯 Objectives

The main objectives of this project are:

To understand customer churn using machine learning.
To preprocess and prepare customer data for machine learning.
To identify relevant features for churn prediction.
To convert categorical data into numerical representations.
To scale numerical features.
To train a Decision Tree classification model.
To predict whether a customer is likely to churn.
To provide churn probability along with the prediction.
To develop an interactive web application using Streamlit.
To deploy the application online.
To make the prediction system accessible through a web browser.
📂 Dataset

The project uses a Telco Customer Churn dataset containing information about telecommunications customers.

The dataset includes customer information related to:

Customer demographics
Gender
Senior citizen status
Partner
Dependents
Tenure
Phone service
Multiple lines
Internet service
Online security
Online backup
Device protection
Technical support
Streaming TV
Streaming movies
Contract type
Paperless billing
Payment method
Monthly charges
Total charges
Churn status
Target Variable

The target variable is:

Churn

It contains two classes:

Yes → Customer churned
No  → Customer did not churn
🔄 Project Workflow

The overall workflow of the project is:

                Telco Dataset
                     │
                     ▼
              Data Collection
                     │
                     ▼
               Data Cleaning
                     │
                     ▼
           Missing Value Handling
                     │
                     ▼
             Feature Selection
                     │
                     ▼
        Categorical Data Encoding
                     │
                     ▼
          Numerical Feature Scaling
                     │
                     ▼
             Data Preparation
                     │
                     ▼
            Model Development
                     │
                     ▼
        Decision Tree Classifier
                     │
                     ▼
             Model Evaluation
                     │
                     ▼
             Model Selection
                     │
                     ▼
            Streamlit Web App
                     │
                     ▼
          Streamlit Cloud Deployment
                     │
                     ▼
             Online Prediction
🧹 Data Preprocessing

Before training the machine learning model, the dataset is processed to make it suitable for model training.

1. Handling Missing Values

The TotalCharges column is converted into a numerical format.

Missing or invalid values are handled appropriately.

2. Removing Unnecessary Columns

The customerID column is not useful for prediction and is removed from the feature set.

3. Target Encoding

The Churn column is converted into numerical values:

Yes → 1
No  → 0
4. Numerical Features

Numerical features are standardized using:

StandardScaler
5. Categorical Features

Categorical features are converted into numerical representations using:

OneHotEncoder

This allows categorical customer information to be processed by the machine learning model.

🤖 Machine Learning Model

The project uses a:

Decision Tree Classifier

A Decision Tree is a supervised machine learning algorithm used for classification and regression problems.

For this project, the Decision Tree is used to classify customers into:

Churn
   or
No Churn
Model Configuration

The deployed application uses the tuned Decision Tree configuration:

DecisionTreeClassifier(
    max_depth=3,
    min_samples_leaf=1,
    class_weight="balanced",
    random_state=42
)
Parameters
Parameter	Value
max_depth	3
min_samples_leaf	1
class_weight	balanced
random_state	42
📊 Prediction Process

When a user enters customer information, the application performs the following steps:

Customer Information
        ↓
Data Preprocessing
        ↓
Numerical Feature Scaling
        ↓
Categorical Feature Encoding
        ↓
Decision Tree Model
        ↓
Prediction
        ↓
Churn / No Churn

The application also displays the estimated:

Churn Probability
🌐 Streamlit Web Application

The machine learning model is integrated into an interactive Streamlit application.

The user can enter information such as:

Customer Information
Gender
Senior Citizen
Partner
Dependents
Tenure
Service Information
Phone Service
Multiple Lines
Internet Service
Online Security
Online Backup
Device Protection
Tech Support
Streaming TV
Streaming Movies
Billing Information
Contract
Paperless Billing
Payment Method
Monthly Charges
Total Charges

After entering the information, the user clicks:

🔍 Predict Churn

The application then displays the prediction.

Example:

✅ Customer is predicted to NOT CHURN

or:

⚠️ Customer is predicted to CHURN

The application also displays the estimated churn probability.

🖥️ Application Interface

The deployed application provides a simple interface:

        TELCO CUSTOMER CHURN PREDICTION

Customer Details

Gender:              [ Female ▼ ]
Senior Citizen:      [ 0 ▼ ]
Partner:             [ Yes ▼ ]
Dependents:          [ No ▼ ]
Tenure:              [ 12 ]

Internet Service:    [ DSL ▼ ]
Contract:            [ Month-to-month ▼ ]
Payment Method:      [ Electronic check ▼ ]

Monthly Charges:     [ 70 ]
Total Charges:       [ 840 ]

             [ 🔍 Predict Churn ]

                Prediction Result

        Customer is predicted to CHURN

             Churn Probability
                  65.20%
🛠️ Technologies Used
Technology	Purpose
Python	Programming language
Pandas	Data manipulation and analysis
NumPy	Numerical operations
Scikit-learn	Machine learning
Streamlit	Web application development
Jupyter Notebook	Model development and experimentation
GitHub	Source code management
Streamlit Community Cloud	Application deployment
📁 Project Structure
telco-customer-churn/
│
├── app.py
│
├── churn.csv
│
├── churun prediction.ipynb
│
├── requirements.txt
│
└── README.md
File Description
app.py

Contains the Streamlit application and the deployed customer churn prediction functionality.

churn.csv

Contains the Telco customer dataset used for model training.

churun prediction.ipynb

Contains the original machine learning experimentation, data preprocessing, model training, evaluation, and prediction work.

requirements.txt

Contains the Python libraries required to run the application.

README.md

Contains complete project documentation.

📦 Required Python Libraries

The project requires the following libraries:

streamlit
pandas
numpy
scikit-learn

These dependencies are listed in:

requirements.txt
💻 How to Run the Project Locally
Step 1: Clone the Repository
git clone https://github.com/charithasaisree2006-max/telco-customer-churn.git
Step 2: Open the Project Directory
cd telco-customer-churn
Step 3: Install Required Libraries
pip install -r requirements.txt
Step 4: Run the Streamlit Application
streamlit run app.py
Step 5: Open the Application

After running the command, Streamlit will provide a local URL, normally:

http://localhost:8501

Open this URL in a web browser.

☁️ Deployment

The application is deployed using:

Streamlit Community Cloud

The deployment process is:

GitHub Repository
       ↓
Connect Repository
       ↓
Select main Branch
       ↓
Select app.py
       ↓
Install requirements.txt
       ↓
Build Application
       ↓
Deploy
       ↓
Public Web Application
🚀 Live Application

The deployed application can be accessed here:

Telco Customer Churn Prediction

https://telco-customer-churn-bjboxtcwxagu5secvyvbxj.streamlit.app/

🔗 GitHub Repository

Source code, dataset, notebook, and deployment files are available in the GitHub repository:

https://github.com/charithasaisree2006-max/telco-customer-churn

📈 Advantages of the System
Provides automated churn prediction.
Easy-to-use web interface.
No programming knowledge is required to use the deployed application.
Provides quick predictions.
Uses customer service and billing information.
Can be accessed through a web browser.
Demonstrates an end-to-end machine learning workflow.
Combines machine learning with web application deployment.
⚠️ Limitations
Prediction quality depends on the dataset and model.
The model is trained using historical customer data.
Customer behaviour can change over time.
The application should not be treated as a guaranteed prediction of future customer behaviour.
Additional real-world customer data could potentially improve the system.
🔮 Future Scope

The project can be enhanced in the future by:

Comparing additional machine learning algorithms.
Performing more extensive hyperparameter optimization.
Adding feature importance visualization.
Adding confusion matrix visualization.
Adding ROC-AUC analysis.
Adding model explainability using SHAP.
Adding prediction history.
Adding customer risk categories.
Improving the user interface.
Adding authentication.
Connecting the application to a live database.
Retraining the model periodically with new customer data.
Developing a mobile-friendly interface.
🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

Data preprocessing
Missing value handling
Feature engineering
Categorical encoding
Feature scaling
Supervised learning
Classification
Decision Tree algorithm
Model training
Model prediction
Machine learning deployment
Streamlit application development
GitHub repository management
Cloud deployment
🔬 End-to-End Machine Learning Pipeline

The complete system can be summarized as:

             CUSTOMER DATA
                   │
                   ▼
          DATA PREPROCESSING
                   │
                   ▼
       FEATURE TRANSFORMATION
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
   Numerical Features   Categorical Features
          │                 │
          ▼                 ▼
    StandardScaler     OneHotEncoder
          │                 │
          └────────┬────────┘
                   ▼
            FEATURE MATRIX
                   │
                   ▼
        DECISION TREE MODEL
                   │
                   ▼
             PREDICTION
              /       \
             /         \
            ▼           ▼
       NO CHURN       CHURN
📌 Conclusion

The Telco Customer Churn Prediction Using Machine Learning project demonstrates an end-to-end machine learning application for predicting customer churn.

The project includes data preprocessing, feature transformation, machine learning model development, prediction, and deployment. A Decision Tree Classifier is used to predict customer churn based on customer and service-related information.

The model has been integrated into a Streamlit web application and deployed online, making the system accessible through a web browser.

The project demonstrates how a machine learning model can be transformed from a Jupyter Notebook experiment into a usable web-based application.

👨‍💻 Project Information

Project Title:
Telco Customer Churn Prediction Using Machine Learning

Domain:
Machine Learning / Data Science

Application:
Customer Churn Prediction

Framework:
Streamlit

Deployment:
Streamlit Community Cloud

⭐ Try the Live Application

🚀 Open Telco Customer Churn Prediction

📜 License

This project is created for educational and academic purposes.
