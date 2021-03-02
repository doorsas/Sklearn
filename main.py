import pandas as pd
import matplotlib.pyplot  as plt
import math
import numpy as np
import json
from sklearn.model_selection import train_test_split

# https://youtube.com/watch?v=M9Itm95JzL0&feature=share

file_name = 'books_small.json'

reviews = []
bandymai = []

class Sentiment:
    NEGATIVE = 'NEGATIVE'
    NEUTRAL = 'NEUTRAL'
    POSITIVE = 'POSITIVE'


class Bandymas:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()
        self.zodis = self.text.split()

    def get_sentiment(self):
        if int(self.score) <= 2 :
            return Sentiment.NEGATIVE
        elif int(self.score) == 3 :
            return Sentiment.NEUTRAL
        else:
            return Sentiment.POSITIVE




class Review:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()


    def get_sentiment(self):
        if int(self.score) <= 2 :
            return Sentiment.NEGATIVE
        elif int(self.score) == 3 :
            return Sentiment.NEUTRAL
        else:
            return Sentiment.POSITIVE


with open(file_name) as f:
    for line in f:
        review = json.loads(line)
        # print (rewiew['reviewText'])
        reviews.append(Review(review['reviewText'], review['overall']))

with open(file_name) as f:
    for line in f:
        review = json.loads(line)
        # print (rewiew['reviewText'])
        bandymai.append(Bandymas(review['reviewText'] + '10',review['overall'] + 20 ))



print (reviews[5].score)



# print (reviews[2].sentiment, reviews[2].score)

print (bandymai[3].text, bandymai[3].zodis[:3])