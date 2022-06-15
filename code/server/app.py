import json
import jsonpickle
from flask import Flask, Response,jsonify,request
from flask import Flask,jsonify,request
from model.chat import get_response
from flask_cors import CORS
import jsonpickle

app = Flask(__name__)
CORS(app)

@app.post('/api/predict/')
def predict():
   userInput = request.get_json()
   botResponse = get_response(userInput['data'])
   #botResponse = jsonpickle.encode(botResponse)
   strResponse = str(botResponse)
   return jsonify(botResponse), 200


app.run(debug=True)

