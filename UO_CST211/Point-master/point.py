"""
CIS 211 Mini Project: Point
Author: Tyler Taormina
Credits: NA
April 3, 2021
"""


class Point:
    """An (x, y) coordinate pair"""

    def __init__(self, x: int, y: int):
        """ Initializes the coordinates"""
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """ Adds the x-values together and the y-values together """
        self.x = self.x + dx
        self.y = self.y + dy

    def __eq__(self, other_pt: "Point"):
        """ Checks to make sure that the self point and the other pt are the same coordinates  """
        if self.x != other_pt.x or self.y != other_pt.y:
            return False
        else:
            return True

    def __str__(self):
        """ Returns the coordinates in the format "(x,y)" """
        return f"({self.x}, {self.y})"
