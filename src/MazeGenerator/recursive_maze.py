from maze_cell import MazeCell, Direction
from maze_generator import MazeGenerator
from random import choice

class RecursiveMaze(MazeGenerator):
    def __init__(self, rows, cols):
        super.__init__(rows, cols)

    def gen_maze(self):
        self.visit_cell(0, 0, Direction.START)

    def visit_cell(self, r, c, move):
        available_moves = []
        available_count = 0
        begin = True
        while available_count > 0 or begin:
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
                if direction == Direction.Start:
                    break
                elif direction == Direction.RIGHT:
                    self.visit_cell(self, r, c+1, Direction.RIGHT)
                elif direction == Direction.FRONT:
                    self.visit_cell(self, r+1, c, Direction.FRONT)
                elif direction == Direction.LEFT:
                    self.visit_cell(self, r, c-1, Direction.LEFT)
                elif direction == Direction.BACK:
                    self.visit_cell(self, r-1, c, Direction.BACK)