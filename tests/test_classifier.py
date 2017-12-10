from classfier import sentimentalize


def test_positive_semantics():
    res = sentimentalize('I like apples.')
    assert res== 'pos'    

def test_negative_semantics():
    res = sentimentalize('I don\'t like their house.')
    assert res== 'neg'        