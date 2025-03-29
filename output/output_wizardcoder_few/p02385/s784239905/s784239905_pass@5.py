class Dice(object):
    """Dice Class
    
    """

    def __init__(self, numbers):
        self.numbers_inverse = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4], 6: numbers[5]}
        self.numbers = {numbers[0]: 1, numbers[1]: 2, numbers[2]: 3, numbers[3]: 4, numbers[4]: 5, numbers[5]: 6}
        
        self.vertical = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal = [self.numbers[4], self.numbers[1], self.numbers[3], self.numbers[6]

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
        while counter < 4:
            if self.vertical[0] == value:
                self.map_values()
                return
            else:
                self.roll_dice("S")
            counter += 1
        
    def set_front(self, value):
        while counter < 4:
            if self.vertical[1] == value:
                self.map_values()
                return
            else:
                self.roll_dice("SWN")
            counter += 1

    def move_south(self):
        self.vertical = (self.vertical * 2)[3:7]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        self.map_values()
        
    def move_north(self):
        self.vertical = (self.vertical * 2)[1:5]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        self.map_values()
        
    def move_east(self):
        self.horizontal = (self.horizontal * 2)[3:7]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        self.map_values()
        
    def move_west(self):
        self.horizontal = (self.horizontal * 2)[1:5]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        self.map_values()
        
    def map_values(self):
        self.numbers[1] = self.vertical[0]
        self.numbers[2] = self.vertical[1]
        self.numbers[3] = self.horizontal[2]
        self.numbers[4] = self.horizontal[0]
        self.numbers[5] = self.vertical[3]
        self.numbers[6] = self.vertical[2]