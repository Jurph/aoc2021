#!/usr/bin/python
# Advent of Code Day 8, Part 2
# 7-segment LED lights
# but make it REALLY broken 

import sys
import pathlib

class Problem():
    def __init__(self, filename):
        decks = []
        quads = []
        with open(filename, "r") as file:
            for line in file:
                data = line.rstrip("\n").split("|")
                decks.append(data[0].split(" ")) # Ten scrambled codes 
                quads.append(data[1].split(" ")) # Four scrambled codes
            for d in decks:
                d.remove('')
            for q in quads:
                q.remove('')
        self.decks = decks
        self.quads = quads
        self.length = len(decks)
        return

class SevenSegmentScramble():
    def __init__(self, tenItemList, fourItemList):
        scrambles = []
        quadjumble = []
        numbers = {}
        
        # Set up the list of 10 scrambles 
        # and the list of 4 jumbles 
        for i in tenItemList:
            scrambles.append(set(i)) 
            # TODO: if you use frozenset, you can use these as keys in a hash table!!
            # Which changes the whole complexion of the code below but also makes it 
            # WAAAAY better-er. 
            # https://docs.python.org/3/library/stdtypes.html#frozenset

        # Unscramble four trivial cases
        for abc in scrambles:
            if len(abc) == 2:
                numbers.update({'1' : abc})
            elif len(abc) == 3:
                numbers.update({'7' : abc})
            elif len(abc) == 4:
                numbers.update({'4' : abc})
            elif len(abc) == 7:
                numbers.update({'8' : abc})
            else:
                continue

        # Unscramble six-segment cases using uniques
        print("Resolved uniques.")
        print("ONE      : {}".format(numbers.get('1')))
        print("FOUR     : {}".format(numbers.get('4')))
        print("SEVEN    : {}".format(numbers.get('7')))
        print("EIGHT    : {}".format(numbers.get('8')))
        for abcdef in scrambles:
            if len(abcdef) == 6:
                if len(abcdef.intersection(numbers.get('1'))) < 2:
                    print("SIX  : {}".format(abcdef))
                    numbers.update({'6' : abcdef})
                elif numbers.get('4').issubset(abcdef):
                    print("NINE  : {}".format(abcdef))
                    numbers.update({'9' : abcdef})
                else:
                    print("ZERO  : {}".format(abcdef))
                    numbers.update({'0' : abcdef})
                    continue
            else:
                continue

        # Unscramble five-segment cases using sixes
        for abcde in scrambles:
            if len(abcde) == 5:
                if numbers.get('1').issubset(abcde):
                    numbers.update({'3' : abcde})
                    print("THREE    : {}".format(abcde))                    
                elif abcde.issubset(numbers.get('9')):
                    numbers.update({'5' : abcde})
                    print("FIVE    : {}".format(abcde))
                else:
                    print("TWO    : {}".format(abcde))
                    numbers.update({'2' : abcde})
                    continue
            else:
                continue
        self.numbers = numbers
        
        # This part is hideous. I blame my COVID booster shot. 
        # NOTE: I do not actually blame my COVID shot. TWAJS.
        values = {}
        ordinals = []
        for i in '0123456789':
            values.update({''.join(numbers.get(i)) : i})
            ordinals.append([i, numbers.get(i)])
        self.values = values

        fourDigitString = ''
        for item in fourItemList:
            for k in ordinals:
                if set(k[1]) == set(item):
                    fourDigitString += k[0]

        self.fourDigitValue = int(fourDigitString)
        return




def main():
    # Parse command-line args to see if a non-default file is specified
    if len(sys.argv) > 1:
        filename = pathlib.Path(sys.argv[1])
    else:
        filename = "C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2021\\day07\\test.txt"
        print("No input file specified.")
    print("Using {}\n\n".format(filename))

    # File I/O
    p = Problem(filename)

    # Brute force the problem
    total = 0
    for i in range(p.length):
        s = SevenSegmentScramble(p.decks[i], p.quads[i])
        total += s.fourDigitValue
    print(total)

if __name__ == "__main__":
    main()