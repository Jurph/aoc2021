#!/usr/bin/python3
# Day 3, Part 1 of Advent of Code 2021
# Measure the most common bit(s) in a binary string 

import binascii

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        strings = [] # We don't need strings in this chapter but it's a neat feature
        with open(filename, "r") as file:
            for line in file:
                strings.append(line.rstrip())
        self.strings = strings
        return

def main():
    # Ingest and format the data
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day03\\input.txt")

    # Set up state variables 
    gamma = ""
    epsilon = ""
    rows = len(p.strings)
    sums = [0]*len(p.strings[0])

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

    print("GAMMA   : {}".format(gamma))
    print("EPSILON : {}".format(epsilon))
    print("Product : {}".format(gamma * epsilon))

if __name__ == "__main__":
    main()