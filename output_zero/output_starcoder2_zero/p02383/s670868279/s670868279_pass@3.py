Here is what I came up with:



class Dice:
    def __init__(self, nums):
        self._labels = tuple(nums)
        self._top = 0

        # Top-bottom (TB), front-back (FB), and left-right (LR)
        # are the first two numbers of the label list and the last two.
        self._tb = tuple(self._labels[:2])
        self._fb = tuple(reversed(self._labels[1:3]))
        self._lr = tuple(reversed(self._labels[2:4]))

    def toN(self):
        # The top-bottom numbers are swapped and the front-back ones are reversed.
        self._tb, self._fb = self._fb, tuple(reversed(self._tb))
        return self

    def toS(self):
        # The top-bottom numbers are swapped and the front-back ones are reversed.
        self._tb, self._fb = tuple(reversed(self._fb)), self._tb
        return self

    def toW(self):
        # The top-bottom numbers are swapped and the left-right ones are reversed.
        self._tb, self._lr = tuple(reversed(self._lr)), self._tb
        return self

    def toE(self):
        # The top-bottom numbers are swapped and the left-right ones are reversed.
        self._tb, self._lr = self._lr, tuple(reversed(self._tb))
        return self

    @property
    def _top(self):
        # The top face is the first number of the top-bottom pair.
        return self._tb[0]

    @top.setter
    def _top(self, value):
        # The top face is the first number of the top-bottom pair.
        self._tb = (value,) + self._tb[1:]


def main():
    nums = list(map(int, input().split(' ')))

    d = Dice(nums)

    for c in input():
        if 'N' == c:
            d.toN()

        elif 'S' == c:
            d.toS()

        elif 'E' == c:
            d.toE()

        elif 'W' == c:
            d.toW()

    print(d._top)


if __name__  == '__main__':
    main()