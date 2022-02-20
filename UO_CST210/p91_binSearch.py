

import random
import time



def isIn(seq, t):
    '''
    (sequence, item) -> boolean

    '''
    for item in seq:
        if item == t:
             return True

    return False

'''
def createSeq(n):
    ''' '''
    seq = []
    for i in range(n):
        seq.append(int(n * random.random()))
    return seq

'''

def isIntest(function):
    ''' '''
    tests = [((1, 2, 3), 3, True),
             ('hello', 'i', False),
             ((), 75, False),
        ]
    for test in tests:
        result = function(test[0],test[1]) == test[2]
        if result == True:
            print('passed!')
        else:
            print('failed!')

    return None

isIntest(isIn)
            
   
''' Takes AVG Time
N = 100000     #length of the list of random integers

repeats = 100     # number of times the seq search is completed

start = time.time()
for r in range(repeats):
    seq = []
    for i  in range(N):
        seq.append(int(N*random.random()))

    t = random.randint(0, N)
    result = isIn(seq, t)
end = time.time()

avg_time = (end - start)/repeats
print('Average time is:', avg_time)
'''






nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 20 , 11, 13, 15, 16, 17, 18, 19, 20,
        21, 22, 23)
target = 15

''' ********RECURSION*********'''

def factR(n):
    ''' '''
    print(n)
    if n == 0:
        return 1
    else:
        return n * factR(n-1)
result = factR(4)
print(result)
