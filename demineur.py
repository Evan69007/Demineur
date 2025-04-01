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


if __name__ == "__main__":
	columns = 10
	lines = 10
	grid = gridGenerator(columns, lines, "0")
	playerGrid = gridGenerator(columns, lines, "-")

	grid = addBombs(grid, 6, "1")

	printGrid(playerGrid)
	while True:
		print("Enter coordinates to open a case")
		coordinateX = input("Enter lign between 1 to "+ str(columns) + " : ")
		coordinateY = input("Enter column between 1 to "+ str(lines) + " : ")

		case(int(coordinateX)-1, int(coordinateY)-1)
		printGrid(playerGrid)
