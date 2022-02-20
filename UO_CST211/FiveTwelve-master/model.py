"""
CIS 211
Project 2: FiveTwelve
Author: Tyler Taormina
Credits: Discord, Coffee, My Dog
April 11, 2021

The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4


class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Vec") -> "Vec":
        """Adds the x coordinate in self to the x coordinate
        in other. Adds the y coordinate in self to the y
        coordinate in other. Sets self coordinates to the added
        values for x and y. """
        moved_vec = Vec(self.x + other.x, self.y + other.y)
        return moved_vec

    def __eq__(self, other: "Vec") -> bool:
        """ Checks to see if the self point and the other pt are the same coordinates"""
        return self.x == other.x and self.y == other.y


class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self, pos: Vec, value: int):
        super().__init__()
        self.row = pos.x
        self.col = pos.y
        self.value = value
        # FIXME potentially if we cannot solve the issue of tiles bumping into one another in the board class

    def __repr__(self):
        """Not like constructor --- more useful for debugging"""
        return f"Tile[{self.row},{self.col}]:{self.value}"

    def __eq__(self, other: "Tile"):
        return type(self) == type(other) and self.value == other.value

    def __str__(self):
        return str(self.value)

    def __add__(self, other: "Tile"):
        """Adds values of tiles"""
        self.value = self.value + other.value
        return self.value

    def move_to(self, new_pos: Vec):
        self.row = new_pos.x
        self.col = new_pos.y
        self.notify_all(GameEvent(EventKind.tile_updated, self))

    def merge(self, other: "Tile"):
        # This tile incorporates the value of the other tile
        self.value = self.value + other.value
        self.notify_all(GameEvent(EventKind.tile_updated, self))
        # The other tile has been absorbed.  Resistance was futile.
        other.notify_all(GameEvent(EventKind.tile_removed, other))


class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.tiles = []
        for row in range(rows):
            row_tiles = []
            for col in range(cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles)

    def __getitem__(self, pos: Vec) -> Tile:
        return self.tiles[pos.x][pos.y]

    def __setitem__(self, pos: Vec, tile: Tile):
        self.tiles[pos.x][pos.y] = tile

    def _empty_positions(self) -> List[Vec]:
        """Return a list of positions of None values,
        i.e., unoccupied spaces.
        """
        empties = []
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] is None:
                    empties.append(Vec(row, col))
        return empties

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        empties = self._empty_positions()
        return len(empties) > 0

    def place_tile(self, value=None):
        """Place a tile on a randomly chosen empty square."""
        empties = self._empty_positions()
        assert len(empties) > 0
        choice = random.choice(empties)
        row, col = choice.x, choice.y
        if value is None:
            # 0.1 probability of 4
            if random.random() <= 0.1:
                value = 4
            else:
                value = 2
        new_tile = Tile(Vec(row, col), value)
        self.tiles[row][col] = new_tile
        self.notify_all(GameEvent(EventKind.tile_created, new_tile))

    def to_list(self) -> List[List[int]]:
        """Test scaffolding: represent each Tile by its
        integer value and empty positions as 0
        """
        result = []
        for row in self.tiles:
            row_values = []
            for col in row:
                if col is None:
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result

    def from_list(self, values: List[List[int]]):
        """Test scaffolding: set board tiles to the
        given values, where 0 represents an empty space.
        """
        result = []
        for row in range(len(values)):
            row_values = []
            for col in range(len(values[row])):
                if values[row][col] == 0:
                    row_values.append(None)
                else:
                    row_values.append(Tile(Vec(row, col), values[row][col]))
            result.append(row_values)
        self.tiles = result

    def in_bounds(self, pos: Vec) -> bool:
        """is position (pos.x, pos.y) a legal position on the board?"""
        return (0 <= pos.x <= (self.rows - 1) and (0 <= pos.y <= (self.cols - 1)))

    def slide(self, pos: Vec, dir: Vec):
        """Slide tile at pos.x, pos.y (if any)
        in direction (dir.x, dir.y) until it bumps into
        another tile or the edge of the board.
        """
        if self[pos] is None:
            return
        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break
            if self[new_pos] is None:
                self._move_tile(pos, new_pos)
            elif self[pos] == self[new_pos]:
                self[pos].merge(self[new_pos])
                self._move_tile(pos, new_pos)
                break
            else:
                # stuck against another tile
                break
            pos = new_pos

    def up(self):
        for row in self.tiles:
            for tile in row:
                if tile:
                    self.slide(pos=Vec(tile.row, tile.col), dir=Vec(-1, 0))  # up

    def down(self):
        for row in self.tiles:
            for tile in row:
                if tile:
                    self.slide(pos=Vec(tile.row, tile.col), dir=Vec(1, 0))  # down

    def right(self):
        for row in self.tiles:
            for tile in reversed(row):
                if tile:
                    self.slide(pos=Vec(tile.row, tile.col), dir=Vec(0, 1))  # right

    def left(self):
        for row in self.tiles:
            for tile in row:
                if tile:
                    self.slide(pos=Vec(tile.row, tile.col), dir=Vec(0, -1))  # left

    def _move_tile(self, old_pos: Vec, new_pos: Vec):
        """Write"""
        tile_mover = self[old_pos]
        tile_mover.move_to(new_pos)
        self[new_pos] = self[old_pos]
        self[old_pos] = None

    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        total_score = 0
        for row in self.tiles:
            for col in row:
                total_score += col.value
        return total_score
