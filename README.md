# Multithreaded_Sudoku

Welcome to the Multithreaded Sudoku Validator and Solver.

Multithreaded sudoku for operating systems project is consised out of frontend and backend and also tested via Postman for Validating.

Sudoku main solving is done through python running Test.py which uses multithreading.

Frontend is: HTML, CSS and JS code.

Backend is: Flask Python.

Database is : sqlite3 by mySQL.

-How to run-

FRONTEND
To run frontend use live server by instaling it on your device. If installed already Go Live is enough to run. Which opens http://127.0.0.1:5501/frontend/index.html

BACKEND
To run the flask backend use in your prefered CLI by inserting: pip install flask and then python app.py which opens http://127.0.0.1:5000/

DATABASE
pip install mysql-connector-python

TESTING
To test the validation use Postman. Bellow are the URL's.

1.To test if board is saved use http://127.0.0.1:5000/api/save switch to POST , in raw choose JSON and enter

{
"board": [
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
}

and send it.

2.To test if board is valid use GET and http://127.0.0.1:5000/api/validate/1 and send.

3.To se solved board enter GET and http://127.0.0.1:5000/api/solve/1 and also send for result.
