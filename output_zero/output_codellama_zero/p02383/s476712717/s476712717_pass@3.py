import random

class Dice:
    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.values = []
    
    def roll(self):
        for _ in range(self.num_dice):
            self.values.append(random.randint(1, 6))
    
    def top(self):
        return sorted(self.values)[-1]

def main():
    num_dice = int(input())
    dice = Dice(num_dice)
    dice.roll()
    com = input()
    for c in com:
        if c == 'N': dice.roll_n()
        if c == 'E': dice.roll_e()
        if c == 'S': dice.roll_s()
        if c == 'W': dice.roll_w()
    print(dice.top())

if __name__ == '__main__':
    main()