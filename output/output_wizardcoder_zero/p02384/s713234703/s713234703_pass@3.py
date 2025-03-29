class Dice:
    def __init__(self, lst):
        self.val = lst[0:6]
    
    def rotate(self, direction):
        if direction == "N":
            self.val = [self.val[1], self.val[4], self.val[5], self.val[3], *self.val[:2]]
        elif direction == "E":
            self.val = [self.val[3], *self.val[2:4], self.val[0], self.val[1]]
        elif direction == "S":
            self.val = [*self.val[-2:], self.val[1], self.val[0], self.val[4], self.val[5]][::-1]
        else:
            self.val = [self.val[3], self.val[0], *self.val[2:4]]
        
    def find_value(self, a, b):
        count = 0
        while True:
            self.rotate(random.choice("NESW"))
            if self.val == [a, b]:
                return self.val[2]
            count += 1
            
x = list(map(int, input().split()))
q = int(input())
dice = Dice(x)

for _ in range(q):
    a, b = map(int, input().split())
    print(dice.find_value(a, b))