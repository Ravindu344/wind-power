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

# Define mapping of months to calendar week ranges
month_week_map = {
    "January": list(range(1, 6)),
    "February": list(range(5, 9)),
    "March": list(range(9, 14)),
    "April": list(range(14, 18)),
    "May": list(range(18, 23)),
    "June": list(range(22, 27)),
    "July": list(range(27, 32)),
    "August": list(range(31, 36)),
    "September": list(range(36, 41)),
    "October": list(range(40, 45)),
    "November": list(range(44, 49)),
    "December": list(range(48, 53))
}

# UI Layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, step=0.1)
    wind_direction = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, step=1.0)

    # Month dropdown
    selected_month = st.selectbox("Month", list(month_week_map.keys()))
    month = list(month_week_map.keys()).index(selected_month) + 1

    # Week dropdown based on month
    week_options = month_week_map[selected_month]
    week = st.selectbox("Week", week_options)

    # Predict button
    if st.button("Predict Active Power"):
        if wind_speed == 0:
            prediction = 0.0
        else:
            input_data = np.array([[wind_speed, wind_direction, month, week]])
            prediction = model.predict(input_data)[0]
        st.success(f"Predicted Active Power: {prediction:.2f} kW")
