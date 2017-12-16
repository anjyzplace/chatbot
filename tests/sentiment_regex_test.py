from app.sentiment_regex import matcher

def test_positive_matcher():
    res = matcher('I like apples.')
    assert res== True

def test_lowercase_positive():
    res = matcher('i like apples.')
    assert res== True    

def test_nagative_matcher():
    res = matcher('I hate apples.')
    assert res== False    

def test_nagative_lowercase():
    res = matcher('i hate apples.')
    assert res== False       