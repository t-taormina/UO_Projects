"""Snakes in a tree:
They can be anywhere in the tree.  And I really
like snakes, so I want to know how many snakes
I can find on one path from root to leaf.
"""

from typing import List

class SnakeTree:
    def max_snakes_path(self) -> int:
        raise NotImplementedError("Help me look for snakes!")

class Leaf(SnakeTree):
    def __init__(self, snakes: int):
        self._snakes = snakes

    def max_snakes_path(self) -> int:
        return self._snakes

class Branch(SnakeTree):
    def __init__(self, snakes: int, children: List[SnakeTree]):
        self._snakes = snakes
        self._children = children

    def max_snakes_path(self) -> int:
        most_snakes = 0
        for branch in self._children:
            if branch.max_snakes_path() > most_snakes:
                most_snakes = branch.max_snakes_path()
        return most_snakes + self._snakes



def main():
    """Smoke test"""
    tree = Branch(3, [
                Branch(2, [
                    Leaf(4), Leaf(2)
                ]),
                Leaf(8)
            ])
    # Max should be 11?
    print(tree.max_snakes_path())

if __name__ == "__main__":
    main()