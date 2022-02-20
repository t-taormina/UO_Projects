'''
CIS 210 Project 2-3: Draw Flower

Author: Tyler Taormina

Credits: N/A

Draws a picture of a flower. 
'''

from turtle import *


def main():
    ''' '''
    drawFlower(25)
    

def drawPolygon(sideLength, numSides):
    ''' (int, int) -> drawing

    Returns a drawing of a square with length
    and number of sides set in the parameter.

    >>>drawPolygon(100, 4)
    Returns drawing of square with side
    length 100 and 4 total sides
    
    
    '''
    for i in range(numSides):
        forward(sideLength)
        right(90)
    penup()
    right(25)
    pendown()


def drawFlower(numSquares):
    '''(int) -> drawing

    Returns a picture of a flower created by
    drawing a number of squares that is
    determined in the parameter.

    >>>drawFlower(25)
    Returns turtle drawing of flower with 25 squares
    
    '''
    right(90)
    forward(250)
    penup()
    left(180)
    pendown()
    forward(250)
    ctr = 1
    for j in range(numSquares - 2):
        drawPolygon(25, 4)
        ctr += 1
        if ctr < numSquares:
            drawPolygon(25, 4)



    
    
    
        
            
        
        
    
