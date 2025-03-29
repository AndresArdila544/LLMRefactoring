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
        if self.top == target:
            return
        for i in range(3):
            self.rotate()
            if self.top == target:
                return
        else:
            print("Error")

dice = Dice(int(input().split()[0]), int(input().split()[1]), int(input().split()[2]), int(input().split()[3]), int(input().split()[4]), int(input().split()[5]))
count = int(input())

for i in range(count):
    buf = input().split()

    dice.getTop(int(buf[0]))
    dice.getSouth(int(buf[1]))
    dice.printEast()