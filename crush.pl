#!/usr/local/bin/hmperl


# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
# This is a hard one, you basically have to find the number(s) that appear MOST often across all sets
# e.g. 5-9999
#      981-2100
#      2005
#      2003-3000
#      8200-9500
# ... then 1005 appears 4X...do I need a binary search implementation?
# so first iterate through all, find range is 5-9999, find midpoint, say that's 4999
#  count # of sets that has values < 4999 vs >?  So we get 4 <, 2 right
#  then we get to divide by 2, 2500 ish, count # < 4, right 1
#  1250, < 2, 1250-2500 is 4
# and so on...this should work, but ugh I hate coding binary searches :)
# ... oh but the values can differ, that makes it more difficult...I'd have to weigh those
# so probably I need to sort these, from highest weight to lowest weigh?

my $line1 = <STDIN>;
my ($size, $iterations) = split(/\s+/, $line1);
my %resultHash;
my $curmax = 0;

my @sets;

foreach my $i (1.. $iterations) {  
    my $operations = <STDIN>;
    my ($start, $end, $add) = split(/\s+/, $operations);
    #$set[$i]->{min} = $start; $set[$i]->{max} $end;  
    foreach my $suffix ($start..$end) {
       $resultHash{"$suffix"} += $add;
       if ($resultHash{"$suffix"} > $curmax) {
            $curmax = $resultHash{"$suffix"};
       }
    }
}

print $curmax;
