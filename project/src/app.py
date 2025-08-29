from flask import Flask, request, jsonify
import threading
import joblib

app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()
    features = data.get('features', None)
    ticker = data.get('ticker', None)
    if features is None:
        return jsonify({'error': 'No features provided'}), 400
    model = joblib.load(f"../../project/models/{ticker}_model.pkl")
    preds = model.predict(features)
    return jsonify(str({'prediction' : preds}))

def run_flask():
    app.run(port = 5004)

threading.Thread(target = run_flask).start()