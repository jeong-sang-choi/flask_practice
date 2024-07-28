from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("user_name")
    passwd = request.args.get("pw")
    email = request.args.get("email")
    print(username, passwd, email)
    
    if username == "jeongsang":
        return_data = {"auth":"success"}
    else:
        return_data = {"auth":"failed"}
    return json.dumps(return_data, ensure_ascii=False)


@app.route("/html_test")
def hello_html():
    return render_template("html_practice.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
