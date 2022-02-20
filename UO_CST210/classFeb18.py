


def GR_scaling(file_name, no_headers):
    ''' '''
    with open(file_name, 'r') as myf:

        for i in range(no_headers):
            myf.readline() #get past header lines

        mags = []

        mylist = myf.readline().strip().split()
        myshortlist = mylist[1:-1]

        for item in myshortlist:
            mags.append(int(item[0]))

        myDict = {mags[0]: [], mags[1]: [], mags[2]: [], mags[3]: []}
        #for line in myf:
            #myDict[
            
        
        print(myDict)


GR_scaling('demo.txt', 3)
