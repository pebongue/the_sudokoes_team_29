import numpy as np

def open_file(filename):

    # fetching file and opening it
    file = open(filename, "r")

    # read the file 
    list_file = file.read().split("\n")

    # use join to display contents and rows and columns
    structure = '\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in list_file])

    # make our rows and columns into an array
    arrayS = np.array(structure)

    # Display our array puzzle
    print(arrayS)
    print(type(arrayS))
    print(arrayS.shape)
    print(arrayS.size)
    
open_file("sample.txt")