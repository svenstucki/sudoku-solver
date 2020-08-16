from abc import ABC, abstractmethod

from sudoku.constraints import _unique_list


class AdvancedConstraint(ABC):
    """ Base interface for additional constraints. """

    @abstractmethod
    def check(self, grid):
        pass

    def __call__(self, grid):
        return self.check(grid)

    @abstractmethod
    def __str__(self):
        pass


class MagicSquare(AdvancedConstraint):
    """ Magic square constraint.

    A magic square is a 3x3 box, which contains the digits 1 to 9 and where the
    sum of each row, column and diagonal is 15.

    The constraint is more strict than it seems at first. It can be shown, that
    this forces even numbers into the corners of the box and the center cell
    must contain a 5. These properties are used as an optimisation.

    The magic square must not necessarily equal one of the regular Sudoku boxes.
    However, if that is the case, the uniqueness check can be disabled.

    Arguments:
    positions -- tuple with indexes of the magic square cells
    check_uniqueness -- whether the digits should be checked for uniqueness
    """

    def __init__(self, positions, check_uniqueness=True):
        self.positions = positions
        self.check_uniqueness = check_uniqueness

    def check(self, grid):
        square = tuple((
            grid.grid[x] for x in self.positions
        ))

        # check uniqueness
        if self.check_uniqueness:
            if not _unique_list(square):
                return False

        # check center cell
        if square[4] not in (None, 5):
            return False

        # check even cells
        even_check = lambda v: v in (None, 2, 4, 6, 8)
        if not even_check(square[0]): return False
        if not even_check(square[2]): return False
        if not even_check(square[6]): return False
        if not even_check(square[8]): return False

        # check odd cells
        odd_check = lambda v: v in (None, 1, 3, 7, 9)
        if not odd_check(square[1]): return False
        if not odd_check(square[3]): return False
        if not odd_check(square[5]): return False
        if not odd_check(square[7]): return False

        # check row sums
        sum_check = lambda x, y, z: x is None or y is None or z is None or x+y+z == 15
        if not sum_check(square[0], square[1], square[2]): return False
        if not sum_check(square[3], square[4], square[5]): return False
        if not sum_check(square[6], square[7], square[8]): return False

        # check column sum
        if not sum_check(square[0], square[3], square[6]): return False
        if not sum_check(square[1], square[4], square[7]): return False
        if not sum_check(square[2], square[5], square[8]): return False

        return True

    def __str__(self):
        return 'Magic square'  # TODO: add positions


class UniqueDiagonal(AdvancedConstraint):
    """ Unique diagonal constraint.

    Ensure digits on a main diagonal do not repeat.

    Arguments:
    direction -- which main diagonal to use (bool, False for top-left to bottom-right)
    """

    def __init__(self, direction=False):
        self.direction = direction

    def check(self, grid):
        if self.direction:
            # top-right to bottom-left
            values = (
                grid.grid[i*9 + 8-i] for i in range(9)
            )
        else:
            # top-left to bottom-right
            values = (
                grid.grid[i*9 + i] for i in range(9)
            )
        return _unique_list(values)

    def __str__(self):
        direction = (
            'top-right to bottom-left' if self.direction else 'top-left to bottom-right'
        )
        return f'Unique diagonal ({direction})'
