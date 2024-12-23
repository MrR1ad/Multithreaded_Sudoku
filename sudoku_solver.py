import threading
from queue import Queue
import json

# Function to check if a number can be placed in a cell
def is_valid(board, row, col, num):
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Sudoku solving function with backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Tentative assignment

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0  # Backtrack
                return False  # No valid number found
    return True

# Validator function for multithreading
def validate_section(queue, result):
    while not queue.empty():
        section = queue.get()
        nums = set()
        for num in section:
            if num != 0:
                if num in nums:
                    result[0] = False
                    return
                nums.add(num)
        queue.task_done()

# Function to validate the Sudoku board using threads
def validate_sudoku_multithreaded(board):
    queue = Queue()
    result = [True]

    # Add rows to the queue
    for row in board:
        queue.put(row)

    # Add columns to the queue
    for col in range(9):
        queue.put([board[row][col] for row in range(9)])

    # Add subgrids to the queue
    for box_row in range(3):
        for box_col in range(3):
            queue.put([
                board[row][col]
                for row in range(box_row * 3, (box_row + 1) * 3)
                for col in range(box_col * 3, (box_col + 1) * 3)
            ])

    # Create and start threads
    threads = []
    for _ in range(9):
        thread = threading.Thread(target=validate_section, args=(queue, result))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return result[0]
