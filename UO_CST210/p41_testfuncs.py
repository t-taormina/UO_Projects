'''
CIS 210 Project 4-1: Testing

Author: Tyler Taormina

Credits: N/A

'''

from p34_sscount_key import *

def test_sscount(f, args, expected_result):
    '''(function, str, num) -> None

    test_sscount will automate testing of sscount0 and sscount1

    EXAMPLES
    >>> test_sscount(sscount0, 'sses assesses', 2)
    testing sscount0
    Checking sses assesses...
    its value 2 is correct!

    >>> test_sscount(sscount1, 'sses assesses', 2)
    testing sscount1
    Checking sses assesses...
    its value 2 is correct!

    >>> test_sccount(sscount1, 'a bbb', 1)
    testing sscount1
    Checking a bbb...
    its value 1 is incorrect
    
    '''
    space_index = str.find(args, ' ')
    needle = args[:space_index]
    haystack = args[space_index + 1:]

    test = f(needle, haystack)

    if test == expected_result:
        return None           #Code removed from this line. See bottom of file. 

    else:
        print('testing', f.__name__)
        print('Checking', args,'...')
        print('its value', expected_result,' is incorrect.')

    return None
    


def main():
    ''' Program driver for test_sscount '''
    test_sscount(sscount0, 'sses assesses', 2)
    test_sscount(sscount1, 'sses assesses', 2)

    test_sscount(sscount0, 'an trans-Panamanian banana', 6)
    test_sscount(sscount1, 'an trans-Panamanian banana', 6)

    test_sscount(sscount0, 'needle haystack', 0)
    test_sscount(sscount1, 'needle haystack', 0)

    test_sscount(sscount0, '!!! !!!!!', 3)
    test_sscount(sscount1, '!!! !!!!!', 3)

    test_sscount(sscount0, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount(sscount1, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)

    test_sscount(sscount0, '', 0)
    test_sscount(sscount1, '', 0)

    test_sscount(sscount0, 'a ', 0)
    test_sscount(sscount1, 'a ', 0)

    test_sscount(sscount0, ' abc', 0) #returns an incorrect finding because there is no substring 
    test_sscount(sscount1, ' abc', 0) #to look for inside of the string

    test_sscount(sscount0, 'a a', 1)
    test_sscount(sscount1, 'a a', 1)

    return None

main()




'''
print('testing', f.__name__)
print('Checking', args, '...')
print('its value', expected_result,' is correct!')
'''


# ^ This is the code that I removed in order to make the test function run silently. 
#test_sscount will now only print a message when the test fails. 



    
    
