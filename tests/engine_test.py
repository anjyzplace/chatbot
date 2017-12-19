from app.engine import calculate_class_score

def test_score():
    value = calculate_class_score("who is this", "identity")
    assert value == 3