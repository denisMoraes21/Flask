from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return json.dumps(request.args)


if __name__ == 'main':
    app.run(debug=True)
