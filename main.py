from microsoftbotframework import MsBot
from tasks import *

# bot = MsBot()
print('Starting Application')
bot = MsBot(cache=False,state='MongodbState')
print('Finished setting MongoDB')
bot.add_process(botresponse)

if __name__ == '__main__':
    bot.run()