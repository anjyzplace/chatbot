import json
from bloodsugar_process import averageBloodSugarin5DaysBeforeMeal, averageBloodSugarin5DaysAfterMeal

def test_the_sugarbefore():
    result = averageBloodSugarin5DaysBeforeMeal('tests\\blood_sugartest.json')
    print(result)
    assert result == 3

