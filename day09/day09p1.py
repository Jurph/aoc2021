#!/usr/bin/python3
# Advent of Code Day 9, Part 1
# Volcanic vents underwater

import sys
import pathlib

class Survey():
    def __init__(self, filename:str):
        grid = []
        with open(filename, "r") as file:
            for line in file:
                newlist = []
                newrow = list(map(str, line.rstrip("\n").split()))
                for letter in str(newrow[0]):
                    newlist.append(letter)     
                grid.append(list(map(int, newlist)))
        # Do I need a per-square class today? Maybe.
        width, height = len(grid[0]), len(grid)
        # for i in range(width):
        #     for j in range(height):
        #         grid[i][j] = BingoSquare(grid[i][j])
        self.grid = grid
        # self.score = self.getScore()
        self.width = width
        self.height = height
        # self.isWinner = False
        return

    def print(self):
        printstring = '\n'
        for row in range(self.height):
            rowstring = ' '
            for col in range(self.width):
                rowstring += str(self.grid[row][col])
            rowstring += '\n'
            printstring += rowstring
        print(printstring)
        return

    def risklevel(squarevalue):
        return int(1+squarevalue)

    def countLowPoints(self, grid):
        
        return

def main():
    # Parse command-line args to see if a non-default file is specified
    if len(sys.argv) > 1:
        filename = pathlib.Path(sys.argv[1])
    else:
        filename = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day07\\test.txt"
        print("No input file specified.")
    print("Using {}\n\n".format(filename))

    # File I/O
    p = Survey(filename)
    print(p.grid)
    p.print()

    # Brute force the problem
    total = 0


if __name__ == "__main__":
    main()