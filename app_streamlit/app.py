import streamlit as st
import numpy as np
import joblib
import pandas as pd
import random
import warnings

warnings.filterwarnings("ignore")

# Load the model

loaded_model = joblib.load('best_model.pkl')

# Define feature names
features = [
    'Patient_ID', 'HR', 'O2Sat', 'Temp', 'MAP', 'Resp', 'SBP', 'DBP',
    'Resp_sys', 'Creatinine', 'Platelets', 'Bilirubin_total', 'Age'
]

# Load a sample dataset to use for random test data
# Replace 'sample_data.csv' with the actual path to your dataset
sample_data = pd.read_csv('sample_data.csv')  # Ensure this file exists and has the correct data

# Streamlit app
def main():
    st.title("Sepsis Prediction App")

    # Sidebar for input features
    st.sidebar.header("Input Features")
    input_values = {}
    for feature in features:
        input_values[feature] = st.sidebar.number_input(
            label=feature,
            value=0.0,  # Default value
            format="%f"  # Float format
        )
    
    # Button to fill inputs with random values
    if st.sidebar.button("Fill with Random Test Data"):
        # Sample random row from the dataset
        random_row = sample_data.sample(n=1).iloc[0]
        for feature in features:
            input_values[feature] = random_row[feature]
        st.sidebar.write("Filled with random test data.")

    # Display input fields with current values
    st.sidebar.write("Current Input Values:")
    st.sidebar.write(input_values)

    # Button to predict
    if st.sidebar.button("Predict"):
        # Prepare the feature vector
        input_vector = np.array([input_values[feature] for feature in features]).reshape(1, -1)
        
        # Predict
        result_prediction = loaded_model.predict(input_vector)
        final_result = "Sepsis" if result_prediction[0] == 1 else "No Sepsis"
        
        # Display the result
        st.write(f"Prediction Outcome: {final_result}")

if __name__ == "__main__":
    main()
