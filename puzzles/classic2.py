""" Classic Sudoku puzzle

From: https://www.youtube.com/watch?v=aBqckBNn03s
"""

from sudoku import Grid

_ = None

grid = [
    3, 4, _, _, _, 1, _, _, _,
    _, 2, _, _, _, 9, _, _, _,
    _, _, _, 5, _, _, _, 7, _,
    _, _, _, _, _, 3, 1, _, 7,
    6, 8, _, _, _, _, 3, _, 2,
    _, _, _, _, _, _, _, 6, _,
    _, _, 8, _, 7, 4, _, 1, _,
    _, _, _, _, _, _, _, _, _,
    _, _, 9, _, _, _, 6, 8, 5,
]

puzzle = Grid(
    grid,
    additional_constraints=(),
)
