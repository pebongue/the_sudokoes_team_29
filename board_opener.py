import numpy as np

def open_file(filename):
#<<<<<<< HEAD
    #file = open(filename, "rb").readlines()
    #print(np.load(file, allow_pickle=True))
#=======
    file = open(filename, "r")
#<<<<<<< HEAD
    list_file = file.read().split("\n")
    structure = '\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in list_file])
    arrayS = np.array(structure)
    print(arrayS)
    print(type(arrayS))
    print(arrayS.shape)
#=======
    #list_file = file.read().split(",\n ")
    #array_file = np.array(list_file)
    #print(array_file)
    #print(type(array_file))
#>>>>>>> 3dee5e017402ca2de875766190c09937a094e41e
#>>>>>>> 3a1083a342ca3d46e0b74e11057bb3659bb2e704
    
open_file("sample.txt")