# pylint: disable=E1136

from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import json
import random
import app.localconfig as localconfig
client = MongoClient(localconfig.MONGO_URI())

db = client.microsoftbotframework
collection = db.exercise
exercises = collection.find()

exerciseValueList=[]
state=False

def suggest(kollection):
        suggestionList = []
        db = client.microsoftbotframework
        mykollection = db.__getattr__(kollection).find()
        # exercises = collection.find()
        for row in mykollection:
            suggestionList.append({"title": row['TITLE'], "value":row['VALUE']})
        mychoice = random.sample(suggestionList, 2)
        state=True
        choicey=mychoice
        print(mychoice)
        first = mychoice[0]
        second = mychoice[1]
        foodtype1 = first['title']
        foodTitle1 = first['value']
        foodtype2 = second['title']
        foodTitle2 = second['value']
        # print(foodtype1, foodTitle1,  foodtype2, foodTitle2)
        suggestionList.clear
        return processJson(foodtype1, foodTitle1,  foodtype2, foodTitle2)

def foodTypesSuggest(category):
        suggestionList = []
        db = client.microsoftbotframework
        mykollection = db.food.find({"CATEGORY": category})
        # mykollection = db.__getattr__(kollection).find({"CATEGORY": "breakfast"})
        # exercises = collection.find()
        for row in mykollection:
            suggestionList.append({"title": row['TITLE'], "value":row['VALUE']})
        mychoice = random.sample(suggestionList, 2)
        state=True
        choicey=mychoice
        print(mychoice)
        first = mychoice[0]
        second = mychoice[1]
        foodtype1 = first['title']
        foodTitle1 = first['value']
        foodtype2 = second['title']
        foodTitle2 = second['value']
        print(foodtype1, foodTitle1,  foodtype2, foodTitle2)
        suggestionList.clear
        return processJson(foodtype1, foodTitle1,  foodtype2, foodTitle2)

def removeSelection():
    # print(choicey)
    # exerciseList.remove(choice)
    print(len(exerciseValueList))
# exerciseSuggest()
def processJson(a,b,c,d):
    newjson = '{{\"actions\":[{{\"type\":\"imBack\",\"title\":\"{0}\",\"value\":\"{1}\"}},{{\"type\":\"imBack\",\"title\":\"{2}\",\"value\":\"{3}\"}},{{\"type\":\"imBack\",\"title\":\"None of the Above\",\"value\":\"None\"}}]}}'.format( a, b, c, d)
    return newjson