'''
CIS 210 Project 6-1: Data Analysis

Author: Tyler Taormina

Credits: NA

Description: Functions for caluclating mean, mode, and median are used
in collaboration to gather insights into sets of data. Uses functions
ft and genFt to print and store data insights in a dictionary. 

'''


def is_even(n):
    ''' (num) -> bool

    Returns a boolean that is True if the number entered
    in the parameter is even, and False if it is odd

    EXAMPLES:
    >>> is_even(2)
    True

    >>> is_even(3)
    False

    >>> is_even(0)
    True
    
    '''
    if (n) % 2 == 0:
        return True
    else:
        return False

    

def mean(aList):
    ''' (list) -> float

    Returns the mean of the list that is entered in the parameter

    EXAMPLES:

    >>> mean([1, 1, 1])
    1.0

    >>>  mean([1, 2, 2, 2, 1])
    1.6

    >>> mean([0])
    0.0
    
    '''
    index = 0
    for word in aList:
        aList[index] = float(word)
        index += 1
        
    mean = sum(aList) / len(aList)
    return mean



def median(aList):
    ''' (list) -> float

    Returns the median of the list entered in the parameter

    EXAMPLES:

    >>> median([1, 1, 1])
    1

    >>> median([1, 2, 2, 3])
    2.0

    >>> median([0])
    0
    
    '''
    copyList = aList[:]    #copy of the list
    copyList.sort()
    if is_even(len(copyList)) == True:   #even list
        rightMid = len(copyList) // 2
        leftMid = rightMid - 1
        median = (copyList[leftMid] + copyList[rightMid]) / 2
    else:   #odd list
        mid = len(copyList) // 2
        median = copyList[mid]
    return median



def mode(aList):
    ''' (list) -> int

    Returns the mode of the list entered in the parameter

    EXAMPLES:

    >>> mode([1, 1, 2])
    [1]

    >>> mode([1, 2, 2, 2])
    [2]

    mode([1, 1, 2, 2])
    [1, 2]
    
    '''
    countDict = {}

    for item in aList:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    countList = countDict.values()
    maxCount = max(countList)

    modeList = []
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)
    return (modeList)


    


def ft(aList):
    ''' (list) -> dict

    Returns a dictionary with the list entered in the parameter
    used as the keys, and the number of occurences of each item
    in the list used as the values

    EXAMPLES:

    > ft([1, 3, 3, 2])
    SIZE     FREQUENCY
    1        1
    2        1
    3        2

    > ft([1, 1, 2, 2, 3, 3])
    SIZE     FREQUENCY
    1        2
    2        2
    3        2
    
    '''
    countDict = {}

    for item in aList:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
            
    itemList = list(countDict.keys())
    itemList.sort()

    print('SIZE', '     ', 'FREQUENCY')
    
    for item in itemList:
        print(item, '      ',  countDict[item])

    genTable = genFt(itemList, countDict)
    
    return genTable

   

def genFt(aList, Dict):
    '''(list, dict) -> dict

    Returns a dictionary with a list used as keys and
    the number of occurences of each key used as the values.

    EXAMPLES:
    > genFt([1, 1, 2, 2], {'1': 2, '2': 2})
    {1: 2, 2: 1}

    > genFt([0], {0 : 1})
    {0: 1}

    '''
    

    newDict = {}
    for item in aList:
        newDict[item] = Dict[item]
    return newDict



def main():
    ''' DRIVER FOR EQUAKES DATA ANALYSIS '''
    
    freqTable = ft(equakes)
    print('FREQUENCY TABLE DICTIONARY:')
    print(freqTable)
    print('The mean of this data set is:', mean(equakes))
    print('The median of this data set is:', median(equakes))
    print('The mode of this data set is:', mode(equakes))
    


equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3, 2.6, 2.9, 4.9, 2.5,
         4.8, 4.2, 2.6, 4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1, 4.1,
         2.8, 5.8, 2.5, 3.9, 4.8, 2.9, 2.5, 4.9, 5.0, 2.5, 3.2,
         2.6, 2.7, 4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7, 3.3, 3.0,
         4.4, 2.7, 5.7, 2.5, 5.1, 2.5, 4.4, 4.6, 5.7, 4.5, 4.7,
         5.1, 2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3, 6.0, 3.0, 5.3,
         2.7, 4.3, 5.4, 4.4, 2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
         2.5,4.9, 4.9, 2.5, 4.8, 3.1, 4.9, 4.4, 6.6, 3.3, 2.5,
         5.0, 4.8, 2.5, 4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6, 2.7,
         2.9, 2.7, 2.9, 3.3, 2.8, 3.1, 2.5, 4.3, 3.2, 4.6, 2.8,
         4.8, 5.1, 2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5, 4.5, 4.5,
         2.8, 4.7, 4.6, 4.6, 5.1, 4.2, 2.8, 2.5, 4.5, 4.6, 2.6,
         5.0, 2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2, 3.2, 5.2, 2.8,
         3.2, 2.6, 5.3, 5.5, 2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
         2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7, 2.7, 4.9, 3.0, 4.9,
         4.7, 2.6, 4.6, 2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9, 2.5,
         5.1, 3.3, 2.5, 4.7, 2.5, 4.1, 3.1, 4.6, 2.8, 3.1, 6.3]

if __name__ == '__main__':
    main()
