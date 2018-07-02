import sys
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import argparse

english_bot = ChatBot("BuffBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

parser = argparse.ArgumentParser(description='Train BuffBot2')
parser.add_argument('-file', help='Training data file', required=False)
parser.add_argument('-all', action='store_true', help='Train all files in the data directory', required=False)
parser.add_argument('-type', default='yml', help='The type of the source file; either \'yml\' or \'txt\'', required=True)

args = parser.parse_args()

if args.file is None and args.all is False:
    print("No file to train with")
    sys.exit(0)
elif args.file is not None and args.all is True:
    print("Invalid source file selection")
    sys.exit(0)

if args.type == 'yml':
    english_bot.set_trainer(ChatterBotCorpusTrainer)

    if args.all:
        for filename in os.listdir('./data'):
            if filename.endswith('.yml'):
                english_bot.train("./data/" + filename)
    else:
        english_bot.train("./data/" + args.file)

elif args.type == 'txt':
    english_bot.set_trainer(ListTrainer)

    if args.all:
        for filename in os.listdir('./data'):
            if filename.endswith('.txt'):
                lines = [line.rstrip('\n') for line in open(filename)]
                english_bot.train(lines)
    else:
        lines = [line.rstrip('\n') for line in open("./data/" + args.file)]
        english_bot.train(lines)
else:
    print("Invalid source type")
