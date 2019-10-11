import smtplib

port = 25

sender = "testgr@cs.nmsu.edu"
receiver = "acruz@cs.nmsu.edu"
message = "\n\nIf you can see this in your email then this was a success.\n\n"

with smtplib.SMTP("smtp.cs.nmsu.edu", port) as server:
   server.login("testgr","Dunedain03\\")
   server.sendmail(sender, receiver, message)