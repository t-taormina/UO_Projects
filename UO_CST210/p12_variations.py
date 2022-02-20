'''
CIS 210 Project 1-2: Python Variations

Author: [Tyler Taormina]

Credits: [NA]

'''

def convert(i,j,k):
    '''
    (list of num) -> int

    Returns integer that combines the 3 digits of
    the parameter with an order of signifigance
    of "k,j,i"

    #EXAMPLES OF USE
    >>>convert(1,2,4)
    421
    >>>convert(1,0,0)
    1
    >>>convert(0,0,0)
    0
    
    '''
    i = i * 1
    j =  j * 10
    k = k * 100
    answer = i + j + k
    return answer

def add_digits(n):
    '''
    (int) -> int

    Returns the sum of the three digits that are entered
    into the parameter.

    #EXAMPLES OF USE
    >>>add_digits(123)
    6
    >>>add_digits(456)
    15
    '''
    x = n % 10
    n_1 = n // 10
    y = n_1 % 10
    n_2 = n_1 // 10
    z = n_2
    result = x + y + z
    return result


def add_digits2(x):
    '''
    (int) -> int

    Returns the sum of all all digits entered in the
    parameters.

    #EXAMPLES OF USE
    >>>add_digits2(1000101)
    3
    >>>add_digits2(12345)
    15

    '''

    counter = 0
    while x > 0:
        x_1 = x % 10
        x = x // 10
        
        counter += x_1
        
    return counter


def profit(n):
    '''
    (int) -> float

    Returns the profit after costs of a single show
    based on the number of attendees

    #EXAMPLES OF USE
    >>>profit(50)
    205.0
    >>>profit(2)
    -11.0
    
    '''
    money = n * 5
    cost = (n * .50) +  20
    total_profit = money - cost
    return total_profit

    
        
        
        
        
        
        
    
    
    
    


    
    
