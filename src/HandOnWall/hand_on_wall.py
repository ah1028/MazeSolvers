import sys
import os
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import MazeGenerator.maze_spawner as ms

# Graph is dictionary of cell Id and adjacent cells (b,r,l,f)
# Also consider cell right is from looking face on but front is as if a player was entering the maze (l <-> r)
graph = ms.graph
entrance = ms.entrance
exit = ms.exit

r, c = entrance
cell = f"{r}-{c}"
route = [cell]
i = 1 % 4
goal = True if [r, c] == exit else False

while not goal:
    can_move = False
    moves = graph[cell].split(",")
    moves = sorted(list(zip([2,3,1,0], moves))) # moves now {f, l, b, r}
    moves = [m for _, m in moves]


    if moves[i] != "":
        cell = moves[i]
        route.append(cell)
        r, c = cell.split("-")
        r, c = int(r), int(c)
        i = (i + 1) % 4
        can_move = True
    else:
        while not can_move:
            if moves [i-1] != "":
                cell = moves[i-1]
                route.append(cell)
                r, c = cell.split("-")
                r, c = int(r), int(c)
                can_move = True
            else:
                i = (i - 1) % 4

    goal = True if [r, c] == exit else False

dim = len(ms.maze_representation[0])*2
print("SOLUTION".center(dim, "="))
for r in range(len(ms.maze_representation)):
    print("".join(ms.solved_maze(route, ms.maze_representation, entrance, exit)[r]))
    