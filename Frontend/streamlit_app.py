import streamlit as st
import requests

st.title("Iris Flower Prediction")

# Input fields for Iris features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

if st.button("Predict"):
    # Prepare input data dictionary for the API
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    # Call FastAPI backend
    try:
        response = requests.post("https://iris-prediction-2.onrender.com/predict", json=input_data)
        response.raise_for_status()  # Raise error for bad status
        prediction = response.json()
        st.success(f"Prediction: {prediction['species']} (class {prediction['prediction']})")
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with the API: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
