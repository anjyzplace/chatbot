import csv
import random

with open('recommendation.csv', 'r') as f:
    reader = csv.reader(f)
    recArray =[]
    for row in reader:
        recArray.append(row)
        # print (row)
print(random.choices(recArray, k=2))
print(len(recArray))