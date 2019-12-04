#This is the master control script for the entire project. When the testgr account recieves an email this
#file is called and runs the other nessecary files. It also contains most of the code needed for creating
#the archive files.

#!/usr/bin/perl

$count = 0;
$myBody = "";
$boundary = "";
$archive = "";


foreach my $line(<>) {
	#Get the date from the MIME and add it to the archive
	if (substr($line,0,5) eq "Date:"){
		chomp $line;
		$date_line = $line;
		$date_line .= "\n";
		$archive .= $date_line;
	}
	#Get the sender from the MIME and add it to the archive
	if (substr($line,0,5) eq "From:"){
		chomp $line;
		$from_line = $line;
		$from_line .= "\n";
		$archive .= $from_line;
	}
	#Get the subject from the MIME and add it to the archive
	if (substr($line,0,8) eq "Subject:"){
		chomp $line;
		$subj_line = $line;
		$subj_line .= "\n";
		$archive .= $subj_line;
	}
	#Set up the reader to get the email body
	if ($line eq "\n" && $count != 2) {
		$count = $count + 1;
		next;
	}
	if ($count == 1 && $boundary eq "") {
		chomp $line;
		$boundary = $line;
	}
	#Get the body of the email from the MIME and add it to the archive
	if ($count == 2) {
		chomp $line;
		if ($line ne $boundary) {
			$myBody .= $line;
			$archive .= $line;
			$archive .= "\n"
		}
		else {
			last;
		}
	}
}

#Call the archiver
system("/usr/bin/python3 /home/groups3/testgr/MergerTest/email_archiver.py \"$archive\" 2>> /home/groups3/testgr/MergerTest/Debug/archiveErrors.txt");

#Call the classifier
system("/usr/bin/python3 /home/groups3/testgr/MergerTest/classification.py \"$myBody\" 2>> /home/groups3/testgr/MergerTest/Debug/nlpErrors.txt");

#Call the auto reply script
system("/usr/bin/python3 /home/groups3/testgr/MergerTest/autoReply.py 2>> /home/groups3/testgr/MergerTest/Debug/replyErrors.txt");

