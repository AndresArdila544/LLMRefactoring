class Dice:
    def __init__(self, top, south, west, east, north):
        self.top = top
        self.south = south
        self.west = west
        self.east = east
        self.north = north

    
    def rotate_N(self):
        tmp = self.top
        self.top = self.south
        self.south = self.bottom
        self.bottom = self.north
        self.north = tmp
    
    def rotate_E(self):
        tmp = self.top
        self.top = self.west
        self.west = self.bottom
        self.bottom = self.east
        self.east = tmp

    def rotate_S(self):
        tmp = self.top
        self.top = self.north
        self.north = self.bottom
        self.bottom = self.south
        self.south = tmp

    def rotate_W(self):
        tmp = self.top
        self.top = self.east
        self.east = self.bottom
        self.bottom = self.west
        self.west = tmp
    
    def printTop(self):
        print(self.top)

    def printWest(self):
        print(self.west)

    def getTop(self, target):
        if self.top == target:
            return
        for i in range(3):
            self.rotate_N()
            if self.top == target:
                return
        for i in range(3):
            self.rotate_E()
            if self.top == target:
                return
        
        if self.top != target:
            print("Error")
    
    def getSouth(self, target):
        for i in range(3):
            self.rotate_N()
            if self.south == target:
                return

    def rotate(self, direction):
        if direction == 'N':
            self.rotate_N()
        elif direction == 'E':
            self.rotate_E()
        elif direction == 'S':
            self.rotate_S()
        elif direction == 'W':
            self.rotate_W()

n = input().split()
count = int(input())
dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3]))

for i in range(count):
    buf = input().split()
    dice.getTop(int(buf[0]))
    dice.rotate(buf[1])
    dice.printEast()