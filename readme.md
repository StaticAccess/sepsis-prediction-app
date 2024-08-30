# Sepsis Prediction Web Application

This is a Flask-based web application that predicts the likelihood of sepsis in patients using a machine learning model. The app allows users to input various health metrics and either fill the form with random test data or make predictions based on the provided data.

## Features

- **Prediction**: Enter patient data to predict whether the patient has sepsis.
- **Random Test Data**: Automatically fill in the input form with random data from a sample dataset.

## Deployment

The application is deployed and accessible at the following URL:

- **Application:** [https://sepsis-prediction-app.onrender.com](https://sepsis-prediction-app.onrender.com)

## Check Installed Packages

To view the versions of all installed packages, visit:

- **Packages Versions:** [https://sepsis-prediction-app.onrender.com/packages](https://sepsis-prediction-app.onrender.com/packages)

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sepsis-prediction-app.git
    cd sepsis-prediction-app
    ```

2. **Create and activate a virtual environment:**

    On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    On macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have a `sample_data.csv` file in the root directory of the project. This file should contain the data used for generating random test inputs.

5. Place the trained model file (`best_model.pkl`) in the root directory.

### Running the Application with WSGI

To run the application using a WSGI server like Gunicorn, follow these steps:

1. **Install Gunicorn:**
    ```bash
    pip install gunicorn
    ```

2. **Run the application using Gunicorn:**
    ```bash
    gunicorn app:app
    ```

    - `app:app` refers to the `app` object in the `app.py` file.

3. Open your web browser and navigate to `http://127.0.0.1:8000/`.

### Running the Application Locally

For local development, you can use Flask's built-in server (not recommended for production):

1. Run the application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/`.

### Usage

- **Home Page**: Enter patient data in the provided form and click "Predict" to see the prediction result.
- **Fill with Random Test Data**: Click the "Fill with Random Test Data" button to populate the form with random data from the `sample_data.csv` file.
- **Installed Packages**: Visit `http://127.0.0.1:5000/packages` to see a list of installed Python packages.

### Project Structure

- `app/app.py`: Main Streamlit application file if you want to run Streamlit Build.
- `app_flask/app.py`: Main Flask application file.
- `templates/`: Contains HTML templates for rendering web pages.
- `requirements.txt`: List of dependencies.
- `sample_data.csv`: Sample data used for generating random test inputs.
- `best_model.pkl`: The trained machine learning model used for predictions.

### Dependencies

The project requires the following Python packages:
- Flask
- numpy
- pandas
- scikit-learn
- joblib

See `requirements.txt` for the exact versions.

### Deactivating the Virtual Environment

To deactivate the virtual environment when you're done working, simply run:

```bash
deactivate
