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

def gridGenerator(largeur, hauteur, nb_bombes):
	grid = []
	i = 0
	for i in range(hauteur):
		j = 0
		grid.append([])
		for j in range(largeur):
			grid[i].append("0")
			j += 1
		i += 1
	grid = addBombs(grid, nb_bombes, "1")
	return grid

def printGrid(grid):
	i = 0
	for i in range(len(grid)):
		print(' | '.join(grid[i]))
		i += 1
	return

grid = gridGenerator(8, 10, 10)

printGrid(grid)