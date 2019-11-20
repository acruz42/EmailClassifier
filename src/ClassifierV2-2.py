import pandas as pd
import io
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle

from google.colab import files
uploaded = files.upload()
#dataset = pd.read_csv('C:\FinalFileLocation.csv')

dataset = pd.read_csv(io.BytesIO(uploaded['EmailQ3.csv']))

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

with open('text_classifier_100', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

import pickle
import sklearn


with open('text_classifier_100', 'rb') as Mymodel:
    model = pickle.load(Mymodel)

X_One = ['What is the GPA I need to be a grad student at NMSU?']
#Using old vect with fitted data instead of a new fit transform
#vect = CountVectorizer()
X_vected = vect.transform(X_One)

y_new = model.predict(X_vected)

print()


#for i in range(len(X)):
#    print ("X is" + X[i] + ", Predicted " + y[i])
