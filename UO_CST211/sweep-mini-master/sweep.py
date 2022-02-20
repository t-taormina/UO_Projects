"""
CIS 211 Sweep Lists
Author: Tyler Taormina
Credits:

"""

def all_same(l: list) -> bool:
    """Checks to see if a list consists of all the same numbers"""
    if len(l) == 0:
        return True
    else:
        first_item = l[1]
        for item in l:
            if item != first_item:
                return False
        return True

def dedup(l: list) -> list:
    """Gets rid of duplicates in a list"""
    new_list = []
    i = 0
    for i in l:
        if i in new_list:
            i += 1

        else:
            new_list.append(i)
            i += 1
    return new_list

def max_run(l: list) -> int:
    """Returns the count of the object in the list with the most occurences """
    prev_character = None
    high_ct = 0
    ctr = 0
    for num in l:
        if num == prev_character or ctr == 0:
            ctr = ctr + 1
            if ctr > high_ct:
                high_ct = ctr
        else:
            ctr = 1

        prev_character = num

    return high_ct
































