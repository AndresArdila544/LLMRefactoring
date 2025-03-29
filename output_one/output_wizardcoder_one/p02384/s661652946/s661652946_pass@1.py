class Dice:
    def __init__(self, top, south, west, east, north, bottom):
        self.top = top
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.bottom = bottom

    def toN(self):
        tmp = self.top
        self.top, self.south, self.bottom, self.north = self.south, self.bottom, self.top

    def toE(self):
        tmp = self.top
        self.top, self.west, self.bottom, self.east = self.bottom, self.east, self.west

    def toW(self):
        tmp = self.top
        self.top, self.north, self.south, self.west = self.bottom, self.south, self.north

    def printTop(self):
        print(self.top)

    def printWest(self):
        print(self.west)

    def getTop(self, target):
        if self.top == target:
            return
        for i in range(3):
            self.toN()
            if self.top == target:
                return
        for i in range(3):
            self.toE()
            if self.top == target:
                return
        
        if self.top != target:
            print("Error")

    def getSouth(self, target):
        if self.south == target:
            return
        for i in range(3):
            self.toN()
            if self.south == target:
                return
    
    def lotate(self):
        tmp = self.north
        self.north, self.east, self.south, self.west = self.east, self.south, self.west, self.north

n = list(map(int, input().split()))
count = int(input())
dice = Dice(n[0], n[1], n[2], n[3])

for i in range(count):
    buf = map(int, input().split())
    dice.getTop(buf[0])
    dice.getSouth(buf[1])
    dice.printEast()