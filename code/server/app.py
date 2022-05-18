from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return "<p>Home page</p>"

app.run()