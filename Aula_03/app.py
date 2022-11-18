from flask import Flask

app = Flask(__name__)

@app.route("/hello/<nome>")
def hello(nome):
        return "<h1>Hello {}</h1>".format(nome)

@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID):
        if postID >= 3:
                return "blog info {}".format(postID)
        else:
                return "blog todo"

if __name__ == 'main':
        app.run()