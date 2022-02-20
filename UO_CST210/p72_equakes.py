'''
CIS 210 Project 7-2: Earthquake Watch

Author: Tyler Taormina

Credits: N/A

Description: This program will determine the number of earthquakes,
and the mean, median, and mode of the magnitudes of the earthquakes,
and then report this information.

'''


import p61_data_analysis as da
import doctest


def equake_readf(fname):
    '''
     (str) -> list

    Reads a file skipping the header lines.  Returns a list with
    new line code and empty strings removed. 

    EXAMPLES:
    >>> equake_readf('p72-50.txt')
    ['5.2', '5.1', '6', '5.9', '5.6', '5.7', '5', '5', '5.2', '5.1',
    '5.4', '5.2', '5.6', '5.18', '5.1', '5', '5', '5.6']
    
    '''
    with open(fname, 'r') as myf:
    
        magli = []
        myf.readline() #mvoes past the header
        
        for line in myf:
            vals = line.strip().split(',')
            mag = float(vals[4])
            magli.append(mag)
            
    return (magli)

magnitudes = equake_readf('p72-50.txt')

def equake_analysis(magnitudes):
    '''
    (list) -> tuple

    Takes in a list and uses the list to compute mode, median,
    and mean values. Returns a tuple that stores those values.

    EXAMPLES:
    >>> equake_analysis(magnitudes)
    (5.326666666666666, 5.2, [5.0])

    '''

    mean_equakes = da.mean(magnitudes)
    median_equakes = da.median(magnitudes)
    mode_equakes = da.mode(magnitudes)
    return (mean_equakes, median_equakes, mode_equakes)



def equake_report(magnitudes, mmm, minmag):
    '''
    (list, tuple, float) -> None

    Takes in a list, a tuple, and a float, and prints out
    a report of these values. Returns None

    EXAMPLES:
    >>> equake_report(magnitudes, mmm, minmag)
    Number of Earthquakes: 18
    Mean of Earthquake Magnitudes: 5.326666666666666
    Median of Earthquake Magnitudes: 5.2
    Mode of Earthquake Magnitudes: [5.0]
    SIZE       FREQUENCY
    5.0        4
    5.1        3
    5.18        1
    5.2        3
    5.4        1
    5.6        3
    5.7        1
    5.9        1
    6.0        1
    
    '''
    eqMean, eqMedian, eqMode = mmm 
    titlew = 40
    print('EARTHQUAKE DATA ANALYSIS'.center(titlew))
    print('100 Years Ago to Present'.center(titlew))
    print('250km Centered at Eugene, OR'.center(titlew))
    print()
    print(f'There have been {len(magnitudes)} earthquakes with magnitude {minmag} or higher over the past 100 years.')
    print(f'Mean magnitude is: {eqMean:2f}')
    print(f'Median magnitude is: {eqMedian}')
    print(f'Mode(s) magnitude is: {eqMode}')
    print()
    
    da.ft(magnitudes)
    
    return None


def main():
    '''
    ()-> None
    
    Calls:  equake_readf, equake_analysis,equake_report

    Top level function for earthquake data analysis.

    Returns None.
    '''
    fname = 'p72-25.txt'
    minmag = 2.5
    #fname = 'p72-50.txt'
    #minmag = 5.0
    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(emags, mmm, minmag)
    return None

if __name__ == '__main__':
    main()

                        



