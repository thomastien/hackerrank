#!/usr/local/bin/hmperl


my $count = 0;


for my $i (1..10){
	$count += $i if ($i%3 == 0 || $i%5 == 0);
	print "after $i it was $count\n";
}
print $count;
