#!/usr/bin/python3
# Day 1, Part 1 of Advent of Code 2021

# Sketch in a generic class for holding the input
class Problem():
    def __init__(self, filename):
        integers = []
        with open(filename, "r") as file:
            for line in file:
                integers.append(int(line))
        self.integers = integers
        self.threesums = self.slidingwindow(integers, 3)
        return
    
    def slidingwindow(self, measurements, windowsize):
        windows = [0] * (len(measurements) - windowsize + 1)
        for i in range(len(windows)):
            for j in measurements[i:i+windowsize]:
                windows[i] += j
        return windows

def main():
    total = 0
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day01\\input.txt")
    previous = -1
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