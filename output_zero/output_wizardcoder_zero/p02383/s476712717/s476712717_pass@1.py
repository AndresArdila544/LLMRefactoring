```python
class DiceRoll:
    def __init__(self):
        self.dice = [int(x) for x in input().split()]
        
    def roll_north(self):
        self.dice[1], self.dice[5], self.dice[2], self.dice[0], self.dice[4] = self.dice[1], self.dice[5], self.dice[2], self.dice[0], self.dice[4]
    
    def roll_east(self):
        self.dice[3], self.dice[1], self.dice[0], self.dice[4], self.dice[2] = self.dice[3], self.dice[1], self.dice[0], self.dice[4], self.dice[2]
        
    def roll_south(self):
        self.dice[4], self.dice[0], self.dice[2], self.dice[3], self.dice[1] = self.dice[4], self.dice[0], self.dice[2], self.dice[3], self.dice[1]
        
    def roll_west(self):
        self.dice[2], self.dice[1], self.dice[5], self.dice[0], self.dice[4] = self.dice[2], self.dice[1], self.dice[5], self.dice[0], self.dice[4]
        
    def top(self):
        return max(self.dice)
        
def main():
    d = DiceRoll()
    for c in input():
        if c == 'N': d.roll_north()
        elif c == 'E': d.roll_east()
        elif c == 'S': d.roll_south()
        elif c == 'W': d.roll_west()
    print(d.top())
    
if __name__ == '__main__':
    main()