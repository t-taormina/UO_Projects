'''
Testing and debugging
CIS 210 Project 4-2 Winter 2021

Author: Tyler Taormina

Credit: N/A

Functions need to be tested.
'''
import doctest

def ratsBug(weight, rate):
    '''(number, number) -> tuple

    Return number of weeks it will
    take for a rat to weigh 1.5 times
    as much as its original weight
    (weight > 0) if it gains at rate (rate > 0).

    >>> ratsBug(10, .1)     # normal
    (16.1, 5)
    >>> ratsBug(1, .5)      # edge - just one week
    (1.5, 1)
    >>> ratsBug(10, 0)
    Improper rate has been entered. Please enter a rate that is > 0
    >>> 
    '''
    weeks = 0
    new_weight = weight * 1.5   #new variable that calculates 1.5x the original weight 
    if rate <= 0:               #add if statement in case of improper parameters
        print('Improper rate has been entered. Please enter a rate that is > 0')
    else:
        while weight < new_weight: #add new variable in loop to maintain proper control 
            weight += weight * rate
            weeks += 1 #changed variable from (wks) -> (weeks) 

        weight = round(weight, 1)

        return (weight, weeks)



def countSeqBug(astr):
    '''(str) -> int

    Returns the length of the longest recurring
    sequence in astr

    >>> countSeqBug('abccde')  # normal  	
    2
    >>> countSeqBug('')        # edge - empty string
    0
    >>> countSeqBug('aabbb')
    3
    >>> countSeqBug('!')
    1
    >>> countSeqBug('abababab')
    1
    '''
    if len(astr) != 0:
        prev_item = astr[0]
        dup_ct = 1
        high_ct = 1
    
    else:
        high_ct = 0
        dup_ct = 0
          
    for i in range(1, len(astr)):
        if astr[i] == prev_item:
            dup_ct += 1
               
        else:
            prev_item = astr[i] 
            
        if dup_ct > high_ct:
            high_ct = dup_ct
            dup_ct = 1 #indented to fall within the if statement in order to reset the duplicate count
                       
    return high_ct



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
        if value != '0': #using values that are not equal to zero
            total += int(value)
            count += 1#indent so it falls within if statement

    if count == 0: #add if statement to avoid dividing by zero 
        avg = 0
        return avg
    
    else:          #add else statement to return the average
        avg = total / count
        return avg

    

print(doctest.testmod())
