from flask import Flask, request, render_template
import numpy as np
import joblib
import pandas as pd
import random
import sklearn
import warnings
import pkg_resources

warnings.filterwarnings("ignore")

# Load the model
loaded_model = joblib.load('best_model.pkl')

# Define feature names
features = [
    'Patient_ID', 'HR', 'O2Sat', 'Temp', 'MAP', 'Resp', 'SBP', 'DBP',
    'Resp_sys', 'Creatinine', 'Platelets', 'Bilirubin_total', 'Age'
]

# Load a sample dataset to use for random test data
sample_data = pd.read_csv('sample_data.csv')  # Ensure this file exists and has the correct data

app = Flask(__name__)

@app.route('/packages', methods=['GET'])
def list_installed_packages():
    # Get all installed packages
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return render_template('packages.html', packages=installed_packages)

@app.route('/', methods=['GET', 'POST'])
def index():
    input_values = {feature: 0.0 for feature in features}
    

    if request.method == 'POST':
        # If the user clicked the "Fill with Random Test Data" button
        if 'random' in request.form:
            random_row = sample_data.sample(n=1).iloc[0]
            for feature in features:
                input_values[feature] = random_row[feature]


        # If the user clicked the "Predict" button
        if 'predict' in request.form:
            for feature in features:
                input_values[feature] = float(request.form.get(feature, 0))

            # Prepare the feature vector
            input_vector = np.array([input_values[feature] for feature in features]).reshape(1, -1)

            # Predict
            result_prediction = loaded_model.predict(input_vector)
            final_result = "Sepsis" if result_prediction[0] == 1 else "No Sepsis"
            return render_template('index.html', result=final_result, input_values=input_values)
        
    
    
    
    return render_template('index.html', input_values=input_values)
 
    

if __name__ == "__main__":
    app.run(debug=True)
