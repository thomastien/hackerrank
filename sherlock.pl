#!/usr/local/bin/hmperl

my $cases = <STDIN>;
my $i = 0;
my $ontime = 0;

last if $i> 20;
while ($i < $cases) {
   my $digits = <STDIN>;
   $i=$i+1;
   
   # The goal is, say given 20
   # we keep subtracting 5s until we get a # divisible by 3
   # so e.g. 20%3 = 2, keep going
   # 15%3 = 0, so we want 55555,55555,55555,33333
   
   my $remaining_chars = $digits;
   my $next_flag = 0;

   while ($remaining_chars%3 != 0) {
   	if ($remaining_chars < 3) {
		$next_flag=1;
		print "-1\n";
		last;
   	}
      $remaining_chars = $remaining_chars - 5;
   }
   next if $next_flag;
   my $num_3s = $digits - $remaining_chars;
   my $num_5s = $remaining_chars || 0;
   #print $num_3s .' is number 3s vs ' . $num_5s . ' as 5s' . "\n";
   print '5' x $num_5s  . '3' x $num_3s, "\n"; 
}
   



#my $foo = '10019-2134 foobar\'s road.; cat/etc/passwd';
#
#$foo =~ s/[^\w\s-_'.,]//g;
#print $foo;
