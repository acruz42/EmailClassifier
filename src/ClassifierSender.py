

import pickle
import smtplib
import sklearn
import stanfordnlp
import sys
from sklearn.feature_extraction.text import CountVectorizer
from email.mime.text import MIMEText

classification = 0

"""
f = open("/home/groups3/testgr/MergerTest/Debug/nlpSuccess.txt","w+")
f.write("SUCCESS\n")
f.close()
"""

features_file = "/home/groups3/testgr/MergerTest/Models/features.pkl"
model_file = "/home/groups3/testgr/MergerTest/Models/text_classifier_main_model"

# stanfordnlp.download('en', force=True)
nlp = stanfordnlp.Pipeline(lang='en')
doc = nlp(sys.argv[4])

with open(model_file, 'rb') as Mymodel:
    model = pickle.load(Mymodel)

vect = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open(features_file, "rb")))

f = open("/home/groups3/testgr/MergerTest/Debug/nlpOutput.txt","w+")
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
	f.write(s)

f.close()

#X_One = ['Who is in charge of Teaching Assistants?','I was wondering how I should go about becoming an RA.','How is your evening?','Hope everything is going okay.']
#Using old vect with fitted data instead of a new fit transform
X_vected = vect.transform(X_One)
classifications = model.predict(X_vected)

all_probs = model.predict_proba(X_vected)
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

if max_prob < .85:
	max_classification = 0
	
"""
i = 0
with open("/home/groups3/testgr/MergerTest/Debug/classifyOutput.txt","w+") as f:
	for c in classifications:
		if true_probs[i] > .85:
			f.write('Category for question ' + str(i)  + ': ' + str(c) + '\n')
			i = i + 1
"""
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

#Compose the message. The message is stored as a string in text.

text = "\nThis is an automated reply from testgr@cs.nmsu.edu.\n\n"

