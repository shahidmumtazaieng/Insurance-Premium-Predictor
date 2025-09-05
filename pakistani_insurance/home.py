import streamlit as st

st.set_page_config(page_title="Insurance Premium Predictor", page_icon="🏥", layout="wide")

st.title("Welcome to the Insurance Premium Category Predictor")
st.markdown("""
    This application helps you predict your insurance premium category based on personal details such as age, weight, height, income, smoking status, city, and occupation. 
    Our machine learning model provides accurate predictions to help you understand potential insurance costs.

    **Get started by clicking the button below to enter your details and receive a prediction.**
""")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Go to Predictor", key="predict_button", help="Click to start predicting"):
        st.switch_page("./frontend.py")

st.image("https://via.placeholder.com/800x200?text=Insurance+Prediction", caption="Predict your insurance premium with ease!")
st.markdown("""
    ### Why Use This Tool?
    - **Fast and Accurate**: Powered by a trained machine learning model.
    - **User-Friendly**: Simple interface to input your details.
    - **Tailored for Pakistan**: Supports cities across Pakistan for localized predictions.
""")