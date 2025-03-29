Here is a more concise and readable implementation of the same functionality:
```python
class Dice:
    def __init__(self):
        self.numbers = []
        self.work = []
        self.order = 'NNNNWNNNWNNNENNNENNNWNNN'

    def setNumber(self, n0, n1, n2, n3, n4, n5):
        self.numbers = [n0, n1, n2, n3, n4, n5]

    def roll(self, loc):
        if loc == 'E':
            self.work = [self.numbers[3], self.numbers[1], self.numbers[0], self.numbers[5], self.numbers[4], self.numbers[2]]
        elif loc == 'N':
            self.work = [self.numbers[1], self.numbers[5], self.numbers[2], self.numbers[3], self.numbers[0], self.numbers[4]]
        elif loc == 'S':
            self.work = [self.numbers[4], self.numbers[0], self.numbers[2], self.numbers[3], self.numbers[5], self.numbers[1]]
        elif loc == 'W':
            self.work = [self.numbers[2], self.numbers[1], self.numbers[5], self.numbers[0], self.numbers[4], self.numbers[3]]

    def equals(self, another):
        for i in range(6):
            if self.work[i] != another.work[i]:
                return False
        return True

diceA = Dice()
diceB = Dice()

table1 = list(map(int, input().split()))
diceA.setNumber(*table1)

table2 = list(map(int, input().split()))
diceB.setNumber(*table2)

if diceA.equals(diceB):
    print("Yes")
else:
    print("No")
```