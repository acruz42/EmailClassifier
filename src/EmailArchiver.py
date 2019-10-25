import sys
import os

i = 1
savedFile = "Email#" + str(i) + ".txt"
while True:
	if not os.path.isfile("/home/groups3/testgr/MergerTest/EmailArchive/"+savedFile):
		break
	i = i + 1
	savedFile = "Email#" + str(i) + ".txt"


fil = open("/home/groups3/testgr/MergerTest/EmailArchive/"+savedFile,"w")
fil.write(sys.argv[1])
fil.close()

