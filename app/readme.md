# Sepsis Prediction App

This is a Streamlit-based web application that predicts the likelihood of sepsis in patients using a machine learning model.

## Features

- **Prediction**: Enter patient data to predict whether the patient has sepsis.
- **Random Test Data**: Automatically fill the input form with random data from a sample dataset.

## How to Use

The application is live and can be accessed at the following URL:

- **[Sepsis Prediction App](https://sepsis-prediction-app-1.onrender.com)**

### Running the Application Locally

If you'd like to run the application locally, follow these steps:

### Prerequisites

Ensure you have Python 3.x and Streamlit installed.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sepsis-prediction-app.git
    cd sepsis-prediction-app
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the `sample_data.csv` file and `best_model.pkl` in the root directory.

### Running the Application

1. Run the Streamlit application:
    ```bash
    streamlit run app_streamlit.py
    ```

2. Open your web browser and navigate to the provided local URL.

### Dependencies

The project requires the following Python packages:
- Streamlit
- numpy
- pandas
- scikit-learn
- joblib

### Deactivating the Virtual Environment

To deactivate the virtual environment when you're done working, simply run:

```bash
deactivate
