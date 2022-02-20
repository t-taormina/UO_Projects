'''
CIS 210 Project 7-1: Who takes CIS 210?

Author: Tyler Taormina

Credits: NA

Description: Program analyzes data to determine the major with the most
students (i.e., the major mode),and the number of times each major code
appears in the file. Reports results. 


'''


def majors_readf(fname):
    '''
    (str) -> list

    Reads a file skipping the header lines.  Returns a list. 

    EXAMPLES:
    >>> majors_readf('majors.txt')
    ['PSY', 'PBA', 'JMS', 'BI', 'SDSC', 'ARCH', 'EXPL', 'CIS',
    'BADM', 'CIS', 'MCOM', 'CIS', 'PBA', 'ART', 'GS', 'PHYS',
    'EC', 'CIS', 'MJS', 'PHYS', 'GS', 'CIS', 'BI', 'CIS', 'CIS',
    'PHYS', 'MATH', 'EXPL', 'BI', 'CIS', 'CIS', 'CIS', 'BADM',
    'EXPL', 'PS', 'CIS', 'CIS', 'BADM', 'CIS', 'CIS', 'SPAN',
    'PHYS', 'EARD', 'ACTG', 'MATH', 'CINE', 'CIS', 'EXPL', 'MACS',
    'CIS', 'CIS', 'EXPL', 'CIS', 'SDSC', 'CIS', 'CIS', 'CIS', 'CIS',
    'CIS', 'CIS', 'CIS', 'PS', 'MACS', 'EC', 'EXPL', 'CIS', 'MACS',
    'CIS', 'EXPL', 'CIS', 'EXPL', 'BADM', 'CIS', 'PSY', 'CIS', 'CIS',
    'CIS', 'EXPL', 'CIS']
    '''
    
    with open(fname, 'r') as myf:
        for i in range(2):
            myf.readline() #get past headers (2 lines)

        majorsli = []
        for item in myf:
            major = myf.readline()
            majorsli.append(major[0:-1]) #gets rid of the new line code (\n)

    majorsli = majorsli[:-1] #removes empty string at the end of the list
    
    return majorsli
        
        
                        
def majors_analysis(majorsli):
    '''
    (list) -> tuple

    Returns a tuple containing a count of items in the list enetered
    as well as the mode of the list entered.

    EXAMPLES:
    >>> majors_analysis(majorsli)
    (['CIS'], 22)
    
    '''
    countDict = {}

    for item in majorsli:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    majors_ct = len(countDict.keys())
    
    countList = countDict.values()
    maxCount = max(countList)

    majors_mode = []
    for item in countDict:
        if countDict[item] == maxCount:
            majors_mode.append(item)
    return majors_mode, majors_ct
    


def majors_report(majors_mode, majors_ct, majorsli):
    '''
    (num, num, list) -> None

    Prints a report of the parameters entered and generates a frequency
    table. Returns None. 
    


    '''
    print(majors_ct,'majors are represented in CIS 210 this term.')
    print('The most represented major(s) this term are:',majors_mode[0])

    countDict = {}

    for item in majorsli:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    itemList = list(countDict.keys())
    itemList.sort()
    
    print('MAJOR', '     ', 'FREQUENCY')
    
    for item in itemList:     #prints frequency column in straight line
        if len(item) == 3:
            print(f'{item} ', '     ',  f' {countDict[item]:>5} ') #one space
        elif len(item) == 2:
            print(f'{item} ', '     ',  f'  {countDict[item]:>5} ') #two spaces
            
        else:
            print(f'{item} ', '     ',  f'{countDict[item]:>5} ') #no spaces

    return None 



def main():
    '''
    () -> None

    Calls: majors_readf, majors_analysis, majors_report

    Top level function for analysis of CIS 210 majors data.

    '''
    fname = 'majors.text'
    majorsli = majors_readf('majors.txt')
    majors_mode, majors_ct = majors_analysis(majorsli)
    majors_report(majors_mode, majors_ct, majorsli)
    return None

if __name__ == '__main__':
    main()
    
    
    
    

    
            
        
            
    
    


    



