from enum import Enum
import time


class Direction(Enum):
    up = 1
    left = 2
    down = 3
    right = 4


def advance_cur(cur, direction):
    if direction == Direction.up:
        return cur - 9
    elif direction == Direction.left:
        return cur - 1
    elif direction == Direction.down:
        return cur + 9
    elif direction == Direction.right:
        return cur + 1

def advance_left(direction):
    if direction == Direction.up:
        return Direction.left
    elif direction == Direction.left:
        return Direction.down
    elif direction == Direction.down:
        return Direction.right
    elif direction == Direction.right:
        return Direction.up

def advance_right(direction):
    if direction == Direction.up:
        return Direction.right
    elif direction == Direction.left:
        return Direction.up
    elif direction == Direction.down:
        return Direction.left
    elif direction == Direction.right:
        return Direction.down


def spiral_path(advance_direction=advance_left):
    cur = 4*9 + 4
    path = [cur]

    dir = Direction.right
    leg = 1
    ctr = 0

    while len(path) < 80:
        for i in range(leg):
            cur = advance_cur(cur, dir)
            path.append(cur)

        dir = advance_direction(dir)

        # increase leg length every two legs
        ctr += 1
        if ctr >= 2:
            leg += 1
            ctr = 0

    return path[:81]


class BacktrackingSolver:
    LINEAR_PATH = list(range(81))
    INVERSE_LINEAR_PATH = LINEAR_PATH[::-1]
    LEFT_SPIRAL_PATH = spiral_path(advance_left)
    RIGHT_SPIRAL_PATH = spiral_path(advance_right)

    def __init__(self, grid, path=LINEAR_PATH):
        self.grid = grid

        self.trail = []
        self.path = path

        self.ticks = 0
        self.ticks_start = time.time()
        self.tps = 0

    def solve(self):
        grid = self.grid

        if grid.complete():
            return grid
        if not grid.valid():
            raise ValueError('invalid puzzle submitted')

        self.calculate_trail()

        return self.backtrack_position(grid)

    def backtrack_position(self, base_grid, level=0, track=''):
        idx = self.trail[level]

        for i in range(9):
            next_track = track + str(i+1)
            if level < 30:
                print(f'Trying {next_track}... {self.tps} tries/s', end='\r')

            # insert digit and check resulting grid
            grid = base_grid.copy()
            grid.grid[idx] = i+1
            if not grid.valid():
                continue
            if grid.complete():
                return grid

            self.tick()

            result = self.backtrack_position(grid, level+1, next_track)
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

    def calculate_trail(self):
        grid = self.grid.grid

        trail = []
        for pos in self.path:
            if grid[pos] is None:
                trail.append(pos)

        self.trail = trail
