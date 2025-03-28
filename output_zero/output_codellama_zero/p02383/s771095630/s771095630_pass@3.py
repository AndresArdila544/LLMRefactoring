class Dice:
    def __init__(self, default = [1, 2, 3, 4, 5, 6]):
        self.d = default

    def rotate(self, direction):
        if direction == 'E':
            self.d[0], self.d[2], self.d[3], self.d[5] = self.d[3], self.d[0], self.d[5], self.d[2]
        elif direction == 'W':
            self.d[0], self.d[2], self.d[3], self.d[5] = self.d[2], self.d[5], self.d[0], self.d[3]
        elif direction == 'S':
            self.d[0], self.d[1], self.d[4], self.d[5] = self.d[1], self.d[5], self.d[0], self.d[4]
        else:
            self.d[0], self.d[1], self.d[4], self.d[5] = self.d[4], self.d[0], self.d[5], self.d[1]

    def top(self):
        return self.d[0]

def main():
    dice = Dice([int(i) for i in input().split()])
    for o in input():
        dice.rotate(o)
    print(dice.top())

if __name__ == '__main__':
    main()