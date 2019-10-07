import smtplib, ssl

port = 465 # For SSL

sender = "testgr@cs.nmsu.edu"
receiver = "adorian@nmsu.edu"
message = "\n\nIf you can see this in your email then this was a success.\n\n"

# Crate a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("cs.nmsu.edu", port, context=context) as server:
   server.login("testgr@cs.nmsu.edu","alRcKyVmaKuS")
   server.sendmail(sender, receiver, message)