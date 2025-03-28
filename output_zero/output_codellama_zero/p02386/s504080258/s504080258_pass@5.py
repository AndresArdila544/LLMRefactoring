class Dice:
    def __init__(self):
        self.faces=[]

    def rotate(self, direction):
        tmp = self.faces.copy()
        
        if direction == "N":
            self.faces[5-1], self.faces[1-1] =  self.faces[1-1], self.faces[2-1]
            self.faces[2-1], self.faces[6-1] =  self.faces[6-1], self.faces[5-1]
        if direction == "S":
            self.faces[5-1], self.faces[1-1] =  self.faces[1-1], self.faces[2-1]
            self.faces[2-1], self.faces[6-1] =  self.faces[6-1], self.faces[5-1]
        if direction == "W":
            self.faces[4-1], self.faces[1-1] =  self.faces[1-1], self.faces[3-1]
            self.faces[3-1], self.faces[6-1] =  self.faces[6-1], self.faces[4-1]
        if direction == "E":
            self.faces[3-1], self.faces[1-1] =  self.faces[1-1], self.faces[4-1]
            self.faces[4-1], self.faces[6-1] =  self.faces[6-1], self.faces[3-1]
        return 0
    
    def spin(self):
        self.faces[4-1], self.faces[2-1],self.faces[5-1],self.faces[3-1] =\
        self.faces[2-1], self.faces[3-1],self.faces[4-1],self.faces[5-1]
    
        return 0

dices = []
lines = int(input())
for i in range(lines):
    dices.append(Dice())
    dices[i].faces=[int(x) for x in input().split(" ")]

def check_equal(d1, d2):
    return d1.faces == d2.faces
    
for i, d1 in enumerate(dices):
    for d2 in dices[i+1 :]:
        if check_equal(d1, d2):
            print("No")
            exit()
        else:
            for _ in range(3):
                for _ in range(4):
                    for ___ in range(4):
                        d2.spin()
                    d2.rotate("W")
                d2.rotate("N")

print("Yes")