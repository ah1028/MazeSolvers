import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MazeGenerator.recursive_maze import RecursiveMaze

rows = 5
cols = 3
recursive_maze = RecursiveMaze(rows=rows, cols=cols)
recursive_maze.gen_maze()
maze = recursive_maze.maze
exit = recursive_maze.entrance
entrance = recursive_maze.exit

maze_representation = [["  " for _ in range(cols * 2 + 1)] for _ in range(rows * 2 + 1)]

# Display maze
for r in range(rows):
    for c in range(cols):
        cell = maze[r][c]
        if cell.wall_back:
            maze_representation[r*2][c*2+1] = "# "
            maze_representation[r*2][c*2+2] = "# "
        if cell.wall_right:
            maze_representation[r*2+1][c*2+2] = "# "
            maze_representation[r*2+2][c*2+2] = "# "
        if cell.wall_left:
            maze_representation[r*2+1][c*2] = "# "
            maze_representation[r*2][c*2] = "# "
        if cell.wall_front:
            maze_representation[r*2+2][c*2+1] = "# "
            maze_representation[r*2+2][c*2] = "# "

# Set entrance and exit
# Entrance is at top of maze
maze_representation[0][entrance[1]*2+1] = "  "
maze_representation[rows*2][exit[1]*2+1] = "  "

for r in range(rows * 2 + 1):
    print("".join(maze_representation[r]))
