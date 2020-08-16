from puzzles.classic1 import puzzle

from sudoku.solver import BacktrackingSolver


print('Grid:')
print(puzzle)
print()

bt = BacktrackingSolver(puzzle)
result = bt.solve()
print()

print('Resulting grid:')
print(result)
