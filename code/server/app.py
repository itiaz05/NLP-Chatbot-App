from flask import Flask, Response,jsonify,request
from model.chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post('/api/predict/')
def predict():
   print(request.get_json())
   userInput = request.get_json()
   print(userInput['data'])
   botResponse = get_response(userInput['data'])
   print(botResponse)
   return jsonify(botResponse), 200
   
   # #args = request.args
   # print(args)
   # text = request.data
   # print('request.data: ', text)
   # #response = get_response(text)
   # massage = {"answer": text}
   # print("finished")
   # return massage, 200
   # #return jsonify(massage), 200

app.run(debug=True)


