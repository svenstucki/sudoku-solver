
class BacktrackingSolver:

    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        grid = self.grid

        if grid.complete():
            return grid
        if not grid.valid():
            raise ValueError('invalid puzzle submitted')

        start_idx = grid.grid.index(None)
        return self.backtrack_position(grid, start_idx, 0)

    def backtrack_position(self, base_grid, from_idx, level):
        for i in range(9):
            if level < 3:
                print(f'trying digit {"_"*level}{i+1}')

            # insert digit and check resulting grid
            grid = base_grid.copy()
            grid.grid[from_idx] = i+1
            if not grid.valid():
                continue
            if grid.complete():
                return grid

            next_idx = grid.grid.index(None)
            result = self.backtrack_position(grid, next_idx, level+1)
            if result:
                return result

        return None
