#!/usr/bin/python
# Advent of Code Day 6, Part 1
# Lanternfish Spawning Simulator

import sys
import pathlib

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

    # Count fish at the start
    fishages = [0]*10
    for s in survey:
        fishages[s] += 1

    days = 256

    # Begin simulation
    for d in range(1, days+1):
        for age in range(10):
            if age == 0:
                parents = fishages[age]
            else:
                fishages[age-1] = fishages[age]
        fishages[6] += parents
        fishages[8] = parents
        parents = 0
        print("After {} days: {} fish : {}".format(d, sum(fishages), fishages))

    return



if __name__ == "__main__":
    main()