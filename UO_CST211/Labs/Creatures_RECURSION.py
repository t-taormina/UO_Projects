"""
Lab 09 "Creatures"
Author: Tyler Taormina
05.26.2021

"""

class Creature(object):

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instanciated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")

    def search(self, value: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")

class Head(Creature):

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def search(self, value: str) -> bool:
        return value == self.name


class Orthus(Creature):

    def __init__(self, left: Creature, right: Creature):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        left_str = str(self.left)
        right_str = str(self.right)
        return f"{left_str}, {right_str}"

    def search(self, value: str) -> bool:
        left_search = self.left.search(value)
        right_search = self.right.search(value)
        return left_search or right_search


class Cerberus(Creature):

    def __init__(self, left: Creature, middle: Creature, right: Creature):
        self.left = left
        self.middle = middle
        self.right = right

    def __str__(self) -> str:
        left_str = str(self.left)
        middle_str = str(self.middle)
        right_str = str(self.right)
        return f"{left_str}, {middle_str}, {right_str}"

    def search(self, value: str) -> bool:
        left_search = self.left.search(value)
        middle_search = self.middle.search(value)
        right_search = self.right.search(value)
        return left_search or right_search or middle_search

def main():
    dog1 = Head("Kane")
    dog2 = Head("Wolfie")
    dog3 = Head("Rugal")
    dog4 = Head("Taker")
    ort1 = Orthus(dog1, dog2)
    ort2 = Orthus(dog3, Head("Jeff"))
    cer = Cerberus(ort1, dog4, ort2)
    print(cer)
    print("Looking for Marley....")
    val = cer.search("Marley")
    print(val)
    if val == False:
        print("Where's Marley? ")
    print("Looking for Wolfie....")
    val2 = cer.search("Wolfie")
    print(val2)

if __name__ == '__main__':
    main()
