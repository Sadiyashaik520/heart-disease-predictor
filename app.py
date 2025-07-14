import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.joblib")

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")
st.title("💓 Heart Disease Risk Prediction")
st.write("Enter your details below to check your risk.")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200)
chol = st.number_input("Cholesterol (mg/dl)", 100, 600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 250)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 6.0, step=0.1)
slope = st.selectbox("Slope of the ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (0=Normal, 1=Fixed, 2=Reversible, 3=Unknown)", [0, 1, 2, 3])

if st.button("Predict"):
    sex_val = 1 if sex == "Male" else 0
    input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ You are at risk of heart disease. Please consult a doctor.")
    else:
        st.success("✅ You are not at risk. Stay healthy!")