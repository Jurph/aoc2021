#!/usr/bin/python3
# Day 3, Part 2 of Advent of Code 2021
# Measure the most common bit(s) in a binary string 

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        strings = [] # We don't need strings in this chapter but it's a neat feature
        with open(filename, "r") as file:
            for line in file:
                strings.append(line.rstrip())
        self.strings = strings
        self.length = len(strings)
        self.width = len(strings[0])
        return
    
    def mostpopular(self, offset=int):
        sum = 0
        for i in self.strings:
            sum += int(i[offset])
        popular = int(round(sum/self.length, 0))
        # print("Sum was {} after {} rows; therefore return {}".format(sum, self.length, popular))
        return popular

def winfilter(diagnostics=list, placevalue=int):
    j = placevalue
    ones = []
    zeroes = []
    for i in diagnostics:
        if i[j] == "1":
            ones.append(i)
        elif i[j] == "0":
            zeroes.append(i)
        else:
            print("ERROR")
        if len(ones) > len(zeroes):
            winner = ones
        elif len(zeroes) > len(ones):
            winner = zeroes
        elif len(ones) == 1:
            winner = ones    
        else:
            winner = diagnostics
    #print("Winner was {}".format(winner))
    return winner

def lossfilter(diagnostics=list, placevalue=int):
    j = placevalue
    ones = []
    zeroes = []
    winner = []
    for i in diagnostics:
        if i[j] == "1":
            ones.append(i)
        elif i[j] == "0":
            zeroes.append(i)
        else:
            print("ERROR")
        if len(ones) > len(zeroes):
            winner = zeroes
        elif len(zeroes) > len(ones):
            winner = ones
        elif len(zeroes) == 1:
            winner = zeroes    
        else:
            winner = diagnostics
    #print("Loser was {}".format(winner))
    return winner


def main():
    # Ingest and format the data
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day03\\input.txt")

    # Set up state variables 
    gamma = ""
    epsilon = ""
    rows = p.length
    sums = [0]*p.width

    # Compute an answer
    for i in p.strings:
        for j in range(len(i)):
            sums[j] += int(i[j])

    for j in sums:
        if j > rows/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"        
            epsilon += "1"

    gamma = int(str(gamma), 2)
    epsilon = int(str(epsilon), 2)

    print("\n-=-= PART ONE =-=-\n")
    print("GAMMA   : {}".format(gamma))
    print("EPSILON : {}".format(epsilon))
    print("Product : {}".format(gamma * epsilon))
    print("\n-=-= PART TWO =-=-\n")

    oxygen = p.strings
    carbon = p.strings
    for q in range(p.width):
        if len(oxygen) > 1:
            oxygen = winfilter(oxygen, q)
        if len(carbon) > 1:
            carbon = lossfilter(carbon, q)
    
    print("Oxygen levels are        : {}".format(oxygen[0]))
    print("CO2 levels are           : {}".format(carbon[0]))

    oxygen = int(str(oxygen[0]), 2)
    carbon = int(str(carbon[0]), 2)

    print("Life Support Rating is   : {}".format(oxygen*carbon))


if __name__ == "__main__":
    main()