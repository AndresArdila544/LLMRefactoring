```python
def main():
    nums = list(map(int, input().split()))
    directions = input()
    dices = [Dice(num) for num in nums]
    for c in directions:
        if 'N' == c:
            for dice in dices:
                dice.toN()
        elif 'S' == c:
            for dice in dices:
                dice.toS()
        elif 'E' == c:
            for dice in dices:
                dice.toE()
        else:  # W == c
            for dice in dices:
                dice.toW()
    print([dice.top for dice in dices])

class Dice:
    def __init__(self, label):
        self._tb = (0, 5)
        self._fb = (1, 4)
        self._lr = (3, 2)
        self.labels = [label]

    def toN(self):
        self._tb, self._fb = self._fb, self._tb
        return self

    def toS(self):
        self._tb, self._fb = tuple(reversed(self._fb)), self._tb
        return self

    def toW(self):
        self._tb, self._lr = self._tb, self._lr[::-1]
        return self

    @property
    def top(self):
        return self.labels[0]
```