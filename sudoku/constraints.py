
def unique_rows(grid):
    for i in range(9):
        if not unique_row(grid, i):
            return False
    return True

def unique_cols(grid):
    for i in range(9):
        if not unique_col(grid, i):
            return False
    return True

def unique_boxes(grid):
    for i in range(9):
        if not unique_box(grid, i):
            return False
    return True


def _unique_list(l):
    """ Return True if all entries in the list are different ignorning None. """
    seen = set()
    return not any(
        i in seen or seen.add(i) for i in l if i is not None
    )

def unique_row(grid, row):
    """ Return True if all digits in a row are unique.

    Rows are indexed from the top.
    """
    return _unique_list(grid[row*9 : row*9 + 9])

def unique_col(grid, col):
    """ Return True if all digits in a column are unique.

    Columns are indexed from the left.
    """
    return _unique_list((
        grid[row*9 + col] for row in range(9)
    ))

def unique_box(grid, box):
    """ Return True if all digits in the box are unique.

    Boxes are indexed left-to-right row-wise, i.e. box 4 is in the left column
    of the middle row.
    """
    box_row = int(box / 3)
    box_col = box % 3
    return _unique_list((
        grid[(box_row*3+0)*9 + box_col*3 + 0],
        grid[(box_row*3+0)*9 + box_col*3 + 1],
        grid[(box_row*3+0)*9 + box_col*3 + 2],

        grid[(box_row*3+1)*9 + box_col*3 + 0],
        grid[(box_row*3+1)*9 + box_col*3 + 1],
        grid[(box_row*3+1)*9 + box_col*3 + 2],

        grid[(box_row*3+2)*9 + box_col*3 + 0],
        grid[(box_row*3+2)*9 + box_col*3 + 1],
        grid[(box_row*3+2)*9 + box_col*3 + 2],
    ))
