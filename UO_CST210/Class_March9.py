'''
CIS 210 FINAL EXAM PRACTICE CODE
'''





def parity(bitrep):
    p = 0
    for bit in bity:
        if bit == '1':
            p += 1
            print(bit)
    if p % 2 == 0:
        p = '0'
    else:
        p = '1'
    return p
p = '11100011'


def mycharct(s, c):
    cct = 0
    for char in s:
        if char == c:
            cct += 1
    return cct
    
def countd(astr):
    ctd = {}
    for item in astr:
        if item in ctd:
            ctd[item] += 1
        else:
            ctd[item] = 1
    print (ctd)
    countli = ctd.values()
    ct = max(countli)
    mli = []
    for item in ctd:
        if ctd[item] == ct:
            mli.append(item)
    return mli

def findRange(salesli):
    salesli.sort()
    low = salesli[0]
    high = salesli[-1]
    return (low, high)

def salesReport(salesli):
    low, high = findRange(salesli)
    print(f'Weekly Range: ${low * 100} - ${high * 100}\n')

    fw = 12
    print( f" {'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} \
{'Thu':<{fw}} {'Fri':<{fw}}")

    for sales in salesli:
        print(f'${(sales * 100 ):<{fw}}', end = '')
    return None

salesRe = ([4, 2, 3, 1, 2])










    
