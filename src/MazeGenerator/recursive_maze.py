import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MazeGenerator.maze_cell import Direction
from MazeGenerator.maze_generator import MazeGenerator
from random import choice, randint

class RecursiveMaze(MazeGenerator):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.entrance, self.exit = self.set_entrance_n_exit()
    
    def set_entrance_n_exit(self):
        start = [self.row_count-1, randint(0, self.col_count-1)]
        end = [0, randint(0, self.col_count-1)]
        return start, end

    def gen_maze(self):
        self.visit_cell(0, 0, Direction.START)

    def visit_cell(self, r, c, move):
        available_moves = []
        available_count = 0
        begin = True
        while available_count > 0 or begin:
            begin = False
            available_count = 0
            if c + 1 < self.col_count and not self.get_cell(r, c+1).visited:
                available_moves.append(Direction.RIGHT)
                available_count += 1
            elif not self.get_cell(r, c).visited and move != Direction.LEFT:
                self.get_cell(r, c).wall_right = True
            
            if r + 1 < self.row_count and not self.get_cell(r+1, c).visited:
                available_moves.append(Direction.FRONT)
                available_count += 1
            elif not self.get_cell(r, c).visited and move != Direction.BACK:
                self.get_cell(r, c).wall_front = True

            if c > 0 and c - 1 >= 0 and not self.get_cell(r, c-1).visited:
                available_moves.append(Direction.LEFT)
                available_count += 1
            elif not self.get_cell(r, c).visited and move != Direction.RIGHT:
                self.get_cell(r, c).wall_left = True

            if r > 0 and r - 1 >= 0  and not self.get_cell(r-1, c).visited:
                available_moves.append(Direction.BACK)
                available_count += 1
            elif not self.get_cell(r, c).visited and move != Direction.FRONT:
                self.get_cell(r, c).wall_back = True

            self.get_cell(r, c).visited = True

            if available_count > 0:
                direction = choice(available_moves)
                if direction == Direction.START:
                    break
                elif direction == Direction.RIGHT:
                    self.visit_cell(r, c+1, Direction.RIGHT)
                elif direction == Direction.FRONT:
                    self.visit_cell(r+1, c, Direction.FRONT)
                elif direction == Direction.LEFT:
                    self.visit_cell(r, c-1, Direction.LEFT)
                elif direction == Direction.BACK:
                    self.visit_cell(r-1, c, Direction.BACK)
