from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
client = MongoClient('mongodb://localhost:27017/')

db = client.microsoftbotframework
collection = db.exercise
pprint.pprint(collection.find_one())