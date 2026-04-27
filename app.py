import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page config
st.set_page_config(
    page_title="Prediksi Dropout Siswa - Jaya Jaya Institut",
    page_icon="🎓",
    layout="wide"
)

# Load model artifacts
@st.cache_resource
def load_model():
    model = joblib.load('model/best_model.joblib')
    scaler = joblib.load('model/scaler.joblib')
    label_encoder = joblib.load('model/label_encoder.joblib')
    feature_names = joblib.load('model/feature_names.joblib')
    return model, scaler, label_encoder, feature_names

model, scaler, label_encoder, feature_names = load_model()

# Title
st.title("🎓 Prediksi Dropout Siswa")
st.markdown("### Jaya Jaya Institut - Sistem Deteksi Dini Dropout")
st.markdown("---")

st.markdown("""
Sistem ini membantu Jaya Jaya Institut untuk mendeteksi siswa yang berpotensi dropout
sehingga dapat diberikan bimbingan khusus sedini mungkin.
""")

# Sidebar for input
st.sidebar.header("📋 Input Data Siswa")

# Demographic Information
st.sidebar.subheader("Informasi Demografis")
marital_status = st.sidebar.selectbox("Status Pernikahan", 
    options=[1, 2, 3, 4, 5, 6],
    format_func=lambda x: {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced", 5: "Facto Union", 6: "Legally Separated"}[x])

gender = st.sidebar.selectbox("Gender", options=[0, 1], format_func=lambda x: {0: "Female", 1: "Male"}[x])
age_at_enrollment = st.sidebar.slider("Usia saat Enrollment", 17, 70, 20)
nacionality = st.sidebar.number_input("Kode Nationality", min_value=1, max_value=109, value=1)
international = st.sidebar.selectbox("International", options=[0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])

# Academic Information
st.sidebar.subheader("Informasi Akademik")
application_mode = st.sidebar.number_input("Application Mode", min_value=1, max_value=57, value=1)
application_order = st.sidebar.slider("Application Order", 0, 9, 1)
course = st.sidebar.selectbox("Course",
    options=[33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991],
    format_func=lambda x: {33: "Biofuel Production Technologies", 171: "Animation and Multimedia Design",
        8014: "Social Service (evening)", 9003: "Agronomy", 9070: "Communication Design",
        9085: "Veterinary Nursing", 9119: "Informatics Engineering", 9130: "Equinculture",
        9147: "Management", 9238: "Social Service", 9254: "Tourism", 9500: "Nursing",
        9556: "Oral Hygiene", 9670: "Advertising and Marketing Management",
        9773: "Journalism and Communication", 9853: "Basic Education", 9991: "Management (evening)"}[x])

daytime_evening = st.sidebar.selectbox("Daytime/Evening", options=[0, 1], format_func=lambda x: {0: "Evening", 1: "Daytime"}[x])
previous_qualification = st.sidebar.number_input("Previous Qualification", min_value=1, max_value=43, value=1)
previous_qualification_grade = st.sidebar.slider("Previous Qualification Grade", 0.0, 200.0, 130.0)
admission_grade = st.sidebar.slider("Admission Grade", 0.0, 200.0, 130.0)

# Family Information
st.sidebar.subheader("Informasi Keluarga")
mothers_qualification = st.sidebar.number_input("Mother's Qualification", min_value=1, max_value=44, value=1)
fathers_qualification = st.sidebar.number_input("Father's Qualification", min_value=1, max_value=44, value=1)
mothers_occupation = st.sidebar.number_input("Mother's Occupation", min_value=0, max_value=194, value=0)
fathers_occupation = st.sidebar.number_input("Father's Occupation", min_value=0, max_value=194, value=0)

# Financial Information
st.sidebar.subheader("Informasi Finansial")
displaced = st.sidebar.selectbox("Displaced", options=[0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])
educational_special_needs = st.sidebar.selectbox("Educational Special Needs", options=[0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])
debtor = st.sidebar.selectbox("Debtor", options=[0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])
tuition_fees_up_to_date = st.sidebar.selectbox("Tuition Fees Up to Date", options=[0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])
scholarship_holder = st.sidebar.selectbox("Scholarship Holder", options=[0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])

# Academic Performance - Semester 1
st.sidebar.subheader("Performa Semester 1")
cu_1st_credited = st.sidebar.number_input("Curricular Units 1st Sem (Credited)", min_value=0, max_value=30, value=0)
cu_1st_enrolled = st.sidebar.number_input("Curricular Units 1st Sem (Enrolled)", min_value=0, max_value=30, value=6)
cu_1st_evaluations = st.sidebar.number_input("Curricular Units 1st Sem (Evaluations)", min_value=0, max_value=50, value=6)
cu_1st_approved = st.sidebar.number_input("Curricular Units 1st Sem (Approved)", min_value=0, max_value=30, value=5)
cu_1st_grade = st.sidebar.slider("Curricular Units 1st Sem (Grade)", 0.0, 20.0, 12.0)
cu_1st_without_eval = st.sidebar.number_input("Curricular Units 1st Sem (Without Evaluations)", min_value=0, max_value=20, value=0)

# Academic Performance - Semester 2
st.sidebar.subheader("Performa Semester 2")
cu_2nd_credited = st.sidebar.number_input("Curricular Units 2nd Sem (Credited)", min_value=0, max_value=30, value=0)
cu_2nd_enrolled = st.sidebar.number_input("Curricular Units 2nd Sem (Enrolled)", min_value=0, max_value=30, value=6)
cu_2nd_evaluations = st.sidebar.number_input("Curricular Units 2nd Sem (Evaluations)", min_value=0, max_value=50, value=6)
cu_2nd_approved = st.sidebar.number_input("Curricular Units 2nd Sem (Approved)", min_value=0, max_value=30, value=5)
cu_2nd_grade = st.sidebar.slider("Curricular Units 2nd Sem (Grade)", 0.0, 20.0, 12.0)
cu_2nd_without_eval = st.sidebar.number_input("Curricular Units 2nd Sem (Without Evaluations)", min_value=0, max_value=20, value=0)

# Macroeconomic factors
st.sidebar.subheader("Faktor Ekonomi Makro")
unemployment_rate = st.sidebar.slider("Unemployment Rate (%)", 0.0, 20.0, 10.0)
inflation_rate = st.sidebar.slider("Inflation Rate (%)", -5.0, 10.0, 1.0)
gdp = st.sidebar.slider("GDP", -10.0, 10.0, 1.0)

# Create input dataframe
input_data = pd.DataFrame([[
    marital_status, application_mode, application_order, course,
    daytime_evening, previous_qualification, previous_qualification_grade,
    nacionality, mothers_qualification, fathers_qualification,
    mothers_occupation, fathers_occupation, admission_grade,
    displaced, educational_special_needs, debtor, tuition_fees_up_to_date,
    gender, scholarship_holder, age_at_enrollment, international,
    cu_1st_credited, cu_1st_enrolled, cu_1st_evaluations, cu_1st_approved,
    cu_1st_grade, cu_1st_without_eval, cu_2nd_credited, cu_2nd_enrolled,
    cu_2nd_evaluations, cu_2nd_approved, cu_2nd_grade, cu_2nd_without_eval,
    unemployment_rate, inflation_rate, gdp
]], columns=feature_names)

# Prediction
if st.sidebar.button("🔍 Prediksi", use_container_width=True):
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)
    
    predicted_label = label_encoder.inverse_transform(prediction)[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Hasil Prediksi")
        if predicted_label == "Dropout":
            st.error(f"⚠️ **Status Prediksi: {predicted_label}**")
            st.markdown("Siswa ini **berpotensi tinggi untuk dropout**. Perlu diberikan bimbingan khusus segera.")
        elif predicted_label == "Enrolled":
            st.warning(f"📝 **Status Prediksi: {predicted_label}**")
            st.markdown("Siswa ini masih **aktif terdaftar**. Perlu monitoring berkelanjutan.")
        else:
            st.success(f"✅ **Status Prediksi: {predicted_label}**")
            st.markdown("Siswa ini diprediksi akan **berhasil lulus**.")
    
    with col2:
        st.subheader("📈 Probabilitas")
        for i, cls in enumerate(label_encoder.classes_):
            prob = prediction_proba[0][i]
            st.write(f"**{cls}**: {prob:.1%}")
            st.progress(prob)
    
    st.markdown("---")
    st.subheader("📋 Data Input")
    st.dataframe(input_data.T.rename(columns={0: "Nilai"}), use_container_width=True)
else:
    st.info("👈 Isi data siswa di sidebar, lalu klik **Prediksi** untuk melihat hasil.")
    
    # Show model info
    st.subheader("ℹ️ Tentang Model")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model", "Random Forest")
    with col2:
        st.metric("Accuracy", "77.7%")
    with col3:
        st.metric("Jumlah Fitur", "36")
    
    st.markdown("""
    ### Faktor Utama yang Mempengaruhi Dropout:
    1. **Curricular Units 2nd Sem (Approved)** - Jumlah MK lulus semester 2
    2. **Curricular Units 2nd Sem (Grade)** - Nilai rata-rata semester 2
    3. **Curricular Units 1st Sem (Approved)** - Jumlah MK lulus semester 1
    4. **Curricular Units 1st Sem (Grade)** - Nilai rata-rata semester 1
    5. **Tuition Fees Up to Date** - Status pembayaran SPP
    """)
