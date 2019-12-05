#-------------------------------------------------------------------------------------------------
#This script handles the actual creation of the email archive file and the writing of the archive
#file. It takes the $archive variable created in EmailClassifier.pl and writes it to a text file
#named Email#X.txt in the archive directory where X is the number higher than the previous highest
#number.
#-------------------------------------------------------------------------------------------------

import sys
import os

#Looks through the archive to find the file with the current largest number and creates a file 
#with a number one larger. Race conditions should not occur in this code.

i = 1
savedFile = "Email#" + str(i) + ".txt"
checked = False

while checked is False:
	try:
		fil = open("/home/groups3/testgr/MergerTest/EmailArchive/"+savedFile,"x")
		checked = True
	except:
		i = i + 1
		savedFile = "Email#" + str(i) + ".txt"

#Write the archive content generated in the perl script to the file created in the previous step
fil = open("/home/groups3/testgr/MergerTest/EmailArchive/"+savedFile,"w")
fil.write(sys.argv[1])
fil.close()

