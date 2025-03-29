"""
class Dice:
    def __init__(self,t,f,r,l,b,u):
        self.t = t
        self.f = f
        self.r = r
        self.l = l
        self.b = b
        self.u = u

    @property
    def top(self):
        return self.a[0]
    
    @top.setter
    def top(self,value):
        self.a=[value for i in self.direction['S']]
        self.t  = self.a[0]
        self.f  = self.a[1]
        self.r  = self.a[2]
        self.l  = self.a[3]
        self.b  = self.a[4]
        self.u  = self.a[5]

    @property
    def face(self):
        return self.a[1]
    
    @face.setter
    def face(self,value):
        self.a=[self.a[i] for i in self.direction['S']]
        self.t  = self.a[0]
        self.f  = value
        self.r  = self.a[2]
        self.l  = self.a[3]
        self.b  = self.a[4]
        self.u  = self.a[5]

    @property
    def right(self):
        return self.a[2]
    
    @right.setter
    def right(self,value):
        self.a=[self.a[i] for i in self.direction['S']]
        self.t  = self.a[0]
        self.f  = self.a[1]
        self.r  = value
        self.l  = self.a[3]
        self.b  = self.a[4]
        self.u  = self.a[5]

    @property
    def left(self):
        return self.a[3]
    
    @left.setter
    def left(self,value):
        self.a=[self.a[i] for i in self.direction['S']]
        self.t  = self.a[0]
        self.f  = self.a[1]
        self.r  = self.a[2]
        self.l  = value
        self.b  = self.a[4]
        self.u  = self.a[5]

    @property
    def back(self):
        return self.a[4]
    
    @back.setter
    def back(self,value):
        self.a=[self.a[i] for i in self.direction['S']]
        self.t  = self.a[0]
        self.f  = self.a[1]
        self.r  = self.a[2]
        self.l  = self.a[3]
        self.b  = value
        self.u  = self.a[5]

    @property
    def under(self):
        return self.a[5]
    
    @under.setter
    def under(self,value):
        self.a=[self.a[i] for i in self.direction['S']]
        self.t  = self.a[0]
        self.f  = self.a[1]
        self.r  = self.a[2]
        self.l  = self.a[3]
        self.b  = self.a[4]
        self.u  = value

    def roll(self,d):
        self.a=[self.a[i] for i in self.direction[d]]
        self.t  = self.a[0]
        self.f  = self.a[1]
        self.r  = self.a[2]
        self.l  = self.a[3]
        self.b  = self.a[4]
        self.u  = self.a[5]

def roll(dice):
    return dice.top, dice.face, dice.right, dice.left, dice.back, dice.under