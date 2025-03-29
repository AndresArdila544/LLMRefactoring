class Dice:
    def __init__(self, nums):
        self._tb = (0, 5) # top board
        self._fb = (1, 4) # front board
        self._lr = (3, 2) # left/right board
        
    def toN(self):
        self._tb, self._fb = self._fb, self._tb
        return self
    
    def toS(self):
        self._tb, self._fb = tuple(reversed(self._tb)), tuple(reversed(self._fb))
        return self
    
    def toW(self):
        self._tb, self._lr = self._tb, self._lr[::-1]
        return self
    
    def toE(self):
        self._tb, self._lr = self._lr, self._tb
        return self
        
    @property
    def top(self):
        return self.labels[self._tb[0]]
        
    def main():
        nums = list(map(int, input().split()))
        directs = input()
        d = Dice(nums)
        for c in directs:
            if 'N' == c:
                d.toN()
            if 'S' == c:
                d.toS()
            if 'E' == c:
                d.toE()
            if 'W' == c:
                d.toW()
        print(d.top)
                
if __name__ == '__main__':
    main()