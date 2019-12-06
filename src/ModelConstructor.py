#-------------------------------------------------------------------------------------------------
#Pass as argument the full file path for the .csv file to use for training. The file should follow
#the same format as the default file found in the repository.
#This is the file that creates the model out of the dataset. The dataset is imported from the
#google doc as a .csv file. The csv is then fed to the RandomForestClassifier which creates the 
#training model.
#-------------------------------------------------------------------------------------------------
import pandas as pd
import io
import sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle

#Import the dataset from the google doc as a csv
from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv(io.BytesIO(uploaded[sys.argv[1]]))

#Split the dataset into questions(X) and categories(Y). The dataset is then trained using the #RandomForestClassifier
X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values
vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X)
with open("features.pkl","wb") as picklefile:
    pickle.dump(vect.vocabulary_,open("features.pkl","wb"))

XTrain, xTest, yTrain, yTest = train_test_split(X_train_dtm, y, test_size=0.3, random_state=0)
classifier = RandomForestClassifier(n_estimators=250, random_state=0)
classifier.fit(XTrain, yTrain)

yPred = classifier.predict(xTest)
theScore = accuracy_score(yTest, yPred)
print(theScore)

with open('text_classifier_100', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)
