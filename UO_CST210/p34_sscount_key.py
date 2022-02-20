'''
Find all substrings of a string (CS Circles Unit 8) - two solutions
CIS 210 Winter 2021 Project 3-4

Author: CIS 210

Credits: N/A
'''

import doctest

def sscount0 (needle, haystack):
    '''(str, str) -> int

    Given a "needle" string to search for in a "haystack" string,
    return the count of the number occurrences of the needle in
    the haystack.  Overlapping substrings are included.
    Uses string slice operation (only).
    
    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0('an', 'trans-Panamanian banana')
    6
    >>> sscount0('needle', 'haystack')
    0
    >>> sscount0('!!!', '!!!!!')
    3
    >>> sscount0('o', 'pneumonoultramicroscopicsilicovolcanoconiosis')
    9
    '''
    ctr = 0
    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+n] == needle:
            ctr += 1
    return ctr

def sscount1 (needle, haystack):
    '''(str, str) -> int

    Given a "needle" string to search for in a "haystack" string,
    return the count of the number occurrences of the needle in
    the haystack.  Overlapping substrings are included.
    Using string startswith method simplifies code a bit.
    
    >>> sscount1('sses', 'assesses')
    2
    >>> sscount1('an', 'trans-Panamanian banana')
    6
    >>> sscount1('needle', 'haystack')
    0
    >>> sscount1('!!!', '!!!!!')
    3
    >>> sscount1('o', 'pneumonoultramicroscopicsilicovolcanoconiosis')
    9
    '''
    ctr = 0
    for i in range(len(haystack)):
        if haystack[i:].startswith(needle):
            ctr += 1
    return ctr

#print(doctest.testmod())
