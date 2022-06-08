from flask import Flask,jsonify,request
from model.chat import get_response

app = Flask(__name__)

@app.post("/predict")
def predict():
    text = request.get_json().get("massage")
    response = get_response(text)
    massage = {"answer": response}
    return jsonify(massage)


if __name__ == "__main__":
    app.run(debug=True)



