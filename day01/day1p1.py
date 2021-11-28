#!/usr/bin/python3
# Day 1, Part 1 of Advent of Code 2021

# Sketch in a generic class for holding the input
class Problem():
    def __init__(self, filename):
        strings = []
        integers = []
        with open(filename, "r") as file:
            for line in file:
                strings.append(line)
                integers.append(int(line))
        self.strings = strings
        self.integers = integers
        return

def main():
    p = Problem("input.txt")
    i = p.integers[0]
    print(i)

if __name__ == "__main__":
    main()