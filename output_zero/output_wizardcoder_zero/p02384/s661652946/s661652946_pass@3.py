class Dice:
    def __init__(self, top, south, west, east, north, bottom):
        self.top = top
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.bottom = bottom
        
    def rotateN(self): #rotate clockwise
        self.top, self.south, self.west, self.east, self.north = self.south, self.east, self.bottom, self.top
        
    def rotateE(self): #rotate 90 degrees anti-clockwise
        self.top, self.west, self.east, self.south, self.bottom = self.west, self.north, self.top, self.east
    
    def printTop(self):
        print(self.top)
        
    def printWest(self):
        print(self.west)
    
    def printEast(self):
        print(self.east)
        
    def getTop(self, target):
        if self.top == target: return
        for i in range(3): self.rotateN() #check top face
        if self.top == target: return
        for i in range(3): self.rotateE() #check bottom face
        
    def getSouth(self, target):
        if self.south == target: return
        for i in range(4): self.rotateN() #check south face
    
n = input().split()
count = int(input())
dice = Dice(*map(int, n))
for _ in range(count):
    buf = map(int, input().split())
    dice.getTop(buf[0])
    dice.getSouth(buf[1])
    print(dice.west) #print east face