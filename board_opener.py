import numpy as np

def open_file(filename):
    file = open(filename, "rb").readlines()
    print(np.load(file, allow_pickle=True))
    
open_file("sample.txt")