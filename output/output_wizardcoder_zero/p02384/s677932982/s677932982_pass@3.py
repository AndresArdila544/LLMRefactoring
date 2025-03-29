class Dice():
    def __init__(self, N):
        self.label = N
        self.top = 1
        self.north = 5
        
    def move(self, ori):
        if ori == 'S':
            self.top, self.north = self.north, self.top
        elif ori == 'N':
            self.top, self.north = self.north, 7 - self.top
        elif ori == 'E':
            self.top = self.East[self.north-1][self.label.index(self.top)]
        elif ori == 'W':
            self.top = self.East[self.label.index(7 - self.top)][self.north-1]
            
    def get_top(self):
        return self.label[self.top-1]
        
label = list(map(int, input().split()))
D = Dice(label)
q = int(input())
for _ in range(q):
    t, s = map(int, input().split())
    t_index = label.index(t)
    s_index = label.index(s)
    n = 5 - s_index
    D.move('N') if t < s else D.move('S')
    print(label[D.East[n][t_index-1])