from MazeGenerator.maze_cell import MazeCell
from abc import ABC, abstractmethod


class MazeGenerator(ABC):
    def __init__(self, rows, cols):
        self.row_count = abs(rows)
        self.col_count = abs(cols)
        self.maze = self.maze_generator()

    def maze_generator(self):
        # Minimum maze size 1x1
        self.row_count = 1 if self.row_count == 0 else self.row_count
        self.col_count = 1 if self.col_count == 0 else self.col_count

        return [[MazeCell() for _ in range(self.col_count)] for _ in range(self.row_count)]

    @abstractmethod
    def gen_maze(self):
        pass

    def get_cell(self, r, c):
        if r >= 0 and r < self.row_count and c >= 0 and c < self.col_count:
            return self.maze[r][c]
        else:
            print("error")