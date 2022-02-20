"""In class-programming challenge: complete the column sequences.
Spec:  Given a rectangular matrix m of integers and "none"  (that is, a matrix
of "optional" integers),  for each column of the matrix,
IF the column can be transformed into a sequence k, k+1, k+2, etc.,
then do so, otherwise do not alter that column.
(Do not alter any matrix entries that are not already integers)
Return True iff the every column has been transformed (with zero or
more operations) into a sequence.
"""

from typing import List, Optional


class RectMatrix:
    """A rectangular matrix in which each element is
    either an int or None.
    """

    def __init__(self, values: List[List[Optional[int]]]):
        # Is it rectangular?
        if len(values) == 0:
            self.items = values
            return
        row_len = len(values[0])
        for row in values:
            if len(row) != row_len:
                raise ValueError("RectMatrix values must be rectangular")
        # OK then!
        self.items = values

    def __eq__(self, other: "RectMatrix") -> bool:
        """Equal if same shape and corresponding items are equal"""
        # Same shape?
        if len(self.items) != len(other.items):
            return False
        if len(self.items) == 0:
            return True
        if len(self.items[0]) != len(other.items[0]):
            return False
        # Shape is same; are items all equal?
        for row_i in range(len(self.items)):
            row = self.items[row_i]
            for col_i in range(len(row)):
                if self.items[row_i][col_i] != other.items[row_i][col_i]:
                    return False
        return True

    def patchable(self):  # a changing value can be indicative of a true or false situation.
        compliant_dict = dict()

        for col in range(len(self.items[0])):
            compliant = True
            ctr = 0

            for row in range(len(self.items)):
                if self.items[row][col] is None and (ctr == 0):
                    continue

                if ctr != 0:
                    ctr += 1

                    if type(self.items[row][col]) == int and self.items[row][col] != ctr:
                        compliant = False
                        break

                if type(self.items[row][col]) == int and (ctr == 0):
                    ctr = self.items[row][col]

            if compliant:
                compliant_dict[col] = ctr

        return compliant_dict

    def complete_sequences(self) -> bool:
        """Each column is either made a sequence
        by replacing None elements,
        OR the column is unaltered if it cannot form a sequence.
        Returns True iff every column has been completed.
        """
        col_key = self.patchable()

        for col in col_key:
            for row in range(1, len(self.items) + 1):
                self.items[(-row)][col] = col_key[col] - (row - 1) # Ask Avery about this

        if len(col_key) != len(self.items[0]):
            return False
        return True


def smoke_test():
    """One simple test case for now"""
    before = RectMatrix([[1, None, None],
                         [None, None, 8],
                         [3, 7, None],
                         [None, None, None],
                         [5, 11, 11]])

    after = RectMatrix([[1, None, 7],
                        [2, None, 8],
                        [3, 7, 9],
                        [4, None, 10],
                        [5, 11, 11]])

    complete = before.complete_sequences()
    print(before.items)
    assert after == after  # __equals__ works?
    assert (not complete) and before == after


if __name__ == "__main__":
    smoke_test()
