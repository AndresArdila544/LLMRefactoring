```python
class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        
    def is_right_surface(self, top, front):
        if {self.a, self.b, self.c, self.d, self.e, self.f}.issubset({1,2,3,4,5,6}):
            if {top,front}.issubset({1,2,3,4,5,6}):
                if top == 1 and front in (2,3):
                    return self.c,self.d, True if front==2 else False
                elif top == 1 and front in (4,5):
                    return self.e,self.b, True if front==4 else False
                elif top == 1 and front in (6,):
                    return self.b,self.e, True if front==4 else False
                elif top in (2,3) and front in (5,6):
                    return self.a,self.f, True if top==2 else False
                elif top == 2 and front in (4,):
                    return self.f,self.a, True if top==4 else False
                elif top in (3,6) and front in (6,):
                    return self.c,self.d, True if top==3 else False
                elif top == 4 and front in (5,6):
                    return self.f,self.a, True if top==4 else False
        else:
            raise ValueError("Invalid input")

    def move(self,move_str):
        for i in move_str:
            if i == "N":
                self.move_N()
            elif i == "E":
                self.move_E()
            elif i == "W":
                self.move_W()
            elif i == "S":
                self.move_S()
    
    def move_N(self):
        tmp1,tmp2 = self.a,self.e
        self.a = self.b
        self.b = self.f
        self.e = tmp1
        self.f = tmp2

    def move_E(self):
        tmp1,tmp2 = self.a,self.d
        self.a = self.d
        self.d = self.f
        self.f = tmp1
        
    def move_W(self):
        tmp1,tmp2 = self.a,self.d
        self.a = self.c
        self.c = self.f
        self.f = tmp1

    def move_S(self):
        tmp1,tmp2 = self.a,self.b
        self.a = self.e
        self.e = self.f
        self.f = tmp1

n,_, a, b, c, d, e, f = map(int,input().split())
dice = Dice(a,b,c,d,e)
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    right, left, is_swap = dice.is_right_surface(x, y)
    print(left if not is_swap else right)
```