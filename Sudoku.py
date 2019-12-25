import GameSettings as gs
from GeneralSudokuFunctions import *
class Sudoku:
	
	def __init__(self):
		# set a random board ... for now just use the one I am inputting
		self.board = [ [None for i in range(gs.rows)] for j in range(gs.columns)]
		#self.solution = [ [None for i in range(gs.rows)] for j in range(gs.columns)]
		self.setupSampleCase()

	def markCell(self, r, c, val):
		self.board[r][c] = val

	def getBoard(self):
		return self.board

	def getNumRows(self):
		return len(self.board)

	def getNumCols(self):
		return len(self.board[0])

	def get(self, r, c):
		return self.board[r][c]

	def setupSampleCase(self):
		"""self.board = [[None, None,    5, None, None, None,    9, None, None],
											  [None, None,    4,    6,    9, None,    1, None, None],
											  [   7,    9, None, None, None, None, None, None, None],
											  [None,    1, None,    2, None, None, None, None,    3],
											  [None,    7, None, None, None,    6, None,    8, None],
											  [None, None, None, None,    1,    4,    6, None,    2],
											  [   2,    3, None, None, None,    8, None, None, None],
											  [None, None, None, None,    5, None, None, None,    7],
											  [None, None, None,    4, None,    3, None,    1, None]
											 ]
						"""
		self.board = [[   5,    3, None, None,    7, None, None, None, None],
					  [   6, None, None,    1,    9,    5, None, None, None],
					  [None,    9,    8, None, None, None, None,    6, None],
					  [   8, None, None, None,    6, None, None, None,    3],
					  [   4, None, None,    8, None,    3, None, None,    1],
					  [   7, None, None, None,    2, None, None, None,    6],
					  [None,    6, None, None, None, None,    2,    8, None],
					  [None, None, None,    4,    1,    9,  None, None,   5],
					  [None, None, None, None,    8, None,  None,    7,   9]
					 ]
		self.solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
						 [6, 7, 2, 1, 9, 5, 3, 4, 8],
						 [1, 9, 8, 3, 4, 2, 5, 6, 7],
						 [8, 5, 9, 7, 6, 1, 4, 2, 3],
						 [4, 2, 6, 8, 5, 3, 7, 9, 1],
						 [7, 1, 3, 9, 2, 4, 8, 5, 6],
						 [9, 6, 1, 5, 3, 7, 2, 8, 4],
						 [2, 8, 7, 4, 1, 9, 6, 3, 5],
						 [3, 4, 5, 2, 8, 6, 1, 7, 9]
						]
		

#testing script

game = Sudoku()
print(isSolution(game.getBoard()))




