from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "order" in user_input:
        return "📦 You can track your order on our website under 'My Orders'. Do you need the link?"

    elif "refund" in user_input:
        return "💳 Refunds are processed within 5–7 business days. Would you like me to guide you through the process?"

    elif "problem" in user_input or "issue" in user_input:
        return "⚠️ I'm sorry to hear that! Could you please describe the problem in more detail?"

    elif "contact" in user_input or "agent" in user_input:
        return "☎️ You can reach our support team at support@example.com or call +44 1234 567890."

    else:
        return "🤖 I'm not sure about that. Let me connect you to a human agent for further help."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return jsonify({"response": chatbot_response(user_text)})

if __name__ == "__main__":
    app.run(debug=True)
