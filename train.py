import sys
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

english_bot = ChatBot("BuffBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

try:

    if sys.argv.count < 2:
        corpus_name = raw_input("Please enter corpus file name: ")
    else:
        corpus_name = sys.argv[1]

    english_bot.set_trainer(ChatterBotCorpusTrainer)

    if corpus_name == '-all':
        for filename in os.listdir('./data'):
            if filename.endswith('.yml'):
                english_bot.train("./data/" + filename)
    else:
        english_bot.train("./data/" + corpus_name)

except KeyboardInterrupt:
    sys.exit(0)

