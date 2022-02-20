"""
05.04.2021

CPU interprets instructions.

at the level of the hardware 0 = False = 0 volts and 1 = True = 3.5 volts (maybe)

a byte is 8 binary digits
a nyble is half a byte
a group of bytes is called a WORD
    usually words are either 4 bytes(32 bits) or 8 bytes(64 bits)

bits are counted from right to left starting at 0.

We are never converting to binary. EVERYTHING IS ALREADY BINARY

USEFUL BINARY VALUES THAT YOU WILL EVENTUALLY KNOW BY HEART
HEX     BINARY    DECIMAL
0       0000       0
1       0001       1
7       0111       7
F       1111       15
FF    1111,1111    255

"""

def my_bin(num: int) -> str:
    """
    Assume num in a positive integer
    """
    mask = 0b1
    values = []

    if num == 0:
        return "0b0"


    while num > 0:
        val = num & mask
        values.append('01'[val])
        num = num >> 1

    values.reverse()
    result = "0b" + "".join(values)
    return result

def log_2(num: int) -> int:
    """
    Assume num in a positive integer
    """
    mask = 0b1
    flag = 0
    ctr = 0

    while num > 0:
        val = num & mask
        if val == 1:
            flag = ctr
        ctr += 1
        num = num >> 1

    return flag

print(log_2(73))
print(my_bin(73))




""""""

