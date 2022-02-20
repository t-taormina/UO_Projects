import random
import math

def montePi(numDarts):
    ''' (int) -> float

    '''
    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)

        if d <= 1:
            inCircle += 1
