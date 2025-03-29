class Dice:
    def __init__(self, N):
        self.label = N
        self.top = 1
        self.north = 5
        self.East = [
            [0, 3, 5, 2, 4, 0],
            [4, 0, 1, 6, 0, 3],
            [2, 6, 0, 0, 1, 5],
            [5, 1, 0, 0, 6, 2],
            [3, 0, 6, 1, 0, 4],
        ]

    def move(self, ori):
        if ori == 'S':
            self.top = self.north
            self.north = 7 - self.top
        elif ori == 'N':
            self.top = 7 - self.north
            self.north = self.top
        elif ori == 'E':
            self.top = 7 - self.East[self.north - 1][self.top - 1]
        elif ori == 'W':
            self.top = self.East[self.north - 1][self.top - 1]

    def get_top(self):
        return self.label[self.top - 1]

N = list(map(int, input().split()))
q = int(input())
D = Dice(N)
for _ in range(q):
    t, s = map(int, input().split())
    t = N.index(t)
    s = N.index(s)
    n = 5 - s
    e = D.East[n][t]
    print(N[e-1])