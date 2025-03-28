Here is a refactored version of the original Python program with fewer lines and improved readability:

buff = "NNNNWNNNWNNNENNNENNNWNNN"

class Dice:
    def __init__(self, nums):
        self.nums = nums

    def roll(self, direction):
        if   direction == "N":
            b = self.nums[0]
            self.nums[0], self.nums[1], self.nums[5], self.nums[4] = self.nums[1], self.nums[5], self.nums[4], b
        elif direction == "S":
            b = self.nums[0]
            self.nums[0], self.nums[4], self.nums[5], self.nums[1] = self.nums[4], self.nums[5], self.nums[2], b
        elif direction == "W":
            b = self.nums[3]
            self.nums[3], self.nums[0], self.nums[2], self.nums[5] = self.nums[0], self.nums[2], self.nums[5], b
        elif direction == "E":
            b = self.nums[3]
            self.nums[3], self.nums[5], self.nums[2], self.nums[0] = self.nums[5], self.nums[2], self.nums[0], b

def isSameDice(d1, d2):
    for direction in buff:
        d1.roll(direction)
        if d1.nums == d2.nums:
            return True
    return False

N = int(input())
dices = [Dice([int(i) for i in input().split()]) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if isSameDice(dices[i], dices[j]):
            print("No")
            exit()

print("Yes")