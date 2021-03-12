#import necessary liraries here - these must be copied during code integration
import numpy as np


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
    return input("Would you like to play again? [Yes/No]")


#this is a correct puzzle for testing
filled_puzzle = np.array([
    [2, 8, 4, 5, 6, 7, 9, 1, 3],
    [3, 9, 5, 8, 1, 2, 7, 4, 6],
    [1, 6, 7, 4, 3, 9, 5, 2, 8],
    [5, 7, 2, 1, 8, 6, 3, 9, 4],
    [9, 4, 8, 3, 2, 5, 6, 7, 1],
    [6, 3, 1, 7, 9, 4, 2, 8, 5],
    [8, 2, 3, 6, 7, 1, 4, 5, 9],
    [4, 1, 9, 2, 5, 3, 8, 6, 7],
    [7, 5, 6, 9, 4, 8, 1, 3, 2]
])

#receive an array of a 9x9 sudoku puzzle with blocks all filled with valid numbers 1 to 9
#filled_puzzle = np.random.randint(1,10, size=(9,9))                #create a dummy array with random int values from [1,10) of dimension 9x9
print(filled_puzzle)

#the puzzle dimension is 9x9 and a grid size or length of a column or row is 9
puzzle_grid_size = 9

#valid set is the range of valid numbers 1 to 9
valid_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#test and display result
print("\n" + is_puzzle_solved(filled_puzzle, puzzle_grid_size, valid_set))

#This is Level 2 - test method here
user_answer = ask_for_replay()
print(f"The user answered: '{user_answer}'")
