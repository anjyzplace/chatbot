import nltk
import re

sentence = "I like rice"

def matcher(sentence):
    if(sentence):
        m = re.search('^I like', sentence, re.IGNORECASE)
        if(m == None):
            return "False"
        else:
            return "True"

print(matcher(sentence))