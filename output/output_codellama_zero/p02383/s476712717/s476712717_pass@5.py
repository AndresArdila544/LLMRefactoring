class Dice:
    def __init__(self, dice):
        self.dice = dice

    def roll(self, direction):
        if direction == 'N':
            return [self.dice[1], self.dice[5], self.dice[2], self.dice[3], self.dice[0], self.dice[4]]
        elif direction == 'E':
            return [self.dice[3], self.dice[1], self.dice[0], self.dice[5], self.dice[4], self.dice[2]]
        elif direction == 'S':
            return [self.dice[4], self.dice[0], self.dice[2], self.dice[3], self.dice[5], self.dice[1]]
        elif direction == 'W':
            return [self.dice[2], self.dice[1], self.dice[5], self.dice[0], self.dice[4], self.dice[3]]

    def top(self):
        return self.dice[0]

def main():
    d = Dice(list(map(int, input().split())))
    com = input()
    for c in com:
        if c == 'N':
            d.roll('N')
        elif c == 'E':
            d.roll('E')
        elif c == 'S':
            d.roll('S')
        elif c == 'W':
            d.roll('W')
    print(d.top())

if __name__ == '__main__':
    main()