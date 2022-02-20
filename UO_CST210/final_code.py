'''
CIS 210 Final Exam code

Tyler Taormina

Credits: Prof Erickson (BIG thanks!)

Returns None and prints an animation of the user's path using the Turtle Module
'''

import turtle

def drawGPS():
    '''
    (str) -> None

    Reads in a file skipping header lines. Retruns none and prints
    an animation of the user's path using turtle module

    '''

    with open('racetrack_gps.txt', 'r') as myf:
        myf.readline() #skips header line

        first_vals = myf.readline().strip().rstrip().split(',')
        startPoint = (float(first_vals[1]), float(first_vals[2])) #establishes starting point
        turtle.pu()
        turtle.setpos(startPoint) # turtle moves to start point
        turtle.pd()
        
        for line in myf:
            vals = line.strip().rstrip().split(',')
            position = (float(vals[1]), float(vals[2])) #establishes each coordinate for turtle to go to
            turtle.goto(position) #go turtle go

    return None 
            
            
            
            
            
            
            
        
