import numpy as np

def open_file(filename):
<<<<<<< HEAD
    file = open(filename, "rb").readlines()
    print(np.load(file, allow_pickle=True))
=======
    file = open(filename, "r")
    list_file = file.read().split(",\n ")
    array_file = np.array(list_file)
    print(array_file)
    print(type(array_file))
>>>>>>> 3dee5e017402ca2de875766190c09937a094e41e
    
open_file("sample.txt")