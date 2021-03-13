# You may create additional functions here:
#Mfundo's comments:  
                                                                   #We import our numpy library:
import numpy as np
                                                                   #declare our grid:
grid = np.array([[0,0,0,0,0,0,0,0,0],
                 [1,2,0,0,0,0,0,8,4],
                 [0,3,0,0,0,0,0,7,0],
                 [0,0,4,0,0,0,6,0,0],
                 [0,0,0,2,0,3,0,0,0],
                 [0,0,5,0,0,0,9,0,0],
                 [0,0,6,0,9,0,5,0,0],
                 [0,7,0,0,0,0,0,0,0],
                 [0,0,0,0,5,0,0,0,0]
                                         ])

                                                                   #Convert our array into a 2D array:
np.concatenate([grid])
                                                                   #Take in user input and keeps code active till specified:
while True:
    print(grid) 
    col_input, row_input, user_input=input("Enter inputs").split()
    col_value = int(col_input)
    row_value = int(row_input)
    user_input_value = int(user_input)
                                                                   #Function used for calculating user input:
    def analyzining(*inputs):
                                                                   #Identifies position and value of variable:
        grid_value= grid[col_value][row_value]
                                                                   #Validates if input is not at a predefined variable and not a zero:
        if grid_value > 0:
            print("Unabe to relpace value")
            pass
                                                                  #Inserts user input if conditions are met:
        else:
                grid[col_value][row_value] = user_input_value
                print(grid)
                pass
        return
                                                                   #Call back to run analyzing function:
    analyzining(col_value,row_value,user_input_value)
    pass
########### End of comment #########
