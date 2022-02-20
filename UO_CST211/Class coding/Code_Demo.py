"""
Tyler Taormina
Code Demo
05.06.2021
"""

from typing import List



class Vector(List):
    def __mul__(self, other: "Vector") -> int:
        total = 0
        for i in range(len(self)):
            value = self[i] * other[i]
            total += value
        return total

    def matrix_mult(self, other: "Matrix"):
        assert len(self) == len(other.rows), "Vector and matrix are incompatible"
        result_list = []
        for col in other.cols:
            result_list.append(self.__mul__(col))
        return Vector(result_list)



class Matrix:
    def __init__(self, rows: List[Vector]):
        self.rows = rows
        self.cols = []
        for col in range(len(rows[0])):
            item = []
            for row in range(len(rows)):
                item.append(rows[row][col])
            self.cols.append(item)











l1 = [1, 2, 3]

l2 = [4, 5, 6]
l1 = Vector(l1)
l2 = Vector(l2)
print(l1.__mul__(l2))

