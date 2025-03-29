Here's a refactored version of the original code:

```python
from collections import Counter
import math

class Dice(object):
    def __init__(self, numbers):
        self._numbers = {n: i for i, n in enumerate(sorted(set(numbers), key=numbers.index)}
        self._inverse_numbers = {v: k for k, v in self._numbers.items()}
    
    def roll_dice(self, directions):
        for s in directions:
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
                self.roll_dice("SWN")
            counter += 1
    
    def set_front(self, value):
        counter = 0
        while counter < 4:
            if self.vertical[1] == value:
                self.map_values()
                return
            else:
                self.roll_dice("SWN")
            counter += 1
    
    def move_south(self):
        self._vertical = (self._vertical * 2)[3:] + [0, 0]
        self._horizontal[1] = self._vertical[0]
        self._horizontal[3] = self._vertical[2]
        self.map_values()
    
    def move_north(self):
        self._vertical = [0, 0] + (self._vertical * 2)[:2]
        self._horizontal[1] = self._vertical[0]
        self._horizontal[3] = self._vertical[2]
        self.map_values()
    
    def move_east(self):
        self._horizontal = (self._horizontal * 2)[3:] + [0, 0]
        self._vertical[0] = self._horizontal[1]
        self._vertical[2] = self._horizontal[3]
        self.map_values()
    
    def move_west(self):
        self._horizontal = [0, 0] + (self._horizontal * 2)[:2]
        self._vertical[0] = self._horizontal[1]
        self._vertical[2] = self._horizontal[3]
        self.map_values()
    
    def map_values(self):
        for i, n in enumerate((self._vertical + self._horizontal)[::-1]:
            if not hasattr(self, f'_number_{i}'):
                setattr(self, f'_number_{i}', n)
    
    def get_top(self):
        return self.getattr('_numbers')[self._vertical[0]]

    @property
    def numbers(self):
        return [getattr(self, f'_number_{i}' if hasattr(self, f'_number_{i}') else None for i in range(6)]


def compare_dice(d1, d2):
    flag = False
    
    if d1.numbers == d2.numbers:
        return True
    
    for _ in range(4):
        d1.set_top(1)
        for __ in range(3):
            d1.roll_dice('SWN')
            if d1.numbers == d2.numbers:
                return True
    
    d1.roll_dice("S")
    
    return False

if __name__ == '__main__':
    dice1 = Dice(sorted([int(x) for x in input().split()])
    dice2 = Dice(sorted([int(x) for x in input().split()]
    
    if compare_dice(dice1, dice2):
        print("Yes")
    else:
        print("No")
```