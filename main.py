import streamlit as st
import joblib
import os
# ---------------- Load models ----------------


# Path to models folder
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

heart_model = joblib.load(os.path.join(MODEL_DIR, "heartdisease.pkl"))
brain_model = joblib.load(os.path.join(MODEL_DIR, "brain.pkl"))
lungs_model = joblib.load(os.path.join(MODEL_DIR, "lungs.pkl"))
kidney_model = joblib.load(os.path.join(MODEL_DIR, "kid.pkl"))


# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}
.card {
    flex: 1 1 calc(50% - 20px);
    max-width: 300px;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    font-size: 20px;
    color: white;
    cursor: pointer;
    transition: 0.3s;
    box-shadow: 2px 4px 10px rgba(0,0,0,0.2);
}
.card:hover {
    transform: scale(1.05);
}
.heart { background-color: #e63946; }
.brain { background-color: #457b9d; }
.lungs { background-color: #2a9d8f; }
.kidney { background-color: #8d5cf6; }
</style>
""", unsafe_allow_html=True)

# ---------------- Initialize Session State ----------------
if "page" not in st.session_state:
    st.session_state["page"] = "🏠 About"

# ---------------- Sidebar ----------------

st.sidebar.title("Diseases Prediction")

menu = ["🏠 About", "❤️ Heart Disease", "🧠 Brain Stroke", "🫁 Lungs Recovery", "🧬 Kidney Disease"]

choice = st.sidebar.radio(
    "Go to:", 
    menu,
    index=menu.index(st.session_state["page"])  # safe because we initialized above
)

# Update session state
st.session_state["page"] = choice


# ---------------- ABOUT PAGE ----------------
if choice == "🏠 About":
    st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🩺 Multi Diseases Prediction App")
    st.markdown("---")

    st.subheader("📌 About this App")
    st.write("""
    The **Multi Diseases Predictor** is a machine learning web app built with **Python** and **Streamlit**.  
    It helps users check the risk of major health conditions using medical inputs.
    """)
    st.markdown("---")

    st.subheader("⚡ Usefulness")
    st.write("""
    - Early **risk detection**  
    - Preventive **health monitoring**  
    - Support **better healthcare decisions**  
    """)
    st.markdown("---")
    st.subheader("🛠️ Tech Stack")
    st.write("""
    - **Language:** Python 🐍  
    - **Libraries:** Streamlit, scikit-learn, joblib, pandas  
    - **Algorithms:** Logistic Regression, Decision Trees, Random Forest, SVM  
    """)
    st.markdown("---")
    st.subheader("🔮 Prediction Process")
    st.write("""
    1️⃣ Enter your health details  
    2️⃣ ML model analyses inputs  
    3️⃣ App predicts **disease risk** instantly  
    """)
    st.markdown("---")
    st.subheader("🔗 Explore Predictions")

    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button("❤️ Heart Disease"):
            st.session_state['page'] = "❤️ Heart Disease"
            st.rerun()
    with col2:
        if st.button("🧠 Brain Stroke"):
            st.session_state['page'] = "🧠 Brain Stroke"
            st.rerun()

    col3, col4 = st.columns(2, gap="large")
    with col3:
        if st.button("🫁 Lungs Recovery"):
            st.session_state['page'] = "🫁 Lungs Recovery"
            st.rerun()
    with col4:
        if st.button("🧬 Kidney Disease"):
            st.session_state['page'] = "🧬 Kidney Disease"
            st.rerun()

    st.markdown("---")

    st.subheader("💡 Recommendations")
    st.write("""
    After prediction, the app provides **personalized recommendations** based on your health risk.  
    These include lifestyle advice such as diet tips, exercise routines, and preventive measures.  
    """)


    
# ---------------- HEART ----------------
elif choice == "❤️ Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    col1, col2 = st.columns(2,gap="large")

    with col1:
        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex", [0,1])
        cp = st.number_input("Chest Pain Type (cp)", 0, 3)
        trestbps = st.number_input("Resting Blood Pressure", 50, 250)
        chol = st.number_input("Cholesterol", 100, 600)
        fbs = st.selectbox("Fasting Blood Sugar > 120mg/dl", [0,1])

    with col2:
        restecg = st.number_input("Resting ECG Results", 0, 2)
        thalach = st.number_input("Maximum Heart Rate", 50, 250)
        exang = st.selectbox("Exercise Induced Angina", [0,1])
        oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, step=0.1)
        slope = st.number_input("Slope", 0, 2)
        ca = st.number_input("Number of Major Vessels (ca)", 0, 4)
        thal = st.number_input("Thalassemia (thal)", 0, 3)


    if st.button("Predict Heart Disease"):
        pred = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,
                                    thalach, exang, oldpeak, slope, ca, thal]])[0]
        if pred == 1:
            st.error("⚠️ Heart Disease Detected")
            st.warning("👉 Recommendations:\n- Regular exercise 🏃‍♂️\n- Maintain a balanced diet 🥗\n- Reduce cholesterol intake 🍳\n- Avoid smoking & alcohol 🚭\n- Regular health check-ups 🩺")
        else:
            st.success("✅ No Heart Disease Detected")
            st.info("👍 Keep maintaining a healthy lifestyle with regular exercise and a balanced diet.")


# ---------------- BRAIN ----------------
elif choice == "🧠 Brain Stroke":
    st.header("🧠 Brain Stroke Prediction")
    col1, col2 = st.columns(2,gap="large")

    with col1:
        gender = st.selectbox("Gender", [0,1])
        age = st.number_input("Age", 1, 120)
        hyper = st.selectbox("Hypertension", [0,1])
        heartdisease = st.selectbox("Heart Disease", [0,1])
        ever = st.selectbox("Ever Married", [0,1])

    with col2:
        fbs = st.selectbox("Work Type (fbs)", [0,1,2,3])
        type_ = st.selectbox("Residence Type", [0,1])
        avg = st.number_input("Average Glucose Level", 50, 300)
        bmi = st.number_input("BMI", 10, 60)
        smoking = st.selectbox("Smoking Status", [0,1,2])


    if st.button("Predict Brain Stroke"):
        pred = brain_model.predict([[gender, age, hyper, heartdisease, ever, fbs,
                                    type_, avg, bmi, smoking]])[0]
        if pred == 1:
            st.error("⚠️ Brain Stroke Risk Detected")
            st.warning("👉 Recommendations:\n- Monitor and control blood pressure 💉\n- Stay physically active 🏋️‍♀️\n- Maintain healthy weight ⚖️\n- Quit smoking 🚭\n- Eat more fruits and vegetables 🥦🍎")
        else:
            st.success("✅ No Brain Stroke Detected")
            st.info("👍 Continue with a healthy diet and regular exercise to prevent risks.")


# ---------------- LUNGS ----------------
elif choice == "🫁 Lungs Recovery":
    st.header("🫁 Lungs Recovery Prediction")
    col1, col2 = st.columns(2,gap="large")

    with col1:
        age = st.number_input("Age", 1, 120)
        gender = st.selectbox("Gender", [0,1])
        somkingtesting = st.selectbox("Smoking Test", [0,1])
        lungcapacity = st.number_input("Lung Capacity", 1, 100)

    with col2:
        diseasetype = st.number_input("Disease Type", 0, 5)
        treatmenttype = st.number_input("Treatment Type", 0, 5)
        hospitalvisits = st.number_input("Hospital Visits", 0, 50)


    if st.button("Predict Lungs Recovery"):
        pred = lungs_model.predict([[age, gender, lungcapacity, diseasetype,
                                    treatmenttype, hospitalvisits, somkingtesting]])[0]
        if pred == 1:
            st.success("✅ Lungs Recovery Detected")
            st.info("🌱 Maintain healthy breathing with yoga, avoid polluted areas, and continue medical follow-ups.")
        else:
            st.error("⚠️ Lungs Not Fully Recovered")
            st.warning("👉 Recommendations:\n- Avoid smoking 🚭\n- Follow prescribed medications 💊\n- Practice breathing exercises 🧘‍♀️\n- Eat antioxidant-rich foods 🍊🥦")


# ---------------- KIDNEY ----------------
elif choice == "🧬 Kidney Disease":
    st.header("🧬 Kidney Disease Prediction")
    col1, col2 = st.columns(2,gap="large")

    with col1:
        bp = st.number_input("Blood Pressure", 50, 200)
        sg = st.number_input("Specific Gravity", 1, 10)
        al = st.number_input("Albumin", 0, 10)
        su = st.number_input("Sugar", 0, 10)
        rbc = st.number_input("Red Blood Cells", 0, 2)
        bu = st.number_input("Blood Urea", 1, 500)

    with col2:
        sc = st.number_input("Serum Creatinine", 0, 20)
        sod = st.number_input("Sodium", 100, 200)
        pot = st.number_input("Potassium", 1, 10)
        hemo = st.number_input("Hemoglobin", 1, 20)
        wbcc = st.number_input("WBC Count", 1000, 20000)
        rbcc = st.number_input("RBC Count", 1, 10)
        htn = st.selectbox("Hypertension", [0,1])


    if st.button("Predict Kidney Disease"):
        pred = kidney_model.predict([[bp, al, su, rbc, sg, bu, sc, sod,
                                    pot, hemo, wbcc, rbcc, htn]])[0]
        if pred == 1:
            st.error("⚠️ Chronic Kidney Disease Detected")
            st.warning("👉 Recommendations:\n- Limit salt intake 🧂\n- Stay hydrated 💧\n- Manage blood pressure and diabetes 💉\n- Avoid overuse of painkillers 💊\n- Consult nephrologist regularly 🩺")
        else:
            st.success("✅ No Kidney Disease Detected")
            st.info("👍 Keep kidneys healthy by drinking enough water and eating a balanced diet.")
