from flask import Flask, Response,jsonify,request
from model.chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/api/predict/')
def predict():
   print(request)
   text = request.data.data
   print('request.data: ', text)
   #response = get_response(text)
   massage = {"answer": text}
   print("finished")
   return jsonify(massage), 200

@app.get('/api/predicts')
def predictTry():
   print("hello")
   return 'works', 200

@app.get('/')
def welcome():
   print("hello")
   return '<h1>Hello</h1>', 200



# @app.route('/api/predict/<string:userInput>', methods=['GET'])
# def predicxt(userInput):
#     print(request)
#     return jsonify({'massage': 'hello mf'}), 200


app.run(debug=True)



