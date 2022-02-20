"""
CIS 211 Project: Waldo
Author: Tyler Taormina
04.24.21
Description: This project acts as an exercise in looping through sequence types. More specifically,
it is an exercise in looping through and accessing objects within matrices - that is lists within lists.


"""
# start with a matrix: list of lists -> [ [] ]

# One of the redundant cases is the all(row, col)/all Waldo's
# because if all the rows have Waldo's and only Waldo's it implies that
# all the columns have Waldo's and only Waldo's

# Another redundant case is the there exists a row/col in which there
# exists a  Waldo. If a Waldo exists in any row, it also exists
# in some column.


Waldo = 'W'
Other = '.'


def transpose(matrix: list[list]) -> list:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    else:
        tran_list = []
        n = 0
        for col in range(len(matrix)):
            tran_list.append([])
            for row in range(len(matrix)):
                tran_list[n].append(matrix[row][col])
            n += 1
        return tran_list


def all_row_exists_waldo(matrix: list[list]) -> bool:
    """one or more waldo in each row """
    for row in matrix:
        if Waldo not in row:
            return False
    return True


def all_col_exists_waldo(matrix: list[list]) -> bool:
    """ one waldo in each column """

    """Assert might be a viable option to account for 
    the empty list error. If we did this we would also 
    need  to implement an assert exception class that
    returns a bool. A question I have is how to scale
    an edge case with a function like this where we
    aren't sure how many empty lists could be inside 
    of the provided matrix?
    """

    ctr = 0
    if len(matrix) < 1 or len(matrix[0]) < 1:  # Vacuous cases
        return True
    for column in range(len(matrix[0])):  # Accessing elements of the list by index
        for row in range(len(matrix)):
            if matrix[row][column] == Waldo:
                ctr += 1
                break  # Find a waldo in a column and break the loop so we can start looking inside of the next column.
    return len(matrix[0]) == ctr  # Compares the number of columns with the count of waldo's found


def all_row_all_waldo(matrix: list[list]) -> bool:
    """only waldo's  """
    for row in matrix:
        if Other in row:
            return False
    return True


def all_col_all_waldo(matrix: list[list]) -> bool:
    """only waldo's """
    for row in matrix:
        if Other in row:
            return False
    return True


def exists_row_all_waldo(matrix: list[list]) -> bool:
    """at least one row with only Waldo's"""
    waldo_row = None
    for row in matrix:
        if Other in row:
            waldo_row = False
        else:
            waldo_row = True
            break
    return waldo_row


def exists_col_all_waldo(matrix: list[list]) -> bool:
    """ one column with all Waldo's"""
    ctr = 0
    column_ct = 0
    if len(matrix) < 1 or len(matrix[0]) < 1:
        return False  # Vacuous cases
    for row in matrix:
        column_ct += 1  # Determines the number of columns
    for column in range(len(matrix)):  # Access objects by index
        for row in range(len(matrix)):
            if matrix[row][column] == Waldo:
                ctr += 1
        if ctr == column_ct:
            return True  # Compare the count of Waldo's to the number of columns to make sure there are only Waldo's
        else:
            ctr = 0
            pass  # If they are unequal then reset count and restart the loop through the next column
    return False


def exists_row_exists_waldo(matrix: list[list]) -> bool:
    """ There is one row with at least one Waldo"""
    for row in matrix:
        if Waldo in row:
            return True
        else:
            pass
    return False


def exists_col_exists_waldo(matrix: list[list]) -> bool:
    """ There is one column with at least one Waldo"""
    for row in matrix:
        if Waldo in row:
            return True
        else:
            pass
    return False




