# Sudoku

Congratulations! You have made it to the final project for the WeThinkCode_ Bootcamp.

Your next task is to take on a group project.

Your project is "Sudoku!", to find out more about this game or to play it a little bit for "research" purposes go to: [SudokuOnline.io](https://www.sudokuonline.io/?gclid=EAIaIQobChMI0Ziw6t3J7gIVV-7tCh2feQkVEAAYASAAEgIiEfD_BwE)

![Sudoku Puzzle](https://upload.wikimedia.org/wikipedia/commons/d/d2/Sudoku_Puzzle_%2818_clue_-_R828-S09%29.png)

## Introduction

Sudoku - pronounced soo-doe-koo - does not require general knowledge, linguistic ability or even mathematical skill. Dubbed the Rubik's Cube of the 21st century, it consists of a grid of 81 squares, divided into nine blocks of nine squares each. Some of the squares contain a figure. The goal is to fill in the empty squares so that the figures 1 to 9 appear just once in every row, column and individual block. The requirement is logic or, for those willing to engage in a fiendish game of trial and error, sheer patience.

The Sudoku story began in 1783 when Leonhard Euler, a Swiss mathematician, devised 'Latin Squares', which he described as 'a new kind of magic squares'. Euler had come up with a grid in which every number or sym bol appears once in each row or column. More than two centuries later, the difference for Sudoku players is that the grid is subdivided into blocks of nine.

[Source: The Guardian](https://www.theguardian.com/media/2005/may/15/pressandpublishing.usnews#:~:text=The%20Sudoku%20story%20began%20in,in%20each%20row%20or%20column.)

## Objectives

The idea is to get you to become familiar with the power of Python and its ability to do complex calculations over different data types and data structures.

Therefore, we wish to remind you, this is **NOT a MATH Problem** but rather a Problem Solving question.

## Instructions

- You are expected to design a function or multiple functions that will solve a Sudoku Puzzle.
- Your function(s) will take an array as input, and return the solution.
- The table just above the [Introduction](#sudoku) would be presented as follows:

    [-1, -1, -1   -1,-1,-1   -1, -1, -1],
    [1, 2, -1   -1, -1, -1   -1, 8, 4],
    [-1, 3, -1   -1, -1, -1,   -1, 7, -1],

    [-1, -1, 4   -1, -1, -1   6, -1, -1],
    [-1, -1, -1   2, -1, 3   -1, -1, -1],
    [-1, -1, 5   -1, -1, -1   9, -1, -1],

    [-1, -1, 6   -1, 9, -1   5, -1, -1],
    [-1, 7, -1   -1, -1, -1   -1, 2, -1],
    [-1, -1, -1   -1, 5, -1   -1, -1, -1]

- The "-1" represents a blank space/square. This represents the number you must solve for.
- It is not a coincidence that there is an empty line or spaces after every three (3) numbers or arrays. It is there to help you solve the puzzle.
- You are given the function 'solve_sudoku', instantiated as:

    ```python
    def sudoku(puzzle):
        #Your Code Below Here

        #Your Code Above Here
    ```

- This function is the only function we will call to solve the puzzle.
- Your programme must be able to take input from the commandline.

Good Luck!

## Mandatory

- The programme must print the puzzle it takes in.
- The programme must print its final solution or stopping case (i.e even if there is no solution for a given puzzle. It must print where it stops.)
- After printing the puzzle, it must also print "Solution!!!" if the puzzle is solved and "No Solution?" if it cannot find a solution.

### Bonus

Overide the functionality for `def solve_sudoku(puzzle)` so that it takes input from a file and outputs the solution to a different file.

The programme must still retain the functionality of the original function.
