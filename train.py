from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

english_bot = ChatBot("BuffBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

corpus_name = raw_input("Please enter corpus file name: ")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("./data/" + corpus_name)

