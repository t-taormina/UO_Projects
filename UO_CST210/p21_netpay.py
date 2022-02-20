'''
Determining Net Pay
CIS 210 Project 2-1

Author: Tyler Taormina

Credits: Tyler Taormina


'''




def netpay(hours):
    '''(int) -> float

    Returns the netpay an employee receives after taxes
    are taken out based on number hours worked and a
    15% tax rate.

    >>>netpay(1)
    9.5625
    >>>netpay(0)
    0.0
    >>>netpay(4)
    38.25
    
    '''
    gross_pay = hours * 11.25
    
    def tax(gross_pay):
        '''(float) -> float
        Computes amount of taxes and subtracts taxes
        from the gross pay resulting in net pay.

        >>>tax(11.25)
        9.5625
        >>>tax(0)
        0
        >>>tax(45.00)
        38.25
        '''
        
        tax1 = gross_pay * .15
        net = gross_pay - tax1

        return net
    
    result = tax(gross_pay)
    result = round(result, ndigits = 2)
    
    return result



    






def main():
    ''' Net pay program driver.'''
    print ('For 1 hours work, netpay is: ', netpay(1))
    print ('For 40 hours work, netpay is: ', netpay(40))
    return None
main()


    
