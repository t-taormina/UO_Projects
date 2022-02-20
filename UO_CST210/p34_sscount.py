'''
CIS 210
Project 3-4: Python Strings/Counting

Author: Tyler Taormina

Credits: N/A

Function returns the number of times that a substring occurs
in another  string.
'''

import doctest


def sscount0(needle, haystack):
    '''(str, str) -> int

    Returns the number of occurrences of a substring
    inside a string.

    EXAMPLES
    >>>sscount0('sses','assesses')
    2
    >>>sscount0('!!!', '!!!!!')
    3
    >>>sscount0('i','tapwater')
    0
    >>>sscount0('ik','23456')
    0
    
    '''
    ctr = 0
    len1 = len(needle)
    len2 = len(haystack)
    for i in range(len2 - len1 + 1):   #Max num of poss occurrences.
        if (haystack[i:i+len1] == needle ): #Breaks string into substring size
            ctr += 1                        #and looks for match
    return ctr

                   
def sscount1(sub,string):
    '''(str, str) -> int

    Returns a count of the number of times that a substring
    occurs inside of a string.

    EXAMPLES
    >>>sscount1('sses', 'assesses')
    2
    >>>sscount1('!!!', '!!!!!')
    5
    >>>sscount1('k', 'lllll')
    0
    >>>sscount1('j', '23456')
    0

    '''
    cnt = 0
    for i in range(len(string)- len(sub) + 1):  #max num of poss occurrences.
        if string.startswith(sub,i,i+len(sub)):  #matching substring with  
            cnt += 1                            #len of substring size portion
            i += 1                          # of the str. 
        else:
            i += 1   #If there is no match, starting point i progresses through                          
    return cnt         #the str.     


print(doctest.testmod())    #can we go over doctest more? 
    
    
            
        
    

            
