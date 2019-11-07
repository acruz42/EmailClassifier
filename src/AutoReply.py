import smtplib
import sys

port = 25

text = sys.argv[1]

mail = ""
condition = False
for c in text:
	if c == "<":
		condition = True
		continue
	if c == ">":
		break
	if condition:
		mail = mail + c

sender = "testgr@cs.nmsu.edu"
receiver = mail
subject = "Email Classifier Automated Reply"
text = "\n\nThis is an automated reply from testgr@cs.nmsu.edu.\n\n"

message = 'Subject: {}\n\n{}'.format(subject, text)

with smtplib.SMTP("smtp.cs.nmsu.edu", port) as server:
	server.login("testgr", "")
	server.sendmail(sender, receiver, message)
	server.quit()
