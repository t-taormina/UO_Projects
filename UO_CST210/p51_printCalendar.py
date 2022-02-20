'''
CIS 210 Project 5-1: Calendar

Author: Tyler Taormina

Credits: NA

Prints out a calnedar of the month given the month and year desired.

'''

from datetime import *
month_days = '31 28 31 30 31 30 31 31 30 31 30 31'
months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'


def month_start(month,year):
    ''' (int, int) -> int

    Returns the index of the day of the week
    that the first day of the month falls on
    in a given year.

    EXAMPLES OF USE:
    >>> month_start(4,2021)
    4

    >>> month_start(1, 2028)
    6

    >>> month_start(3, 1996)
    5
    
    '''
    start = date(year, month, 1)
    week_day = start.isoweekday() % 7
    return week_day
   

    


    
def calendar(month, year):
    '''(int, int) -> str
    
    Returns a printed calendar of the desired month in a given year.

    EXAMPLES OF USE:

    >>> calendar(2,2021)
        Feb 2021 
    Su Mo Tu We Th Fr Sa 
        1  2  3  4  5  6 
     7  8  9 10 11 12 13 
    14 15 16 17 18 19 20 
    21 22 23 24 25 26 27 
    28

    >>> calendar(2, 2050)
         Feb 2050 
    Su Mo Tu We Th Fr Sa 
           1  2  3  4  5 
     6  7  8  9 10 11 12 
    13 14 15 16 17 18 19 
    20 21 22 23 24 25 26 
    27 28 
    
    '''
    week_day = month_start(month, year)

    daysInMonth = month_days.split(' ')[month -1]
    
    month = months.split(' ')[month-1]
    days = 'Su Mo Tu We Th Fr Sa'

    print(f'{month:>8} ', end ='')
    print(f'{year:>2} ')
    print(f'{days:>2} ')

    start = '   ' * (week_day)
    
    print(f'{start}', end ='')

    for day in range (int(daysInMonth)):
        print(f'{day + 1:>2} ', end= '')
        if (week_day + day + 1) % 7 == 0:
            print()
    print()
    
    
           



