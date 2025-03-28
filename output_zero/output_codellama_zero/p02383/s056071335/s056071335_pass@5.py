import sys

class Dice:
    def __init__(self, nums):
        self.nums = nums

    def roll(self, direction):
        if direction == 'E':
            self.nums = (self.nums[2], self.nums[3], self.nums[0], self.nums[1])
        elif direction == 'N':
            self.nums = (self.nums[4], self.nums[5], self.nums[0], self.nums[1])
        elif direction == 'S':
            self.nums = (self.nums[6], self.nums[7], self.nums[0], self.nums[1])
        elif direction == 'W':
            self.nums = (self.nums[2], self.nums[3], self.nums[4], self.nums[5])

d = Dice([int(i) for i in input().split()])
for _ in range(len(sys.stdin.readline())):
    d.roll(sys.stdin.readline())
print(d.get_top())