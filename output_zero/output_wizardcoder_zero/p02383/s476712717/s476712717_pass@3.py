```python
class Dice:
    def __init__(self, dice):
        self._dice = dice

    def roll_n(self):
        self._dice = [self._dice[1], self._dice[5], self._dice[2], self._dice[0], self._dice[4]]

    def roll_e(self):
        self._dice = [self._dice[3], self._dice[1], self._dice[0], self._dice[4], self._dice[2]]

    def roll_s(self):
        self._dice = [self._dice[4], self._dice[0], self._dice[2], self._dice[3], self._dice[5]]
    
    def roll_w(self):
        self._dice = [self._dice[2], self._dice[1], self._dice[5], self._dice[0], self._dice[4]]
    
    def top(self):
        return self._dice[0]

def main():
    dice = Dice(list(map(int,input().split()))
    for c in input():
        if c == 'N': dice.roll_n()
        if c == 'E': dice.roll_e()
        if c == 'S': dice.roll_s()
        if c == 'W': dice.roll_w()
    print(dice.top())
```