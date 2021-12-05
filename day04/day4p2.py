#!/usr/bin/python3
# Day 4, Part 2 of Advent of Code 2021
# Playing BINGO with a giant kraken ... to lose!

# BingoGame() is my class that ingests the day's input and structures it for easy computation
class BingoGame():
    def __init__(self, filename):
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
                print(rows)
                boards.append(BingoBoard(rows))
                rows = []

        # Set game variables: callouts, boards, and whether there are any winning boards in play 
        self.callouts = callouts
        self.boards = boards
        self.winners = self.countWinners()
        return

    def countWinners(self):
        winners = 0
        for board in self.boards:
            if board.isWinner:
                winners += 1
        return winners

# A BingoSquare stores its value and marking status.
# In this game, where unmarked squares are added to score,
# a BingoSquare can also tell you whether it contributes to the score. 
class BingoSquare():
    def __init__(self, number:int, isMarked=False):
        self.value = number
        self.isMarked = isMarked

    def __repr__(self):
        printstring = "BingoSquare("
        if self.isMarked:
            r = "\033[1;36m{0:>2}\033[0;37m".format(str(self.value))
            m = " is marked"
        else:
            r = str(self.value)
            m = " is not marked"
        printstring += "Value = {} {})".format(r,m)
        return printstring
        
    def score(self):
        if self.isMarked:
            return 0
        else:
            return int(self.value)

    def mark(self, stamp=True):
        self.isMarked = stamp
        return

# A BingoBoard is a grid of BingoSquares
class BingoBoard():
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
        for row in self.grid:
            for square in row:
                if square.value == callout:
                    print("Marked a {}".format(callout))
                    square.mark(stamp)
        return

    def getScore(self):
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
            if sum == self.height:
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
            if sum == self.width:
                self.isWinner = True

        # At least in this version, diagonals don't count 
        # TODO: prepare for a version where they do? 
        return

    # A method for pretty-printing a BingoBoard
    # Marks squares in cyan and reports its score and/or win status 
    def print(self):
        for row in self.grid:
            rowstring = "   "
            for square in row:
                if square.isMarked:
                    printstring = "\033[1;36m{0:>2}\033[0;37m".format(str(square.value))
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
    filename = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day04\\input.txt"
    game = BingoGame(filename)
    winners = []
    for number in game.callouts:
        print("Calling {} now...".format(number))
        for b in game.boards:
            b.mark(number)
            b.checkWinner()            

        for b in game.boards:
            if b.isWinner:
                winners.append(b)
                game.boards.remove(b)
                lastround = number
                print("Removed a winning board during round {} ... {} boards remain.".format(number, len(game.boards)))
                for b in game.boards:
                    b.print()
    lastwinner = winners[-1]
    lastwinner.getScore()
    lastwinner.print()
    print("Total Score: {} x {} = {}".format(lastwinner.score, lastround, lastwinner.score * lastround))        
    return


if __name__ == "__main__":
    main()