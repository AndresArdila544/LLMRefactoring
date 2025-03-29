```python
class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.n_list = [a, b, c, d, e, f]
    
    def is_right_surface(self, top, front):
        swapped = False
        
        if self.n_list.index(top) > self.n_list.index(front):
            top, front = front, top
            swapped = True
            
        return {1: (c, d, swapped), 2: (e, b, swapped), 3: (b, e, swapped), 4: (d, c, swapped), 5: (a, f, swapped), 6: (f, a, swapped)
               }.get((self.n_list.index(top), self.n_list.index(front)), None)
    
    def move(self, moves):
        for m in moves:
            if m == "N":
                tmp1 = self.a
                self.a, self.e = self.e, tmp1
                continue
            elif m == "E":
                tmp1 = self.a
                self.a, self.c, self.f = self.c, self.d, tmp1
            elif m == "W":
                tmp1 = self.a
                self.a, self.d, self.f = self.d, self.c, tmp1
            else:
                tmp1 = self.a
                self.a, self.b, self.e = self.e, self.f, tmp1
        
n, a, b, c, d, e = map(int, input().split())
dice = Dice(a, b, c, d, e)

for _ in range(int(input())):
    x, y = map(int, input().split())
    right_surface = dice.is_right_surface(x, y)
    
    if right_surface is not None:
        print("Yes" if right_surface[2] else "No")
```