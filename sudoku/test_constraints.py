from copy import copy
from puzzles.classic1 import grid

from sudoku.constraints import (
    _unique_list,
    unique_rows, unique_cols, unique_boxes,
)


_ = None

def test_unique_list():
    l = [1, 2, 3, 4, 5] # no repeats
    assert _unique_list(l) == True

    l = [1, 2, 3, 4, 1] # repeated digit
    assert _unique_list(l) == False

    l = [1, _, 3, 4, 5] # no repeated digits with None
    assert _unique_list(l) == True

    l = [1, _, _, 2, 3] # no repeated digits, repeated None
    assert _unique_list(l) == True

    l = [1, _, 1, 4, 5] # repeated digit with None
    assert _unique_list(l) == False

    l = [1, 2, 3, 1, 1] # multiple repeats of same digit
    assert _unique_list(l) == False

    l = [1, 2, 3, 2, 1] # multiple repeated digits
    assert _unique_list(l) == False


def test_base_constraints():
    def copy_and_set(idx, v):
        c = copy(grid)
        c[idx] = v
        return c

    def check_rcb(grid, rows=True, cols=True, boxes=True):
        assert unique_rows(grid) == rows
        assert unique_cols(grid) == cols
        assert unique_boxes(grid) == boxes

    # the puzzle is valid
    check_rcb(grid)

    # repeat 8 in row, column and box
    g = copy_and_set(4, 8)
    check_rcb(g, rows=False, cols=False, boxes=False)

    # repeat 9 in row and column
    g = copy_and_set(8, 9)
    check_rcb(g, rows=False, cols=False)

    # repeat 3 in row
    g = copy_and_set(8*9+6, 3)
    check_rcb(g, rows=False)

    # repeat 1 in col
    g = copy_and_set(4*9+7, 1)
    check_rcb(g, cols=False)

    # repeat 8 in box
    g = copy_and_set(3*9+3, 8)
    check_rcb(g, boxes=False)
