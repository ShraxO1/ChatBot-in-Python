from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)
while True:
    message = input('You:')
    print(message)
    if message.strip() == 'bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        print('ChatBot:', reply)
