import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import MazeGenerator.maze_spawner as ms

# Graph is dictionary of cell Id and adjacent cells (b,r,l,f)
# Also consider cell right is from looking face on but front is as if a player was entering the maze (l <-> r)
graph = ms.graph
entrance = ms.entrance
exit = ms.exit
goal = False

r, c = 0, 0
cell = f"{r}-{c}"

while not goal:
    moves = graph[cell].split(",")
    print(moves)
    moves = sorted(list(zip([3,2,0,1], moves))) # moves now {l, f, r, b}
    print(moves)

    goal = True if [r, c] == exit else False
    goal = True
