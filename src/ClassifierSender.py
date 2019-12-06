#-------------------------------------------------------------------------------------------------
#This is the script that composes the reply email based on the senders email. The email is split
#into sentences and lemmatized using the stanfordnlp library. The lemmatized sentences are then
#fed to the model created in ModelConstructor.py which determines how closely each sentence
#matches our training data. If a sentences matches the training data closely enough the answer to
#the question detected is added to the response email. Once the original email has been parsed
#completely the response email is sent as a reply to the original email.
#-------------------------------------------------------------------------------------------------

username = #Insert Username here
password = #Insert Password Here

import pickle
import smtplib
import poplib
import sklearn
import stanfordnlp
import sys
import time
from sklearn.feature_extraction.text import CountVectorizer
from email.mime.text import MIMEText

classification = 0

#Get nessecary files and instantiate the model and nlp pipeline
features_file = "/home/groups3/testgr/EmailClassifier/src/Models/features.pkl"
model_file = "/home/groups3/testgr/EmailClassifier/src/Models/text_classifier_100"

# stanfordnlp.download('en', force=True)
nlp = stanfordnlp.Pipeline(lang='en')
doc = nlp(sys.argv[4])

with open(model_file, 'rb') as Mymodel:
    model = pickle.load(Mymodel)


vect = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open(features_file, "rb")))

#Parse and lemmatize the email body and put the lemmatized sentences into list X_One
X_One = []
output = ""
for i, sent in enumerate(doc.sentences):
	s = ""
	output = output + ("[Sentence {}]".format(i+1)) + "\n"
	for word in sent.words:
		if word.dependency_relation == "punct":
			s = s + word.text
		else:            
			s = s + " " + word.text
	s = s[1:]
	X_One.append(s)
	s = s + '\n'

#Use the model to predict the classification and determine the certainty of classification of 
#each sentence in X_One
X_vected = vect.transform(X_One)
classifications = model.predict(X_vected)

all_probs = model.predict_proba(X_vected)

#Find all the sentences with a classification probability higher than 85% and add the questions
#classification number to the true_class list
true_probs = []
true_class = []
max_classification = 0
i = 0
for probs in all_probs:
    index = classifications[i]
    true_probs.append(probs[index - 1])
    if probs[index - 1] >= .85:
        true_class.append(classifications[i])
    i = i + 1

max_prob = true_probs[0]
max_classification = classifications[0]
for i in range(1, len(true_probs)):
    if true_probs[i] > max_prob:
        max_prob = true_probs[i]
        max_classification = classifications[i]

	
#Establish contact with the perl script and fetch the MIME of the original email
port = 25

text = sys.argv[1]
messageID = sys.argv[2]
originalSubject = sys.argv[3]

#Parse the original sender of the email out of the MIME file so we can send the reply
receiver = ""
condition = False
for c in text:
	if c == "<":
		condition = True
		continue
	if c == ">":
		break
	if condition:
		receiver = receiver + c

sender = "testgr@cs.nmsu.edu"
subject = "Re: " + originalSubject

#Compose the message. The message is stored as a string list joined at the end.

text = []
text.append("<pre>\nThis is an automated reply from testgr@cs.nmsu.edu.\n\nWe've attempted to automatically identify your questions, and we got these results:\n\n")

for classification in true_class:
    if classification == 1:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification1.txt","r")
        for line in f:
            text.append(line)

    elif classification == 2:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification2.txt","r")
        for line in f:
            text.append(line)

    elif classification == 3:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification3.txt","r")
        for line in f:
            text.append(line)

    elif classification == 4:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification4.txt","r")
        for line in f:
            text.append(line)

    elif classification == 5:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification5.txt","r")
        for line in f:
            text.append(line)

    elif classification == 6:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification6.txt","r")
        for line in f:
            text.append(line)

    elif classification == 7:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification7.txt","r")
        for line in f:
            text.append(line)

    elif classification == 8:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification8.txt","r")
        for line in f:
            text.append(line)

    elif classification == 9:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification9.txt","r")
        for line in f:
            text.append(line)

    elif classification == 10:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification10.txt","r")
        for line in f:
            text.append(line)

    elif classification == 11:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification11.txt","r")
        for line in f:
            text.append(line)

    elif classification == 12:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification12.txt","r")
        for line in f:
            text.append(line)

    elif classification == 13:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification13.txt","r")
        for line in f:
            text.append(line)

    elif classification == 14:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification14.txt","r")
        for line in f:
            text.append(line)

    elif classification == 15:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification15.txt","r")
        for line in f:
            text.append(line)

    elif classification == 16:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification16.txt","r")
        for line in f:
            text.append(line)

    elif classification == 17:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification17.txt","r")
        for line in f:
            text.append(line)

    elif classification == 18:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification18.txt","r")
        for line in f:
            text.append(line)

    elif classification == 19:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification19.txt","r")
        for line in f:
            text.append(line)

    elif classification == 20:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification20.txt","r")
        for line in f:
            text.append(line)

    elif classification == 21:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification21.txt","r")
        for line in f:
            text.append(line)

    elif classification == 22:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification22.txt","r")
        for line in f:
            text.append(line)

    elif classification == 23:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification23.txt","r")
        for line in f:
            text.append(line)

    elif classification == 24:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification24.txt","r")
        for line in f:
            text.append(line)

    elif classification == 25:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification25.txt","r")
        for line in f:
            text.append(line)

    elif classification == 26:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification26.txt","r")
        for line in f:
            text.append(line)

    elif classification == 27:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification27.txt","r")
        for line in f:
            text.append(line)

    elif classification == 28:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification28.txt","r")
        for line in f:
            text.append(line)

    elif classification == 29:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification29.txt","r")
        for line in f:
            text.append(line)

    elif classification == 30:
        f = open("/home/groups3/testgr/EmailClassifier/src/ResponseTemplates/Classification30.txt","r")
        for line in f:
            text.append(line)

    text.append("\n\n")

text.append("\nIf your questions weren't answered to your satisfaction, please reply to this email with your inquiry and include the following line at the beginning of your email:\n--THIS DID NOT ANSWER MY QUESTIONS--\nThe graduate advisor will get back to you soon.\n\nIf your questions were answered to your satisfaction, please reply to this email with the string:\n--MY QUESTIONS WERE ANSWERED--\n</pre>")

txt = ''.join(text)

#Format the MIME message

msg = MIMEText(txt,'html')
msg['Subject'] = subject
msg['To'] = receiver
msg['From'] = sender
msg['In-Reply-To'] = messageID
msg['References'] = messageID
text1 = msg.as_string()

#message = 'Subject: {}\nIn-Reply-To: {}\nReferences: {}\n\n{}'.format(subject, messageID, messageID, text)
if max_prob >= .85:
	with smtplib.SMTP("smtp.cs.nmsu.edu", port) as server:
		server.login(username, password)
		server.sendmail(sender, receiver, msg.as_string())
		server.quit()
