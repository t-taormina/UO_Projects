'''
CIS 210 Project 4-2: Bugs, bugs, bugs

Author: Tyler Taormina

Credits: N/A

'''
import doctest
def my_averageBug(dataset):
    '''(str) -> float

    Returns average of values in input string values,
    but zeros do not count at all.  Return 0 if there
    is no real data.
    
    >>> my_averageBug('23')    #normal, no zeros
    2.5
    >>> my_averageBug('203')   #normal, a zero
    2.5
    >>> my_averageBug('0000')  #all zeros
    0
    >>> my_averageBug('1')     #single item string
    1.0
    >>> my_averageBug('05050505')  
    5.0
    '''
    count = 0
    total = 0
    for value in dataset:
        if value != '0':
            total += int(value)
 # use int to change string to integer
            count += 1
        else:
            total += int(value)
            count += 0
    if count == 0:
        avg = 0
        return avg
    else:
        avg = total / count
        return avg

print(doctest.testmod())
