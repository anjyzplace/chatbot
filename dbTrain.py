from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import json
import random
client = MongoClient('mongodb://localhost:27017/')

db = client.microsoftbotframework
collection = db.healthdata
data = collection.find()
# print(data)

def trainingData():
    for x in data:
        print(x["CLASS"], x["SENTENCE"])

trainingData()

#     return processJson(foodtype1, foodTitle1,  foodtype2, foodTitle2)

# def removeSelection():
#     print(choicey)
#     print(len(exerciseList))

