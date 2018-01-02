# coding=utf-8
from microsoftbotframework import MsBot, conversationoperations
from tasks import *

# bot = MsBot()
# conversationoperations.CreateConversation()
bot = MsBot(state='MongodbState',verify_jwt_signature=False)
bot.add_process(botresponse)

if __name__ == '__main__':
    bot.run()