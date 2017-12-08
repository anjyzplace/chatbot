from microsoftbotframework import ReplyToActivity, MongodbState, Config
from newengine import sendResponse
from newengine import sentenceClass
from recommender import foodRecomendation, exerciseRecommendation
from recommender import isItInFile
from dbSuggest import exerciseSuggest, removeSelection
import chathistory


# from pymongo import MongoClient
import json


# jsonData ='{"actions":[{"type":"imBack","title":"Blue","value":"Blue"},{"type":"imBack","title":"Red","value":"Red"},{"type":"imBack","title":"Green","value":"Green"}]}'
jsonFoodData = foodRecomendation()
# jsonExerciseData = exerciseRecommendation()
jsonExerciseData = exerciseSuggest()
removeSelection()
# jsonToPython = json.loads(jsonData)
jsonToPython = None
greeting = 'I dey o'
def echo_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text=message["text"]).send()                        

def botresponse(message):
    print(message)
    if(message["type"] == "conversationUpdate"):
        if(message["membersAdded"][0]["name"] == "Bot"):
            print("")
        elif message["membersAdded"][0]["name"] != "Bot":
                name = message["from"]["name"]
                ReplyToActivity(fill=message,
                                text="Welcome, " + name).send()
                ReplyToActivity(fill=message,
                                text="I am LifeBot. I can give healthy recommendations.").send()
    elif message["text"] == "None":
        ReplyToActivity(fill=message,
            text='Let me make you another suggestion').send()                                
    elif isItInFile(message["text"])== True:
        ReplyToActivity(fill=message,
            text='Thanks, I will make a note of that.').send()
    elif message["type"] == "message":
        print("It's a message")
        botreply = sendResponse(message["text"])
        sententenceclass = sentenceClass(message["text"])
        print("Two")
        input = message["text"]
        print('The input is {0}'.format(input))
        if sententenceclass == "food":
                # print(botreply)
                # print(jsonFoodData)
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




























    # if message["text"] == None:
    #         print("Hi")    
    #     # print(valu.get_lastchat())
    # botreply = sendResponse(message["text"])
    # # print("One")
    # sententenceclass = sentenceClass(message["text"])
    # # print("Two")
    # input = message["text"]
    # print('The input is {0}'.format(input))
    # if isItInFile(message["text"])== True:
    #     ReplyToActivity(fill=message,
    #         text='Thanks, I will make a note of that.').send()

    # # print(selectRecomendation())
    # elif message["type"] == "message":
    #     if sententenceclass == "food":
    #         # print(botreply)
    #         # print(jsonFoodData)
    #         jsonToPython = json.loads(jsonFoodData)
    #         ReplyToActivity(fill=message,
    #                     text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
    #     elif sententenceclass == "exercise":
    #         # print(botreply)
    #         print(jsonExerciseData)
    #         jsonToPython = json.loads(jsonExerciseData)
    #         ReplyToActivity(fill=message,
    #                     text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
    #     else:
    #         jsonToPython = None
    #         ReplyToActivity(fill=message,
    #                     text=botreply, inputHint="acceptingInput", suggestedActions=jsonToPython).send()
