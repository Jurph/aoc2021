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
        # print("\n-=-=-= Calculating points =-=-=-")
        points = [[self.startx, self.starty], [self.endx, self.endy]]
        distancevector = [self.endx - self.startx, self.endy - self.starty]
        # print("Computed distance vector of {}".format(distancevector))
        if (distancevector[0] * distancevector[1]) != 0:
            points = []
            pass
            # print("This must be diagonal - generating no additional points")
        elif (distancevector[0] == distancevector[1]):
            points.pop()
            pass
            # print("Only one point to count")
        elif (distancevector[1] > 0):
            for y in range(self.starty+1, self.endy):
                points.append([self.startx, y])
            # print("Made {} vertical points: {}".format(len(range(self.starty, self.endy)), points))
        elif (distancevector[1] < 0):
            for y in range(self.endy+1, self.starty):
                points.append([self.startx, y])
            # print("Made {} vertical points: {}".format(len(range(self.starty, self.endy)), points))
        elif (distancevector[0] > 0):
            for x in range(self.startx+1, self.endx):
                points.append([x, self.starty])
            # print("Made {} horizontal points: {}".format(len(range(self.startx, self.endx)), points))
        elif (distancevector[0] < 0):
            for x in range(self.endx+1, self.startx):
                points.append([x, self.starty])
            # print("Made {} horizontal points: {}".format(len(range(self.startx, self.endx)), points))
        else:
            points = []
            pass
            # print("Made no points.")            
        self.pointlist = points
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
        self.ventchart[x][y] += vents
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
    return

if __name__ == "__main__":
    main()
