'''
CIS 210 Project 5-2: Parity Bit

Author: Tyler Taormina

Credits: NA

'''

def encode(letter):
    '''(str) -> str

    Returns an encoded version of the binary representation of
    the character entered in the parameter by adding a parity
    bit to the binary sequence. 

    EXAMPLES OF USE:
    >>> encode('a')
    '10b1100001'

    >>> encode('z')
    '10b1111010'

    >>> encode('p')
    '10b1110000'

    '''
    
    binary_rep = bin(ord(letter))
    parity_ch = parity(binary_rep)
    return parity_ch + binary_rep
      

def parity(bitrep):
    ''' (str) -> str

    Returns a str of '1' or '0' based on the amount of
    1's found in the binary sequence. If there is an
    odd number of 1's, a one is added. If there is an
    even number of 1's, a zero is added.

    EXAMPLES OF USE:
    >>> parity('0b111000')
    '1'

    >>> parity('0b110011')
    '0'

    >>> parity('0b111111')
    '0'

    '''
    ctr = 0
    for i in bitrep:
        if i == '1':
            ctr += 1
    if ctr % 2 == 0:
        return '0'
    else:
        return '1'
          

def decode(pletter):
    '''(str) -> str

    Returns the character indicated by the binary sequence
    after removing the parity bit. Returns asterisk if there
    is an error.

    EXAMPLES OF USE:
    >>> decode('10b1110000')
    'p'

    >>> decode('10b1100001')
    'a'

    >>> decocce('10b111001')
    '*'
    
    '''
    payload = pletter[1:]
    parity_check = parity(payload)
    if parity_check == pletter[0]:
        Raw_Value = int(payload, 2)
        return chr(Raw_Value)
    else:
        return '*'
    
def main():
    ''' Driver for decode and encode funtions'''

    
    word = 'cat'
    for letter in word:
        print(decode(encode(letter)), end='')
    print()

if __name__ == '__main__':
    main()
    
    



    
    
    

    
            
    
    
