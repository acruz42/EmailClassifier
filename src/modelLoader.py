#This is a proof of concept script that loads the model generated in the Classifier script and runs some 
#basic test using it.
import pickle
import numpy
#import sklearn
'''
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
'''

#Generate the testing questions
X = ['This is not a question.', 'Should this one be a question?', 'After I arrive what should I do?']
print (X)

for i in range(len(X)):
    print (X[i])

#Load the model
#model = LogisticRegression()
with open('text_classifier_100', 'rb') as training_model:
    model = pickle.load(training_model)


#Fit the testing data to the model and predict the test question group
vect = CountVectorizer()
X_vected = vect.fit_transform(X)
y = model.predict(X_vected)
y2 = model.predict_proba(X_vected)

#Print results
for i in range(len(X)):
    print ("X is" + X[i] + ", Predicted " + y[i] + ", Probability " + y2[i])

