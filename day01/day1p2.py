#!/usr/bin/python3
# Day 1, Part 2 of Advent of Code 2021
# Sum three elements in a list and compare them to the previous sum 

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        integers = []
        with open(filename, "r") as file:
            for line in file:
                integers.append(int(line))
        self.integers = integers
        self.threesums = self.slidingwindow(integers, 3)
        return
    
    # slidingwindow computes the sum of 'windowsize' elements in a list of measurements
    def slidingwindow(self, measurements, windowsize):
        windows = [0] * (len(measurements) - windowsize + 1)
        for i in range(len(windows)):
            for j in measurements[i:i+windowsize]:
                windows[i] += j
        return windows

def main():
    # Ingest and structure the data
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day01\\input.txt")

    # Set globals and state variables 
    total = 0
    previous = -1

    # Compute the solution 
    for i in p.threesums:
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