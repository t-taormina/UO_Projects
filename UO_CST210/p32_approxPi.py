'''
CIS 210
Project 3-2: Approximating Pi

Author: Tyler Taormina

Credits: N/A


'''

import random
import math

def montePi (numDarts):
    ''' (int) -> float

    Returns an approximation of pi using the Monte
    Carlo algorithm.

    EXAMPLES:
    >>>montePi(100)
    3.24
    >>>montePi(1000)
    3.22
    >>>montePi(10000)
    3.11

    '''
    inCircle = 0
    

    for i in range(numDarts):
        x = random.random()
        y = random.random()
        
        lands_inCircle = isInCircle(x, y, 1)
        
        if lands_inCircle == True:
            inCircle += 1
        else:
            inCircle += 0
    
    mypi = inCircle / numDarts * 4
    return mypi

def isInCircle (x, y, r):
    '''(float, float, float) -> bool

    Returns true or false based on whether or not
    the the x and y point falls within the radius

    EXAMPLES
    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False 

    '''
    
    dist = math.sqrt (x**2 + y**2)

    if dist <= r:
        return True
    else:
        return False
    
        
def reportPi (numDarts, mypi):
    '''(int, float) -> str

    Returns a print out with a percent error calculation
    for the difference between the math library value
    for pi and an approximation for pi found using the
    monte carlo algorith.

    EXAMPLES
    >>>reportPi(100,3.04)
    With 100 iterations:
    My approximate value for pi is: 3.04
    Math lib pi value is: 3.141592653589793
    This is a 3.23 percent error.
    '''

    percent_error = (abs(math.pi - mypi)/ (math.pi) * 100)
    percent_error = round(percent_error, ndigits=2)
    print('With', numDarts, 'iterations:')
    print('My approximate value for pi is:', mypi)
    print('Math lib pi value is:', math.pi)
    print('This is a', percent_error, 'percent error.')
    print('')
    return None

    

def main():
    ''' reportPi comparison program driver. '''
    k = 1000
    mypi = montePi(k)
    reportPi(k, mypi)
    

main()

   
    
