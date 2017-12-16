from positive_interests import storeInterest
import localconfig
from pymongo import MongoClient

class Test:

    def setup_method(self, test_method):
        client = MongoClient(localconfig.MONGO_URI())
        cc = client.get_database(name="microsoftbotframework").get_collection("interest")
        cc.remove({})
    def testdatastore(self):
        client = MongoClient(localconfig.MONGO_URI())
        storeInterest("12345", "interest", "I like doughnuts")
        cc = client.get_database(name="microsoftbotframework").get_collection("interest")
        stored_obj = cc.find_one({"user_id" : "12345"})
        assert stored_obj["user_id"] == "12345"
        assert stored_obj["value"] == "I like doughnuts"

    def teardown_method(self, test_method):
        client = MongoClient(localconfig.MONGO_URI())
        cc = client.get_database(name="microsoftbotframework").get_collection("interest")
        cc.remove({})       