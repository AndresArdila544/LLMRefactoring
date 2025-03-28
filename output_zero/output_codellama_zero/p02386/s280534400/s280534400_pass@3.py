Here's the refactored version of the code:
```python
buff = "NNNNWNNNWNNNENNNENNNWNNN"
class Dice:
    num = [-1 for _ in range(6)]
    def roll(self, d):
        if d == "N":
            b = self.num[0]
            self.num[0] = self.num[1]
            self.num[1] = self.num[5]
            self.num[5] = self.num[4]
            self.num[4] = b
        elif d == "S":
            b = self.num[0]
            self.num[0] = self.num[4]
            self.num[4] = self.num[5]
            self.num[5] = self.num[1]
            self.num[1] = b
        elif d == "W":
            b = self.num[3]
            self.num[3] = self.num[0]
            self.num[0] = self.num[2]
            self.num[2] = self.num[5]
            self.num[5] = b
        elif d == "E":
            b = self.num[3]
            self.num[3] = self.num[5]
            self.num[5] = self.num[2]
            self.num[2] = self.num[0]
            self.num[0] = b
    def __init__(self, lst):
        self.num = lst
    def print_num(self, m):
        return self.num[m]
    def return_lst(self):
        return self.num

def isSameDice(d1, d2):
    for d in buff:
        d1.roll(d)
        if d1.return_lst() == d2.return_lst():
            return True
    return False

N = int(input())
dices = []
for _ in range(N):
    lst = [int(i) for i in input().split()]
    dices.append(Dice(lst))
for i in range(N):
    for j in range(i + 1, N):
        if isSameDice(dices[i], dices[j]):
            print("No")
            exit()
print("Yes")
```