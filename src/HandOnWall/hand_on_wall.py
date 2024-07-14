import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from prims_generator import generate_maze, print_maze

maze = generate_maze()
print_maze(maze, 11, 27)
