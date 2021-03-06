#!/usr/bin/python3
# Day 4, Part 1 of Advent of Code 2021
# Playing BINGO with a giant kraken

import sys
import pathlib

class BingoGame():
    """
    A BingoGame ingests a file and sets up a game of BINGO.
    The object of BINGO is to mark off numbers on a randomized grid
    until five marked numbers form a contiguous row or column. The 
    first player to have such an arrangement yells "BINGO" and wins.

    This version is slightly different from BINGO games you may have played.
    Diagonals don't count, and boards score points based on their unmarked
    remaining squares. 

    See https://adventofcode.com/2021/day/4 for full rules. 
    """

    def __init__(self, filename):
        """ 
        'filename' is a reference to an ASCII text file. 
        
        - The first line of the file must be a comma-separated list of integers
        - The next line must be blank
        - Thereafter, we expect five lines of five space-separated integers
        - A newline should separate each set of 25 numbers
        
        """
        boards = []
        rows = []
        with open(filename, "r") as file:
            # Assign the "callouts" - the numbers that will be called during the game
            callouts = list(map(int, file.readline().split(",")))
            file.readline() # Eat a random blank line 
            cards = file.readlines()

        # Build groups of five lines into BINGO cards 
        for line in cards:
            if len(line) == 0:
                rows = []
            else:
                pass

            if len(rows) < 5: # TODO: if I were smarter I could just take these in chunks of non-newlines
                rows.append(line.rstrip())
            else:
                boards.append(BingoBoard(rows))
                rows = []

        # Set game variables: callouts, boards, and whether there are any winning boards in play 
        self.callouts = callouts
        self.boards = boards
        self.winners = self.countWinners()
        return

    def countWinners(self):
        """ 
        It is possible that more than one player might win on the same turn. This function
        ensures that we have an accurate count of winners so we can break ties, if they 
        occur. 
        """
        winners = 0
        for board in self.boards:
            if board.isWinner:
                winners += 1
        return winners

class BingoSquare():
    """ 
    A BingoSquare stores its integer value and boolean marking status.
    In this game, where unmarked squares are added to score, a BingoSquare 
    can also report how many points it contributes to the score.

    - Squares start unmarked unless initialized otherwise
    - Squares can be marked by calling mark() and unmarked with mark(False)

    """
    def __init__(self, number:int, isMarked:bool=False):
        self.value = number
        self.isMarked = isMarked

    def mark(self, stamp=True):
        self.isMarked = stamp
        return

    def score(self):
        if self.isMarked:
            return 0
        else:
            return int(self.value)


# A BingoBoard is a grid of BingoSquares
class BingoBoard():
    """ 
    A BingoBoard is a grid of BingoSquares, traditionally 5x5.
    It must be initialized with a list of 'rowstrings':

    - The number of rows becomes the height
    - The number of ints parsed out from a rowstring becomes the width
    
    This has only been tested with 5x5 layouts.
    """
    def __init__(self, rowstrings):
        grid = []
        for row in rowstrings:
            row.rstrip()
            newrow = list(map(int, row.split()))
            grid.append(newrow)
        width, height = len(grid[0]), len(grid)
        for i in range(width):
            for j in range(height):
                grid[i][j] = BingoSquare(grid[i][j])
        self.grid = grid
        self.score = self.getScore()
        self.width = width
        self.height = height
        self.isWinner = False
        return

    # Call a number, and a BingoBoard.mark() will mark the square
    def mark(self, callout:int, stamp:bool=True):
        """
        When a number ('callout') is called out, BingoBoard.mark()
        will find whether that number exists in its self.grid
        and mark it with the 'stamp', which defaults to True.

        Unmarking is achieved by setting 'stamp' to False.
        """
        for row in self.grid:
            for square in row:
                if square.value == callout:
                    square.mark(stamp)
        return

    
    def getScore(self):
        # Asks its squares how much score they are each worth
        # and returns the sum of the score values. 
        total = 0
        for row in self.grid:
            for square in row:
                total += square.score()
        self.score = total
        return total

    def checkWinner(self):
        self.isWinner = False

        # Check each row for five marked squares 
        for row in self.grid:
            sum = 0
            for square in row:
                if square.isMarked:
                    sum += 1
                else:
                    pass
            if sum == self.width:
                self.isWinner = True
            else:
                pass
        
        # Check each column for five marked squares
        for j in range(self.width):
            sum = 0
            for row in self.grid:
                square = row[j]
                if square.isMarked:
                    sum += 1
            if sum == 5:
                self.isWinner = True

        # NOTE: Diagonals do not count (yet)
        return

    # A method for pretty-printing a BingoBoard
    def print(self):
        for row in self.grid:
            rowstring = "   "
            for square in row:
                if square.isMarked:
                    printstring = "\033[1;36m{0:>2}\033[0;37m".format(str(square.value))
                    """ Uses ANSI escape sequences to mark squares in cyan
                    See https://bluesock.org/~willkg/dev/ansi.html for
                    other color options """ 
                else:
                    printstring = str(square.value)
                rowstring += "{0:>2} ".format(printstring)
            print(rowstring)
        print("Current score: {}".format(self.getScore()))
        self.checkWinner()
        if self.isWinner:
            print("WINNER")
        print("\n")
        return

def main():
    # Parse command-line args to see if a non-default file is specified
    if len(sys.argv) > 1:
        filename = pathlib.Path(sys.argv[1])
    else:
        filename = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day04\\test.txt"
        print("No input file specified.")
    print("...using {}".format(filename))

    # Initialize the game
    game = BingoGame(filename)
    winners = 0
    for number in game.callouts:
        print("Calling {} now...".format(number))
        for b in game.boards:
            b.mark(number)
            b.checkWinner()            
            if b.isWinner:
                winners += 1
                b.getScore()
                b.print()
                print("Total Score: {} x {} = {}".format(b.score, number, b.score * number))
                for b in game.boards:
                    if b.isWinner:
                        b.print()
            else:
                pass
        if winners > 0:
            return
    return

if __name__ == "__main__":
    main()