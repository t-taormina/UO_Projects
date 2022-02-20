"""
Lab 07
Author: Tyler Taormina
05.12.2021

"""

from typing import Callable

def total_sum(num_list: list) -> int:
    total = 0
    for num in num_list:
        total += num
    return total

def apply(f: Callable, int_list: list) -> list:
    total = []
    for item in int_list:
        total.append(f(item))
    return total

def square(int_list: list) -> list:
    # call apply and
    return apply(lambda x: x ** 2, int_list)


def magnitude(vector: list) -> int:
    square_list = square(vector)
    mag = (total_sum(square_list)) ** (1/2)
    return mag


t = total_sum
s = square
m = magnitude

dispatch_table = dict()
dispatch_table[1] = t
dispatch_table[2] = s
dispatch_table[3] = m

class FunctionDispatcher:
    def __init__(self, table: dict):
        self.table = table

    def process_command(self, key: int, num_list: list):
        result = self.table[key](num_list)
        print(result)

def main():
    fd = FunctionDispatcher(dispatch_table)
    fd.process_command(1, [3, 4])
    fd.process_command(2, [3, 4])
    fd.process_command(3, [3, 4])


if __name__ == '__main__':
    main()