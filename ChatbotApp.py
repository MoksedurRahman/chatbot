from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a chatbot instance
chatbot = ChatBot('CustomerSupportBot')

# Train the bot with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    bot_response = chatbot.get_response(user_message)
    return jsonify({'response': str(bot_response)})

if __name__ == '__main__':
    app.run(debug=True)
