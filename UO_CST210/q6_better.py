def q6_better():
    '''
    () -> int
    
    Returns value of p that is double the initial value.
    
    #EXAMPLES OF USE
    >>>q6()
    2
    '''
    i = 0
    p = 1
    for i in range(1):
        i = 1
        p = p * 2
        i += 1

    return p



def q6_final(n,m):
    '''
    (int, int) -> int
    
    Returns value of "n" raised to an exponent "m"
    
    #EXAMPLES OF USE
    >>>q6_final(2,2)
    4
    >>>q6_final(4,1)
    4
    '''
    result = 0

    for i in range(2):
        result = n**m
        i += 1
    return result



def add_digits2a_better(n):
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
    
    result = 0
    
    for i in range(3):
         x = n % 10
         n = n // 10
         result += x
         
    return result


def add_digits2b(x):
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
                # I would not use a for loop in this situation
                #because we do not know the number of digits
                #that will be entered into the parameters.
                #A while loop should be used in this situation.
    counter = 0
    while x > 0:
        x_1 = x % 10
        x = x // 10
        
        counter += x_1
        
    return counter

