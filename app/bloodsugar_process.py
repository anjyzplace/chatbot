import json
from statistics import mean
# import logging
# logging.basicConfig(filename='chatbot.log',level=logging.DEBUG)


# path = 'blood_sugar_five.json'
def averageBloodSugarin5DaysBeforeMeal(path):
    data = json.load(open(path))
    con = data["bloodsugar"]["results"]
    FiveDayList=[]
    for x in con:
        for y in x:
            my_dict = y
            FiveDayList.append(my_dict['before_meal'])
    memean = mean(FiveDayList)
    # logging.info('Mean blood sugar is ')
    return memean


def averageBloodSugarin5DaysAfterMeal(path):
    data = json.load(open(path))
    con = data["bloodsugar"]["results"]
    FiveDayList=[]
    for x in con:
        for y in x:
            my_dict = y
            FiveDayList.append(my_dict['after_meal'])
    memean = mean(FiveDayList)
    print(memean)
    return memean

def lastAfterMealBloodResult(path):
    data = json.load(open(path))
    con = data["bloodsugar"]["results"]
    FiveDayList=[]
    for x in con:
        for y in x:
            my_dict = y
            FiveDayList.append(my_dict['after_meal'])
    return FiveDayList[-1]

def lastPremealBloodResult(path):
    data = json.load(open(path))
    con = data["bloodsugar"]["results"]
    FiveDayList=[]
    for x in con:
        for y in x:
            my_dict = y
            FiveDayList.append(my_dict['before_meal'])
    return FiveDayList[-1] 