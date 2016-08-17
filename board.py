import random
from config import BoardConfiguration
		
class SudokuBoard(object):
	def __init__(self, vertex, row_sep, column_sep):
		self.vertex = vertex
		self.row_sep = row_sep
		self.column_sep = column_sep
	
	def draw_empty_board(self, rows, columns):
		for _ in range(rows):
			print(columns*self._row() + self.vertex) 
			print(columns*self.draw_empty_cell() + self.column_sep) 
		print(columns*self._row() + self.vertex)
		
	def _row(self):
		return self.vertex + 4 * self.row_sep
		
	def _middle(self, number=1):
		# number = (str(random.randrange(0,10)) + 2 * " ") if fill else (3 * " ")
		return self.column_sep + " " + number + 2 * " "
	
	def draw_empty_cell(self):
		return self.column_sep + 4 * " "
		
	def draw_one_square(self):
		print(self._row() + self.vertex),
		print(self._middle(number=self.get_num()) + self.column_sep)

	def draw_board(self):
		for _ in range(9):
			print(9 * self._row() + self.vertex),
			
			for _ in range(9):	
				print(9 * self._middle(number=self.get_num()) + self.column_sep)
				# print(self._middle(number=self.get_num()) + self.column_sep),
				# print(self._middle(number=self.get_num()) + self.column_sep)
		print(9 * self._row() + self.vertex)	
		
	def create_board(self):
		"""
			1. Create unique solution to sudoku
			2. Based on difficulty, delete members of the sudoku board
			3. Print the final sudoku board
		"""
		
		print("This will print the board ready for playing.")
		
		
	def get_num(self):
		return str(random.randrange(1,10))
	
