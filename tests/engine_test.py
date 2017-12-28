from app.newengine import calculate_class_score, calculate_class_score_commonality, sentenceClass, wordCounter

def test_score_positive():
    value = calculate_class_score("who is this", "identity")
    assert value == 3

def test_score_negative():
    value = calculate_class_score("who is this", "identity")
    assert value !=  4

def test_score_without_common_postitive():
    value = calculate_class_score_commonality("who is this", "identity")
    assert value <  2 

def test_score_without_common_negative():
    value = calculate_class_score_commonality("who is this", "identity")
    assert value !=  4    

def test_sent():
    val = sentenceClass("how is my blood sugar")
    assert val == "blood-sugar"      

def test_counter():
    count = wordCounter("How are you")
    assert count == 3

def test_counter_negative():
    count = wordCounter("How are you doing.")
    assert count == 4