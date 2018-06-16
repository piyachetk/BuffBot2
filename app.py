# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

bot = ChatBot(
    "BuffBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.25,
            'default_response': "ขอโทษนะครับ BuffBot สับสนครับ"
        },
        {
            'import_path': 'chatterbot.logic.TimeLogicAdapter',
            'positive': [
                "อะไรคืืือเวลาตอนนี้",
                "ขอเวลา",
                "ขอเวลาตอนนี้",
                "ขอเวลาในตอนนี้",
                "ขอเวลาในตอนนี้หน่อย",
                "ขอเวลาตอนนี้หน่อย"
                "ขอเวลาหน่อย",
                "เวลาตอนนี้คืออะไร",
                "เวลาตอนนี้คือเท่าไหร่",
                "ตอนนี้เวลาเท่าไหร่"
            ],
            'negative': [
                "อะไรคือเวลา",
                "เวลาคืออะไร"
            ]
        }
    ],
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg').encode("utf-8")
    return unicode(bot.get_response(user_text))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
