# coding: utf-8

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"


@app.route("/user/<name>")
def user_name(name):
    return "user_name<br /><h1>Hello, %s!</h1>" % name


@app.route("/user/<int:id>")
def user_id(id):
    return "user_id<br /><h1>Hello, %s!</h1>" % id


@app.route("/goods/<float:total>")
def goods_total(total):
    return "goods_total<br /><h1>Hello, %s!</h1>" % total


@app.route("/user/<path:uri>")
def user_uri(uri):
    return "user_uri<br /><h1>Hello, %s!</h1>" % uri


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
