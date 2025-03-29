```python
from itertools import combinations

class Dice:
    def __init__(self, list_):
        self.label = list_
        
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
        self.label = [self.getLabel(i) for i in [1, 3, 5, 2, 4, 6]][::-1]
        
    def rotate(self, rotates: str):
        if rotates == 'S':
            self.rotateS()
        elif rotates == 'N':
            self.rotateN()
        elif rotates == 'E':
            self.rotateE()
        elif rotates == 'W':
            self.rotateW()
    
    def matchTopFront(self, top, front):
        iTop = self.label.index(top) + 1
        topRot = {1: '', 2: 'N', 3: 'W', 4: 'E', 5: 'SS'}
        self.rotate(topRot[iTop])
        
        iFront = self.label.index(front) + 1
        frontRot = {2: '', 3: 'B', 4: 'T', 5: 'TT'}
        try:
            self.rotate(frontRot[iFront])
            return True
        except KeyError:
            return False
    
    def copy(self):
        return Dice(self.label[:])
    
    def equalWithoutOverlap(self, other) -> bool:
        if self.matchTopFront(*other.getLabel(0)):
            return all(a == b for a, b in zip(self.label, other.label))
        else:
            return False
    
    def equalWithOverlap(self, other) -> bool:
        self_set = set(self.label)
        other_set = set(other.label)
        if len(self_set) != len(other_set):
            return False
        
        for rs in [(), 'S', 'N', 'E', 'W']:
            tmp = self.copy()
            for r in rs:
                tmp.rotate(r)
            if all(a == b for a, b in zip(tmp.label[1:5], other.label[1:5])):
                return True
        else:
            return False
    
    def __eq__(self, other):
        if len(set(self.label) != len(other.label):
            return self.equalWithoutOverlap(other)
        elif len(self.label) == len(set(self.label):
            return self.equalWithOverlap(other)
        else:
            raise NotImplementedError("Unsure how to compare dice with overlapping faces")

def main():
    n = int(input())
    faces = [map(int, input().split()) for _ in range(n)]
    pairs = combinations(faces, 2)
    print('Yes' if any(dice_a == dice_b or Dice(*dice_a) == Dice(*dice_b) for dice_a, dice_b in pairs) else 'No')

if __name__ == '__main__':
    main()
```