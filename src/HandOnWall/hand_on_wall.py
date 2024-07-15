import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import MazeGenerator.maze_spawner as ms

# Graph is dictionary of cell Id and adjacent cells (b,r,l,f)
# Also consider cell right is from looking face on but front is as if a player was entering the maze (l<->r)
graph = ms.graph

