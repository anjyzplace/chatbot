# coding=utf-8
from microsoftbotframework import MsBot, conversationoperations
from tasks import *

# bot = MsBot()
# conversationoperations.CreateConversation()
bot = MsBot(state='MongodbState')
bot.add_process(botresponse)

if __name__ == '__main__':
    bot.run()