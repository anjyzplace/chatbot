import json
from app.bloodsugar_process import averageBloodSugarin5DaysBeforeMeal, averageBloodSugarin5DaysAfterMeal, lastAfterMealBloodResult, lastPremealBloodResult

def test_the_sugarbefore():
    result = averageBloodSugarin5DaysBeforeMeal('./tests/blood_sugartest.json')
    print(result)
    assert result == 3

def testaftermeallastresult():
    result = lastAfterMealBloodResult('./tests/blood_sugartest.json')
    assert result == 15

def testpremeallastresult():
    result = lastPremealBloodResult('./tests/blood_sugartest.json')
    assert result == 5    