'''
Tuesday Feb 23- Lab
Description: More info on debugging; using assert and try/except; 



'''

def dubNum():
    value = input("Enter a number between 1 and 10: ")
    int_value = float(value)
    assert(int_value == int_value>=1 and int_value <= 10), f'input {int_value} should be a number between 1 and 10'
    dub_value = int_value * 2
    print(dub_value)
    
    
    
    
