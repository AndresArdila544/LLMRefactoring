def main():
    nums = list(map(int, input().split(' ')))
    directs = input()

    d = Dice(nums)

    for c in directs:
        if c == "N":
            d.toN()
        elif c == "S":
            d.toS()
        elif c == "E":
            d.toE()
        elif c == "W":
            d.toW()
    print(d.top)

class Dice:
    def __init__(self, labels):
        self.labels = labels

        self._tb = (0, 5)
        self._fb = (1, 4)
        self._lr = (3, 2)

    def toN(self):
        self._tb, self._fb = self._fb, tuple(reversed(self._tb))

    def toS(self):
        self._tb, self._fb = tuple(reversed(self._fb)), self._tb

    def toW(self):
        self._tb, self._lr = self._lr, tuple(reversed(self._tb))

    def toE(self):
        self._tb, self._lr = self._lr, self._tb

    @property
    def top(self):
        return self.labels[self._tb[0]]