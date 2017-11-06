from microsoftbotframework import ReplyToActivity
from engine import sendResponse
import json
jsonData ='{"actions":[{"type":"imBack","title":"Blue","value":"Blue"},{"type":"imBack","title":"Red","value":"Red"},{"type":"imBack","title":"Green","value":"Green"}]}'
jsonToPython = json.loads(jsonData)
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
                        text=botreply, inputHint="acceptingInput", suggestedActions=jsonToPython).send()
