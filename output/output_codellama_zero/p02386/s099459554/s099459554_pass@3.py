Here is a refactored version of the code with fewer lines and improved readability:
```
# coding=utf-8
from itertools import combinations

class Dice:
    def __init__(self, label):
        self.label = label

    @property
    def getLabel(self, i):
        return self.label[i - 1]

    def rotateS(self):
        self.label = [self.getLabel(i) for i in [5, 1, 3, 4, 6, 2]]

    def rotateN(self):
        self.label = [self.getLabel(i) for i in [2, 6, 3, 4, 1, 5]]

    def rotateE(self):
        self.label = [self.getLabel(i) for i in [4, 2, 1, 6, 5, 3]]

    def rotateW(self):
        self.label = [self.getLabel(i) for i in [3, 2, 6, 1, 5, 4]]

    def spinPos(self):
        self.label = [self.getLabel(i) for i in [1, 4, 2, 5, 3, 6]]

    def spinNeg(self):
        self.label = [self.getLabel(i) for i in [1, 3, 5, 2, 4, 6]]

    def rotate(self, rotates):
        for r in rotates:
            if r == 'S':
                self._rotateS()
            elif r == 'N':
                self._rotateN()
            elif r == 'E':
                self._rotateE()
            elif r == 'W':
                self._rotateW()
            elif r == 'T':
                self._spinPos()
            elif r == 'B':
                self._spinNeg()

    def matchTopFront(self, top, front):
        iTop = self.label.index(top) + 1
        topRot = {1: '', 2: 'N', 3: 'W', 4: 'E', 5: 'S', 6: 'SS'}
        self.rotate(topRot[iTop])

        iFront = self.label.index(front) + 1
        frontRot = {2: '', 3: 'B', 4: 'T', 5: 'TT'}
        try:
            self.rotate(frontRot[iFront])
            return True
        except KeyError:
            return False

    def __eq__(self, other):
        if set(self.label) != set(other.label):
            return False
        elif len(self.label) == len(set(self.label)):
            return self._equalWithoutOverlap(other)
        else:
            return self._equalWithOverlap(other)

def main():
    n = int(input())
    faces = [map(int, raw_input().split()) for _ in range(n)]
    for f1, f2 in combinations(faces, 2):
        if not (f1 == f2 or Dice(f1) == Dice(f2)):
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    main()
```