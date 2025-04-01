import random

def addBombs(grid, nb_bombes, bombe_character):
	nb_case_bombe = 0
	while nb_case_bombe < nb_bombes:
		i = random.randint(0, len(grid) - 1)
		j = random.randint(0, len(grid[i]) - 1)
		if grid[i][j] != bombe_character:
			grid[i][j] = bombe_character
			nb_case_bombe += 1
	return (grid)

def gridGenerator(largeur, hauteur, char):
	grid = []
	i = 0
	for i in range(hauteur):
		j = 0
		grid.append([])
		for j in range(largeur):
			grid[i].append(char)
			j += 1
		i += 1
	return grid

def printGrid(grid):
	i = 0
	for i in range(len(grid)):
		print(' | '.join(grid[i]))
		print("")
		i += 1
	return

def case(x, y):
    if x >= 0 and x < len(grid):
        if y >= 0 and y < len(grid[x]):
            playerGrid[x][y] = grid[x][y]
        else:
            print("Out of the grid! Play again")
    else:
        print("Out of the grid! Play again")

def hasLost(x, y, bomb_char):
	if grid[x][y] == bomb_char:
		return True
	return False

def hasWon(empty_char):
	i = 0
	for i in range(len(grid)):
		j = 0
		for j in range(len(grid[i])):
			if playerGrid[i][j] == "-":
				if grid[i][j] == empty_char:
					return (False)
			j += 1
		i += 1
	return (True)

def count_mines(grid, x, y, bomb_char):
    # Directions for 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),           (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    
    mine_count = 0
    
    for dr, dc in directions:
        neighbor_x = x + dr
        neighbor_y = y + dc
        
        # Check if the neighbor is within bounds of the grid
        if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]):
            if grid[neighbor_x][neighbor_y] == bomb_char:  # Mine found
                mine_count += 1
    return mine_count

if __name__ == "__main__":
	columns = int(input("Enter column number for the game: "))
	lines = int(input("Enter line number for the game: "))
	bombs = int(input("Enter bomb number for the game: "))
	grid = gridGenerator(columns, lines, "0")
	playerGrid = gridGenerator(columns, lines, "-")

	grid = addBombs(grid, bombs, "1")

	print("grid generated")
	printGrid(playerGrid)
	while True:
		print("Enter coordinates to open a case")
		coordinateX = int(input("Enter lign between 1 to "+ str(columns) + " : "))
		coordinateY = int(input("Enter column between 1 to "+ str(lines) + " : "))

		case(coordinateX - 1, coordinateY - 1)
		printGrid(playerGrid)
		if (hasLost(coordinateX - 1, coordinateY - 1, "1")):
			print("Sorry, you lost")
			break
		elif (hasWon("0")):
			print("Congrats, You Won")
			break
		else:
			playerGrid[coordinateX - 1][coordinateY - 1] = str(count_mines(grid, coordinateX - 1, coordinateY - 1, "1"))
		
