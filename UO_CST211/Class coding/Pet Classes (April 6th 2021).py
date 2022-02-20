""" This lecture is focused on Classes and how they can inherit
from a super class. In the case below we see the two subclasses
'cat' and 'dog' both inherit from the super class 'pet'. In this
weeks project we will be doing a game that uses this technique.
Subclass may inherit or override methods in the superclass.

Substitution Principal: Anywhere superclass can be used, subclass
can be used. Python does not guarantee this, the programmer must
ensure that sub principle is in effect.
 """


class Pet(object):
    """Abstract class"""

    def __init__(self):
        raise NotImplementedError("No method voice in class") #flags errors early

    def rename(self, new_name: str):
        self.name = new_name

    def voice(self) -> str:
        raise NotImplementedError("No method voice in class")

    def speak(self):
        print(self.voice())




class Dog(Pet):
    """ doc"""
    def __init__(self, name: str):
        self.name = name

    def voice(self) -> str:
        return "Arf"




class Cat(Pet):
    """ Doc"""
    def __init__(self, name: str):
        self.name = name

    def voice(self) -> str:
        return "Meow"




def main():
    Felip = Cat("Felip")
    Tillman = Dog("Tillman")
    Felip.speak()
    Tillman.speak()

if __name__ == "__main__":
    main()



