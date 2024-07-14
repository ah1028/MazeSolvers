import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MazeGenerator.recursive_maze import RecursiveMaze

recursive_maze = RecursiveMaze(rows=10, cols=10)
recursive_maze.gen_maze()
print(recursive_maze.maze[0][0].visited)