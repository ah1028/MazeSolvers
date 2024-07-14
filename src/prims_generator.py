#=======RANDOM MAZE GENERATION ALGORTIHM=======#
#===============PRIM'S ALGORITHM===============#

# Old implementation of Prim's to be used for maze solving algorithms
# To be updated

#Import libraries
import random

#Procedure prints the maze    
def print_maze(maze, height, width):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                print(str(maze[i][j]), end=" ")
            elif (maze[i][j] == ' '):
                print(str(maze[i][j]), end=" ")
            else:
                print(str(maze[i][j]), end=" ")
        print('\n')

# Find number of surrounding cells
def surrounding_cells(maze, rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == ' '):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == ' '):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == ' '):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == ' '):
		s_cells += 1

	return s_cells

def generate_maze():
    ## Main code
	# Init variables
	wall = '#'
	cell = ' '
	unvisited = 'u'
	height = 11
	width = 27
	maze = []


	# Denote all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		maze.append(line)

	# Randomize starting point and set it a cell
	starting_height = int(random.random()*height)
	starting_width = int(random.random()*width)
	if (starting_height == 0):
		starting_height += 1
	if (starting_height == height-1):
		starting_height -= 1
	if (starting_width == 0):
		starting_width += 1
	if (starting_width == width-1):
		starting_width -= 1

	# Mark it as cell and add surrounding walls to the list
	maze[starting_height][starting_width] = cell
	walls = []
	walls.append([starting_height - 1, starting_width])
	walls.append([starting_height, starting_width - 1])
	walls.append([starting_height, starting_width + 1])
	walls.append([starting_height + 1, starting_width])

	# Denote walls in maze
	maze[starting_height-1][starting_width] = '#'
	maze[starting_height][starting_width - 1] = '#'
	maze[starting_height][starting_width + 1] = '#'
	maze[starting_height + 1][starting_width] = '#'

	while (walls):
		# Pick a random wall
		rand_wall = walls[int(random.random()*len(walls))-1]

		# Check if it is a left wall
		if (rand_wall[1] != 0):
			if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == ' '):
				# Find the number of surrounding cells
				s_cells = surrounding_cells(maze, rand_wall)

				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = ' '

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != ' '):
							maze[rand_wall[0]-1][rand_wall[1]] = '#'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])


					# Bottom cell
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != ' '):
							maze[rand_wall[0]+1][rand_wall[1]] = '#'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):	
						if (maze[rand_wall[0]][rand_wall[1]-1] != ' '):
							maze[rand_wall[0]][rand_wall[1]-1] = '#'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
				

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check if it is an upper wall
		if (rand_wall[0] != 0):
			if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == ' '):

				s_cells = surrounding_cells(maze, rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = ' '

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != ' '):
							maze[rand_wall[0]-1][rand_wall[1]] = '#'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != ' '):
							maze[rand_wall[0]][rand_wall[1]-1] = '#'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])

					# Rightmost cell
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != ' '):
							maze[rand_wall[0]][rand_wall[1]+1] = '#'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check the bottom wall
		if (rand_wall[0] != height-1):
			if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == ' '):

				s_cells = surrounding_cells(maze, rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = ' '

					# Mark the new walls
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != ' '):
							maze[rand_wall[0]+1][rand_wall[1]] = '#'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != ' '):
							maze[rand_wall[0]][rand_wall[1]-1] = '#'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != ' '):
							maze[rand_wall[0]][rand_wall[1]+1] = '#'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)


				continue

		# Check the right wall
		if (rand_wall[1] != width-1):
			if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == ' '):

				s_cells = surrounding_cells(maze, rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = ' '

					# Mark the new walls
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != ' '):
							maze[rand_wall[0]][rand_wall[1]+1] = '#'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != ' '):
							maze[rand_wall[0]+1][rand_wall[1]] = '#'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[0] != 0):	
						if (maze[rand_wall[0]-1][rand_wall[1]] != ' '):
							maze[rand_wall[0]-1][rand_wall[1]] = '#'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Delete the wall from the list anyway
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)
		


	# Mark the remaining unvisited cells as walls
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				maze[i][j] = '#'

	# Set entrance and exit
	for i in range(0, width):
		if (maze[1][i] == ' '):
			maze[0][i] = ' '
			break

	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == ' '):
			maze[height-1][i] = ' '
			break

	return maze