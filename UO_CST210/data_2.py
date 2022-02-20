'''
CIS 210 Project 6-1: Data Analysis

Author: Tyler Taormina

Credits: NA

Description

'''


def is_even(n):
    '''   '''
    if n % 2 == 0:
        return True
    else:
        return False
    

def mean(aList):
    ''' '''
    mean = sum(aList) / len(aList)
    return mean


def meadian(aList):
    ''' '''
    copyList = aList[:]    #copy of the list
    copyList.sort()
    if is_even(copyList) == True:   #even list
        rightMid = len(copyList) // 2
        leftMid = rightMid - 1
        median = (copyList[leftMid] + copyList[rightMid]) / 2
    else:   #odd list
        mid = len(copyList) // 2
        median = copyList[mid]
    return median


def mode(aList):
    ''' '''
    countDict = {}

    for item in aList:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    countList = countDict.values()
    maxcount = max(countList)

    modeList = []
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)

    return modeList


def ft(aList):
    ''' '''
    countDict = {}

    for item in aList:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
            
    itemList = list(countDict.keys())
    itemList.sort()

    print('SIZE', 'FREQUENCY')
    newDict = {}
    
    for item in itemList:
        newDict[item] = countDict[item]
    return newDict

