from app import app
from flask import render_template, request


@app.route("/")
def index():
    return render_template("index.html")


# Get Fetch API
@app.route("/get-message", methods=["GET"])
def get_entry():

    if request.method == "GET":
        req = request.args
        name = req["name"]
        message = req.get("message")
        print(f"Get Fetch API - name: {name} message: {message}")

    return render_template("index.html")


# Post Fetch API
@app.route("/post-message", methods=["POST"])
def post_entry():

    if request.method == "POST":
        req = request.get_json()
        user = req.get("user")
        secret = req["password"]
        
        print(f"Post Fecth API - user: {user} password: {secret}")
    
    return render_template("index.html")
