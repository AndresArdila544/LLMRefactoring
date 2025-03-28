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
            tmp = self.top
            self.top = self.south
            self.south = self.bottom
            self.bottom = self.north
            self.north = tmp
        elif direction == "E":
            tmp = self.top
            self.top = self.west
            self.west = self.bottom
            self.bottom = self.east
            self.east = tmp
        elif direction == "S":
            tmp = self.top
            self.top = self.north
            self.north = self.bottom
            self.bottom = self.south
            self.south = tmp
        elif direction == "W":
            tmp = self.top
            self.top = self.east
            self.east = self.bottom
            self.bottom = self.west
            self.west = tmp
        else:
            raise ValueError("Invalid direction")
    
    def printTop(self):
        print(self.top)
    
    def printWest(self):
        print(self.west)
    
    def getTop(self, target):
        for i in range(3):
            self.rotate("N")
            if self.top == target:
                return
        for i in range(3):
            self.rotate("E")
            if self.top == target:
                return
    
        if self.top != target:
            print("Error")
    
    def getSouth(self, target):
        for i in range(3):
            self.rotate("N")
            if self.south == target:
                return
    
    def lotate(self):
        tmp = self.north
        self.north = self.east
        self.east = self.south
        self.south = self.west
        self.west = tmp

n = input().split()
count = int(input())
dice = Dice(*map(int, n))

for i in range(count):
    buf = input().split()
    dice.getTop(int(buf[0]))
    dice.getSouth(int(buf[1]))
    dice.printEast()