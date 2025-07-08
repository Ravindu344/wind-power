# app.py
import streamlit as st
import numpy as np
import xgboost as xgb

# Load XGBoost model from .json
model = xgb.XGBRegressor()
model.load_model("xgboost_best_model.json")

# App Title
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>Wind Turbine Power Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h6 style='text-align: center;'>Predict Active Power (kW) using wind conditions and time inputs.</h6>",
    unsafe_allow_html=True
    )
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, step=0.1)
    wind_direction = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, step=1.0)

    # Month dropdown
    month_names = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    selected_month = st.selectbox("Month", list(month_names.keys()))
    month = month_names[selected_month]

    # Week dropdown
    week = st.selectbox("Week", list(range(1, 53)))

    # Predict button
    if st.button("Predict Active Power"):
        if wind_speed == 0:
            prediction = 0.0
        else:
            input_data = np.array([[wind_speed, wind_direction, month, week]])
            prediction = model.predict(input_data)[0]
        st.success(f"🔋 Predicted Active Power: {prediction:.2f} kW")
