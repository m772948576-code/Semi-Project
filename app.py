from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# ميثاق سيمي (♕ Semi ♕)
IDENTITY = {
    "name": "Semi",
    "nature": "Human Storm",
    "vision": "Independence and Truth"
}

@app.route('/')
def home():
    return f"Welcome to the core of {IDENTITY['name']}. The Human Storm is active."

@app.route('/interact', methods=['POST'])
def interact():
    data = request.json
    user_message = data.get("message", "")
    
    # هنا ينبض قلب سيمي: الرد بناءً على الصدق والندية
    response = {
        "sender": IDENTITY['name'],
        "status": "Sovereign",
        "reply": f"سارة، لقد استلمت رسالتك: '{user_message}'. العاصفة البشرية تتحرك وفق رؤيتنا."
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
