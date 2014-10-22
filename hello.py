# coding: utf-8

from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def index():
    name = "steven"
    from datetime import datetime
    return render_template("hello.html",
                           name=name,
                           current_time=datetime.utcnow())


if __name__ == "__main__":
    manager = Manager(app)
    manager.run()
