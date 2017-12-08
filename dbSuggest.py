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
exercises = collection.find_one()
con = exercises['exercise']
exerciseList=[]
state=False
choicey="car"

def exerciseSuggest():
    # exerciseList=[]
    print(len(con))
    for x in con:
        print(x)
        exerciseList.append(x)
    mychoice = random.choices(exerciseList, k=2)
    state=True
    choicey=mychoice
       
    # print(mychoice)
    first = mychoice[0]
    second = mychoice[1]
    foodtype1 =first['type']
    foodTitle1 =first['name']
    foodtype2 =second['type']
    foodTitle2 =second['name']
    # print(foodtype1, foodTitle1,  foodtype2, foodTitle2)
    # exerciseList.remove(mychoice)  
    return processJson(foodtype1, foodTitle1,  foodtype2, foodTitle2)

def removeSelection():
    print(choicey)
    # exerciseList.remove(choice)
    print(len(exerciseList))
# exerciseSuggest()

