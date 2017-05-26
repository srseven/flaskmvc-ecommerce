from flask import render_template
from dbooad import app


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login.html")
def login():
    return render_template("login.html")


@app.route("/cart.html")
def cart():
    return render_template("cart.html")


# ----------------------------------------------------------------------------#
# Error handlers.
# ----------------------------------------------------------------------------#


@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html"), 404
