from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

# Load your trained model (update the path to where your model is saved)
model = load('/Users/shaiksaheer/Documents/College_Docs/Advanced Data Mining/ics-dataset-for-smart-grids/Updated_Data/stacked_model.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Receive data sent to the endpoint
    data = request.json
    # Convert the data into a DataFrame (update according to the format of your input data)
    input_data = pd.DataFrame([data])

    # Apply model prediction
    prediction = model.predict(input_data)

    # Return the prediction as a JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in a production environment
