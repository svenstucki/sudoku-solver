import time


class BacktrackingSolver:

    def __init__(self, grid):
        self.grid = grid

        self.ticks = 0
        self.ticks_start = time.time()
        self.tps = 0

    def solve(self):
        grid = self.grid

        if grid.complete():
            return grid
        if not grid.valid():
            raise ValueError('invalid puzzle submitted')

        start_idx = grid.grid.index(None)
        return self.backtrack_position(grid, start_idx)

    def backtrack_position(self, base_grid, from_idx, level=0, track=''):
        for i in range(9):
            next_track = track + str(i+1)
            if level < 30:
                print(f'Trying {next_track}... {self.tps} tries/s', end='\r')

            # insert digit and check resulting grid
            grid = base_grid.copy()
            grid.grid[from_idx] = i+1
            if not grid.valid():
                continue
            if grid.complete():
                return grid

            self.tick()

            next_idx = grid.grid.index(None)
            result = self.backtrack_position(grid, next_idx, level+1, next_track)
            if result:
                return result

        return None

    def tick(self):
        self.ticks += 1

        clock = time.time()
        if clock - self.ticks_start >= 1.0:
            self.tps = int(self.ticks / (clock - self.ticks_start))

            self.ticks = 0
            self.ticks_start = clock
