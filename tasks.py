from microsoftbotframework import ReplyToActivity, MongodbState
from engine import sendResponse
from engine import sentenceClass
from recommender import foodRecomendation, exerciseRecommendation
from recommender import isItInFile
import chathistory


# from pymongo import MongoClient
import json


# jsonData ='{"actions":[{"type":"imBack","title":"Blue","value":"Blue"},{"type":"imBack","title":"Red","value":"Red"},{"type":"imBack","title":"Green","value":"Green"}]}'
jsonFoodData = foodRecomendation()
jsonExerciseData = exerciseRecommendation()
# jsonToPython = json.loads(jsonData)
jsonToPython = None
greeting = 'I dey o'
def echo_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text=message["text"]).send()

def botresponse(message):
    valu = chathistory.DataStore()
    print(valu.get_history())
    # print('The user id is {0}'.format(mongodb_state.get_user_data(user_id)))
    botreply = sendResponse(message["text"])
    sententenceclass = sentenceClass(message["text"])
    input = message["text"]
    print('The input is {0}'.format(input))
    if isItInFile(message["text"])== True:
        ReplyToActivity(fill=message,
            text='Thanks, I will make a note of that.').send()

    # print(selectRecomendation())
    elif message["type"] == "message":
        if sententenceclass == "food":
            # print(botreply)
            print(jsonFoodData)
            jsonToPython = json.loads(jsonFoodData)
            ReplyToActivity(fill=message,
                        text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
        elif sententenceclass == "exercise":
            # print(botreply)
            print(jsonExerciseData)
            jsonToPython = json.loads(jsonExerciseData)
            ReplyToActivity(fill=message,
                        text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
        else:
            jsonToPython = None
            ReplyToActivity(fill=message,
                        text=botreply, inputHint="acceptingInput", suggestedActions=jsonToPython).send()
