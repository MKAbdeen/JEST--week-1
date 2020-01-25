
# **Implementing a Sudoku puzzle game.**
If you are not familiar with Sudoku, check wikipedia: https://en.wikipedia.org/wiki/Sudoku .

**Goal**
You are asked to implement a command-line program which consists of two parts: initialization and the game itself. 

**Flow**
In the initialization phase, the board is partially filled with random digits from 1 to 9. The program randomly generates a solved board, and then clears several cells chosen at random. The user chooses the number of these cells.

After the initialization, the game itself begins. In each move, the program prints the state of the board in a predefined format (described below) and wait for user input. The game continues in this manner until the puzzle is solved and all the cells are filled with correct values.

In order to generate the board, solve the board and give hints to the user, you will use the backtracking algorithm. It’s a simple, stupid and recursive algorithm that solves the board using brute force - going over all the possabilities. We will use two variants of this algorithm: randomized and deterministic.

**Backtracking**
Deterministic backtracking
The algorithm visits all the empty cells (filled cells aren’t touched by the algorithm) from right to left, top to bottom. In each empty cell, the algorithm tries to fill in digits sequentially (from 1 to 9). If an option is legal, the algorithm continues to the next cell. If There isn’t a valid option, the algorithm backtracks (goes one cell back) and continues to the next number in that cell.
For example: Let’s say that there are only two empty cells in the Sudoku puzzle, in the coordinates x (1,3),y (7,9). The algorithm starts at x, and tries to place “1”. This is a valid value, therefore the algorithm continues to y, and tries all the numbers from 1 to 9 sequentially. None of them is legal. The algorithm backtracks to x, tries to place 2-5, but none of them is legal. Then it gets to “6”, which is legal. The algorithm places “6”, and continues to “y”. Tries to place “1” in y successfully. The board is solved (impossible mathematically, but for the sake of the example).
The algorithm terminates in two conditions (solvable board and unsolvable board). What are they? (It’s on you).

**Random backtracking**
Almost similar to the deterministic backtracking. The only difference is in the way the algorithm chooses which numbers to try. In each empty cell, the algorithm randomizes the order of the number it’ll try to fill in. 1

- General notes about backtracking
The algorithm can be very slow (calculate its complexity yourself). That’s OK.
You are required to use recursion in the implementation of this algorithm.

**Initialization**
The game starts by asking the user to enter the number of cells to fill. The program prints the following message and waits for the user’s input:
“Please enter the number of cells to fill [0-80]”.
The user then enters a number, this is the number of fixed cells, cells with values that never change throughout the game.
If the user enters an invalid number, the program prints an error message: “Error: invalid number of cells to fill”, and lets the user to try again by printing the same first message. This phase finishes only when the user provides a valid number.

**Puzzle generation**
To , you will use the following procedure:
Create an empty board
Use randomized backtracking to get a random solved board.
Repeat X times:
Randomly select an empty cell (x,y). If the cell is fixed (was previously selected), repeat randomizing until the chosen cell isn’t fixed.
Mark the chosen cell as a fixed cell.
Clear all the cells that are not fixed from the board.
In addition, you should store a mirror of the solution (the complete board you’ve generated efore), it’ll be used for giving hints to the user.

**Game flow**
After initialization, the game begins where the user attempts to solve the generated puzzle.

The program prints the game board, and then repeatedly gets commands from the user as follows:

The command includes at least one non-whitespace character.
The command and its parameters are separated by one or more whitespaces.
A command can contain “extra” parameters - we allow this and ignore any sufficient parameters. Commands with insufficient parameters are invalid.
Commands are not case sensitive.

 List of valid commands:
***Set X Y Z***
Sets the value Z in the cell that’s placed in the Xth column and the Yth row.

Its on you to check whether the values of X, Y and Z are correct (X and Y (1-9), Z (0-9).

If cell (x,y) has already been filled by the program at initialization, the program prints “Error: value is invalid”, and the command is ignored.

If the value Z is invalid for the cell, the program prints “Error: value is invalid”, and the command is ignored.

Otherwise, the program prints the game board again.

If the game is over (the board is filled), the program prints “Puzzle solved successfully”. 

From the point, all the commands besides exit and restart are invalid.

Pay attention: Z can be 0, and it means to delete the content of a cell.

***Hint x y***
Give a hint to the user by showing a possible legal value for a single cell. 
You should check whether x y are valid parameters (parameters of an unfilled cell).
The program prints “Hint: set cell to z” where z is the value of x,y according to the solution of the board (stored during puzzle initialization, or during validate described below).

Pay attention: the hint can be incorrect! It’s okay.

***Validate***
Validates that the current state of the board is solvable.
Solve the generated board with deterministic backtracking.
If no solution is found, the program prints: “validation failed, the board is unsolvable”.
If a solution is found, update the stored solution to the newly-found solution (so future hints are given from the new solution), and the program prints: “validation passed: board is solvable”.

***Restart***
Restart the game by starting over with the initialization procedure from the start (including solving a new board randomly, etc).

***Exit***
The program prints “Exiting…” and terminates.

**Remarks**
Columns and rows are 1-based; the first column and row are indexed 1. 
If the user enters an invalid command, i.e, a command that doesn’t match any of the commands defined in this section or has insufficient arguments in any way, the program prints “Error: invalid command”.
Ignore blank lines and don’t output anything in this case.

**Printing format**
After initialization and whenever a successful set happens, the board is printed to the user.
The board has 13 rows, consists of two types:
Separator row: a series of 34 dashes: “-”.
Cells row - each cell is represented as two characters. A dot (‘.’) and a digit for a fixed cell, and a space and a digit for an unfixed cell. A pipe (‘|’) starts and ends the row and separates each set of 3 digits. A space separates all cells and pipes, for example: 
“|.1 2.3 | 4 5 6 | .7 8 9 |”.
The board will be printed in the following format:
Separator row
Three rows of cells
Separator row
Three rows of cells
Separator row
Three rows of cells
Separator row

