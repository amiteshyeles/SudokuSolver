from Sudoku import Sudoku
from GeneralSudokuFunctions import *
class SudokuSolver:

	def __init__(self):
		self.game = Sudoku()
		self.pencilBoard = [ [set([1,2,3,4,5,6,7,8,9]) for i in range(self.game.getNumRows())] for j in range(self.game.getNumCols())]
		self.queue = [i for i in range(81)]
		self.updatePencilBoard()
		print(self.pencilBoard)
		print(self.game.getBoard())
		self.solver()

	def solver(self):
		i = 0
		while not isSolution(self.game.getBoard()):
			if not self.fillObvious():
				print("there are no more obvious choices")
				break

		print(self.game.getBoard())

	def fillObvious(self):
		out = False
		for r, row in enumerate(self.pencilBoard):
			for c, options in enumerate(row):
				if len(options) == 1:
					self.game.markCell(r, c, options.pop())
					options.discard(self.game.get(r, c))
					out = True
		self.updatePencilBoard()
		#print(self.pencilBoard)
		return out

	def updatePencilBoard(self):
		board = self.game.getBoard()
		for r in range(self.game.getNumRows()):
			for c in range(self.game.getNumCols()):
				if board[r][c] != None:
					self.pencilBoard[r][c] = set()
				diff = set()
				for i in self.pencilBoard[r][c]:
					self.game.markCell(r, c, i)
					if not (safeBox(board, r, c) and safeCol(board, c) and safeRow(board, r)):
						#self.pencilBoard[r][c].discard(i)
						diff.add(i)
					self.game.markCell(r, c, None)
				self.pencilBoard[r][c] = self.pencilBoard[r][c].difference(diff)

	def clearRowOptions(self, r, c, value):
		for options in self.pencilBoard[r]:
			if c != 0:
				options.discard(value)
			c -= 1

	def clearColOptions(self, r, c, value):
		for row in self.pencilBoard:
			if r != 0:
				row[c].discard(value)
			r -= 1

	def clearBoxOptions(self, r, c, value):
		row, col = getBoxCoor(r, c)
		for i in range(3):
			for j in range(3):
				if r - row != i or c - col != j:
					self.pencilBoard[row + i][col + j].discard(value)

s = SudokuSolver()