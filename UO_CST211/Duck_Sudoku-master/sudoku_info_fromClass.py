"""
Info provided in class
4.27.21
SUDOKU

The hard part is going to be loop design.
Each col has 1-9 and each row has 1-9.
Think Waldo....

ALIASING
Each tile will be long to three lists. a column list, row list, and block list.
If we alter a tile in one list we must alter it in the other two.


RECURSIVE SEARCH
A guess and check method.
We will use a combination of both.

THREE STEPS
1. Puzzle representation and consistency check
2. Constraint propagation to solve simple puzzles and recognize correct solutions.
        Naked single - only one possible option for a given cell
        Hidden single - multiple options but further examination
        reveals only one possible number for the cell

***Part 2 requires careful logic and loop design

3. Search for a solution to harder puzzles,
Depth-first recursive search (guess-and-check)

Tactics:
    Each cell has a "candidates" attribute (Python Set)
        for each row, column, and block:
            loop through groups to find used symbols
            loop through to remove symbols from candidates set
            if len(candidates) is 1, choose that symbol

    -> go through all the rows and do this for each tile in the row
    -> then go through all the columns and do this for each tile in the col
    -> then go through each block and do this for each tile in the block

We can think of each tile as accumulating constraints (as we remove items from
the candidates set we narrow down the options for each tile).

GUESS-AND-CHECK
    a recursive search w/ backtracking in other words.
    Can think of it as a tree of possible solutions. Most of them will be wrong.
    It is a space to test the possible solutions.

    psuedocode:
    Recursive function (solve):
        if the partial solution is complete:
            return true
        if there partial solution can't possibly work:
        return false
        for each possible next step:
            apply the step to partial solution:
            if solve(partial solution):
                return true
            else:
                undo step # how do we undo steps???
        # All possible next steps have failed
        return False

    # to undo steps we need to make a copy of the board prior to making a guess and proceeding in testing the guess.
    # save it as a new puzzle
    # we need a way to generate "next" states and a way to restore prior states


*** My thoughts***
# make a matrix (list of lists)
# make new lists for the rows, columns, and blocks each with 9 tiles in it
# for each tile we will run it through the three different lists and start
    eliminating candidates for that tile


"""
