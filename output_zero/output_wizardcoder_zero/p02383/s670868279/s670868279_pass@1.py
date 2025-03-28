```python
def main():
    nums = list(map(int, input().split()))
    directs = input()
    
    d = Dice(nums)
    for c in directs:
        if 'N' == c:
            d.toN()
        elif 'S' == c:
            d.toS()
        elif 'E' == c:
            d.toE()
        elif 'W' == c:
            d.toW()
    
    print(d.top)

class Dice:
    def __init__(self, labels):
        self.labels = labels
        self._tb = (0, 5) # top-bottom positions
        self._fb = (1, 4) # front-back positions
        self._lr = (3, 2) # left-right positions
    
    def toN(self):
        tb = self._tb
        self._tb = self._fb
        self._fb = tb[::-1]
        return self
    
    def toS(self):
        tb = self._tb
        self._tb = tuple(reversed(tb))
        self._fb = tuple(reversed(self._fb))
        return self
    
    def toW(self):
        tb = self._tb
        self._tb = (tb[0], tb[1] - 2) if tb[1] != 4 else (tb[0] + 2, tb[1]) # wrap around if index 4 is reached
        self._lr = tuple(reversed(self._fb))
    
    def toE(self):
        tb = self._tb
        self._tb = (tb[0] - 2, tb[1]) if tb[0] != 5 else (tb[0], tb[1] + 2) # wrap around if index 5 is reached
        self._lr = tuple(reversed(self._fb))
    
    def get_top(self):
        return self.labels[self._tb[0]]
    
    top = property(get_top)
```