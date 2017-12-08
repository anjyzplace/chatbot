import csv
import random
import csvmapper
with open('food_recommendation.csv', 'r') as f:
    reader = csv.reader(f)
    recArray =[]
    for row in reader:
        recArray.append(row)

mychoice = random.choices(recArray, k=2)
first = mychoice[0]
second = mychoice[1]


foodtype1 =first[0]
foodTitle1 =first[1]
foodValue1 =first[2]
foodtype2 =second[0]
foodTitle2 =second[1]
foodValue2 =second[2]

def processJson(a,b,c,d):
    newjson = '{{\"actions\":[{{\"type\":\"imBack\",\"title\":\"{0}\",\"value\":\"{1}\"}},{{\"type\":\"imBack\",\"title\":\"{2}\",\"value\":\"{3}\"}},{{\"type\":\"imBack\",\"title\":\"None of the Above\",\"value\":\"None\"}}]}}'.format( a, b, c, d)
    return newjson


def foodRecomendation():
    return processJson(foodTitle1, foodValue1,  foodTitle2, foodValue2)

def exerciseRecommendation():
    with open('exercise_recommendation.csv', 'r') as f:
        reader = csv.reader(f)
        recArray =[]
        for row in reader:
            recArray.append(row)

        mychoice = random.choices(recArray, k=2)
        first = mychoice[0]
        second = mychoice[1]

        foodtype1 =first[0]
        foodTitle1 =first[1]
        foodValue1 =first[2]
        foodtype2 =second[0]
        foodTitle2 =second[1]
        foodValue2 =second[2]   
    return processJson(foodTitle1, foodValue1,  foodTitle2, foodValue2)












def isItInFile(searchValue):
    result = False
    with open('database.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')    
        for row in reader:
                if searchValue == row[2]:
                    result = True
        return result