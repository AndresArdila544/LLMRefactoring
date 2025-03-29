class Dice:
    def __init__(self, nums):
        self.top, self.front, self.right, self.left, self.back, self.bottom = nums

    def roll(self, direction):
        if direction == 'E':
            self.top, self.right, self.left, self.bottom = self.left, self.top, self.bottom, self.right
        elif direction == 'N':
            self.top, self.front, self.back, self.bottom = self.front, self.bottom, self.top, self.back
        elif direction == 'S':
            self.top, self.front, self.back, self.bottom = self.back, self.top, self.bottom, self.front
        elif direction == 'W':
            self.top, self.right, self.left, self.bottom = self.right, self.bottom, self.top, self.left

if __name__ == '__main__':
    nums = [int(i) for i in input().split()]
    directions = input()

    d = Dice(nums)
    for i in range(len(directions)):
        d.roll(directions[i])

    print(d.top)