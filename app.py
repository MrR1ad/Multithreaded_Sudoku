from flask import Flask, request, jsonify
from sudoku_db import create_database, save_board, get_board_by_id
from sudoku_solver import validate_sudoku_multithreaded, solve_sudoku

app = Flask(__name__)

# Initialize the database
create_database()

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Sudoku API! Use the following routes: /api/save, /api/validate/<board_id>, /api/solve/<board_id>"})


@app.route('/api/save', methods=['POST'])
def save_board_api():
    data = request.json
    board = data.get('board', [])
    save_board(board, is_valid=True, is_solved=False)
    return jsonify({"message": "Board saved successfully."})

@app.route('/api/validate/<int:board_id>', methods=['GET'])
def validate_board_api(board_id):
    board = get_board_by_id(board_id)
    if not board:
        return jsonify({"message": "Board not found."}), 404

    is_valid = validate_sudoku_multithreaded(board)
    return jsonify({"is_valid": is_valid})

@app.route('/api/solve/<int:board_id>', methods=['GET'])
def solve_board_api(board_id):
    board = get_board_by_id(board_id)
    if not board:
        return jsonify({"message": "Board not found."}), 404

    if validate_sudoku_multithreaded(board):
        is_solved = solve_sudoku(board)
        save_board(board, is_valid=True, is_solved=is_solved)
        return jsonify({"is_solved": is_solved, "board": board})
    else:
        return jsonify({"message": "Invalid Sudoku board."}), 400

if __name__ == "__main__":
    app.run(debug=True)
