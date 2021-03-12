import numpy as np

def open_file(filename):
    file = open(filename)
    print(np.genfromtxt(file))
    
open_file("sample.txt")