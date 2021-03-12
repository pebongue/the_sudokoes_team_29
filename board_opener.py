myfile = open("sample.txt")

def print_soduko_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print_soduko_board(myfile)


'''import numpy as np

def open_file(filename):
    file = open(filename)
    return np.array(file)
    
print(open_file("sample.txt"))
'''