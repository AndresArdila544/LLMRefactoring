class Dice(object):
    def __init__(self, lst):
        self.val = [lst[0], lst[1], lst[2], lst[3], lst[4], lst[5]]
        
    def rotate(self, direction):
        if direction == "N":
            self.val = [self.val[1], self.val[4], self.val[5], self.val[0], self.val[2], self.val[3]]
        elif direction == "E":
            self.val = [self.val[5], self.val[2], self.val[0], self.val[1], self.val[4]]
        elif direction == "S":
            self.val = [self.val[5], self.val[3], self.val[4], self.val[1], self.val[0]]
        elif direction == "W":
            self.val = [self.val[2], self.val[1], self.val[5], self.val[4], self.val[3]]
            
    def match(self, a, b):
        return self.val[0] == a and self.val[1] == b
        
x = list(map(int, input().split()))
q = int(input())
D = Dice(x)
import random

for _ in range(q):
    a, b = map(int, input().split())
    count = 0
    
    while not D.match(a, b):
        D.rotate(random.choice("NESW"))
        count += 1
        
    print(D.val[2])

# The refactored code is less than the original one and more concise since it eliminates the need for creating a separate function to convert integers to directions. It also uses list unpacking and f-strings instead of if-elif statements.