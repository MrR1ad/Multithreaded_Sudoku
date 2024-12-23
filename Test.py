from sudoku_db import create_database, save_board, get_board_by_id
from sudoku_solver import validate_sudoku_multithreaded, solve_sudoku
from sudoku_db import save_board

# Example Sudoku board
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

# Save the board to the database
save_board(board, is_valid=True, is_solved=False)  # Initially marked as valid but not solved

def main(board_id):
    # Retrieve the board from the database
    board = get_board_by_id(board_id)
    if not board:
        print("Board not found.")
        return

    # Validate the board using multithreading
    if validate_sudoku_multithreaded(board):
        print("Sudoku board is valid.")
        is_solved = solve_sudoku(board)
        if is_solved:
            print("Sudoku solved:")
            for row in board:
                print(row)
        else:
            print("No solution exists.")
        save_board(board, is_valid=True, is_solved=is_solved)
    else:
        print("Sudoku board is invalid.")
        save_board(board, is_valid=False, is_solved=False)

if __name__ == "__main__":
    create_database()  # Ensure the database is created when running the script
    # Example: Assuming you have a board with ID 1 in the database
    main(1)
