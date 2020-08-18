from puzzles.classic1 import puzzle as classic1
from puzzles.classic2 import puzzle as classic2

from sudoku.solver import BacktrackingSolver


def test_solves_classic1():
    solver = BacktrackingSolver(classic1, BacktrackingSolver.LINEAR_PATH)
    result = solver.solve()

    assert result.grid == [
        5, 6, 4,  9, 1, 2,  8, 7, 3,
        1, 3, 7,  4, 5, 8,  9, 6, 2,
        9, 8, 2,  7, 6, 3,  5, 1, 4,

        4, 2, 9,  6, 3, 1,  7, 5, 8,
        8, 7, 5,  2, 9, 4,  1, 3, 6,
        3, 1, 6,  5, 8, 7,  2, 4, 9,

        6, 4, 1,  8, 7, 9,  3, 2, 5,
        7, 5, 8,  3, 2, 6,  4, 9, 1,
        2, 9, 3,  1, 4, 5,  6, 8, 7,
    ]


def test_solves_classic2():
    solver = BacktrackingSolver(classic2, BacktrackingSolver.LINEAR_PATH)
    result = solver.solve()

    assert result.grid == [
        3, 4, 5,  7, 8, 1,  9, 2, 6,
        7, 2, 6,  4, 3, 9,  8, 5, 1,
        8, 9, 1,  5, 2, 6,  4, 7, 3,

        2, 5, 4,  8, 6, 3,  1, 9, 7,
        6, 8, 7,  1, 9, 5,  3, 4, 2,
        9, 1, 3,  2, 4, 7,  5, 6, 8,

        5, 3, 8,  6, 7, 4,  2, 1, 9,
        1, 6, 2,  9, 5, 8,  7, 3, 4,
        4, 7, 9,  3, 1, 2,  6, 8, 5,
    ]
