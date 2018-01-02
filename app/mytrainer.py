import nltk
import csv
import random as rd
from nltk.stem.lancaster import LancasterStemmer
# from classfier import sentimentalize
from pymongo import MongoClient
import app.localconfig as localconfig
from textblob import TextBlob

stemmer = LancasterStemmer()
client = MongoClient(localconfig.MONGO_URI())
db = client.microsoftbotframework
collection = db.healthdata
data = collection.find()

personal_data = []


for row in data:
        personal_data.append({"class": row['CLASS'], "item":row['ITEM']})