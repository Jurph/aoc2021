#!/usr/bin/python3
# Day 1, Part 1 of Advent of Code 2021
# Measure how many times the depth increased in a list of sonar measurements

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        strings = [] # We don't need strings in this chapter but it's a neat feature
        integers = []
        with open(filename, "r") as file:
            for line in file:
                strings.append(line)
                integers.append(int(line))
        self.strings = strings
        self.integers = integers
        return

def main():
    # Ingest and format the data
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day01\\input.txt")

    # Set up state variables 
    total = 0
    previous = -1

    # Compute an answer
    for i in p.integers:
        if previous == -1:
            print("N/A - no previous measurement")
        elif i > previous:
            print("{}  (increased)".format(i))
            total += 1
        elif i < previous:
            print("{}  (decreased)".format(i))
        elif i == previous:
            print("{}  (no change)".format(i))
        else:
            print("{}  (ERROR: {} , {})".format(i, previous))
        previous = i
    print("-=-=-=-=-\n")
    print("{} measurements were larger than the previous one.\n".format(total))


if __name__ == "__main__":
    main()