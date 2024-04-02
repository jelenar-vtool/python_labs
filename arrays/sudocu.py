def is_valid(board, row, col, num):
    # Check if the num is already present in the row
    if num in board[row]:
        return False
    
    # Check if the num is already present in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the num is already present in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku_util(board):
    # Find the next empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku_util(board):
                            return True
                        # Backtrack
                        board[i][j] = 0
                return False
    return True

def solve_sudoku(board):
    if solve_sudoku_util(board):
        return True
    else:
        return False

def print_board(board):
    for row in board:
        print(row)

if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(board):
        print("Sudoku solved successfully:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku board.")
"""
Write a Python function solve_sudoku(board) that takes a 9x9 Sudoku board represented as a 2D list of integers board as input.
The function should solve the Sudoku puzzle and modify the board in place to contain the solved puzzle.
The Sudoku board is represented as a 9x9 grid, where each cell contains an integer from 1 to 9 or 0 (indicating an empty cell).
The solution should satisfy the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The function should return True if the Sudoku puzzle is solvable and False if it is unsolvable.
"""