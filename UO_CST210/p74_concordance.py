'''
CIS 210 Project 7-4: File Concordance

Author: Tyler Taormina

Credits: N/A

Description: Reads a file and returns a concordance of the file
with each line(s) of the file where the word appears.

'''
import string

def fconcordance(fname):
    '''
    (string) -> None

    Returns a report with the words in the file and the lines
    of the file where the word appears.

    EXAMPLES:
    >>> fconcordance('demo.txt')
    hello appears in lines [1, 3]
    world appears in lines [2]

    ''' 

    wordList = []
    conDict = {}
    line_ctr = 0

    with open(fname, 'r') as myf:     #opens file and returns list with words, punctuation, and a line count
        for line in myf:
            wordList = line.split()
            line_ctr += 1
            
            for word in wordList:
                word = word.strip(string.punctuation).lower()
                if word not in conDict:
                    conDict[word] = []
                if line_ctr not in conDict[word]:
                    conDict[word].append(line_ctr)

        for k in conDict:
            print(k, 'appears in lines', conDict[k])
            
    return None

                    
                
                                
            
        
            
            
            
          
        

    
