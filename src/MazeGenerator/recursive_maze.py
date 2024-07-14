from maze_cell import MazeCell, Direction
from maze_generator import MazeGenerator

class RecursiveMaze(MazeGenerator):
    def __init__(self, rows, cols):
        super.__init__(rows, cols)