for classification in true_class:
    if classification == 1:
        text = text + "The basic TODOs are:\n\t1. Attend the orientation session organized by graduate school. If you do not know the orientation information, please contact gradinfo@nmsu.edu.\n\t2. Read this FAQ page carefully.\n\t3. Please read the NMSU catalog. In particular, under the “Degree” tab, please find the degree requirement for your program.\n\t4. Make an appointment with the department graduate advisor to discuss your study plan. Before talking with the department graduate advisor, please first (i) read this FAQ page carefully and (ii) read your degree requirement in the catalog carefully. When you talk with the department graduate advisor, you will know your deficiency courses. You will also discuss your options of courses in the first two semesters.\n\t5. Go to see Ivan or Mark and get a CS email address with cs.nmsu.edu and get an access code to the graduate student lab. The information of Ivan and Mark can be found from https://www.cs.nmsu.edu/wp/people/staff/.\n\t6. Attend the department’s graduate student orientation which is organized by the Computer Science Graduate Student Organization (CSGSO, gradrep@cs.nmsu.edu, https://www.cs.nmsu.edu/~gradrep/)."

    elif classification == 2:
        text = text + "The current department graduate advisor is Dr. Huiping Cao (hcao at cs dot nmsu dot edu)."

    elif classification == 3:
        text = text + "If you are a newly admitted student and you are not given any TAship before your arrive, you miss the deadline to apply for TA in your first semester. However, you can get TA in other semesters. The details of applying for TA can be found from https://www.cs.nmsu.edu/wp/student-information/grad-students/graduate-financial-aid/.\n\nThe procedure of applying for TAs:\n\t1. New students send an email to gradcs at cs dot nmsu dot edu to denote that they want to apply for teaching assistantship.\n\t2. Deadline to send the TA application email: (1) mid of November for students that will start their first semester at CS in the coming Spring semester and (2) mid of April for students who will start their first semester at CS in the coming Fall semester.\n\t3. Decisions about TAs to new students are generally made at (1) the end of November for students that will start their first semester at CS in the coming Spring semester and (2) the end of April for students who will start their first semester at CS in the coming Fall semester."

    elif classification == 4:
        text = text + "The decision of RA is made by individual professors. You can check each professor’s research interest and contact the professor with whom you want to work with."

    elif classification == 5:
        text = text + "Please read the NMSU catalog and find the information in the “Courses” tab."

    elif classification == 6:
        text = text + "All the course credit transfer must be requested at the time of arrival. If you get a grade lower than B, your course credit cannot be transferred. If you get a grade of B or above B, you need to show the course syllabus to the department graduate advisor. The department graduate advisor decides whether your course credits can be transferred. If the graduate advisor cannot make the decision, the graduate advisor will contact the professors who teach those courses. These professors may need to talk with you to make this decision. If the graduate advisor/professor thinks that your course credit cannot be transferred and you insist on getting it transferred, then you need to take a challenge test (time/location agreed by both parties) and ask the professor to grade it. If you manage to get a B, then your course credit can be transferred.\n\nIf the graduate advisor/professor thinks that your course credit cannot be transferred and you insist on getting it transferred, then you need to take a challenge test (time/location agreed by both parties) and ask the professor to grade it. If you manage to get a B, then your course credit can be transferred.A."

    elif classification == 7:
        text = text + " Please contact the graduate advisor to ask for suggestions about which courses to take. Not every course is offered every semester. Thus, if you are new to the department, you are encouraged to talk with the general graduate advisor first."

    elif classification == 8:
        text = text + "lease contact the course instructor (not the graduate advisor) who will be teaching that course to ask for approval. Please note that if you do not meet the course prerequisites, the course instructor (not the graduate advisor) decides whether you are allowed to take that course or not."

    elif classification == 9:
        text = text + "Please talk with the department graduate advisor by making an appointment."

    elif classification == 10:
        text = text + "The steps are:\n\n\t1. Fill in the “program of study form”, which can be downloaded from https://gradschool.nmsu.edu/graduate-forms/, and denote that it is coursework only.\n\t2. Ask the department graduate advisor, the department head, and the college dean to sign the form.\n\t3. Send the signed program of study form to graduate school.\n\t4. Form a committee to have a final exam. The committee should consist of two CS faculty members, where one faculty member will serve as committee chair and the other one is a regular committee member, and one external (non-CS) faculty member, who will serve as dean’s representative. The student chooses the committee.\n\t5. Decide the time to have the final exam by coordinating with the committee members.\n\t6. The student reserves a room to have the final exam by working with the CS admin.\n\t7. Fill in the “Masters Final Examination Form”, which can be downloaded from https://gradschool.nmsu.edu/graduate-forms/, and have it signed properly. Send this form to graduate school.\n\t8. Final oral exam. The exam is generally two hours or until the committee feels it is sufficient to decide. Note that the exam covers the four areas (rubrics can be found from Page two of https://www.cs.nmsu.edu/wp/wp-content/uploads/2019/10/gradAssessmentForm2019.pdf). You will be asked questions on one course for each category. "

    elif classification == 11:
        text = text + "No. RA/TA can only be awarded to students taking at least 9 graduate credits."

    elif classification == 12:
        text = text + "Yes. However, they are not counted towards your graduate program (MS or PhD)."

    elif classification == 13:
        text = text + "A D-grade course will be used in your GPA calculation, thus it affects your GPA. However, a D-grade course will NOT be counted towards your graduate program. For example, if you get a D in C S 510, which is a required course for your Master’s program. In order for it to be counted for your program, you need to retake it and get a higher grade."

    elif classification == 14:
        text = text + "Yes. You will be assigned with deficiency courses."

    elif classification == 15:
        text = text + "There is no specific deadline for the applications. The department generally processes applications within about 1-2 weeks after we receive your complete application package and submit the recommendation to graduate school. The graduate school may take some time to issue the formal admission letter. The graduate school can be reached through email gradinfo AT nmsu.edu."

    elif classification == 16:
        text = text + "Please have the following documents ready before you apply.\n\t1) your transcripts (undergraduate or graduate (if available))\n\t2) Personal statement\n\t3) English test results (TOEFL/IELTS) for international students\n\t4) Names of three reference providers\n\nThen, please go to the application website (https://gradschool.nmsu.edu) and use the “Apply to Graduate School” button.\n\nPlease note that the computer science department does not require any hardcopy of your documents. Thus, please do NOT submit any hardcopy of the materials to the computer science department. If you are requested to submit hardcopy of any documents, please make sure to ask for the right address and the right person to send your documents to."

    elif classification == 17:
        text = text + "When you submit your applications on line (see the previous question), you need to submit the names and email addresses of three referees. Once you provide your referees’ information, your referees will automatically receive an email from our system. They can use the link in the email to upload your recommendation letters.\n\nPlease do NOT send any hardcopy of the recommendation letters (if not requested). Please do NOT email your recommendation letters (if not requested). "

    elif classification == 18:
        text = text + "Please find the GPA requirements from https://catalogs.nmsu.edu/nmsu/graduate-school/#admissionstext."

    elif classification == 19:
        text = text + "No. Graduate Record Examinations are not required"

    elif classification == 20:
        text = text + "Please find the university calendar from https://academiccalendar.nmsu.edu."

    elif classification == 21:
        text = text + " Please find the requirement on English exams from https://isss.nmsu.edu/index-8/. Note that students from some countries can have their TOEFL/IELTS exams waived. You can find the list of such countries from https://isss.nmsu.edu/index-8/."

    elif classification == 22:
        text = text + "Please find the requirement on English exams from https://isss.nmsu.edu/index-8/. Note that students from some countries can have their TOEFL/IELTS exams waived. You can find the list of such countries from https://isss.nmsu.edu/index-8/."

    elif classification == 23:
        text = text + "The degree requirements can be found from https://catalogs.nmsu.edu/nmsu/arts-sciences/computer-science/#degreestext. To get a degree, you need to finish the required courses and the total number of credits. Thus, the time depends on you. For example, the Master’s in Computer Science degree requires 33 credits. If you take 9 credits per semester, then you will need at least 4 semesters to finish your degree. If you need to take English courses or other deficiency courses, the time will be longer. "

    elif classification == 24:
        text = text + "The tuition and fee information can be found from https://uar.nmsu.edu/tuition-fees/tuition-rates/. For example, for non-resident, the rate per Credit (1 – 14 Credits) when enrolled in >6 credits in Spring 2020 is 985.70. Then, the total cost of one semester taking 9 credits will be 8871.3. The total cost of finishing a degree then depends on the total number of credits that you need to finish."

    elif classification == 25:
        text = text + "If you have any questions when you apply for our graduate program (Master’s or PhD), please send emails to gradcs AT cs.nmsu.edu."

    elif classification == 26:
        text = text + "There is a change of admission semester form which can be found on the graduate school website, https://gradschool.nmsu.edu/graduate-forms/. You need to complete the form and send it to gradcs AT cs.nmsu.edu. The department will process it and forward it to Graduate School. The Graduate School will update your enrollment semester. When it has gone through, you will receive an updated admission letter indicating the new semester."

    elif classification == 27:
        text = text + "Please go to https://hr.nmsu.edu/employment/salary/ and click the “Graduate Assistants Salary Table” link."

    elif classification == 28:
        text = text + "The department selects excellent applicants to give them teaching assistantships (TA). We will make the decisions in April for applications that we received in the Spring semesters and in November for applications that we received in the Fall semester. If you are not selected to get TA, you are welcome to contact department faculty members for a potential graduate research assistantship (RA). Even you are not offered TA/RA in the first semester, both graduate teaching and research positions are possible in future semesters if you show strong academic performance."

    elif classification == 29:
        text = text + "The Office of International Student and Scholar Services (ISSS, isss@nmsu.edu, https://isss.nmsu.edu/) will process your I-20 form for Visa application. Please contact the ISSS office if you have any questions related to this."

    text = text + "\n\n"

text = text + "If your question wasn't answered to your satisfaction please contact the graduate advisor.\n"

#Format the new MIME file and send the composed message

msg = MIMEText(text)
msg['Subject'] = subject
msg['To'] = receiver
msg['From'] = sender
msg['In-Reply-To'] = messageID
msg['References'] = messageID

#message = 'Subject: {}\nIn-Reply-To: {}\nReferences: {}\n\n{}'.format(subject, messageID, messageID, text)

if max_classification > 0:
	with smtplib.SMTP("smtp.cs.nmsu.edu", port) as server:
		server.login("testgr", "Dunedain03\\")
		server.sendmail(sender, receiver, msg.as_string())
		server.quit()
