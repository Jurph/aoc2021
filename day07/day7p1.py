#!/usr/bin/python
# Advent of Code Day 7, Part 1
# Crab Submarines

import sys
import pathlib

def fuelcost(travel: int):
    return int((travel) * (travel + 1)/2)

def main():
    # Parse command-line args to see if a non-default file is specified
    if len(sys.argv) > 1:
        filename = pathlib.Path(sys.argv[1])
    else:
        filename = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day06\\test.txt"
        print("No input file specified.")
    print("Using {}\n\n".format(filename))

    # File I/O
    with open(filename, "r") as file:
        survey = list(map(int, file.read().rstrip("\n").split(",")))

    # Set left and right bounds
    left = min(survey)
    right = max(survey)

    # Begin simulation
    best = 999999999999999999999999
    for newposition in range(left, right+1):
        fuel = 0
        for position in survey:
            fuel += fuelcost(abs(newposition - position))
        if fuel < best:
            best = fuel
            print("New optimum: {} fuel at position {}".format(best, newposition))

    return



if __name__ == "__main__":
    main()