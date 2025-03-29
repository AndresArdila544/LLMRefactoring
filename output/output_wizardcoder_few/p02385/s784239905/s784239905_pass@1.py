class Dice(object):
    def __init__(self, numbers):
        self.numbers = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4], 6: numbers[5]}
        
        self.vertical = [self.numbers[num] for num in (1,2,6,5) if num != 0] # removes zeros from vertical list
        self.horizontal = {4: self.numbers[1], 1: self.numbers[3], 2: self.numbers[5]} # creates dictionary to map values horizontally
    
    def roll_dice(self, str):
        for s in str:
            if s == 'N':
                self.move_north()
            elif s == 'S':
                self.move_south()
            elif s == 'W':
                self.move_west()
            elif s == 'E':
                self.move_east()
    
    def set_top(self, value):
        counter = 0
        while not (self.vertical[0] == value and self.horizontal[1] == value) or counter >= 8:
            if self.roll_dice("SWN") != value:
                self.set_front(value)
            counter += 1
            
    def set_front(self, value):
        while not (self.vertical[0] == value and self.horizontal[3] == value) or counter >= 8:
            if self.roll_dice("SWN") != value:
                self.set_top(value)
    
    def move_south(self):
        self.vertical = self.vertical * 2
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        
    def move_north(self):
        self.vertical = self.vertical[-4:] + self.vertical[:2]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        
    def move_east(self):
        self.horizontal = self.horizontal * 2
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
    
    def move_west(self):
        self.horizontal = self.horizontal[-4:] + self.horizontal[:2]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        
    def map_values(self):
        self.numbers[1] = self.vertical[0]
        self.numbers[2] = self.vertical[1]
        self.numbers[3] = self.horizontal[2]
        self.numbers[4] = self.horizontal[0]
        self.numbers[5] = self.vertical[3]
        self.numbers[6] = self.vertical[2]
        
    def get_top(self):
        return self.vertical[0]
    
dice1, dice2 = Dice([int(x) for x in input().split()]), Dice([int(x) for x in input().split()])
if all(dice1.numbers[i] == dice2.numbers[i] for i in range(1,6)) or any(Dice(list(map(lambda x: (x-dice2.get_top()) % 6, dice1.numbers))):
    print("Yes")
else:
    print("No")