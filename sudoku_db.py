import sqlite3
import json

# Create the database and table if they don't exist
def create_database():
    conn = sqlite3.connect('sudoku.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sudoku_boards (
        id INTEGER PRIMARY KEY,
        board TEXT,
        is_valid BOOLEAN,
        is_solved BOOLEAN
    )
    """)
    conn.commit()
    conn.close()

# Save a board to the database
def save_board(board, is_valid, is_solved):
    conn = sqlite3.connect('sudoku.db')
    cursor = conn.cursor()
    # Convert the board (list of lists) into a string format (e.g., JSON)
    board_str = json.dumps(board)
    cursor.execute("""
    INSERT INTO sudoku_boards (board, is_valid, is_solved)
    VALUES (?, ?, ?)
    """, (board_str, is_valid, is_solved))
    conn.commit()
    conn.close()

# Retrieve a board by its ID
def get_board_by_id(board_id):
    conn = sqlite3.connect('sudoku.db')
    cursor = conn.cursor()
    cursor.execute("SELECT board FROM sudoku_boards WHERE id = ?", (board_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])  # Convert the JSON string back to a list of lists
    return None

# Delete a board by its ID
def delete_board_by_id(board_id):
    conn = sqlite3.connect('sudoku.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sudoku_boards WHERE id = ?", (board_id,))
    conn.commit()
    conn.close()
