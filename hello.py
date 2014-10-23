# coding: utf-8

from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("hello.html")


if __name__ == "__main__":
    manager = Manager(app)
    manager.run()
