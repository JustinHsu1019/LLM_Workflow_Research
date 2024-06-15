from flask import Flask, request, jsonify
from flask_cors import CORS

from utils.call_ai import call_aied
from utils.gemini_tem import Gemini_Template
from utils.gpt_tem import GPT_Template

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type, Qs-PageCode, Cache-Control'

@app.route("/")
def index():
    """Server 是否正常的確認頁面."""
    return "server is ready"

@app.route("/chat", methods=['POST', 'GET'])
def chat_bot():
    chart = request.values.get("chart")
    mess = request.values.get("mess")

    if not mess:
        response = "無內容"
    else:
        try:
            response = call_aied(chart, mess)
        except Exception as e:
            print(f"get error: {e}")
            response = f"Error: {e}"

    return jsonify({"llm": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
