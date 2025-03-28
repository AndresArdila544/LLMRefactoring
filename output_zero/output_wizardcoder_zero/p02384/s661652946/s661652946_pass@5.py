class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.bottom = bottom
        
    def toN(self):
        self.top, self.south, self.bottom, self.north = self.south, self.bottom, self.top
        
    def toE(self):
        self.top, self.west, self.bottom, self.east = self.west, self.bottom, self.top

    def toS(self):
        self.top, self.north, self.bottom, self.south = self.north, self.bottom, self.top
        
    def toW(self):
        self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.top
        
    def printTop(self):
        print(self.top)
    
    def printWest(self):
        print(self.west)
        
    def getTop(self, target):
        for i in range(3):
            if self.top == target:
                return
            elif self.south == target:
                self.toN()
            elif self.east == target:
                self.toN(); self.toW(); self.toN()
            else:
                print("Error")
                
    def getSouth(self, target):
        for i in range(3):
            if self.south == target:
                return
            elif self.north == target:
                self.lotate()
            elif self.east == target:
                self.toN(); self.toW(); self.toN(); self.toE()
        else:
            print("Error")
            
    def lotate(self):
        self.north, self.east, self.south, self.west = self.east, self.south, self.west, self.north
        
dice = Dice(*map(int, input().split()))

for i in range(int(input())):
    dice.getTop(int(input()); dice.getSouth(int(input())); dice.printEast()