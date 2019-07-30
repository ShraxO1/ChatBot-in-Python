from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = 'C:/Users/shray/PycharmProjects/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

