# You may create additional functions here:
#We import our library:
import numpy as np

incomplete_grid = open("sample.txt")
#print(myfile.read())
solution_grid = open("sol_puzzle.txt")

#this is a correct puzzle for testing
""""
[2,8,4,5,6,7,9,1,3],
[3,9,5,8,1,2,7,4,6],
[1,6,7,4,3,9,5,2,8],
[5,7,2,1,8,6,3,9,4],
[9,4,8,3,2,5,6,7,1],
[6,3,1,7,9,4,2,8,5],
[8,2,3,6,7,1,4,5,9],
[4,1,9,2,5,3,8,6,7],
[7,5,6,9,4,8,1,3,2]
"""
solution = np.array([solution_grid])

#Convert our array into a 2D array
np.concatinate([solution])

#declare our unsolved_grid:
"""
[0,0,0,0,0,0,0,0,0],
[1,2,0,0,0,0,0,8,4],
[0,3,0,0,0,0,0,7,0],
[0,0,4,0,0,0,6,0,0],
[0,0,0,2,0,3,0,0,0],
[0,0,5,0,0,0,9,0,0],
[0,0,6,0,9,0,5,0,0],
[0,7,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,0]
"""
grid = np.array([incomplete_grid])
np.concatenate([grid])
print(grid)

#Passes user input into the analyzing function
while True:
    col_input, row_input, user_input=input("Enter inputs:").split()
    col_value = int(col_input)
    row_value = int(row_input)
    user_input_value = int(user_input)
    analyzining(col_value,row_value,user_input_value)
    pass

def analyzining(*inputs):
    #Identifies position and value of variable
    grid_value= grid[col_value][row_value]
    #Validates if input is not at a predefined variable and not a zero
    if grid_value > 0:
        print("Unabe to relpace value")
        print(grid[col_value])
        print(grid[row_value])
        pass
    elif ((grid[col_value]).all()) or ((grid[row_value]).all()) == False:
        print("Value of : "+ str(user_input_value) +" already exists in row and columb")
        pass
    else:
        grid[col_value][row_value] = user_input_value
        print(grid)
        pass
        return
    #analyzining(col_value,row_value,user_input_value)
    return

def is_puzzle_solved(row_value):
    # Check each row
    for row_value in range(0, 8):
        #is_row_correct = (set(grid[0:]))
        if grid[row_value].all() ==True:
            print("Horray!!")
            pass
        pass
    return

# Check each column
#    for col in range(0, grid_size):
 #       is_col_correct = (set(puzzle_filled[:, col]) == valid_set)   

    # Check each cube unit 3x3 size
#    for unit_row in range(0, grid_size, 3):
#        for unit_col in range(0, grid_size, 3):
#            is_unit_correct = (set(puzzle_filled[unit_row:unit_row+3, unit_col:unit_col+3].flatten()) == valid_set)
#    return
