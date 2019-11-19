import pickle
import sklearn

model = LogisticRegression()
with open('filePath', 'rb') as training_model:
    model = pickle.load(training_model)

X = ['This is not a question.', 'Should this one be a question?', 'After I arrive what should I do?']
vect = CountVectorizer()
X_vected = vect.fit_transform(X)
y = model.predict(X_vected)

for i in range(len(X)):
    print ("X is" + X[i] + ", Predicted " + y[i])

