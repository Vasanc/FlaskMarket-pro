from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about/<username>")
def about(username):
    return f"<h1>Hello, {username}!</h1>"

if __name__=='__main__':
    app.run(port=4000)