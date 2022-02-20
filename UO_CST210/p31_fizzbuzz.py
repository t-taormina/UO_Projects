'''
CIS 210
Project 3-1: Fizzbuzz

Author: Tyler Taormina

Credits: N/A

Fizzbuzz is a game where numbers are counted from 1 through x.
Anytime a number is divisble by 3, the player should say "fizz".
Anytime a number is divisble by 5, the player should say "buzz".
If a number is divisible by both 3 and 5, the player should
say "fizzbuzz". Players alternate counting until number x is
reached.

'''

def fb(n):
    '''(int) -> str

    Enter int "n" in the parameters. Returned is fizzbuzz (see above)
    game played up to the integer entered in the parameter.

    EXAMPLES
    >>>fb(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz

    '''
    
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ('fizzbuzz')
            continue 

            
        elif i % 3 == 0:
            print ('fizz')
            continue 

        
        elif i % 5 == 0:
            print ('buzz')
            continue 

        
        else:
            print (i)
            continue
            
    
        return None
    

