import json
import chathistory


valu = chathistory.DataStore()
con = valu.get_lastchat()
# data = json.load(open('lastchat.json'))
first_ignoredchoice = con[0]["activity"]["suggestedActions"]["actions"][0]["value"]
second_ignoredchoice = con[0]["activity"]["suggestedActions"]["actions"][1]["value"]
print(first_ignoredchoice, second_ignoredchoice)