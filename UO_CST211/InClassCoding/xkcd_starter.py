"""XKCD Regex detective.

Your mission, if you choose to accept it, is
to find and print all the addresses in
clues.txt
"""
import re

# Starter pattern is any string of digits.
# We will improve this together in class
CLUE_PATTERN = re.compile(r"""
[0-9]+  # match any string of digits 
""", re.VERBOSE)
# re.VERBOSE allows us to enter white space in our comments

def get_a_clue(s: str):
    """Print any addresses found in s"""
    for match in re.finditer(CLUE_PATTERN, s):
        print(match.group(0))

def scan_file(filename: str):
    """Look for clues in a file"""
    f = open(filename)
    for line in f:
        get_a_clue(line)

if __name__ == "__main__":
    scan_file("clues.txt")
