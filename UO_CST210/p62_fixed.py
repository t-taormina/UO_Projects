'''
More Automated Testing and Debugging
CIS 210 Project 6-2 Winter 2021

Author: Tyler Taormina

Credits: NA

Functions need to be tested and debugged & 
write a function to automate testing of calendar function (project 5-1)
'''
import doctest
from p51_printCalendar import *

def bigSalesBug(sales_list):
    '''(list) -> number

    Returns sum of all sales for amounts at or over $40,000.
    sales_list has the record of all the sales.

    >>> bigSalesBug([40_000, 45.67, 19_000.0, 25000, 100_000])
    140000.0

    >>> bigSalesBug([40000, 40_000, 40000.00])
    120000.0

    >>> bigSalesBug([1, 0, 1, 0.0])
    0.0
    
    '''
    total = 0.00
    for sales in sales_list:
        if sales >= 40_000:       # changed greater than sign to a greater than or equal to sign
            total = total + sales #typo (ttotal) fixed and written as (total)
    return total                  # indentation error. Moved return outside of the for-loop

buggy = [ 40_000, 45.67, 19_000.0, 25000, 1 ]


############

def findRangeBug(salesli):
    '''(list) -> tuple

    Returns largest and smallest number in non-empty salesli.
    (Note that Python has built in funcs max and min
    to do this, but not using them here, so we can
    work with the list directly.)

    >>> findRangeBug([40000, 45.67, 19000.0, 25000, 100000])
    (45.67, 100000.0)

    >>> findRangeBug([1, 2, 3])
    (1.0, 3.0)

    >>> findRangeBug([1, 1, 1])
    (1.0, 1.0)

    >>> findRangeBug([0 ,0 ,0])
    (0.0, 0.0)
    
    '''
    salesli.sort() #sort function updates the list in place and returns none. 
    
    low = float(salesli[0])
    high = float(salesli[-1])
   
    return low, high

def salesReportBug(salesli):
    '''(list) --> None

    Prints report of sales totals for each day of week (salesli)
    and range of per-day sales. salesli is non-empty - 0 sales
    for any day are reported as 0.

    >>> salesReportBug([40000, 45.67, 19000.0, 25000, 100000])
    Weekly Range: $45.67 - $100,000.00
    
    Mon          Tue          Wed          Thu          Fri         
    $40,000.00   $45.67       $19,000.00   $25,000.00   $100,000.00  
    '''
    #calculate and report low and high sales
    sorted_salesli = salesli.copy()     #copy of list that will change to a sorted list once used in findRangeBug function.
    low, high = findRangeBug(sorted_salesli)
    print(f'Weekly Range: ${low:,.2f} - ${high:,.2f}\n')

    #print daily report header
    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")

    #report on sales per day from list data
    for sales in salesli:               #keep original salesli in proper order in order to accurately display
        print(f'${float(sales):<{fw},.2f}', end='')   #the total sales on each day of the week
        
    return None



def test_calendar():
    ''' () -> str

    Returns a print out calendar for each of the test cases.

    VISUALLY INSPECT CALENDAR PRINTOUT TO CONFIRM TEST CASES

    '''
    test_sets = [(2, 2021), (2, 2022), (1, 1), (1, 3000), (5, 1994), (1, 2022) ]

    for tests in test_sets:
        print(calendar(tests[0], tests[1]))
    
    
    #print(doctest.testmod())
