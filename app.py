from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)


loaded_model = tf.keras.models.load_model('my_churn')

def preprocess_input(input_data):
    try:

        preprocessed_data = np.array(input_data, dtype=float)
        return preprocessed_data
    except Exception as e:
        raise ValueError("Error in preprocessing input data: " + str(e))

@app.route('/')
def home():
    return "Welcome to the Churn Prediction App!"

@app.route('/predict', methods=['POST'])
def predict_churn():
    try:
        
        user_input = request.json
        
        
        preprocessed_data = preprocess_input([user_input])  
        
        predictions = loaded_model.predict(preprocessed_data)
        
        churn_prediction = 1 if predictions[0][0] >= 0.5 else 0
        
        return jsonify({'churn_prediction': churn_prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=False)
