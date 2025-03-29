class Dice:
    def __init__(self, dice):
        self.dice = dice
    
    @property
    def top(self):
        return self.dice[0]
    
    def roll(self, direction):
        d = self.dice
        if direction == 'N':
            self.dice = [d[1], d[5], d[2], d[3], d[0], d[4]]
        elif direction == 'E':
            self.dice = [d[3], d[1], d[0], d[5], d[4], d[2]]
        elif direction == 'S':
            self.dice = [d[4], d[0], d[2], d[3], d[5], d[1]]
        elif direction == 'W':
            self.dice = [d[2], d[1], d[5], d[0], d[4], d[3]]
    
def main():
    dice = Dice(list(map(int, input().split())))
    for c in input():
        if c == 'N':
            dice.roll('N')
        elif c == 'E':
            dice.roll('E')
        elif c == 'S':
            dice.roll('S')
        elif c == 'W':
            dice.roll('W')
    print(dice.top)
    
if __name__ == '__main__':
    main()