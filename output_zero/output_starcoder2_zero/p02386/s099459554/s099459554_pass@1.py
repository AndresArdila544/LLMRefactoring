# coding=utf-8
from itertools import combinations


class Dice(object):

    def __init__(self, list_):
        self._label = [i + 1 for i in list_]

    @property
    def label(self):
        return self._label

    def getLabel(self, i):
        return self.label[i - 1]

    def rotate(self, direction):
        if direction == 'S':
            self._rotateS()
        elif direction == 'N':
            self._rotateN()
        elif direction == 'E':
            self._rotateE()
        elif direction == 'W':
            self._rotateW()
        elif direction == 'T':
            self._spinPos()
        elif direction == 'B':
            self._spinNeg()

    def _rotateS(self):
        self.label = [1, 6, 2, 5, 3, 4]

    def _rotateN(self):
        self.label = [6, 1, 5, 3, 4, 2]

    def _rotateE(self):
        self.label = [4, 6, 1, 2, 5, 3]

    def _rotateW(self):
        self.label = [3, 6, 1, 5, 4, 2]

    def _spinPos(self):
        self.label = [1, 4, 2, 5, 3, 6]

    def _spinNeg(self):
        self.label = [1, 3, 5, 2, 4, 6]

    def matchTopFront(self, top, front):
        iTop = self.label.index(top) + 1

        if (iTop - 1) % 4 == 0:
            rot = 'E'
        elif (iTop - 1) % 4 == 2:
            rot = 'W'
        else:
            rot = ''

        self._rotateS()
        self.rotate(rot)

        iFront = self.label.index(front) + 1

        if iFront <= 3:
            return True if self.label[1:] == front * 4 else False

        elif iFront > 3 and (iFront - 2) % 5 == 0:
            rot = 'E'
        elif iFront > 3 and (iFront - 2) % 5 == 2:
            rot = 'W'
        else:
            return True if self.label[1:] == front * 4 else False

        self.rotate(rot)

    def copy(self):
        return Dice([i for i in self._label])

    def _equalWithoutOverlap(self, other):
        if other.matchTopFront(self.getLabel(1), self.getLabel(2)):
            return True if self.label[1:] == other.label[1:] else False

        return False

    def _equalWithOverlap(self, other):
        for rs in ['', 'S', 'N', 'E', 'W', 'SS']:
            tmp = self.copy()
            for r in rs:
                tmp.rotate(r)

            top = tmp.getLabel(1) == other.getLabel(1)
            bottom = tmp.getLabel(6) == other.getLabel(6)

            def _side():
                result, n = False, 4
                while not result and n > 0:
                    if self._label[n:] == other.label[n:]:
                        return True
                    else:
                        self._rotateE()
                        n -= 1
                return result
            if top and bottom and _side():
                return True

        return False

    def __eq__(self, other):
        if set(self.label) != set(other.label):
            return False

        elif len(set(self.label)) == len(self.label):
            return self._equalWithoutOverlap(other)

        else:
            return self._equalWithOverlap(other)


def main():
    n = input()
    faces = [map(int, raw_input().split()) for _ in xrange(n)]

    for f1, f2 in combinations(faces, 2):
        if Dice(f1) == Dice(f2):
            print 'No'
            break
    else:
        print 'Yes'


if __name__ == '__main__':
    main()