
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

def sentimentalize(sentence):
    with open('./app/sentiment.csv', 'r') as fp:
       cl = NaiveBayesClassifier(fp, format="csv")
    # print(cl.classify("I like apples."))
    # print(cl.classify("I don't like their house."))
    return cl.classify(sentence)
