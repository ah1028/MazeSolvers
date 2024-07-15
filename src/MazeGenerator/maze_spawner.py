import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MazeGenerator.recursive_maze import RecursiveMaze

graph = {}
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
        id = f"{r}-{c}"
        tmpStr = ""     # "b,r,l,f"
        tmpId = ""      # Cell ID to be added to tmpStr

        if cell.wall_back:
            maze_representation[r*2][c*2+1] = "# "
            maze_representation[r*2][c*2+2] = "# "
            tmpId = ","
        elif r-1>=0 and not maze[r-1][c].wall_front:
            tmpId = f"{r-1}-{c},"
        else:
            tmpId = ","
        tmpStr += tmpId
        tmpId = ""

        if cell.wall_right:
            maze_representation[r*2+1][c*2+2] = "# "
            maze_representation[r*2+2][c*2+2] = "# "
        elif c < cols-1 and not maze[r][c+1].wall_left:
            tmpId = f"{r}-{c+1},"
        else:
            tmpId = ","
        tmpStr += tmpId
        tmpId = ""

        if cell.wall_left:
            maze_representation[r*2+1][c*2] = "# "
            maze_representation[r*2][c*2] = "# "
            tmpId = ","
        elif c-1>=0 and not maze[r][c-1].wall_right:
            tmpId = f"{r}-{c-1},"
        else:
            tmpId = ","
        tmpStr += tmpId
        tmpId = ""
        
        if cell.wall_front:
            maze_representation[r*2+2][c*2+1] = "# "
            maze_representation[r*2+2][c*2] = "# "
        elif r+1<rows and not maze[r+1][c].wall_back:
            tmpId = f"{r+1}-{c}"
        tmpStr += tmpId

        graph[id] = tmpStr

# Set entrance and exit
# Entrance is at top of maze
maze_representation[0][entrance[1]*2+1] = "  "
maze_representation[rows*2][exit[1]*2+1] = "  "

for r in range(rows * 2 + 1):
    print("".join(maze_representation[r]))
