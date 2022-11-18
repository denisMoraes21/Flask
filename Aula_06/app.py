from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder="page")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return dumps(request.form['nome'])
    return "OK POST"


if __name__ == 'main':
    app.run(debug=True)
