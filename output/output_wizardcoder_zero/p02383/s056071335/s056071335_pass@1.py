class Dice:
    def __init__(self, nums):
        self.top, self.front, self.right, self.left, self.back = nums

    
    def roll(self, direction):
        if direction == 'E':
            self.top, self.right, self.left, self.bottom = self.left, self.top, self.bottom, self.right
        elif direction == 'N':
            self.top, self.front, self.back, self.bottom = self.bottom, self.top, self.front, self.back
        elif direction == 'S':
            self.top, self.front, self.back, self.bottom = self.back, self.top, self.front, self.bottom
        elif direction == 'W':
            self.top, self.right, self.left, self.bottom = self.right, self.bottom, self.top, self.left
    
    def get_top(self):
        return self.top

nums = [int(i) for i in input().split()]
d = Dice(nums)
directions = input()
for direction in directions:
    d.roll(direction)
print(d.get_top())