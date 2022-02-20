


def fileread(fname):
    ''' '''
    stateDict = {}
    key_list = []
    value_list = []
    percentage_list = []
    index = 0
    

    with open(fname, 'r') as myf:
        myf.readline() #past header
        for line in myf:
            line = line.strip().split(',')
            key_list.append(line[0])
            value = int(line[-1]) / int(line[1])
            percentage = value
            percentage_list.append(percentage)

    
        for item in key_list:
            stateDict[item] = percentage_list[index]
            index += 1

    sorted_vaccines = sorted(stateDict.items(), key = lambda kv: kv[1])
    sorted_Dict = dict(sorted_vaccines)

    vaccine_value = sorted_Dict.values()
    vaccine_valueList = list(vaccine_value)
    state_keys = sorted_Dict.keys()
    state_keyList = list(state_keys)
    
    print(f'''State with highest percentage of population vaccinated: {state_keyList[-1]}
Percentage Vaccinated: {vaccine_valueList[-1]:.2%}''')
 

    
    
    

        
        
        
        
        
       

           
        
            
            
            
        
        
        
  #percentage = '{:.2%}'.format(value)
