import numpy as np

def open_file(filename):
<<<<<<< HEAD
    # fetching file and opening it
    file = open(filename, "r")

    # read the file 
=======
#<<<<<<< HEAD
    #file = open(filename, "rb").readlines()
    #print(np.load(file, allow_pickle=True))
#=======
    file = open(filename, "r")
#<<<<<<< HEAD
>>>>>>> d7e759a30a6aa7cce209823c67fc716f4c6e6e42
    list_file = file.read().split("\n")

    # use join to display contents and rows and columns
    structure = '\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in list_file])

    # make our rows and columns into an array
    arrayS = np.array(structure)

    # Display our array puzzle
    print(arrayS)
    print(type(arrayS))
<<<<<<< HEAD
=======
#=======
    #list_file = file.read().split(",\n ")
    #array_file = np.array(list_file)
    #print(array_file)
    #print(type(array_file))
#>>>>>>> 3dee5e017402ca2de875766190c09937a094e41e
#>>>>>>> 3a1083a342ca3d46e0b74e11057bb3659bb2e704
>>>>>>> d7e759a30a6aa7cce209823c67fc716f4c6e6e42
    
open_file("sample.txt")