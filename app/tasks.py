from microsoftbotframework import ReplyToActivity, MongodbState, Config
from newengine import sendResponse, sentenceClass
from dbSuggest import suggest
from sentiment_regex import matcher
import chathistory
from  positive_interests import storeInterest
from bloodsugar_process import *
import json
# import logging
# logging.basicConfig(filename='chatbot.log',level=logging.INFO)


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
    elif(matcher(message["text"]) == True):
        user_id = message["from"]["id"]
        interest = message["text"]
        storeInterest(user_id, "interest", interest)
        ReplyToActivity(fill=message,
            text='Great, I have made a note of that.').send()
    elif message["text"] == "None":
        offset =3
        info = chathistory.DataStore()
        lastchats = info.get_lastnumberofchats(offset)
        intentId = lastchats[0]["_id"]
        print(intentId)
        print(lastchats)
        sentence = lastchats[0]["activity"]["text"]
        if(sentence == "None"):
            print("**********************")
            offset = offset + 2
            lastchats = info.get_lastnumberofchats(offset)
            print('Fetching {0} messages'.format(offset))
            print(lastchats)
            sentence = lastchats[0]["activity"]["text"]
        sententenceclass = sentenceClass(sentence)

        responder(sententenceclass, message)
    elif message["type"] == "message":
        botreply = sendResponse(message["text"])
        sententenceclass = sentenceClass(message["text"])
        input = message["text"]
        print('The input is {0}'.format(input))
        if sententenceclass == "food":
                jsonToPython = json.loads(suggest('food'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
        elif sententenceclass == "drink":
                jsonToPython = json.loads(suggest('drinks'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()                            
        elif sententenceclass == "exercise":
                jsonToPython = json.loads(suggest('exercise'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
        elif sententenceclass == "blood-sugar":
                ReplyToActivity(fill=message,
                    text='I have some information about your blood sugar.').send()
                before = averageBloodSugarin5DaysBeforeMeal("blood_sugar_five.json")
                template = "Your average pre meal blood sugar in the last 5 days is {0} mmol/L".format(before)
                ReplyToActivity(fill=message,
                    text=template).send()                                           
        else:
                jsonToPython = None
                ReplyToActivity(fill=message,
                            text=botreply, inputHint="acceptingInput", suggestedActions=jsonToPython).send()

def responder(sentenceclass, message):
    if sentenceclass == "food":
            jsonToPython = json.loads(suggest('food'))
            ReplyToActivity(fill=message,
                        text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
    elif sentenceclass == "exercise":
            jsonToPython = json.loads(suggest('exercise'))
            ReplyToActivity(fill=message,
                        text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()

























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
