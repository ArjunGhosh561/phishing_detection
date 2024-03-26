import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

# Load the trained model
with open('phishing.pkl', 'rb') as model_file:
    phish_model = pickle.load(model_file)

# Endpoint for predicting whether a URL is phishing or not
@app.route('/predict', methods=['POST'])
def predict():
    # Get the URL from the request
    url = request.json['url']
    
    # Predict using the loaded model
    prediction = phish_model.predict([url])[0]
    
    # Probability of being a phishing site
    probabilities = phish_model.predict_proba([url])[0]
    phishingProbability = probabilities[0] if prediction == 'bad' else probabilities[1]
    
    # Determine the result message based on the prediction
    result = "This is a Phishing Site" if prediction == 'bad' else "This is not a Phishing Site"
    
    # Return the prediction result along with the probability
    return jsonify({'url': url, 'result': result, 'phishingProbability': phishingProbability})

if __name__ == '__main__':
    app.run(debug=True)