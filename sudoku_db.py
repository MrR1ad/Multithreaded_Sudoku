import sqlite3
import json

# Function to create the database and the table
def create_database():
    conn = sqlite3.connect('sudoku.db')
    cursor = conn.cursor()

    # Create the sudoku_boards table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sudoku_boards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        board TEXT NOT NULL,
        is_valid BOOLEAN NOT NULL,
        is_solved BOOLEAN NOT NULL
    )''')

    conn.commit()
    conn.close()
    print("Database and table created successfully.")

# Function to save the board to the database
def save_board(board, is_valid=True, is_solved=False):
    conn = sqlite3.connect('sudoku.db')
    cursor = conn.cursor()

    # Insert the board into the table (convert the board to JSON format before inserting)
    cursor.execute("INSERT INTO sudoku_boards (board, is_valid, is_solved) VALUES (?, ?, ?)",
                   (json.dumps(board), is_valid, is_solved))

    conn.commit()
    conn.close()
    print("Board saved to database.")

# Function to retrieve a board by its ID from the database
def get_board_by_id(board_id):
    conn = sqlite3.connect('sudoku.db')
    cursor = conn.cursor()

    # Fetch the board from the database
    cursor.execute("SELECT board FROM sudoku_boards WHERE id = ?", (board_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return json.loads(row[0])  # Convert JSON string back to a list of lists
    return None
