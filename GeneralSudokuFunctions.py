#GeneralSudokuFunctions.py

def safeRow(board, r):
	seen = set()
	for value in board[r]:
		if value != None:
			if value in seen:
				return False
			seen.add(value)
	return True

def safeCol(board, c):
	seen = set()
	for row in board:
		if row[c] != None:
			if row[c] in seen:
				return False
			seen.add(row[c])
	return True

def safeBox(board, r, c):
	row, col = getBoxCoor(r, c)
	seen = set()
	for r in range(3):
		for c in range(3):
			if board[row + r][col + c] != None:
				if board[row + r][col + c] in seen:
					return False
				seen.add(board[row + r][col + c])
	return True

def getBoxCoor(r, c):
	return ((r // 3) * 3, (c // 3) * 3)

def isSolution(board):
	for i in range(9):
		if not safeRow(board,i):
			return False
		if not safeCol(board,i):
			return False

	for r in range(0, 9, 3):
		for c in range(0, 9, 3):
			if not safeBox(board, r, c):
				return False
	for r in range(9):
		for c in range(9):
			if board[r][c] == None:
				return False
	return True