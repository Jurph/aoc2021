#!/usr/bin/python3
# Day 5, Part 1 of Advent of Code 2021
# Finding volcanic vents on the sea floor

import sys
import pathlib

class Survey():
    def __init__(self, filename):
        entries = []
        self.readings = []
        with open(filename, "r") as file:
            for line in file:
                entries.append(line.rsplit())
        for e in entries:
            self.readings.append(Reading(e))
        return

class Reading():
    def __init__(self, surveystring):
        del surveystring[1]
        startpoint = list(map(int, surveystring[0].split(",")))
        endpoint = list(map(int, surveystring[1].split(",")))
        self.pointlist = []
        self.startx = int(startpoint[0])
        self.starty = int(startpoint[1])
        self.endx = int(endpoint[0])
        self.endy = int(endpoint[1])
        points = [[self.startx, self.endx], [self.starty, self.endy]]
        self.isVertical = False
        self.isHorizontal = False
        self.isDiagonal = False
        if self.startx == self.endx:
            self.isVertical == True
        elif self.starty == self.endy:
            self.isHorizontal == True
        else:
            self.isDiagonal == True
        self.fillPoints()
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
        print(points)
        return
        

class SeaFloor():
    def __init__(self, x=1000, y=1000):
        self.easting = x
        self.northing = y
        self.ventchart = [[0 for _ in range(x)] for _ in range(y)]
        return

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

    def print(self):
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
    print("...using {}".format(filename))
    survey = Survey(filename)
    f = SeaFloor()
    for r in survey.readings:
        for p in r.pointlist:
            f.addvent(p)
    print("DANGER SCAN: Found {} vents of Danger Level 2 or worse".format(f.countvents(2)))
    # f.print()
    return

if __name__ == "__main__":
    main()
