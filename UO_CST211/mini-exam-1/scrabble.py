"""
CIS 211 Mini Exam 1
Author: Tyler Taormina
Credits:
April 10, 2021
"""


class Tile:

    def __init__(self, letter: str, value: int):
        """Constructor"""
        self.letter = letter
        self.value = value

    def __str__(self) -> str:
        """Looks like ('X', 8)"""
        return f"('{self.letter}', {self.value})"

    def __repr__(self):
        """ Looks like Tile ('X', 8) """
        return f"Tile('{self.letter}', {self.value})"


class Tray:

    def __init__(self):
        self.tiles = []

    def add_tile(self, tile: Tile):
        """Add tile to the collection of tiles in this tray"""
        self.tiles.append(tile)

    def __str__(self) -> str:
        """Looks like ('A', 1),('X', 8),('E', 1)"""
        return ",".join([str(t) for t in self.tiles])

    def __repr__(self):
        """Looks like Tray(('A', 1),('X', 8),('E', 1))"""
        return f"Tray({str(self)})"

    def has(self, letter: str) -> bool:
        """Does this tray hold a tile with the specified letter?"""
        for tiles in self.tiles:
            if letter == tiles.letter:
                return True
        return False

    def would_score(self, word: str):
        """"""
        value_check = 0
        total_score = 0
        letter_list = self.tiles.copy()

        for i in word:
            for t in letter_list:
                if t.letter == i:
                    total_score += t.value
                    letter_list.pop(letter_list.index(t))
                    break
            if value_check == total_score:
                print(f"You don't have the letters to make the {word}.")
                return 0
            else:
                value_check = total_score
        return total_score
