"""Unit tests for testme.py
CIS 211 April 13th, 2021
Author: Tyler Taormina
Credits: NA

Looking for bugs in a function that loops through a list and looks
for the longest streak of consecutive identical objects. In this case
the only objects that we are putting in the list are integers.

"""

import unittest
from buggy import *


class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        test_1 = max_run([1, 2, 2, 2, 3])
        test1_expected = [2, 2, 2]
        self.assertEqual(test1_expected, test_1)

    def test_secondary_max_run(self):
        """Checks to see if function counts max run that occurs
        later in the list"""
        test_2 = max_run([1, 1, 2, 2, 1, 1, 1])
        test2_expected = [1, 1, 1]
        self.assertEqual(test2_expected, test_2)

    def test_max_run_shortList(self):
        """Checks to see if the function counts a the max run of a
        list with one object and returns the one object"""
        test_3 = max_run([1])
        test3_expected = [1]
        self.assertEqual(test3_expected, test_3)


if __name__ == "__main__":
    unittest.main()
