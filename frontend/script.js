const board = document.getElementById("board");

// Predefined Sudoku board
const predefinedBoard = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9],
];

// Function to create and pre-fill the 9x9 grid of input fields
for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    const input = document.createElement("input");
    input.type = "number";
    input.min = "1";
    input.max = "9";
    input.dataset.row = i;
    input.dataset.col = j;

    // Fill input with predefined values or 0 if empty
    input.value = predefinedBoard[i][j] === 0 ? "" : predefinedBoard[i][j];

    board.appendChild(input);
  }
}

// Helper to get the board values from the grid
function getBoardValues() {
  const grid = [];
  for (let i = 0; i < 9; i++) {
    const row = [];
    for (let j = 0; j < 9; j++) {
      const value =
        document.querySelector(`input[data-row="${i}"][data-col="${j}"]`)
          .value || "0";
      row.push(parseInt(value, 10));
    }
    grid.push(row);
  }
  return grid;
}

// Event listener for Validate button
document.getElementById("validate").addEventListener("click", async () => {
  const boardData = { board: getBoardValues() };
  const response = await fetch("http://127.0.0.1:5000/api/save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(boardData),
  });
  const data = await response.json();
  alert(data.message);
});

// Event listener for Solve button
document.getElementById("solve").addEventListener("click", async () => {
  const boardData = { board: getBoardValues() };
  const response = await fetch("http://127.0.0.1:5000/api/save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(boardData),
  });
  const data = await response.json();

  if (data.message.includes("valid")) {
    alert("Board saved and validated!");
    // Now you can get the board ID and solve it
    const boardId = 1; // For testing, replace with the actual saved ID if needed
    const solveResponse = await fetch(
      `http://127.0.0.1:5000/api/solve/${boardId}`
    );
    const solveData = await solveResponse.json();

    if (solveData.is_solved) {
      alert("Sudoku Solved!");
      // Update the board with solved values
      const solvedBoard = solveData.board;
      for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
          const input = document.querySelector(
            `input[data-row="${i}"][data-col="${j}"]`
          );
          input.value = solvedBoard[i][j];
        }
      }
    } else {
      alert("Unable to solve the Sudoku.");
    }
  } else {
    alert(data.message); // Board is invalid
  }
});
