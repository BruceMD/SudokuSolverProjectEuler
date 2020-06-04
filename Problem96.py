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

def printGrid(grid):
	for line in grid:
		for num in line:
			if len(num) > 1:
				print("_", end="|")
			else:
				print(num[0], end="|")
		print("")

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
