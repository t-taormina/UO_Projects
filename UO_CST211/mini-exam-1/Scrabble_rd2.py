"""
CIS 211 Scrabble Mini Exam Practice Round 2

"""

class Tile:

    def __init__(self, letter: str, value: int):
        self.letter = letter
        self.value = value

    def __str__(self) -> str:
        """ Looks like ('X', 8)"""
        return f"('{self.letter}', {self.value})"

    def __repr__(self) -> str:
        """ Looks like Tile ('X', 8) """
        return f"Tile ('{self.letter}', {self.value})"


class Tray:
    def __init__(self):
        self.tiles = []

    def add_tile(self, tile: Tile):
        """Add tile to collection of tiles"""
        self.tiles.append(tile)

    def __str__(self) -> str:
        """Looks like ('A', 1),('X', 8),('E', 1)"""
        return ",".join([str(t) for t in self.tiles])

    def __repr__(self):
        """Looks like Tray(('A', 1),('X', 8),('E', 1))"""
        return f"Tray({str(self)})"

    def has(self, letter: str) -> bool:
        """Does this tray hold a tile with this letter"""
        for tile in self.tiles:
            if tile.letter == letter:
                return True
        return False

    def would_score(self, word: str):
        score = 0
        value_check = 0
        letter_list = self.tiles.copy()

        for letter in word:
            for let in letter_list:
                if let.letter == letter:
                    score += let.value
                    letter_list.pop(letter_list.index(let))
                    break
            if value_check == score:
                print(f"You don't have the letters to make the word '{word}'")
                return 0
            else:
                value_check = score
        return score

    def dict_score(self, word: str) -> int:
        """ alternate method"""







