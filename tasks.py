from microsoftbotframework import ReplyToActivity
from engine import sendResponse
from engine import sentenceClass
import json
jsonData ='{"actions":[{"type":"imBack","title":"Blue","value":"Blue"},{"type":"imBack","title":"Red","value":"Red"},{"type":"imBack","title":"Green","value":"Green"}]}'
# jsonToPython = json.loads(jsonData)
jsonToPython = None
greeting = 'I dey o'
def echo_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text=message["text"]).send()

def botresponse(message):
    botreply = sendResponse(message["text"])
    sententenceclass = sentenceClass(message["text"])
    # print(botreply)
    if message["type"] == "message":
        if sententenceclass == "food":
            print(botreply)
            jsonToPython = json.loads(jsonData)
            ReplyToActivity(fill=message,
                        text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
        else:
            jsonToPython = None
            ReplyToActivity(fill=message,
                        text=botreply, inputHint="acceptingInput", suggestedActions=jsonToPython).send()
