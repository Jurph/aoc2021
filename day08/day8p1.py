#!/usr/bin/python
# Advent of Code Day 8, Part 1
# 7-segment LED lights
# but make it broken 

import sys
import pathlib

class Problem():
    def __init__(self, filename):
        decks = []
        quads = []
        with open(filename, "r") as file:
            for line in file:
                data = line.rstrip("\n").split("|")
                decks.append(data[0].split(" ")) # Ten scrambled codes 
                quads.append(data[1].split(" ")) # Four scrambled codes
            for d in decks:
                d.remove('')
            for q in quads:
                q.remove('')
        self.decks = decks
        self.quads = quads
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
    p = Problem(filename)
    # print(p.decks, "\n\n", p.quads)
    uniques = [2, 3, 4, 7]
    count = 0
    for q in p.quads:
        for i in q:
            if len(i) in uniques:
                count += 1
    print("Found {} easily resolved values in the quads.".format(count))



if __name__ == "__main__":
    main()