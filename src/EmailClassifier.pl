#!/usr/bin/perl

#-------------------------------------------------------------------------------------------------
#This is the master control script for the entire project. When the testgr account recieves an 
#email the email server passes the email to this script via the .forward file. This script then 
#runs the files that are directly related to the email classification. It also contains most of 
#the code needed for creating the archive files.
#-------------------------------------------------------------------------------------------------

$count = 0;
$myBody = "";
$boundary = "";
$archive = "";
$sender = "";
$process_messageID = 0;
$bypassCondition = 0;


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
		$sender .= $from_line;
	}
	#Get the subject from the MIME and add it to the archive
	if (substr($line,0,8) eq "Subject:"){
		chomp $line;
		$subj_line = $line;
		$subj_line .= "\n";
		$archive .= $subj_line;
	}
	#get Message-ID
	if (substr($line,0,11) eq "Message-ID:"){	
		$process_messageID = 1;
		next;
	}
	if ($process_messageID == 1){
		chomp $line;
		$id_line = "Message-ID:";
		$id_line .= $line;
		$id_line .= "\n";
		$archive .= $id_line;
		$process_messageID = 0;
	}
	if (substr($line,0,13) eq "Thread-Topic:"){
		chomp $line;
		$topic_line = $line;
		$topic_line .= "\n";
		$archive .= $topic_line;
	}
	if (substr($line,0,13) eq "Thread-Index:") {
		chomp $line;
		$index_line = $line;
		$index_line .= "\n";
		$archive .= $index_line;
	}
	if ($line eq "\n" && $count != 2) {
		$count = $count + 1;
		next;
	}
	#Set up the reader to get the email body
	if ($count == 1 && $boundary eq "") {
		chomp $line;
		$boundary = $line;
		$archive .= "Body:\n";
	}
	if ($count == 2) {
		chomp $line;
		if ($line eq "--THIS DID NOT ANSWER MY QUESTIONS--" || $line eq "--MY QUESTIONS WERE ANSWERED--") {
			$bypassCondition = 1;
			last;
		}
		if ($line ne $boundary) {
			$myBody .= $line;
			$archive .= $line;
			$archive .= "\n";
		}
		else {
			last;
		}
	}
}

$message_ID = substr($id_line,12);
$subject = substr($subj_line,9);

if ($bypassCondition == 0) {
	#Call the archiver
	system("/usr/bin/python3 /home/groups3/testgr/EmailClassifier/src/EmailArchiver.py \"$archive\" 2>> /home/groups3/testgr/EmailClassifier/src/Debug/archiveErrors.txt");

	#Call the classifier and auto reply script
	system("/usr/bin/python3 /home/groups3/testgr/EmailClassifier/src/ClassifierSender.py \"$sender\" \"$message_ID\" \"$subject\" \"$myBody\" 2>> /home/groups3/testgr/EmailClassifier/src/Debug/classificationErrors.txt");
}
