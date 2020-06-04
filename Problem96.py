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


if __name__ == '__main__':
	main()
