import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below to predict your insurance premium category:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.selectbox(
    "City",
    options=[
        "Abbottabad", "Bahawalpur", "Burewala", "Chakwal", "Charsadda", "Chiniot",
        "Dera Ghazi Khan", "Dera Ismail Khan", "Faisalabad", "Gujranwala", "Gujrat",
        "Hafizabad", "Haripur", "Hyderabad", "Islamabad", "Jacobabad", "Jhang",
        "Jhelum", "Kamoke", "Kandhkot", "Karachi", "Kasur", "Khanewal", "Khanpur",
        "Khairpur", "Khuzdar", "Kohat", "Lahore", "Larkana", "Mandi Bahauddin",
        "Mardan", "Mianwali", "Mirpur Khas", "Multan", "Muzaffargarh", "Narowal",
        "Nawabshah", "Nowshera", "Okara", "Pakpattan", "Peshawar", "Quetta",
        "Rahim Yar Khan", "Rawalpindi", "Sadiqabad", "Sahiwal", "Sargodha",
        "Sheikhupura", "Shikarpur", "Sialkot", "Sukkur", "Tando Allahyar",
        "Tando Muhammad Khan", "Turbat", "Vihari"
    ],
    index=20  # Default to Karachi
)
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "predicted_category" in result:
            prediction = result["predicted_category"]
            st.success(f"Predicted Insurance Premium Category: **{prediction}**")
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")