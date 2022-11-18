from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route("/")
def index():
        x = 50
        y = 70
        return render_template("template.html", x = x, z = y)

if __name__ == 'main':
    app.run(debug=True)
