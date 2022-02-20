"""In-class live coding exercise:
Trees that can be compared.

t1 == t2 iff they are the same shape
and have the same elements.

Note: isinstance(o,C) returns True
     iff o is an object of type C
     Also o.__class__ is the class of an object
"""
from typing import List

def same_class(this: object, that: object) -> bool:
    """Is that thing a member of the class of this thing?
    For use in comparisons, a rare case where it is ok
    to explicitly test the class of an object.
    """
    return isinstance(that, this.__class__)


class Tree:
    """Abstract base class for comparable trees"""
    def __init__(self):
        raise NotImplementedError("Quit it!")

    def __eq__(self, other: "Tree") -> bool:
        raise NotImplementedError("Did you forget something?")

class Leaf(Tree):
    def __init__(self, value: int):
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        # are they both leaves?
        if same_class(self, other):
            # are they the same value?
            return self.value == other.value
        # they are not the same value
        else:
            return False

class Inner(Tree):
    def __init__(self, children: List[Tree]):
        self.children = children

    def __str__(self) -> str:
        return f"[{', '.join(str(child) for child in self.children)}]"

    def __repr__(self) -> str:
        return f"Inner({', '.join(str(child) for child in self.children)})"

    def __eq__(self, other):
        if not same_class(self, other) or len(self.children) != len(other.children):
            return False

        # Both inner nodes

        for child in range(len(self.children)):
            if self.children[child] != other.children[child]:
                return False
        return True



t1 = Inner([Leaf(5), Inner([Leaf(6), Leaf(7)])])
print(t1)
t2 = Inner([Leaf(5), Leaf(4)])
print(t2)
t3 = Inner([Leaf(5), Inner([Leaf(6), Leaf(7)])])
print(t3)
t4 = Inner([Leaf(5), Leaf(6)])
print(t4)
t5 = Inner([Leaf(2), Inner([Leaf(1), Leaf(4)]), Leaf(9)])
print(t5)
t6 = Inner([Inner([]), Leaf(0)])
print(t6)
t7 = Inner([Leaf(5), Inner([Leaf(6), Leaf(7)])])
print(t7)


# assert t1 == t3
assert t1 != t2
assert t2 != t3
assert t2 != t4
assert t1 == t7

