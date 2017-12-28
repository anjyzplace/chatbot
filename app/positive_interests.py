from pymongo import MongoClient
import app.localconfig
import json

client = MongoClient(app.localconfig.MONGO_URI())

# Refactor for blank user, blank interest
def storeInterest(user, collection, interest):

    data = '{{\"user_id\": \"{0}\", \"value\":\"{1}\"}}'.format(user, interest)
    db = client.microsoftbotframework
    db.__getattr__(collection).insert(json.loads(data))