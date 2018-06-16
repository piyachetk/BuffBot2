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
            'default_response': u"ขอโทษนะครับ BuffBot สับสนครับ"
        },
        {
            'import_path': 'chatterbot.logic.TimeLogicAdapter',
            'positive': [
                u"อะไรคืืือเวลาตอนนี้",
                u"ขอเวลา",
                u"ขอเวลาตอนนี้",
                u"ขอเวลาในตอนนี้",
                u"ขอเวลาในตอนนี้หน่อย",
                u"ขอเวลาตอนนี้หน่อย"
                u"ขอเวลาหน่อย",
                u"เวลาตอนนี้คืออะไร",
                u"เวลาตอนนี้คือเท่าไหร่",
                u"ตอนนี้เวลาเท่าไหร่"
            ],
            'negative': [
                u"อะไรคือเวลา",
                u"เวลาคืออะไร"
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
