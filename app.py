import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Cloud Run!"

if __name__ == "__main__":
    # Cloud Run では、環境変数 PORT が設定されます（通常 8080）
    port = int(os.environ.get("PORT", 8080))
    # 0.0.0.0 でリッスンしないと外部アクセスできません
    app.run(host="0.0.0.0", port=port)
