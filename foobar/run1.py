#!/usr/bin/python



'''
Welcome to foobar version 1-325-g43507c9-beta (2020-05-16T03:14:38.702942)

Google has a code challenge ready for you.
Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on her space station. From here, you just might be able to subvert her plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

Warning! Your invitation may expire if you leave this page. Sign in to save progress and resume later.


Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme. 

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.



-- Python cases --
Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113


You survived a week in Commander Lambda's organization, and you even managed to get yourself promoted. Hooray! Henchmen still don't have the kind of security access you'll need to take down Commander Lambda, though, so you'd better keep working. Chop chop!
Submission: SUCCESSFUL. Completed in: 55 mins, 17 secs.





                                                                                                   @\
                                                                                          @@     @\~@
                                                                                         @%$@   % \~~@
                                                                                        @\\\\\% %))))))~@
                                                                                        @~~\\~@\\\\\\))@
                                                                                         @\\\\\\@ \\\)@
                                                                                        @~\~~~@ %\\@
                                                                                        @\~~\\\@ $$$@\
                                                                                       @@\\$\\\%@\%   @
                                                                                       @ ~\)))))\\\\    $@
                                                                                      @\\\))))@@@\\\    $@
                                                                         @@\\\\\\%\   \\%%\\))))@  @)\\    $@
                                                            \\\$@\\    @\\\\\\~~~\\\@@      \\))))@@@))\    @
                                                          \@\$  $@\ @@\\\~~~~~~~~~  %     )))))))))      ~ @
                                                        @        $@\\\\\\\~~~~~~~            ))))))       @
                                                        @$      @\\\\~~~~~~~~~~~                   $@@
                                                          @$  @@$@\\\\\~~~~~~~~~           ~~\%%@@@\\
                                                           @@@\\\\~~~~)~~~~~~~~              ~$
                                                               @\\\\\\\\\)))~~~~~~               $$$
                                                                @$)\\\\\\\\)~~~~~~     //$$$$$   ~~~$
                                                                @%%%))))))~~~~~~   \  /%%  @  ~~$$@
                                                                  @$$$$$$$$$$      \        @~~~@
                                                                   @%%%%%$$$ $$     @@$     \\@@
                                                                     @%%%%%%$$$$       \ @
                                                                         @@@@@@@@@@@@\\\\@
Level 1 complete
You are now on level 2
Challenges left to complete level: 2

Level 1: 100% [==========================================]
Level 2:   0% [..........................................]
Level 3:   0% [..........................................]
Level 4:   0% [..........................................]
Level 5:   0% [..........................................]
'''
import solution1


#235711131719
# so e.g. 3 should give, from 3rd char 71113, 

print(solution1.solution(3))
print(solution1.solution(4))
print(solution1.solution(5))
print(solution1.solution(100))
