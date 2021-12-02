#!/usr/bin/python3
# Day 2, Part 1 of Advent of Code 2021
# Convert commands into a final depth and travel position

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        strings = []
        commands = []
        with open(filename, "r") as file:
            for line in file:
                strings.append(line)
        self.strings = strings
        command = "nothing"
        magnitude = 0
        for entry in strings:
            command, magnitude = entry.split(" ")
            magnitude = int(magnitude)
            commands.append([command, magnitude])
        self.commands = commands
        return

class Submarine():
    def __init__(self, position=list):
        self.x = position[0]
        self.y = position[1]
        self.depth = 0
        return


def main():
    # Ingest and format the data
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day02\\input.txt")

    # Set up state variables 
    depth = 0
    range = 0

    # Compute an answer
    for order in p.commands:
        command = order[0]
        magnitude = int(order[1])
        if command == "forward":
            range += magnitude
        elif command == "down":
            depth += magnitude
        elif command == "up":
            depth -= magnitude
        else:
            print("ERROR: encountered unknown command")

    print("-=-=-=-=-")
    print("DEPTH: {}\nRANGE: {}\nConfirmation Code: {}\n".format(depth, range, depth * range))


if __name__ == "__main__":
    main()