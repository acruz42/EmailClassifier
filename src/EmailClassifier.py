import fileinput
import stanfordnlp
import smtplib
import os, sys

f = open("PythonTest.txt","w+")
f.write(sys.argv[1])
f.close()
