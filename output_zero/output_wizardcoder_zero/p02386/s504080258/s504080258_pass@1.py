class Dice:
    def __init__(self):
        self.faces = []
        
    def rotate(self, direction):
        tmp = self.faces.copy()
        if direction == "N":
            self.faces[5-1] = tmp[1-1]
            self.faces[1-1] = tmp[2-1]
            self.faces[2-1] = tmp[6-1]
            self.faces[6-1] = tmp[5-1]
        elif direction == "S":
            self.faces[5-1] = tmp[6-1]
            self.faces[1-1] = tmp[5-1]
            self.faces[2-1] = tmp[1-1]
            self.faces[6-1] = tmp[2-1]
        elif direction == "W":
            self.faces[4-1] = tmp[1-1]
            self.faces[1-1] = tmp[3-1]
            self.faces[3-1] = tmp[6-1]
            self.faces[6-1] = tmp[4-1]
        elif direction == "E":
            self.faces[3-1] = tmp[1-1]
            self.faces[1-1] = tmp[4-1]
            self.faces[4-1] = tmp[6-1]
            self.faces[6-1] = tmp[3-1]
        return 0
    
    def spin(self):
        self.faces[4-1], self.faces[2-1], self.faces[5-1], self.faces[3-1] =\
        self.faces[2-1], self.faces[3-1], self.faces[4-1], self.faces[5-1]
        
        return 0

lines = int(input())
dices = []
for _ in range(lines):
    dices.append(Dice())
    dices[-1].faces = [int(x) for x in input().split()]
    
for i, d1 in enumerate(dices[:-1]):
    for j, d2 in enumerate(dices[i+1:], start=i+1):
        while True:
            if not any([d1.faces == d2.faces for _ in range(3)] or\
                     all([d1.rotate("W"), d1.spin(), d1.rotate("N")]) < 0 and\
                     all([d2.rotate("W"), d2.spin(), d2.rotate("N")]):
                break
        else:
            print("Yes")
            exit()
print("No")