import joblib
import numpy as np

model_file = 'best_model.pkl'
model = joblib.load(model_file)

# Sample features
features = [
    3, 36, 7.2, 0, 0.03, 17, 28, 1.5, 0.7, 0.9, 0, 0, 8
]

input_vector = np.array(features).reshape(1, -1)
result_prediction = model.predict(input_vector)
print("Prediction:", "Sepsis" if result_prediction[0] == 1 else "No Sepsis")
