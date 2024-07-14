from enum import Enum

class Direction(Enum):
    START = 0
    RIGHT = 1
    FRONT = 2
    LEFT = 3
    BACK = 4

class MazeCell:
    visited = False
    wall_right = False
    wall_front = False
    wall_left = False
    wall_back = False