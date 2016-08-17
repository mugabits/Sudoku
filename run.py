from board import SudokuBoard
from config import BoardConfiguration
from sudoku import SudokuNumbers

sudoku_board = SudokuBoard("*", "-" , "|")
# sudoku_board.draw_empty_board(9,9)
sudoku_board.create_board()

for _ in range(9):
	sudoku_board.draw_one_square()
print(sudoku_board._row() + sudoku_board.vertex)

