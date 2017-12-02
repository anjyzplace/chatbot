from recommender import isItInFile

def func(x):
    return x + 1

def test_answer():
    assert func(5) == 6

def test_food_is_not_in_database():
    res = isItInFile('sugar')
    assert res== False    

def test_food_is_in_database():
    res = isItInFile('beans')
    assert res== True       