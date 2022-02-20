






def GR_scaling(file_name, no_headerlines):
    ''' '''
    with open(file_name, 'r') as myf:

        for i in range(no_headerlines):
            myf.readline() #gets past headers

        mags = []
        mylist = myf.readline().strip().split()
        myshortlist = mylist[1:5]

        for item in myshortlist:
            mags.append(int(item[0]))

        myDict = {mags[0]: [], mags[1]: [], mags[2]: [], mags[3]: []}
        myvalues_li = []
        for line in myf:
            
            myvalues_li = line.strip().split()

            for i in range(4):
                myDict[mags[i]].append(int(myvalues_li[i+1]))

        return(myDict)

myD = GR_scaling('worldwideEQstats.txt', 3)

M = []
N = []


for key in myD:
    M.append(key)
    sum = 0
    for i in range(len(myD[key])):
        sum += myD[key][i]
    N.append(sum/16)
    
print(M)
print(N)
    
        
        
        
    
    

#for key in myD:



