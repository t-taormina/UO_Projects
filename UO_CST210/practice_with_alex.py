'''
Write a function, mysqrt, which will return an approximate square root for a positive integer.
mysqrt will have two parameters: n, a positive integer to find the square root of, and k,
the number of times the iterative square root approximation process should run. The function
should use the equationgiven below to determine the approximate square root of n, and return
(note: not print) this result. (P2c -Approximate Square Root)

xk + 1 = .5 * (xk + n/xk)
x0 = 1

'''
import doctest

def mysqrt(n, steps):
    ''' (int, int) -> float

    Returns an approximation of the square root of "n"

    EXAMPLES:
    >>> mysqrt(4, 1)
    2.5

    >>> mysqrt(4, 3)
    2.000609756097561

    >>> mysqrt(4, 100)
    2.0

    '''
    xk = 1

    for i in range(steps):
        guess = .5 * (xk + n/xk)
        xk = guess
        
    return xk 
        
print(doctest.testmod())
