""" Magic square Sudoku by Aad van de Wetering

From: https://www.youtube.com/watch?v=hAyZ9K2EBF0
"""

from sudoku import Grid
from sudoku.advanced_constraints import MagicSquare, UniqueDiagonal

_ = None

grid = [
    _, _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _, _,
    3, 8, 4, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _, 2,
]

puzzle = Grid(
    grid,
    additional_constraints=(
        UniqueDiagonal(False),
        UniqueDiagonal(True),
        # magic square in the middle box
        MagicSquare((
            3*9 + 3, 3*9 + 4, 3*9 + 5,
            4*9 + 3, 4*9 + 4, 4*9 + 5,
            5*9 + 3, 5*9 + 4, 5*9 + 5,
        ), check_uniqueness=False),
    ),
)
