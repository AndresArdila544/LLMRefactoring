Here is a refactored version of the code that has fewer lines and improved readability:
```
from itertools import combinations

class Dice:
    def __init__(self, label):
        self.label = label
    
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
    
    def _equalWithoutOverlap(self, other):
        for rs in ['', 'S', 'N', 'E', 'W', 'SS']:
            tmp = self.copy()
            for r in rs:
                tmp.rotate(r)
            top = tmp.getLabel(1) == other.getLabel(1)
            bottom = tmp.getLabel(6) == other.getLabel(6)
    
            def _side():
                result, n = False, 3
                while not result and n > 0:
                    if tmp.label[1:5] == other.label[1:5]:
                        result = True
                    else:
                        tmp.rotate('T')
                        n -= 1
                return result
    
            if top and bottom and _side():
                return True
        else:
            return False

def main():
    n = int(input())
    faces = [map(int, raw_input().split()) for _ in range(n)]
    for f1, f2 in combinations(faces, 2):
        if not (f1 == f2 or Dice(f1) == Dice(f2)):
            print('No')
            break
    else:
        print('Yes')
```