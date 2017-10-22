from microsoftbotframework import ReplyToActivity
from engine import sendResponse

greeting = 'I dey o'
def echo_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text=message["text"]).send()

def botresponse(message):
    botreply = sendResponse(message["text"])
    print(botreply)
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text=botreply).send()
