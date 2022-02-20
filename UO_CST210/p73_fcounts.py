'''
CIS 210 Project 7-3: Inspecting Files

Author: Tyler Taormina

Credits: N/A

Description: Program reads a text file and counts the number of lines,
characters, and words in the text file. Prints a frequency table
with words and the number of occurences for each word.

'''
import string

def fcounts(fname):
    '''
    (str) -> None

    Description: Program reads a text file and counts the number of lines,
    characters, and words in the text file. Prints a frequency table
    with words and the number of occurences for each word.

    EXAMPLES:
    >>> fcounts('demo.txt')
    The number of lines in file demo.txt is: 3
    The number of characters in file demo.txt is: 18
    Word count for file demo.txt:
    WORD     FREQUENCY
    hello     2
    world     1
    


    '''
    lineCtr = 0
    charCtr = 0
    wordList = []
    countDict = {}
    clean_wordList = []

    with open(fname, 'r') as myf:     #opens file and returns list with words, punctuation, and a line count
        for line in myf:
            lineCtr += 1
            wordList += line.split()
    
    wordCtr = len(clean_wordList)     #counts words in the cleaned word list
    
    for word in wordList:     #counts number of characters in each word including punctuation
        charCtr = charCtr + len(word)

    for word in wordList:     #removes puntucation, white space, new line code, and puts all words in lower case 
        clean_wordList.append(word.lower().strip(string.punctuation))     #for accurate occurences count. Returns Clean list.
        
    for word in clean_wordList:
        if word in countDict:     #keeps track of how many times each word occurs
            countDict[word] = countDict[word] + 1
        else:
            countDict[word] = 1

    itemList = list(countDict.keys())
    itemList.sort()
    
      


    print('The number of lines in file', fname, 'is:', lineCtr)
    print('The number of characters in file', fname, 'is:', charCtr)
    print('Word count for file ' + fname +':')
    print('WORD', '   ', 'FREQUENCY')

    for item in itemList:
        print(f'{item} ', f'   {countDict[item]}')
    return None

def main():
    '''
    () -> None

    Calls: fcounts

    Program driver for fcounts function

    '''
    fcounts('demo.txt')
    return None

if __name__ == '__main__':
    main()
        
    
