from flask import Flask
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSON 응답을 UTF-8로 인코딩

@app.route("/json_test")
def hello_json():
    data = {
        "name": "김대리",
        "place": "파스쿠찌"
    }
    return json.dumps(data, ensure_ascii = False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")  # 포트 번호를 정수로 지정
    
import requests

response = requests.get("http://localhost:8080/json_test")
print(response.json())



