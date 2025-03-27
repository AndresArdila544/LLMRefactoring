def main():
    labels = list(map(int, input().split(' ')))
    directs = input()
    
    d = Dice(labels)
    
    for c in directs:
        if c == 'N': d.to_n()
        elif c == 'S': d.to_s()
        elif c == 'E': d.to_e()
        elif c == 'W': d.to_w()
    
    print(d.top)

class Dice:
    def __init__(self, labels):
        self.labels = labels
        
        self._tb = (0, 5)
        self._fb = (1, 4)
        self._lr = (3, 2)
    
    @property
    def top(self):
        return self.labels[self._tb[0]]
    
    def to_n(self):
        tb = self._tb
        self._tb = self._fb
        self._fb = tuple(reversed(tb))
    
    def to_s(self):
        tb = self._tb
        self._tb = tuple(reversed(self._fb))
        self._fb = tb
    
    def to_w(self):
        tb = self._tb
        self._tb = tuple(reversed(self._lr))
        self._lr = tb
    
    def to_e(self):
        tb = self._tb
        self._tb = self._lr
        self._lr = tuple(reversed(tb))