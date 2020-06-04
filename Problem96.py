import random

randomCheck = True				# global variable for randomGuess() if True, first time performing random go
randomSkip = []					# list of i, j indices that didn't work on the first time
randomBackUp = []				# global backUp for randomGuess()

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
	
	for key in sudokuDic.keys():
		print(key)
		printGrid(gridGen(sudokuDic[key]))
		print()
		printGrid(solve(gridGen(sudokuDic[key])))

	
def solve(grid):					# get all options for all numbers in each cell, recursive until it can't do anymore
	for i in range(9):
		for j in range(9):
			if len(grid[i][j]) > 1:
				for num in grid[i][j]:
					if resolve(num, i, j, grid):
						grid[i][j].remove(num)
						return solve(grid)
	if completeCheck(grid):
		return grid
	else:
		grid = eliminateBlock(grid)
		grid = eliminateRow(grid)
		grid = eliminateColumn(grid)
		if completeCheck(grid) == False and randomCheck:
#			printGridFull(grid)
			randomGuess(grid)
	return grid
	
def eliminateColumn(grid):
	for j in range(9):
		tempDic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		for i in range(9):
			if len(grid[i][j]) > 1:
				for dig in grid[i][j]:
					tempDic[dig] += 1
#		print(tempDic)
		for key, v in tempDic.items():
			if v == 1:
				for k in range(9):
					if key in grid[j][j]:
						grid[k][j] = [key]
						return solve(grid)
	return grid

def eliminateRow(grid):
	for i in range(9):
		tempDic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		for j in range(9):
			if len(grid[i][j]) > 1:
				for dig in grid[i][j]:
					tempDic[dig] += 1
#		print(tempDic)
		for key, v in tempDic.items():
			if v == 1:
				for k in range(9):
					if key in grid[i][k]:
						grid[i][k] = [key]
						return solve(grid)
	return grid

def eliminateBlock(grid):
	blocks = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
	for blocX in blocks:
		for blocY in blocks:					# cycle through each 3 by 3 grid
#			print(blocX, blocY)
			tempDic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
			for i in blocX:
				for j in blocY:					# make a list of all the contents I suppose
					if len(grid[i][j]) > 1:
						for dig in grid[i][j]:
							tempDic[dig] += 1
#			print(tempDic)
			for key, v in tempDic.items():
				if v == 1:
					for i in blocX:
						for j in blocY:
							if key in grid[i][j]:
								grid[i][j] = [key]
								return solve(grid)
	return grid

def randomGuess(grid):			# nudge approach
	global randomBackUp			# lis[lis[]]
	global randomCheck			# boolean
	
	randomCheck = False
	print("We are GUESSING!!!!!!!!!!!!!!!!!!!!!")
	
	randomBackUp = grid
	tempInd = []
	
	for i in range(9):
		for j in range(9):
			if len(grid[i][j]) == 2:
				tempInd = grid[i][j]
				for k in range(2):
					grid[i][j] = [tempInd[k]]
					print(tempInd[k], i, j)
					if completeCheck(solve(grid)) and validate(solve(grid)):
						return
	
	return grid

def validate(grid):
	for i in range(9):
		tempDic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		for j in range(9):
			tempDic[grid[i][j][0]] += 1
		for v in tempDic.values():
			if v != 1:
				return False
	return True

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

def completeCheck(grid):		# return false if we are not finished
	count = 0
	for i in range(9):
		for j in range(9):
			if len(grid[i][j]) == 1:
				count += 1
			elif len(grid[i][j]) > 1:
				return False
	return (count == 81)

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
