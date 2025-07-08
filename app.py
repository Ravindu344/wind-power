# app.py
import streamlit as st
import numpy as np
import xgboost as xgb

#  Load model from .json
model = xgb.XGBRegressor()
model.load_model("xgboost_best_model.json")

# Title
st.title("⚡ Wind Turbine Power Prediction App")
st.write("Enter wind data to predict Active Power output (kW).")

# Input fields
wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, step=0.1)
wind_direction = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, step=1.0)
month = st.number_input("Month", min_value=1, max_value=12, step=1)
week = st.number_input("Week", min_value=1, max_value=5, step=1)

# Button to predict
if st.button("Predict Active Power"):
    if wind_speed == 0:
        prediction = 0.0
    else:
        input_data = np.array([[wind_speed, wind_direction, month, week]])
        prediction = model.predict(input_data)[0]

    st.success(f"Predicted Active Power: {prediction:.2f} kW")
