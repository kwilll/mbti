## Text Analysis using the Natural Language Toolkit (NLTK)

import csv
import nltk
from nltk.tokenize import word_tokenize

with open('mbti.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for field in row:
            tokens = word_tokenize(field)
            print(tokens)
