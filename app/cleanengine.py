import nltk
import csv
import random as rd
from nltk.stem.lancaster import LancasterStemmer
from classfier import sentimentalize
stemmer = LancasterStemmer()

training_data = []

with open('healthdata.csv', 'rt') as csvfile:
    x = csv.DictReader(csvfile,delimiter=',',quotechar='|')
    for row in x:
        training_data.append({"class": row['CLASS'], "sentence":row['SENTENCE']})


corpus_words = {}
class_words = {}

classes = list(set([a['class'] for a in training_data]))
for c in classes:
    class_words[c] = []

for data in training_data:
    for word in nltk.word_tokenize(data['sentence']):
        if word not in ["?", "'s", "."]:
            stemmed_word = stemmer.stem(word.lower())
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1
            class_words[data['class']].extend([stemmed_word])


def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    for word in nltk.word_tokenize(sentence):
        if stemmer.stem(word.lower()) in class_words[class_name]:
            score += 1
            
            if show_details:
                print ("   match: %s" % stemmer.stem(word.lower() ))
    return score

sentence = "good day for us to have lunch?"


for c in class_words.keys():
    print ("Class: %s  Score: %s \n" % (c, calculate_class_score(sentence, c)))

def calculate_class_score_commonality(sentence, class_name, show_details=True):
    score = 0
    for word in nltk.word_tokenize(sentence):
        if stemmer.stem(word.lower()) in class_words[class_name]:
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score

for c in class_words.keys():
    print ("Class: %s  Score: %s \n" % (c, calculate_class_score_commonality(sentence, c)))


def classify(sentence):
    high_class = None
    high_score = 0
    for c in class_words.keys():
        score = calculate_class_score_commonality(sentence, c, show_details=False)
        if score > high_score:
            high_class = c
            high_score = score
    return high_class, high_score


def sentenceClass(sentence):
    high_class = None
    high_score = 0
    for c in class_words.keys():
        score = calculate_class_score_commonality(sentence, c, show_details=False)
        if score > high_score:
            high_class = c
            high_score = score
    return high_class

def sendResponse(sentence):
    high_class = None
    high_score = 0
    for c in class_words.keys():
        score = calculate_class_score_commonality(sentence, c, show_details=False)
        if score > high_score:
            high_class = c
            high_score = score
            
    return selectResponse(high_class, sentence)

def selectResponse(dclass, sentence):
    GREETING_RESPONSES = ["'Hello", "Hey", "Hey there", "Hi", "Good day to you", "Hi there"]
    GOODBYE_RESPONSES =  ["See you later", "Bye",  "Talk to you later", "Bye for now", "Take care"]
    IDENTITY_RESPONSES = ["I am LifeBot. How can I help you", " I am LifeBot, I can give healthy recommendations."]
    FOOD_RESPONSES = ["beans", "soup", "rice"]
    responses = list(set([a['response'] for a in training_data]))
    if(dclass=='greeting'):
     return rd.choice(GREETING_RESPONSES)
    elif(dclass=='goodbye'):
     return rd.choice(GOODBYE_RESPONSES)
    elif(dclass=='identity'):
     return rd.choice(IDENTITY_RESPONSES) 
    elif(dclass=='food'):
     return ' You can try some ' + rd.choice(FOOD_RESPONSES)    
    else:
     print('--------------------------')
    #  print(sentence)
    #  return (sentimentalize(sentence))
     return ('Sorry, I dont understand that')
# print("End of training..............")
# print(classify("make me some lunch?"))
