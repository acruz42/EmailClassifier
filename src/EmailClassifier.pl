#!/usr/bin/perl

$count = 0;
$myBody = "";

foreach my $line(<>) {
	if ($line eq "\n" && $count != 2) {
		$count = $count + 1;
	}
	if ($count == 2) {
		$tag = substr($line,0,7);
		if ($tag ne "--_000_") {
			chomp $line;
			$myBody .= $line;
		}
		else {
			last;
		}
	}
}

system("echo \"$myBody\" > /home/groups3/testgr/EmailClassifierPrototype/testlog.txt");

system("python /home/groups3/testgr/EmailClassifierPrototype/EmailClassifier.py \"$myBody\"");

