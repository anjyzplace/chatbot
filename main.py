from microsoftbotframework import MsBot
from tasks import *

bot = MsBot()
bot.add_process(botresponse)

if __name__ == '__main__':
    bot.run()