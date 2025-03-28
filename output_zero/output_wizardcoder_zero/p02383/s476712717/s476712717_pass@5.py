class Dice:
    def __init__(self, dice):
        self.dice = dice
        
    def roll(self, direction):
        d = self.dice
        if direction == 'N':
            self.dice = [d[1], d[5], d[2], d[0], d[4]]
        elif direction == 'E':
            self.dice = [d[3], d[1], d[0], d[4], d[2]]
        elif direction == 'S':
            self.dice = [d[4], d[0], d[2], d[3], d[5]
        elif direction == 'W':
            self.dice = [d[2], d[1], d[5], d[0], d[4]]
    
    def top(self):
        return self.dice[0]
        
def main():
    dice_list = list(map(int, input().split()))
    direction = input()
    while direction:
        d = Dice(dice_list)
        getattr(d, f"roll_{direction}")()
        print(d.top())
        direction = input()

if __name__ == '__main__':
    main()