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
    
    def printSouth(self):
        print(self.south)
    
    def printEast(self):
        print(self.east)
    
    def getTop(self, target):
        for i in range(3):
            self.rotate()
            if self.top == target:
                return 
        
        if self.top != target:
            print("Error")

n = input().split()
count = int(input())
dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3]), int(n[4]), int(n[5]))

for i in range(count):
    buf = input().split()
    dice.getTop(int(buf[0]))
    dice.rotate()
    dice.printEast()