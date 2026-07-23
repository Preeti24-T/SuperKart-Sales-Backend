from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('backend/superkart_v1_0.joblib')

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Welcome to SuperKart Sales Forecast API"
    }

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Create a DataFrame from the input data
        input_df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(input_df)

        return jsonify({
            "Predicted Sales": round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rename app to house_price_api, matching the Dockerfile CMD
house_price_api = app
