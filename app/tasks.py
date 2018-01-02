from microsoftbotframework import ReplyToActivity, MongodbState, Config
from engine import sendResponse, sentenceClass, calculate_class_score, wordCounter
from dbSuggest import suggest, foodTypesSuggest, suggestPersonal
from sentiment_regex import matcher
import chathistory
from profiler import profile
from  positive_interests import storeInterest, storeInterestwithClass
from bloodsugar_process import averageBloodSugarin5DaysBeforeMeal, averageBloodSugarin5DaysAfterMeal, lastAfterMealBloodResult, lastPremealBloodResult
import json
from textblob import TextBlob
from trimmer import Trimmer
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
        sententenceclass = sentenceClass(interest)
        storeInterestwithClass(user_id, "personal", sententenceclass, Trimmer(interest))
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
        user_id = message["from"]["id"]
        if sententenceclass == "food":
            if(wordCounter(message["text"])>=3):
                if(suggestPersonal("personal",sententenceclass, user_id) != None):
                    jsonToPython = json.loads(suggestPersonal("personal",sententenceclass, user_id))
                    ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
                else:
                    jsonToPython = json.loads(suggest('food'))
                    ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()        
            else:
                guide(sententenceclass, message)
        elif sententenceclass == "breakfast":
            if(wordCounter(message["text"])>=3):
                if(suggestPersonal("personal",sententenceclass, user_id)):
                    jsonToPython = json.loads(suggestPersonal("personal",sententenceclass, user_id))
                else:
                    jsonToPython = json.loads(foodTypesSuggest('breakfast'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", \
                            inputHint="acceptingInput", suggestedActions=jsonToPython).send()  
            else:
                guide(sententenceclass, message) 
        elif sententenceclass == "lunch":
            if(wordCounter(message["text"])>=3):
                jsonToPython = json.loads(foodTypesSuggest('lunch'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()  
            else:
                guide(sententenceclass, message) 
        elif sententenceclass == "dinner":
            if(wordCounter(message["text"])>=3):
                jsonToPython = json.loads(foodTypesSuggest('dinner'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()  
            else:
                guide(sententenceclass, message)                                 
        elif sententenceclass == "drink":
            if(wordCounter(message["text"])>=3):
                jsonToPython = json.loads(suggest('drinks'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()  
            else:
                guide(sententenceclass, message)                                                     
        elif sententenceclass == "exercise":
            if(wordCounter(message["text"])>=3):           
                jsonToPython = json.loads(suggest('exercise'))
                ReplyToActivity(fill=message,
                            text="Which of the following would you consider ?", inputHint="acceptingInput", suggestedActions=jsonToPython).send()
            else:
                guide(sententenceclass, message)                            
        elif sententenceclass == "blood-sugar":
            sentence = message["text"]
            if(wordCounter(sentence)>=3):
                if("status" in sentence or "profile" in sentence):
                    result_pre = lastPremealBloodResult("./app/blood_sugar_five.json")  
                    result_after = lastAfterMealBloodResult("./app/blood_sugar_five.json")   
                    status = profile(result_pre, result_after)
                    templateStatus = "Your last blood result is {0} mg/dL, which mean your status is {1} ".format(result_pre, status)                              
                    ReplyToActivity(fill=message,
                        text=templateStatus).send()
                elif("lastest" in sentence or "result" in sentence or "five" in sentence):                        
                    before = averageBloodSugarin5DaysBeforeMeal("./app/blood_sugar_five.json")
                    after = averageBloodSugarin5DaysAfterMeal("./app/blood_sugar_five.json")
                    templateBefore = "Your average pre meal blood sugar in the last 5 days is {0} mg/dL".format(before)
                    ReplyToActivity(fill=message,
                        text=templateBefore).send()                                           
                    templateAfter = "Your average post meal blood sugar in the last 5 days is {0} mg/dL".format(after)
                    ReplyToActivity(fill=message,
                        text=templateAfter).send()
                else:
                    before = averageBloodSugarin5DaysBeforeMeal("./app/blood_sugar_five.json")
                    after = averageBloodSugarin5DaysAfterMeal("./app/blood_sugar_five.json")                                          
                    template = "Your average blood sugar in the last 5 days is Fasting {0} mg/dL, random: {1} mg/dL ".format(before, after)
                    ReplyToActivity(fill=message,
                        text=template).send()                                 
        elif sententenceclass == "goodbye":
                name = message["from"]["name"]
                jsonToPython = None
                messagetosend = botreply + ", " + name
                ReplyToActivity(fill=message,
                            text=messagetosend, inputHint="acceptingInput", suggestedActions=jsonToPython).send()
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

def guide(sentenceClass, message):
    guideMessage = "I am LifeBot. I can give healthy "+ sentenceClass +" recommendations."
    ReplyToActivity(fill=message,
            text=guideMessage).send()
