import random


def main():
	sudokuDic = {}
	tempKey = ""
	with open('C:\\Users\\ASUS\\Desktop\\ProjectEuler\\p096_sudoku.txt', 'r') as file:
		for line in file.readlines():
			if line[0] == "G":
				tempKey = line.strip("\n")
				sudokuDic[tempKey] = []
			else:
				sudokuDic[tempKey] += convert(line.strip("\n"))
	
	
	printGrid(gridGen(sudokuDic["Grid 01"]))
	print()
	printGrid(solve(gridGen(sudokuDic["Grid 01"])))
	
def solve(grid):					# get all options for all numbers in each cell
#	printGridFull(grid)
#	print()
	for i in range(9):
		for j in range(9):
			if len(grid[i][j]) > 1:
				for num in grid[i][j]:
					if resolve(num, i, j, grid):
						grid[i][j].remove(num)
						return solve(grid)
	
	return grid
	
def resolve(num, i, j, grid):			# if num at i, j matches anything in the rows, columns or blocks then return True, there is a match, remove it from list of options
	for k in range(9):
		if [num] == grid[k][j] or [num] == grid[i][k]:
			return True
	for l in block(i):
		for m in block(j):
			if [num] == grid[l][m]:
				return True
	return False

def block(num):
	if num in [0, 1, 2]:
		return [0, 1, 2]
	elif num in [3, 4, 5]:
		return [3, 4, 5]
	else:
		return [6, 7, 8]

def printGrid(grid):
	for line in grid:
		for num in line:
			if len(num) > 1:
				print("_", end="|")
			else:
				print(num[0], end="|")
		print("")

def printGridFull(grid):
	for line in grid:
		for num in line:
			if len(num) > 1:
				print(num, end="|")
			else:
				print(num[0], end="|")
		print()

def gridGen(numLis):
	grid = []
	tempLine = []
	for i in range(81):
		if numLis[i] == 0:
			tempLine.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
		else:
			tempLine.append([numLis[i]])
		if (i + 1) % 9 == 0:
			grid.append(tempLine)
			tempLine = []
	#			print(grid)
	return grid

def convert(name):
	lis = []
	for c in name:
		lis.append(int(c))
	return lis


if __name__ == '__main__':
	main()
