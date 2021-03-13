# You may create additional functions here:

#all import for the solution goes below
import numpy as np
import os


'''Level 1 - solutions will go here

    1. read from a text file, load into an np array and return it
    2. print a sudoku grid from the array read from the file
    3. allow a user to substitute value into the grid
'''

                                        #----------- end of Level 1 Tasks --------------------------
'''Level 2 - solutions will go here

    1. after the grid or puzzle has been filled with candidate values, display whether or not the user solution is correct
    2. Ask the user if he wants to play again or just select a puzzle for the system to solve
'''
''' The method below is an adaption of Felicia Hsieh GitHub @feliciahsieh 
    Her solution was heavily modified to adapt to our solution.

    (ref = https://medium.com/@feliciaSWE/solving-sudoku-with-python-numpy-and-set-95ca55f9ba01)

    Args:
        puzzle_filled (ndarray): the sudoku puzzle filled with numbers
        grid_size (int): the number of rows or columns
        valid_set (set): it is the set {1, 2, 3, 4, 5, 6, 7, 8, 9}

    Level 2 - step 1: This method checks if the user's solution for the puzzle_array is valid or not, and return a string
'''
def is_puzzle_solved(puzzle_filled, grid_size, valid_set):
# Check each row
    for row in range(0, grid_size):
      is_row_correct = (set(puzzle_filled[row]) == valid_set)   

# Check each column
    for col in range(0, grid_size):
        is_col_correct = (set(puzzle_filled[:, col]) == valid_set)   

    # Check each cube unit 3x3 size
    for unit_row in range(0, grid_size, 3):
        for unit_col in range(0, grid_size, 3):
            is_unit_correct = (set(puzzle_filled[unit_row:unit_row+3, unit_col:unit_col+3].flatten()) == valid_set)

#return correct if there are no duplicate 1 to 9 values accross row and col, else incorrect                
    if is_row_correct and is_col_correct and is_unit_correct:
        return "Correct solution!"
    else:
        return "Incorrect solution!"


#This is Level 2 - step 2: ask the user if they want to play again. This is repeated in Level 3 - step 1
def ask_for_replay():
    print(" ------------- Select 1 or 2 ----------\n")
    return input("1. Would you like to play another game? \n OR \n 2. Select a sudoku for the system to solve? ")

                                            #----------- end of Level 2 Tasks --------------------------
'''Level 3 - solutions will go here

    1. This is the same as Level 2 - 2
    2. When user select solve puzzle, type in a file name, read files from a folder of unsolved puzzle and display
        a. if the user selected in Level 2 - 2 to continue playing, load grid and allow user to input values, then check if puzzle is solved
        b. if the user selected just to solve puzzle - do Level 3 - 3 
    3. the program must automatically solve the puzzle
'''
# display the list of unsolved puzzle from a folder
def display_puzzle_unsolved():
    files = os.listdir('/unsolved_puzzle')

    count = 1
    for f in files:
        print(f"{count}. {f}")
        count += 1
    return files

def play_game_or_solve():
    if int(ask_for_replay()) == 1:    #user selected to play a new game
        fiels_list = display_puzzle_unsolved()
        file_selected = int(input('Input a file number to start playing: '))
        puzzle_array = get_array_from_file(files[file_selected - 1])  #this method is called from Level - reading a file into an array

        print('Solve this puzzle: ', puzzle_array)  # display the puzzle to be solved
        user_completed_puzzle = play_game(puzzle_array) # this is the method where the user add vallues to the grid - from Level 1 - 3
        is_puzzle_solved(user_completed_puzzle) # this method displays correct or incorrect solution

                                            #----------- end of Level 3 Tasks --------------------------
# Additional Functions above this comment

# Implement your Sudoku Solution Below:
def solve_sudoku(puzzle):
    #Edit the code Below Here



    pass
    #Edit the code Above Here