from itertools import combinations

class Dice:
    def __init__(self, label):
        self._label = label
    
    def getLabel(self, i):
        return self._label[i - 1]
    
    def rotateS(self):
        self._label = [self.getLabel(i) for i in [5, 1, 3, 4, 6, 2]]
        
    def rotateN(self):
        self._label = [self.getLabel(i) for i in [2, 6, 3, 4, 1, 5] ]
    
    def rotateE(self):
        self._label = [self.getLabel(i) for i in [4, 2, 1, 5, 3] ]
        
    def rotateW(self):
        self._label = [self.getLabel(i) for i in [3, 2, 6, 1, 5] ]
    
    def spinPos(self):
        self._label = [self.getLabel(i) for i in [1, 4, 2, 5, 3] ]
        
    def spinNeg(self):
        self._label = [self.getLabel(i) for i in [1, 3, 5, 2, 6] ]
    
    def rotate(self, rotates):
        if rotates == 'S':
            self.rotateS()
        elif rotates == 'N':
            self.rotateN()
        elif rotates == 'E':
            self.rotateE()
        elif rotates == 'W':
            self.rotateW()
    
    def matchTopFront(self, top, front):
        iTop = self._label.index(top) + 1
        topRot = {1: '', 2: 'N', 3: 'W', 4: 'E', 5: 'SS'}
        self.rotate(topRot[iTop])
        
        iFront = self._label.index(front) + 1
        frontRot = {2: '', 3: 'B', 4: 'T', 5: 'TT'}
        
        try:
            self.rotate(frontRot[iFront])
            return True
        except KeyError:
            return False
        
    def copy(self):
        return Dice(self._label[:] )
    
    def equalWithoutOverlap(self, other):
        if other.matchTopFront(self.getLabel(1), self.getLabel(2)):
            return True if self._label == other._label else False
        else:
            return False
        
    def equalWithOverlap(self, other):
        for rs in ['', 'S', 'N', 'E', 'W', 'SS']:
            tmp = self.copy()
            for r in rs:
                tmp.rotate(r)
                
            top = tmp.getLabel(1) == other._label[1]
            bottom = tmp.getLabel(6) == other._label[6]
            
            def side():
                result, n = False, 3
                while not result and n > 0:
                    if tmp._label[1:5] == other._label[1:5]:
                        result = True
                    else:
                        tmp.rotate('T')
                        n -= 1
                return result
            
            if top and bottom and side():
                return True
        
        return False
    
def main():
    n = int(input())
    faces = [map(int, input().split()) for _ in range(n)]
    for f1, f2 in combinations(faces, 2):
        if f1 == f2 or Dice(f1).equalWithOverlap(Dice(f2):
            print('No')
            break
    else:
        print('Yes')
        
if __name__ == '__main__':
    main()