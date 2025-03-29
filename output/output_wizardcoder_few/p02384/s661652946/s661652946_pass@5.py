class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.bottom = bottom

    def rotateN(self):
        tmp = self.top
        self.top = self.south
        self.south = self.bottom
        self.bottom = self.north
        self.north = tmp

    def rotateE(self):
        tmp = self.top
        self.top = self.west
        self.west = self.bottom
        self.bottom = self.east
        self.east = tmp

    def rotateS(self):
        tmp = self.top
        self.top = self.north
        self.north = self.bottom
        self.bottom = self.south
        self.south = tmp

    def rotateW(self):
        tmp = self.top
        self.top = self.east
        self.east = self.bottom
        self.bottom = self.west
        self.west = tmp

    def printTop(self):
        print(self.top)

    def printWest(self):
        print(self.west)

    def printEast(self):
        print(self.east)

    def getTop(self, target):
        for i in range(3):
            self.rotateN()
            if self.top == target:
                return
        for i in range(3):
            self.rotateE()
            if self.top == target:
                return
        print("Error")

    def getSouth(self, target):
        for i in range(4):
            self.rotateW()
            if self.south == target:
                return

n = input().split()
count = int(input())
dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3]))

for i in range(count):
    buf = input().split()
    dice.getTop(int(buf[0])
    dice.getSouth(int(buf[1]))
    dice.printEast()