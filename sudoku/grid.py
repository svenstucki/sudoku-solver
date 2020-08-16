import copy

from sudoku.constraints import unique_rows, unique_cols, unique_boxes


class Grid:
    """ Full Sudoku grid.

    The grid is stored sequentally from left to right, row by row, from top to
    bottom in a list. The entry at `(row, col)` is stored at index `row*9 +
    col`.
    """

    def __init__(self, grid, additional_constraints=()):
        self.grid = grid
        self.additional_constraints = additional_constraints

    def copy(self):
        return Grid(
            copy.copy(self.grid),
            self.additional_constraints,
        )

    def valid(self):
        """ Return whether there are no conflicting entries in the grid. """
        # standard constraints
        if not unique_rows(self.grid): return False
        if not unique_cols(self.grid): return False
        if not unique_boxes(self.grid): return False

        for constraint in self.additional_constraints:
            if not constraint(self):
                return False

        return True

    def complete(self):
        """ Return whether grid is completely filled out. """
        return None not in self.grid

    def check(self):
        """ Return whether grid is complete and valid. """
        return self.valid() and self.complete()

    def __str__(self):
        top = '\u250c' + (('\u2500' * 7) + '\u252c') * 2 + '\u2500' * 7 + '\u2510'
        horizontal_divider = '\u251C' + (('\u2500' * 7) + '\u253c') * 2 + '\u2500' * 7 + '\u2524'
        bot = '\u2514' + (('\u2500' * 7) + '\u2534') * 2 + '\u2500' * 7 + '\u2518'

        rows = []
        def triple_to_string(t):
            return (
                (str(t[0]) if t[0] else ' ') + ' ' +
                (str(t[1]) if t[1] else ' ') + ' ' +
                (str(t[2]) if t[2] else ' ')
            )
        for i in range(9):
            rows.append(
                '\u2502 ' +
                triple_to_string(self.grid[i*9+0 : i*9+3]) +
                ' \u2502 ' +
                triple_to_string(self.grid[i*9+3 : i*9+6]) +
                ' \u2502 ' +
                triple_to_string(self.grid[i*9+6 : i*9+9]) +
                ' \u2502'
            )

        constraints = ''
        if len(self.additional_constraints) > 0:
            constraints = '\nAdditional constraints:\n' + '\n'.join([
                '- ' + constraint for constraint in self.additional_constraints
            ])

        return '\n'.join([
            top,
            rows[0], rows[1], rows[2],
            horizontal_divider,
            rows[3], rows[4], rows[5],
            horizontal_divider,
            rows[6], rows[7], rows[8],
            bot,
        ]) + constraints

