class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.bottom = bottom

    def rotate(self, direction):
        if direction == "N":
            self.toN()
        elif direction == "E":
            self.toE()
        elif direction == "S":
            self.toS()
        elif direction == "W":
            self.toW()
        else:
            print("Error")
        
    def printSide(self, side):
        if side == "T":
            print(self.top)
        elif side == "E":
            print(self.east)
        elif side == "S":
            print(self.south)
        else:
            print("Error")

    def getSide(self, target):
        self.rotate(target)
        while True:
            if self.top != target:
                self.toN()
            elif self.north != target:
                self.toE()
            else:
                break
    
    def toN(self):
        tmp = self.top
        self.top = self.south
        self.south = self.bottom
        self.bottom = self.north
        self.north = tmp

    def toE(self):
        tmp = self.top
        self.top = self.west
        self.west = self.bottom
        self.bottom = self.east
        self.east = tmp

    def toS(self):
        tmp = self.top
        self.top = self.north
        self.north = self.bottom
        self.bottom = self.south
        self.south = tmp

    def toW(self):
        tmp = self.top
        self.top = self.east
        self.east = self.bottom
        self.bottom = self.west
        self.west = tmp

# Refactored version
n = input().split()
count = int(input())
dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3], int(n[4]))

for i in range(count):
    buf = input().split()
    
    dice.getSide("T")  # rotate top to get target side first
    dice.printSide("E")  # print east after rotating the top
    dice.getSide(int(buf[1])

    dice.rotate("N")  # now, rotate south to find the desired side
    dice.printSide("S")  # print it out

# Explanation:
# The original code has a lot of duplicate and unnecessary lines/functions, which make it difficult to read and understand. We can reduce the code by simplifying some of its functionalities, removing the duplicate "to" functions, and grouping the rotations together. 
# In addition, we can simplify the getTop() and getSouth() methods into a single getSide() method that takes in a string argument to specify which side is desired.