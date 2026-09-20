import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

@st.cache_resource
def train_model():
    # Load dataset
    df = pd.read_csv("churn.csv")

    # Same cleaning used in the notebook
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    ).fillna(0)

    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    df["Churn"] = df["Churn"].apply(
        lambda x: 1 if str(x).strip().lower() == "yes" else 0
    )

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Same automatic separation of numeric/categorical columns
    cat_cols = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    num_cols = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    # Same preprocessing approach as the notebook
    scaler = StandardScaler()
    X_num = scaler.fit_transform(X[num_cols])

    ohe = OneHotEncoder(
        drop="first",
        sparse_output=False,
        handle_unknown="ignore"
    )
    X_cat = ohe.fit_transform(X[cat_cols])

    X_final = np.hstack((X_num, X_cat))

    # The notebook's final exported model was a tuned Decision Tree.
    # Its reported best parameters were max_depth=3, min_samples_leaf=1.
    model = DecisionTreeClassifier(
        max_depth=3,
        min_samples_leaf=1,
        class_weight="balanced",
        random_state=42
    )

    # Train on the complete available dataset for the deployed app.
    model.fit(X_final, y)

    return model, scaler, ohe, num_cols, cat_cols


model, scaler, ohe, num_cols, cat_cols = train_model()

st.title("📊 Telco Customer Churn Prediction")
st.write(
    "Enter customer information below to predict whether the customer "
    "is likely to churn."
)

st.info(
    "This deployed app uses the same dataset, preprocessing approach, "
    "and tuned Decision Tree configuration used in the project notebook."
)

st.header("Customer Details")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input(
        "Tenure (months)", min_value=0, max_value=100, value=12, step=1
    )
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

with col2:
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )
    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )
    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )
    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

with col3:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )
    paperless_billing = st.selectbox(
        "Paperless Billing", ["Yes", "No"]
    )
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0,
        step=1.0
    )
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0,
        step=10.0
    )

st.divider()

if st.button("🔍 Predict Churn", type="primary", use_container_width=True):

    new_customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    # Apply exactly the same preprocessing objects used for training
    new_num = scaler.transform(new_customer[num_cols])
    new_cat = ohe.transform(new_customer[cat_cols])
    new_final = np.hstack((new_num, new_cat))

    prediction = model.predict(new_final)[0]
    probability = model.predict_proba(new_final)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is predicted to CHURN")
    else:
        st.success("✅ Customer is predicted to NOT CHURN")

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )

    st.caption(
        "The probability is the model's estimated probability for the "
        "Churn = Yes class."
    )
