class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.east = east
        self.west = west
        self.north = north
        self.bottom = bottom
    
    def rotate(self):
        tmp = self.north
        self.north = self.east
        self.east = self.south
        self.south = self.west
        self.west = tmp
    
    def printTop(self):
        print(self.top)
    
    def printWest(self):
        print(self.west)
    
    def printEast(self):
        print(self.east)
    
    def getTop(self, target):
        while self.top != target:
            self.rotate()
            if self.top == target:
                break
        else:
            print("Error")

    def getSouth(self, target):
        while self.south != target:
            self.rotate()
            if self.south == target:
                break
    
n = input().split()
count = int(input())
dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3]), int(n[4]), int(n[5]))

for i in range(count):
    buf = input().split()

    dice.getTop(int(buf[0]))
    dice.getSouth(int(buf[1]))
    dice.printEast()