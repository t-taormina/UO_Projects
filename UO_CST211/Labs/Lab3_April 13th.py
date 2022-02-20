"""
CIS 211 Lab 3
Author: Tyler Taormina
Credits:Bruce

Goes over inheritance, superclasses, and subclasses.
Don't forget to include parentheses when calling a function. See 'print_info' method.
"""
from math import pi


class Shape3D:

    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def print_info(self):
        print(f"Area: {self.area()} Volume: {self.volume()}")
        # not f"Area: {self.area} Volume: {self.volume}"  ***Need to include () after self.area/volume
        # do not return a statement that you want printed!


class Cylinder(Shape3D):

    def __init__(self, radius: float, height: float):
        """"""
        self.radius = radius
        self.height = height

    def area(self) -> float:
        return (pi * self.radius ** 2) + (2 * pi * self.height)

    def volume(self) -> float:
        return pi * self.radius ** 2 * self.height


class Cuboid(Shape3D):

    def __init__(self, width: float, length: float, height: float):
        self.width = width
        self.length = length
        self.height = height

    def area(self) -> float:
        return (2 * self.width * self.length) + (2 * self.width * self.height) + (2 * self.length * self.height)

    def volume(self) -> float:
        return (self.width * self.length * self.height)


class Cube(Cuboid):

    def __init__(self, width: float):
        super().__init__(width, width, width)


def main():
    cyl = Cylinder(3, 5)
    cuboid = Cuboid(6, 4, 9)
    lst = [Cube(3), cyl, cuboid]
    for shape in lst:
        shape.print_info()


if __name__ == "__main__":
    main()
