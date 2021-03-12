import numpy as np

def open_file(filename):
    file = open(filename, "r")
    list_file = file.read().split("\n")
    structure = '\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in list_file])
    arrayS = np.array(structure)
    print(arrayS)
    print(type(arrayS))
    
open_file("sample.txt")