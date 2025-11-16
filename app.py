import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Car Price Predictor", layout="centered")

st.title("🚗 Car Price Prediction App")
st.write("Enter car details to get an estimated selling price.")

# Load the trained simple model
@st.cache_resource
def load_model():
    model = joblib.load("car_price_app_model.joblib")
    return model

model = load_model()

st.sidebar.header("Input Features")

# These names MUST match features_app in the notebook
enginesize = st.sidebar.number_input("Engine Size (cc)", min_value=50, max_value=5000, value=1500, step=50)
horsepower = st.sidebar.number_input("Horsepower", min_value=30, max_value=500, value=120, step=5)
citympg = st.sidebar.number_input("City Mileage (mpg)", min_value=5, max_value=60, value=20, step=1)
highwaympg = st.sidebar.number_input("Highway Mileage (mpg)", min_value=5, max_value=60, value=25, step=1)
curbweight = st.sidebar.number_input("Curb Weight (kg)", min_value=500, max_value=3000, value=1200, step=50)
carlength = st.sidebar.number_input("Car Length (inches)", min_value=100, max_value=250, value=170, step=1)

# Build dataframe for prediction
input_dict = {
    "enginesize": enginesize,
    "horsepower": horsepower,
    "citympg": citympg,
    "highwaympg": highwaympg,
    "curbweight": curbweight,
    "carlength": carlength
}

input_df = pd.DataFrame([input_dict])

st.subheader("Your Input")
st.write(input_df)

if st.button("Predict Price"):
    try:
        pred = model.predict(input_df)[0]
        st.success(f"Estimated Car Price: ₹ {pred:,.2f}")
        st.caption("Note: This is a model-based estimate. Actual prices may vary.")
    except Exception as e:
        st.error("Something went wrong while predicting.")
        st.write(e)
