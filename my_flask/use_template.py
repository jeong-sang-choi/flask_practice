from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("html_practice.html")

if __name__ == "__main__":
    app.run(host= "localhost",port = "8080")