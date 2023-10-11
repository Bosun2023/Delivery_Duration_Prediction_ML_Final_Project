import os
from flask import Flask, request, jsonify
import joblib
import xgboost as xgb
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Define the path to your saved model file
model_file_path = 'C:/Users/User/Desktop/Lighthouse BootCamp/Delivery_Duration_Prediction_ML_Final_Project/delivery_time_model.pkl'

# Load the model and any necessary preprocessing steps
try:
	loaded_model = joblib.load(model_file_path)

	# If the model includes a StandardScaler, load it as well
	if isinstance(loaded_model, xgb.XGBRegressor) and isinstance(loaded_model.named_steps['scaler'], StandardScaler):
		scaler = loaded_model.named_steps['scaler']
	else:
		scaler = None

except FileNotFoundError:
	loaded_model = None
	scaler = None

@app.route('/predict', methods=['POST'])
def predict():
	#try:
	if True:
		if loaded_model is None:
			return jsonify({'error': 'Model not found. Please make sure the model file exists.', 'prediction': None})

		# Get input data from JSON request
		data = request.get_json()
		features = data.get('features')  # Use .get() to avoid KeyError

		if features is None:
			return jsonify({'error': 'Features not found in request.', 'prediction': None})

		# If a StandardScaler is available, transform the input data
		# if scaler is not None:
		#   features = scaler.transform([features])
		features = pd.DataFrame(features, index=[0])
		# Make predictions using the loaded model
		predictions = loaded_model.predict(features)
		# Check if the prediction is a numeric value
		#if not isinstance(predictions[0], (int, float)):
		#	return jsonify({'error': 'Invalid prediction value.', 'prediction': None})

		# Convert the prediction to a float (if it's numeric)
		#prediction_float = float(predictions[0]) if isinstance(predictions[0], (int, float)) else None

		# Return the predictions as JSON response with the 'prediction' key
		return jsonify({'prediction': float(predictions[0]), 'error': None})

	# except Exception as e:
	#	return jsonify({'error': str(e), 'prediction': None})

if __name__ == '__main__':
	app.run(debug=True)





