# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

bot = ChatBot(
    "BuffBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": "extensions.comparisons.synset_distance_thai",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            'default_response': "ขอโทษนะครับ BuffBot สับสนครับ"
        }
    ],
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')

    import extensions.preprocess as preprocessor
    preprocessed_text = preprocessor.preprocess(user_text)

    response = str(bot.get_response(preprocessed_text))
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
