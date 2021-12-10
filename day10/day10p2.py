#!/usr/bin/python3
# Day 10, Part 1 of Advent of Code 2021
# Parsing open & closed brackets for "fun"

import sys
import pathlib
from statistics import median

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

def errorscore(character):
    table = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }
    return table.get(character)

def completionscore(string):
    cscore = 0
    table = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    for letter in string:
        cscore *= 5
        cscore += table.get(letter)
    return cscore
    

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
    partonescore = 0
    scores = []
    parttwoscore = 0

    # Compute an answer
    for chungus in p.strings:
        isError = False
        for bracket in chungus:
            if isOpen(bracket):
                stack.append(bracket)
            elif isClose(bracket):
                if bracket == matches(stack[-1]):
                    stack.pop()
                else:
                    partonescore += errorscore(bracket)
                    print("{} : Expected {} but found {} instead.".format(chungus, matches(stack[-1]),bracket))
                    isError = True
                    break
            elif isError:
                break
            else:
                pass
        if not isError:
            completionstring = ''
            stack.reverse()
            for dangler in stack:
                completionstring += matches(dangler)
            print("{} : Completion string is {} - scores {}".format(chungus, completionstring, completionscore(completionstring)))
            scores.append(completionscore(completionstring))
        stack = []
        pass

    
    print("ERROR CORRECTION SCORE: {}".format(partonescore))
    print("COMPLETION SCORE      : {}".format(median(scores)))


if __name__ == "__main__":
    main()