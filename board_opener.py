import numpy as np

def open_file(filename):
    file = open(filename, "r")
    list_file = file.read().split(",\n ")
    array_file = np.array(list_file)
    print(array_file)
    print(type(array_file))
    
open_file("sample.txt")