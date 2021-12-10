#!/usr/bin/python3
# Day 10, Part 1 of Advent of Code 2021
# Parsing open & closed brackets for "fun"

import sys
import pathlib

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        strings = [] 
        with open(filename, "r") as file:
            for line in file:
                strings.append(line.rstrip())
        self.strings = strings
        return

def matches(character):
    complements = { 
        "(" : ")",
        ")" : "(",
        "[" : "]",
        "]" : "[",
        "{" : "}",
        "}" : "{",
        "<" : ">",
        ">" : "<"
    }
    return complements.get(character)

def isOpen(character):
    openers = ["(", "[", "<", "{"]
    if character in openers:
        return True
    else:
        return False

def isClose(character):
    closers = [")", "]", ">", "}"]
    if character in closers:
        return True
    else:
        return False

def score(character):
    table = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }
    return table.get(character)

def main():
        # Parse command-line args to see if a non-default file is specified
    if len(sys.argv) > 1:
        filename = pathlib.Path(sys.argv[1])
    else:
        filename = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day10\\test.txt"
        print("No input file specified.")
    print("Using {}\n\n".format(filename))
    
    # Ingest and format the data
    p = Problem(filename)
    # print("First character: {} \nExpected complement: {}".format(p.strings[0][0], matches(p.strings[0][0])))

    # Set up state variables 
    stack = []
    totalscore = 0

    # Compute an answer
    for chungus in p.strings:
        for bracket in chungus:
            if isOpen(bracket):
                stack.append(bracket)
            elif isClose(bracket):
                if bracket == matches(stack[-1]):
                    stack.pop()
                else:
                    totalscore += score(bracket)
                    print("Expected {} but found {} instead.".format(matches(stack[-1]),bracket))
                    break
            else:
                pass
        print("If I got this far, it must be an incomplete line...")
        pass
    
    print("Total score was {}".format(totalscore))


if __name__ == "__main__":
    main()