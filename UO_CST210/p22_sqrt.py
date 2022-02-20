''' 
CIS 210
Project 2-2: Approximate Square Root

Author: Tyler Taormina

Credits: N/A


'''

def main():
    '''
    Square root comparison program driver.
    
    '''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)

    return None

def mysqrt(n, k):
    '''(int, int) -> float

    Returns an approximate square root of "n"
    that is computed "k" times with each
    iteration becoming more accurate.

    #EXAMPLES OF USE
    >>>mysqrt(25, 5)
    5.000000000016778
    >>>mysqrt(25, 10)
    5.0
    >>>mysqrt(100, 10)
    10.0
    >>>mysqrt(10000, 8)
    100.0071330766507
    '''
    guess = n/2
    
    for i in range(k):
        guess = .5 * (guess + (n/guess))
            
    return guess


    
    
    

import math
    
def sqrt_compare (num, iterations):
    ''' (int, int) -> float
    
    Returns a comparison of the mysqrt function
    and the math library function with a print out
    of each and the percent error, if any, found
    between the two results.

    >>>sqrt_compare(4, 2)
    For 4 using 2 iterations: 
    mysqrt value is: 2.0
    math lib sqrt value is: 2.0
    This is a 0.0 percent error.

    >>>sqrt_compare(10000, 8)
    For 10000 using 8 iterations: 
    mysqrt value is: 100.00713307665073
    math lib sqrt value is: 100.0
    This is a 0.01 percent error.
    
    '''
    approx_value = mysqrt(num, iterations)
    actual_value = math.sqrt(num)
    percent_error = (abs(actual_value - approx_value)/(actual_value) * 100)
    percent_error = round(percent_error, ndigits=2)
    print ('For', num, 'using', iterations, 'iterations: ')
    print ('mysqrt value is:', approx_value)
    print ('math lib sqrt value is:', actual_value)
    print('This is a', percent_error, 'percent error.')
    print('')
    
    
    
    
