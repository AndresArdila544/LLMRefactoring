```python
class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.bottom = bottom
    
    def rotate_n(self):
        tmp = self.top
        self.top = self.south
        self.south = self.bottom
        self.bottom = self.north
        self.north = tmp
    
    def rotate_e(self):
        tmp = self.top
        self.top = self.west
        self.west = self.bottom
        self.bottom = self.east
        self.east = tmp
    
    def rotate_s(self):
        tmp = self.top
        self.top = self.north
        self.north = self.bottom
        self.bottom = self.south
        self.south = tmp
    
    def rotate_w(self):
        tmp = self.top
        self.top = self.east
        self.east = self.bottom
        self.bottom = self.west
        self.west = tmp
    
    def print_top(self):
        print(self.top)
    
    def print_west(self):
        print(self.west)
    
    def get_top(self, target):
        if self.top == target:
            return
        for i in range(3):
            self.rotate_n()
            if self.top == target:
                return
        for i in range(3):
            self.rotate_e()
            if self.top == target:
                return
        
        if self.top != target:
            print("Error")
    
    def get_south(self, target):
        if self.south == target:
            return
        for i in range(3):
            self.rotate()
            if self.south == target:
                return
    
    def rotate(self):
        tmp = self.north
        self.north = self.east
        self.east = self.south
        self.south = self.west
        self.west = tmp
    
# Read the input for number of dice positions and values to be swapped
n = list(map(int,input().split()))
count = int(input())
dice = Dice(*n)

for i in range(count):
    buf = list(map(int, input().split()))

    dice.get_top(buf[0])
    dice.get_south(buf[1])
    
    # Print the value on east face after swapping
    dice.print_east()
```