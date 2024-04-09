def is_valid(board, row, col, num):
    #TODO: Check if the num is already present in the row
  
    
    #TODO: Check if the num is already present in the column
    
    
    #TODO: Check if the num is already present in the 3x3 sub-grid
    
    
    return True

def solve_sudoku_util(board):
    #TODO: Find the next empty cell


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
