#__author__ = Mohammad Abdin
import sys

# the only thing left to do is start the game from index 1 instead of 0
#to play the game please notice that :
# the top left cell (first cell) exists in the (0,0) and not (1,1)
#the last cell (8,8)
#the '|' and '-' do't have indexes.
#example: Set x y z -> Set 4 6 1 -> sets the cell in the 4th column and the 6th row to 1
from random import sample


# find an empty cell
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None

#the backtracking solving algorithm
def solve(bo):

    # we found the solution and we are done
    find = find_empty(bo)
    if not find:
        return True

    else:
        row, col = find
    #loop through the values 1 to 9, in attempt to put those in out solution
    for i in range(1,10):
        #if this is valid
        if valid(bo, i, (row, col)):
            # we put that value into the board
            bo[row][col] = i
            # recursive call to finish the solution by calling solve on our new board
            if solve(bo):
                return True

            #reset the last element we've just added
            bo[row][col] = 0

    # if we loop through all the numbers and none of them is valid:
    return False

#check if the num entered in position in board is valid
def valid(board, number, position):
    # Check row
    for i in range(len(board[0])):
        #check if the number we added exists in the same row  in another column
        #notice we don't check in the position we just inserted
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        # check if the number we added exists in the same column  in another row
        # notice we don't check in the position we just inserted
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box of 3*3
    #we need to determine which block we are in
    box_x = position[1] // 3
    box_y = position[0] // 3

    #loop inside the block and make sure that no number is repeated of the 9 elements
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            #check if the number we entered, exits in the block
            if board[i][j] == number and (i,j) != position:
                return False

    return True
#print the board
def print_board(bo):
    #every time we're in the 3rd row we print this horizontal line
    for i in range(len(bo)):
        if i % 3 == 0 :
            print("-"*34)

        #for every cell in the row check if we're in the 3rd col then we print this vectorial line
        for j in range(len(bo[0])):
            if j % 3 == 0 :
                print("| ", end="")

            if j == 8:
                print("." + str(bo[i][j]) + " |")
            else:
                print("." + str(bo[i][j]) + " " , end="")

    print("-"*34)

#create a sudoku board
def create_board():
    base = 3
    side = base * base
    nums = sample(range(1, side + 1), side)  # random numbers
    board = [[nums[(base * (r % base) + r // base + c) % side] for c in range(side)] for r in range(side)]
    rows = [r for g in sample(range(base), base) for r in sample(range(g * base, (g + 1) * base), base)]
    cols = [c for g in sample(range(base), base) for c in sample(range(g * base, (g + 1) * base), base)]
    board = [[board[r][c] for c in cols] for r in rows]

    return board

def make_puzzle(my_board,filled_cells):
    side = 9
    squares = side * side
    empties = squares * 3 // 4
    counter =0
    for p in sample(range(squares), empties):
        if counter != squares-filled_cells :
            my_board[p // side][p % side] = 0
            counter +=1


    return my_board

# is the board solver yet
def is_solved(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return False

    return True


def main():

    user_input = (int(input("enter the number of cells to fill[0-80]\n")))

    board = create_board()

    puzzle = make_puzzle(board, user_input)
    print("the puzzle board ")
    print_board(puzzle)
    while not is_solved(puzzle):
        #print_board(puzzle)

        if not is_solved(puzzle):


            user_command = input("not solved - enter a command\n")
            user_command = user_command.replace(" ", "")

            if user_command[:3] == "Set":
                # print(user_command[3])
                # print(user_command[4])
                # print(user_command[5])
                #
                # print(puzzle[int(user_command[4])][int(user_command[3])])
                if puzzle[int(user_command[4])][int(user_command[3])] == board[int(user_command[4])][int(user_command[3])]:
                    puzzle[int(user_command[4])][int(user_command[3])] = int(user_command[5])
                else:
                    print("Error: value is invalid ")

                print_board(puzzle)

            elif user_command[:7] == "Restart":
                board = create_board()

                puzzle = make_puzzle(board, user_input)
                print("the puzzle board ")
                print_board(puzzle)

            elif user_command[:4] == "Exit":
                print("Exiting...")
                exit(0)

            elif user_command[:8] == "Validate":
                tmp_puzzle=[[0]*9 for _ in range(9)]
                for i in range(len(puzzle)):
                    for j in range(len(puzzle[0])):
                        tmp_puzzle[i][j] = puzzle[i][j]

                solve(tmp_puzzle)
                if not solve(tmp_puzzle):
                    print("Validation failed, the board is un solvable")

                else:
                    #the solve function is designed to automatically update the passed board
                    print("Validation passed: board is solvable")

            elif user_command[:4] == "Hint":
                count = 0
                for i in range(len(puzzle)):
                    for j in range(len(puzzle[0])):
                        if puzzle[ int(user_command[5])][ int(user_command[4])] == 0 and count == 0:
                            #puzzle[i][j] = board[ int(user_command[4])][ int(user_command[5])]
                            solver = solve(board)
                            print("hint: set cell to {} ".format(board[ int(user_command[5])][ int(user_command[4])]))
                            count += 1


            else:
                print("Error: value is invalid")
                continue


    print("Puzzle solved successfully")






if __name__ == '__main__':
    main()
