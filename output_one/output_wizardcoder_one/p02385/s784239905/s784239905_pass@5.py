```python
class Dice:
    def __init__(self, numbers):
        self.numbers_inverse = {n: i for i, n in enumerate(numbers)}
        self.numbers = dict((i, n) for i, n in enumerate(numbers))
        self.vertical = [None] * 4
        self.horizontal = [None] * 5
        self.move_counts = {}

    def roll_dice(self, str):
        for s in str:
            if s == 'N':
                self.roll("S")
            elif s == 'S':
                self.roll("N")
            elif s == 'W':
                self.roll("E")
            else:
                self.roll("W")
    
    def roll(self, direction):
        if direction in "SN":
            for _ in range(4):
                if self.vertical[0] not in self.move_counts or self.move_counts[self.vertical[0]] == 0:
                    break
            else:
                self.roll("S")
            self.move_counts[self.vertical[0]] = self.move_counts.get(self.vertical[0], 0) + 1
        elif direction in "WE":
            for _ in range(4):
                if self.horizontal[0] not in self.move_counts or self.move_counts[self.horizontal[0]] == 0:
                    break
            else:
                self.roll("W")
            self.move_counts[self.horizontal[0]] = self.move_counts.get(self.horizontal[0], 0) + 1
        else:
            raise ValueError("Invalid direction")
    
    def set_top(self, value):
        while not (self.vertical[0] == value or self.roll_dice("S")): pass
        
        if self.vertical[0] != value:
            return
            
        for _ in range(4):
            self.set_front(value)
    
    def set_front(self, value):
        while not (self.vertical[1] == value or self.roll_dice("SWN")): pass
        
        if self.vertical[1] != value:
            return
        
        for _ in range(4):
            self.move_south()
    
    def move_north(self):
        self.vertical = [self.vertical[i*2-3] for i in range(5) if (i+1) % 5 != 0] + [None, None]
        
        self.horizontal[1], self.horizontal[-1] = self.vertical[0], self.vertical[0]
        self.horizontal[3], self.horizontal[-2] = self.vertical[2], self.vertical[2]
    
    def move_south(self):
        self.vertical = [self.vertical[(i+1) % 5] for i in range(4)] + [None, None]
        
        self.horizontal[1], self.horizontal[-1] = self.vertical[0], self.vertical[0]
        self.horizontal[3], self.horizontal[-2] = self.vertical[2], self.vertical[2]
    
    def move_east(self):
        self.horizontal = [self.horizontal[i*2-1] for i in range(5) if (i+1) % 4 != 0] + [None, None, None, None]
        
        self.vertical[0], self.vertical[-1] = self.horizontal[1], self.horizontal[1]
        self.vertical[2], self.vertical[-2] = self.horizontal[3], self.horizontal[3]
    
    def move_west(self):
        self.horizontal = [self.horizontal[(i+1) % 4] for i in range(5)] + [None, None, None]
        
        self.vertical[0], self.vertical[-1] = self.horizontal[1], self.horizontal[1]
        self.vertical[2], self.vertical[-2] = self.horizontal[3], self.horizontal[3]
    
    def map_values(self):
        self.numbers[1], self.numbers[2], self.numbers[4], self.numbers[6] = self.vertical[0], self.vertical[1], self.horizontal[2], self.vertical[3]
        
    def get_top(self):
        return self.vertical[0]

dice1 = Dice([int(x) for x in input().split()])
dice2 = Dice([int(x) for x in input().split()])

if dice1.numbers == dice2.numbers:
    print("Yes")
else:
    dice1.set_top(6)
    
    if all(v1 == v2 or dice1.move_counts[k] < dice2.move_counts.get(k, 0) for k in range(1, 7)):
        print("Yes")
    else:
        print("No")
```