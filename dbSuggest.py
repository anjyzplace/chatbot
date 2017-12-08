from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import json
import random
from recommender import processJson
import localconfig
client = MongoClient(localconfig.MONGO_URI())

db = client.microsoftbotframework
collection = db.exercise
exercises = collection.find()
# con = exercises['exercise']
exerciseValueList=[]
state=False

def exerciseSuggest():
    # exerciseList=[]
    # print(len(con))
    for row in exercises:
        # print(row['CATEGORY'], row['TITLE'], row['VALUE'] )
        exerciseValueList.append({"title": row['TITLE'], "value":row['VALUE']})
        mychoice = random.choices(exerciseValueList, k=2)
        state=True
        choicey=mychoice
            
        print(mychoice)
        first = mychoice[0]
        second = mychoice[1]
        foodtype1 =first['title']
        foodTitle1 =first['value']
        foodtype2 =second['title']
        foodTitle2 =second['value']
        # print(foodtype1, foodTitle1,  foodtype2, foodTitle2)     
    return processJson(foodtype1, foodTitle1,  foodtype2, foodTitle2)

def removeSelection():
    # print(choicey)
    # exerciseList.remove(choice)
    print(len(exerciseValueList))
# exerciseSuggest()