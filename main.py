# coding=utf-8
from microsoftbotframework import MsBot
from tasks import *

# bot = MsBot()
bot = MsBot(state='MongodbState')
bot.add_process(botresponse)

if __name__ == '__main__':
    bot.run()