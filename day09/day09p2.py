#!/usr/bin/python3
# Advent of Code Day 9, Part 2
# Volcanic vents underwater ... and BASINS.

import sys
import pathlib

class Square():
    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.value = value
        return

    def __str__(self):
        return str(self.value)

    def findNeighbors(self):
        neighbors = []
        row, col = self.x, self.y
        if row == 0:
            neighbors.append([row + 1, col])
        elif row == self.height-1:
            neighbors.append([row - 1, col])
        else:
            neighbors.append([row + 1, col])
            neighbors.append([row - 1, col])

        if col == 0:
            neighbors.append([row, col + 1])
        elif col == self.width - 1:
            neighbors.append([row, col - 1])
        else:
            neighbors.append([row, col + 1])
            neighbors.append([row, col - 1])
        return neighbors


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
        width, height = len(grid[0]), len(grid)
        squaregrid = [[0 for i in range(width+1)] for j in range(height+1)]
        for i in range(width):
            for j in range(height):
                squaregrid[i][j] = Square(grid[i][j], i, j)
                # Now all calls to self.grid[i][j] return a Square object 
                # ...which unlike a list, can be in a Set. 
        self.grid = squaregrid
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
                # TODO: add fancy ANSI highlighting of low points :) 
                rowstring += str(self.grid[row][col])
            rowstring += '\n'
            printstring += rowstring
        print(printstring)
        return

    def risklevel(squarevalue):
        return int(1+squarevalue)

    def countRiskScore(self):
        risk = 0
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.findNeighbors([row, col])
                risks = []
                for n in neighbors:
                    risks.append(self.grid[n[0]][n[1]])
                print("Checking {} against value of {}".format(self.grid[row][col], sorted(risks)))
                if self.grid[row][col] < sorted(risks)[0]:
                    risk += self.grid[row][col] + 1
                    print("Found low point at {},{}".format(row, col))
        return risk

    def findNeighbors(self, xypair: list):
        neighbors = []
        row, col = xypair[:]
        if row == 0:
            neighbors.append([row + 1, col])
        elif row == self.height-1:
            neighbors.append([row - 1, col])
        else:
            neighbors.append([row + 1, col])
            neighbors.append([row - 1, col])

        if col == 0:
            neighbors.append([row, col + 1])
        elif col == self.width - 1:
            neighbors.append([row, col - 1])
        else:
            neighbors.append([row, col + 1])
            neighbors.append([row, col - 1])
        return neighbors

    # Oh this won't work unless I create a specific "gridSquare" type that I can
    # store in a set()... 
    def getBasin(self, xypair: list):
        basinSet = set()
        basinSet.update(xypair)
        lasttime = 0
        thistime = len(basinSet)
        while thistime > lasttime:
            print("Basin now size {} ; was {} last check")
            for neighbor in basinSet:
                row = neighbor[0]
                col = neighbor[1]
                points = set(self.findNeighbors([row, col]))
            for p in points:            
                if self.grid[p[0]][p[1]] == 9:
                    points.discard(p)
            basinSet.update(points)
            lasttime = thistime
            thistime = len(basinSet)
        return frozenset(basinSet)
                

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

    # Solve the problem
    print(p.grid)
    p.print()
    j = p.countRiskScore()
    print(j)
    basinlist = set()
    for row in range(p.width):
        for col in range(p.height):
            basinlist.add(p.getBasin([row, col]))


if __name__ == "__main__":
    main()