from flask import Flask, request, jsonify
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = {
        "input": user_input,
        "output": "This is a placeholder response."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT)
