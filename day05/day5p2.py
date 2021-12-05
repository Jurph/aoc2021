#!/usr/bin/python3
# Day 5, Part 1 of Advent of Code 2021
# Finding volcanic vents on the sea floor

import sys
import pathlib

class Survey():
    def __init__(self, filename:str):
        entries = []
        self.readings = []
        self.span = 0
        with open(filename, "r") as file:
            for line in file:
                entries.append(line.rsplit())
        for e in entries:
            self.readings.append(Reading(e))
        for r in self.readings:
            self.span = max(self.span, r.span)
        return

class Reading():
    def __init__(self, surveystrings:list):
        del surveystrings[1]        # Removes the "->" entry from the list
        startpoint = list(map(int, surveystrings[0].split(",")))
        endpoint = list(map(int, surveystrings[1].split(",")))
        self.pointlist = []
        self.startx = int(startpoint[0])
        self.starty = int(startpoint[1])
        self.endx = int(endpoint[0])
        self.endy = int(endpoint[1])
        self.fillPoints()
        self.span = max(self.startx, self.starty, self.endx, self.endy)
        return

    def fillPoints(self):
        points = [[self.startx, self.starty], [self.endx, self.endy]]
        dist = [self.endx - self.startx, self.endy - self.starty]
        if (dist[0] * dist[1]) != 0: # Must be diagonal
            if dist[0] > dist[1]: # of the form (8, -8) : EndX larger, EndY smaller
                for d in range(1, dist[0]):
                    points.append([self.startx + d, self.starty - d])
            elif dist[0] < dist[1]: # of the form (-8, 8) : EndX smaller, EndY larger
                for d in range(1, dist[1]):
                    points.append([self.startx - d, self.starty + d])
            elif abs(dist[0]) == dist[0]: # of the form (8, 8) : End points both larger 
                for d in range(1, abs(dist[0])):
                    points.append([self.startx + d, self.starty + d])
            else: # of the form (-8, -8) : End points both smaller
                for d in range(1, abs(dist[0])):
                    points.append([self.startx - d, self.starty - d])
        elif (dist[1] > 0):
            for y in range(self.starty+1, self.endy):
                points.append([self.startx, y])
        elif (dist[1] < 0):
            for y in range(self.endy+1, self.starty):
                points.append([self.startx, y])
        elif (dist[0] > 0):
            for x in range(self.startx+1, self.endx):
                points.append([x, self.starty])
        elif (dist[0] < 0):
            for x in range(self.endx+1, self.startx):
                points.append([x, self.starty])
        else:
            print("ERROR calculating {} - made no points".format(points))
            points = []
            pass
        self.pointlist = points
        return
        

class SeaFloor():
    def __init__(self, size=1000):
        self.size = size
        self.ventchart = [[0 for _ in range(size)] for _ in range(size)]
        return

    # AddVent of Code 2021
    def addvent(self, xypoint: list, vents=1):
        x = xypoint[0]
        y = xypoint[1]
        # We use "y, x" notation so our visualized grid matches the example
        self.ventchart[y][x] += vents
        return

    def countvents(self, dangerlevel=1):
        dangerousvents = 0
        for row in self.ventchart:
            for entry in row:
                if entry >= dangerlevel:
                    dangerousvents += 1
                else:
                    pass
        return dangerousvents

    def print(self, maxsize=80):
        if self.size > maxsize:
            print("Sea Chart exceeds {0} x {0} - No Display".format(maxsize))
        else:
            printstring = ""
            for row in self.ventchart:
                rowstring = "  "
                for entry in row:
                    if entry == 0:
                        rowstring += "."
                    else:
                        rowstring += str(entry)
                printstring += rowstring
                printstring += "\n"
            print(printstring)
        return


def main():
    # Parse command-line args to see if a non-default file is specified
    if len(sys.argv) > 1:
        filename = pathlib.Path(sys.argv[1])
    else:
        filename = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day05\\test.txt"
        print("No input file specified.")
    print("Using {}\n\n".format(filename))

    # Start solving the problem
    survey = Survey(filename)
    f = SeaFloor(survey.span + 1)
    dangerlevel = 2
    for r in survey.readings:
        for p in r.pointlist:
            f.addvent(p)

    # Output the answers 
    # For my inputs the correct answers are
    #   test.txt  - 12      [prints a chart]
    #   input.txt - 18442   [no chart print]
    print("DANGER SCAN: Found {} vents of Danger Level {} or worse\n".format(f.countvents(dangerlevel), dangerlevel))
    f.print()
    return

if __name__ == "__main__":
    main()