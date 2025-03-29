class Dice():
    def __init__(self, N):
        self.label = N
        self.top = 1
        self.north = 5
    
    def move(self, ori):
        t = self.top
        if ori == 'S':
            self.top = self.north
            self.north = 7 - t
        elif ori == 'N':
            self.top = 7 - self.north
            self.north = t
        elif ori == 'E':
            east = self.East[self.north-1][self.top-1]
            self.top = 7 - east
        elif ori == 'W':
            east = self.East[self.north-1][self.top-1]
            self.top = east
    
    def get_top(self):
        return self.label[self.top-1]
            
label = list(map(int, input().split()))
D = Dice(label)
q = int(input())
for _ in range(q):
    t, s = map(int, input().split())
    t = label.index(t)
    s = label.index(s)
    n = 5 - s
    e = D.East[n][t]
    print(label[e-1])