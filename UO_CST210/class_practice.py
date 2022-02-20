'''
p12_variations-W21

Author: Tyler K Taormina

Credits: N/A

Write some functions that manipulate integers, return a value
and practice writing docstrings.

'''

def convert(i,j,k):
    '''(int,int,int) -> int

    Return an integer from i,j,k where i
    is the least signicant digit (ones place).
    j is the tens place, and k is the hundreds
    place.

    >>>convert(1,2,3)
    321
    >>>convert(1,0,0)
    1
    >>>convert(0,0,1)
    100
    

    '''
    return k * 100 + j * 10 + i * 1

    
def twice(x):
    '''

    '''
    result = 2*x
    print(result)
    return None



def thrice(x):
    '''

    
    '''
    result = 3*x
    return result



def sum(num_list,length):
    ''' '''
    i = 0
    total = 0
    
    while i < length:
        total += length[i]
        i += 1
        
    return total

    
    
    












