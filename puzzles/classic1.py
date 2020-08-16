""" Classic Sudoku puzzle

From: https://www.youtube.com/watch?v=k8fSrnQ9QJ4
"""

from sudoku import Grid

_ = None

grid = [
    _, 6, _, 9, _, 2, 8, _, _,
    _, _, _, _, 5, 8, _, _, _,
    _, _, _, 7, _, _, 5, 1, _,
    4, _, 9, _, 3, _, _, 5, _,
    8, _, _, _, _, _, _, _, 6,
    _, 1, _, _, 8, _, 2, _, 9,
    _, 4, 1, _, _, 9, _, _, _,
    _, _, _, 3, 2, _, _, _, _,
    _, _, 3, 1, _, 5, _, 8, _,
]

puzzle = Grid(grid)
