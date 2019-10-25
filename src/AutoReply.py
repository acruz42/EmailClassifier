import smtplib

port = 25

sender = "testgr@cs.nmsu.edu"
receiver = "millerd@nmsu.edu"
subject = "Email Classifier Automated Reply"
text = "\n\nThis is an automated reply from testgr@cs.nmsu.edu.\n\n"

message = 'Subject: {}\n\n{}'.format(subject, text)

with smtplib.SMTP("smtp.cs.nmsu.edu", port) as server:
    server.login("testgr", "Dunedain03\\")
    server.sendmail(sender, receiver, message)
    server.quit()
