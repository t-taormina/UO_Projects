def est_tax(income, exemptions):    			
    '''(number, integer) -> float  
 													
    Generates an estimate for federal income tax.
    Prints result.
    Example from class, revised to print (not return) estimated tax.

    >>> est_tax(20000, 1)
    1870.0      
    '''    									 
    # Set values needed to generate estimate    	 
    STD_EXEMPT = 4150    					 
    STD_DEDUCT = 6500    
    TAX_RATE = .20

    taxable_income = taxable (income, exemptions, STD_EXEMPT, STD_DEDUCT)
    estimated_tax = taxable_income * TAX_RATE
    print('Estimated tax is:', estimated_tax)
    
    return None

def taxable(income,exemptions, STD_EXEMPT,STD_DEDUCT):
    '''(number, int, number, number)'''
    taxable_income = income - STD_DEDUCT
    exempt_adjust = STD_EXEMPT * exemptions
    taxable_income = taxable_income - exempt_adjust
    
    print('Taxable income is:', taxable_income)
    
    return taxable_income



