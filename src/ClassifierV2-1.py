# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bCJ-qEpzdvC8naL7ydMNfAkPEd5QPQbL
"""

import pandas as pd
import io
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

from google.colab import files
uploaded = files.upload()
#dataset = pd.read_csv('C:\FinalFileLocation.csv')

dataset = pd.read_csv(io.BytesIO(uploaded['EmailQ.csv']))

X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X)

XTrain, xTest, yTrain, yTest = train_test_split(X_train_dtm, y, test_size=0.3, random_state=0)

classifier = RandomForestClassifier(n_estimators=10, random_state=0)
classifier.fit(XTrain, yTrain)

yPred = classifier.predict(xTest)
theScore = accuracy_score(yTest, yPred)
print(theScore)

tst = "What is the min GPA I need?"
tst2 = vect.fit_transform(tst)
myPred = classifier.predict(tst)