import json
from statistics import mean

data = json.load(open('blood_sugar_five.json'))
con = data["bloodsugar"]["results"]

def averageBloodSugarin5DaysBeforeMeal():
    FiveDayList=[]
    for x in con:
        for y in x:
            my_dict = y
            FiveDayList.append(my_dict['before_meal'])
    memean = mean(FiveDayList)
    print(memean)
    return memean


def averageBloodSugarin5DaysAfterMeal():
    FiveDayList=[]
    for x in con:
        for y in x:
            my_dict = y
            FiveDayList.append(my_dict['after_meal'])
    memean = mean(FiveDayList)
    print(memean)
    return memean
averageBloodSugarin5DaysBeforeMeal()
averageBloodSugarin5DaysAfterMeal()    