#!/usr/bin/python3
# Day 4, Part 1 of Advent of Code 2021
# Playing BINGO with a giant kraken

# BingoGame() is my class that ingests the day's input and structures it for easy computation
class BingoGame():
    def __init__(self, filename):
        boards = []
        rows = []
        with open(filename, "r") as file:
            callouts = list(map(int, file.readline().split(",")))
            file.readline()
            cards = file.readlines()
            # TODO: figure out arbitrary line input

        for line in cards:
            if len(line) == 0:
                rows = []
            else:
                pass

            if len(rows) < 5:
                rows.append(line.rstrip())
            else:
                print(rows)
                boards.append(BingoBoard(rows))
                rows = []
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

class BingoSquare():
    def __init__(self, number:int, isMarked=False):
        self.value = number
        self.isMarked = isMarked

    def score(self):
        if self.isMarked:
            return 0
        else:
            return int(self.value)

    def mark(self, stamp=True):
        self.isMarked = stamp
        return

class BingoBoard():
    def __init__(self, rowstrings):
        grid = []
        # For input debugging
        # TODO: remove this once the code runs
        # print(rowstrings)
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

    def mark(self, callout:int, stamp:bool=True):
        for row in self.grid:
            for square in row:
                if square.value == callout:
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
                    # print("Found marked square with value {}".format(square.value))
                else:
                    pass
            if sum == self.width:
                self.isWinner = True
                # print("Won with a row")
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
                # print("Won with column {}".format(j))
        return

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
    highscore = 0
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
            
        # j = input()
    print("High score: {}".format(highscore))
    return


if __name__ == "__main__":
    main()