#!/usr/bin/perl

$count = 0;
$myBody = "";
$boundary = "";
$archive = "";


foreach my $line(<>) {
	if (substr($line,0,5) eq "Date:"){
		chomp $line;
		$date_line = $line;
		$date_line .= "\n";
		$archive .= $date_line;
	}
	if (substr($line,0,5) eq "From:"){
		chomp $line;
		$from_line = $line;
		$from_line .= "\n";
		$archive .= $from_line;
	}
	if (substr($line,0,8) eq "Subject:"){
		chomp $line;
		$subj_line = $line;
		$subj_line .= "\n";
		$archive .= $subj_line;
	}
	if ($line eq "\n" && $count != 2) {
		$count = $count + 1;
		next;
	}
	if ($count == 1 && $boundary eq "") {
		chomp $line;
		$boundary = $line;
	}
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

system("/usr/bin/python3 /home/groups3/testgr/MergerTest/email_archiver.py \"$archive\" 2>> /home/groups3/testgr/MergerTest/Debug/archiveErrors.txt");

system("/usr/bin/python3 /home/groups3/testgr/MergerTest/classification.py \"$myBody\" 2>> /home/groups3/testgr/MergerTest/Debug/nlpErrors.txt");

system("/usr/bin/python3 /home/groups3/testgr/MergerTest/autoReply.py 2>> /home/groups3/testgr/MergerTest/Debug/replyErrors.txt");

