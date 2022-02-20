''' 
Prior programming experience quiz.
CIS 210 Project 1-1 Hello-Quiz Solution

Author: [Tyler Taormina]

Credits: [N/A]

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket.py for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    '''
    Type contract: (str, str) -> str
    
    Description: Retruns greeting message based on parameters
    entered in q1
    
                    #EXAMPLES OF USE
    >>>q1(onTime)
    'Hello!'
    >>>q1(absent)
    'Is anyone there?'
    >>>q1()
    'Better late than never.'

    '''
    
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''
    (int) -> bool
    
    Return true or false for whether or not a child is
    considered a dependent based on the age and salary
    of the child that is entered in q2

                    #EXAMPLES OF USE
    >>>q2(14,2000)
    True
    >>>q2(19,15000)
    False
    >>>q2(17,31000)
    False
    
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''
    () -> int
    
    Returns a result for p that is reached by comparing
    the p and q values

    >>>q3()
    6
    
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    '''
    (float) -> float
    
    Returns the balance of an account after a deposit
    while counting the number of times a deposit is made.
    
    >>>q4(5,10)
    15
    >>>q4(0,20)
    20
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''
    (list of numbers) -> int
 
    Returns a count of the numbers that are greater
    than or equal to zero in the list.
     
    #EXAMPLES OF USE
    >>> q5([0, 1, 2, 3, 4, 5])    
    6
    >>> q5([0, -1, 2, -3, 4, -5])
    3
    '''
    
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6():
    '''
    () -> int
    
    Returns value of p that is double the initial value.
    
    #EXAMPLES OF USE
    >>>q6()
    2
    '''
    i = 0
    p = 1
    while i < 4:
        i = 1
        p = p * 2
        i += 1

    return p








    
    
     
        
    
