# You may create additional functions here:

#all import for the solution goes below
import numpy as np
import os


'''Level 1 - solutions will go here

    1. read from a text file, load into an np array and return it
    2. print a sudoku grid from the array read from the file
    3. allow a user to substitute value into the grid
'''
def get_array_from_file(filename):
    file = open(filename, "r")
    list_file = file.read().split("\n")
    structure = '\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in list_file])
    file_array = np.array(structure)

    return file_array     #return an array with the file's values


def play_game(unsolved_puzzle):
        #np.concatenate([unsolved_puzzle])
                                                                   #Take in user input and keeps code active till specified:
        while True:
            print(unsolved_puzzle)
            col_input, row_input, user_input=input("Enter inputs as 'row col your_number' (without quotes and consider zero indexing): ").split()
            col_value = int(col_input)
            row_value = int(row_input)
            user_input_value = int(user_input)
                                                                        #Function used for calculating user input:
            def analyzining(*inputs):
                                                                        #Identifies position and value of variable:
                grid_value= unsolved_puzzle[col_value][row_value]
                                                                        #Validates if input is not at a predefined variable and not a zero:
                if grid_value > 0:
                    print("Unabe to relpace value")
                    pass
                                                                        #Inserts user input if conditions are met:
                else:
                        unsolved_puzzle[col_value][row_value] = user_input_value
                        print(grid)
                        pass
                return
                                                                        #Call back to run analyzing function:
            analyzining(col_value,row_value,user_input_value)
            pass

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
    return int(input("1. Would you like to play another game? \n OR \n 2. Select a sudoku for the system to solve? "))

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

def play_game_or_solve():             #Level 3 - 1,2
    if int(ask_for_replay()) == 1:    #user selected to play a new game
        fiels_list = display_puzzle_unsolved()
        file_selected = int(input('Input a file number to start playing: '))
        puzzle_array = get_array_from_file(files[file_selected - 1])  #this method is called from Level - reading a file into an array

        print('Solve this puzzle: ', puzzle_array)  # display the puzzle to be solved
        user_completed_puzzle = play_game(puzzle_array) # this is the method where the user add vallues to the grid - from Level 1 - 3
        is_puzzle_solved(user_completed_puzzle) # this method displays correct or incorrect solution
    
    if int(ask_for_replay() == 2):
        fiels_list = display_puzzle_unsolved()
        file_selected = int(input('Input a file number to start playing: '))
        puzzle_array = get_array_from_file(files[file_selected - 1])  #this method is called from Level - reading a file into an array

        print('The system is solving this puzzle: ', puzzle_array)  # display the puzzle to be solved
        solved_puzzle = update_empty_blocks(puzzle_array)           #fill in empty blocks and return solved puzzle
        is_puzzle_solved(solved_puzzle)                              #confirm if the puzzle was solved the right way
         



'''This is the second method in the @feliciahsieh series after heavy adaptation

    Args:
        puzzle_filled (ndarray): the sudoku puzzle filled with numbers
        grid_size (int): the number of rows or columns
        valid_set (set): it is the set {1, 2, 3, 4, 5, 6, 7, 8, 9}
'''
def update_empty_blocks(unsolved_puzzle, grid_size=9, valid_set={1, 2, 3, 4, 5, 6, 7, 8, 9}):
    # Process grid with Possible array values
    list_possible_values = possible_set_values(unsolved_puzzle, grid_size, valid_set)

    for row in range(0, grid_size):
        for col in range(0, grid_size):
            # Found correct cell value = Only 1 possible value
            if np.size(list_possible_values[row, col]) == 1:
                is_single_value = list_possible_values[row][col][0]
                unsolved_puzzle[row][col] = is_single_value         
                
                # Remove from Possible list
                list_possible_values[row, col].remove(is_single_value)         
                
                # Remove from Possible in row
                for pos_col in range(0, grid_size):
                    if is_single_value in list_possible_values[row, pos_col]:
                        list_possible_values[row, pos_col].remove(is_single_value)         
                    
                # Remove from Possible in col
                for pos_row in range(0, grid_size):
                    if is_single_value in list_possible_values[pos_row, col]:
                        list_possible_values[pos_row, col].remove(is_single_value)         
                
                # Remove from Possible in cube
                row_index = row//3*3
                col_index = col//3*3
                for i in range(row_index, row_index+3):
                    for j in range(col_index, col_index+3):
                        if is_single_value in list_possible_values[i, j]:
                            list_possible_values[i, j].remove(is_single_value)
    
    #return the puzzle array
    return unsolved_puzzle
 

#This method is call by update_empty_blocks(,) to return the array of posible set of values for each block
def possible_set_values(unsolved_puzzle, grid_size, valid_set):
    #create an empty array to store the list of possible values 
        list_possible_values = np.empty(shape=[9,9], dtype=object )
        for r in range(0, grid_size):
            for c in range(0, grid_size):
                list_possible_values[r, c] = []

    # Create Possible values of 1..9 for each Cell
        for row in range(0, grid_size):
            for col in range(0, grid_size):
                if unsolved_puzzle[row][col] == 0:
                    
                    # Create possible values in row and subtract from full set
                    r = valid_set - set(unsolved_puzzle[row])         
                    
                    # Create possible values in column and subtract
                    c = r - set(unsolved_puzzle[:, col])         
                    
                    # Create possible values in cube and subtract
                    row_index = (row//3) * 3
                    col_index = (col//3) * 3
                    list_possible_values[row][col] = list(c - set(unsolved_puzzle[row_index:row_index+3, col_index:col_index+3].flatten()))
        print(list_possible_values) #remember to delete
        return list_possible_values
                                            #----------- end of Level 3 Tasks --------------------------
# Additional Functions above this comment

# Implement your Sudoku Solution Below:
def solve_sudoku(puzzle):                #Assumption: puzzle is a file name for a puzzle
    #Edit the code Below Here
    puzzle_from_file = get_array_from_file(puzzle)
    puzzle_filled = play_game(puzzle_from_file) #user play the game
    is_puzzle_solved(puzzle_filled) #system check if puzzle is solved

    play_game_or_solve()            #ask user if they wanna play again or solve the puzzle


    pass
    #Edit the code Above Here

solve_sudoku("unsolved_puzzle/puzzle_1.txt")