from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/append")
def append():
    open("data", "a").write(str(request.args.get("msg")) + "\n\r")
    return ""

@app.route("/retreive")
def retreive():
    return open("data").read()

if __name__ == "__main__":
    app.run( host= '0.0.0.0',port=9899 )
