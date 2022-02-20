'''
Key items in this code are the sorting dictionary in the first function (tempD)

'''



days = ['Mo', 'Tu', 'We', 'Th']
temps = [ 55, 23, 42, 44]

def tempD(x_list, y_list):
    ''' '''
    day_temp_Dict = {}
    for item in range(len(days)):
        day_temp_Dict[x_list[item]] = y_list[item]
    return day_temp_Dict


dd = tempD(days, temps)
    

    
        
def counter(alist):
    ''' '''
    counter = 0
    
    for item in alist:
        counter += 1
    return counter
count = counter(temps)
print(count)

def 

        
