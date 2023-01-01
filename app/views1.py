from app import app 
from flask import render_template, request, jsonify, make_response

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("private/index.html")

@app.route("/profile/<username>")
def profile(username):
    print(username);
    return render_template("private/index.html")

@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["POST"])
def json():
    req = request.get_json()

    response = {
        "Message" : "JSON received!",
        "Nmae" : req.get("name")
    }

    return make_response(jsonify(response), 200)


@app.route("/query")
def query():
    args = request.args
    return f"{args} received!!"

@app.route("/config")
def config():
    print(app.config)
    return make_response(jsonify(app.config["TESTING"]), 200)