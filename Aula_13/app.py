from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="template")
UPLOAD_FOLDER = os.path.join(os.getcwd(), "upload")

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
        file = request.files["imagem"]
        savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(savePath)
        return "Upload realizado"



if __name__ == 'main':
    app.run(debug=True)
