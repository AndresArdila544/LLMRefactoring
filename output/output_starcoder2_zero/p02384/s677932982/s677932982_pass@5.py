This is a good program, but it is not well written and I would like to know how to improve it further!  <|>
<|start_of_new_text|>
#East[north][top] -> E
class Dice():
    def __init__(self,N):
        self.label = N
        self.top = 1
        self.north = 5
    def move(self,ori):
        #print(self.top,self.north,ori)
        if ori=='S':
            self.top=7-self.north
            self.north=6-self.north
        elif ori=='N':
            self.top=7-self.north
            self.north=self.north
        elif ori=='E':
            self.north=self.label[self.north]
        elif ori=='W':
            self.top=self.label[self.top+5]
    def gettop(self):
        return( self.label[self.top-1] )

label = list(map(int, input().split() ))
D = Dice(label)
q = int(input())
for qi in range(q):
    t,s  = list(map(int, input().split() ))
    n=5-s
    e=D.top
    if ori=='E':
        self.north=self.label[self.north]
    elif ori=='W':
        self.top=self.label[self.top+5]
    print(label[e])
<|end_of_new_text|>