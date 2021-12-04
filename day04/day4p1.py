#!/usr/bin/python3
# Day 4, Part 1 of Advent of Code 2021
# Playing BINGO with a giant kraken

# BingoGame() is my class that ingests the day's input and structures it for easy computation
class BingoGame():
    def __init__(self, filename):
        boards = []
        with open(filename, "r") as file:
            callouts = file.readline().split(",")
            while len(boards) < 3:  # TODO: work on arbitrary input length
                file.readline().lstrip()
                rows = []
                for i in range(5):
                    row = file.readline().rstrip()
                    rows.append(row)
                boards.append(BingoBoard(rows))
        self.boards = boards
        self.winners = 0
        return

    def countWinners(self):
        winners = 0
        for board in self.boards:
            if board.isWinner():
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
            return self.isMarked


class BingoBoard():
    def __init__(self, rowstrings):
        grid = []
        print(rowstrings)
        for row in rowstrings:
            row.rstrip()
            newrow = list(map(int, row.split()))
            grid.append(newrow)
        width, height = len(grid[0]), len(grid)
        for i in range(width):
            for j in range(height):
                grid[i][j] = BingoSquare(grid[i][j])
        self.grid = grid
        self.score = self.score()
        return

    def mark(self, callout:int, marking:bool=True):
        for row in self.grid:
            for square in row:
                if square.value == callout:
                    square.isMarked = marking
        return

    def score(self):
        total = 0
        for row in self.grid:
            for square in row:
                total += square.score()
        return total

    def isWinner(self):
        isWinner = False
        

        return isWinner

    def print(self):
        for row in self.grid:
            rowstring = ""
            for square in row:
                if square.isMarked:
                    printstring = "\033[1m{0:>2}\033[0m".format(str(square.value))
                else:
                    printstring = str(square.value)
                rowstring += "{0:>2} ".format(printstring)
            print(rowstring)
        print("\n")
        return

def main():
    input = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day04\\test.txt"
    game = BingoGame(input)
    for b in game.boards:
        b.mark(7)
        b.print()
    return


if __name__ == "__main__":
    main()