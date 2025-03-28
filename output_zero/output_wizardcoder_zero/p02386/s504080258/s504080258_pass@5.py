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
        else:
            pass
        return 0
    
    def spin(self):
        self.faces[4-1], self.faces[2-1],self.faces[5-1],self.faces[3-1] = self.faces[2-1], self.faces[3-1],self.faces[4-1],self.faces[5-1]
        return 0
    
dices = []
lines = int(input())
for i in range(lines):
    dices.append(Dice())
    dices[i].faces=[int(x) for x in input().split(" ")]

for i, d1 in enumerate(dices):
    for d2 in dices[i+1:]:
        if all(map(lambda face: d1.faces != d2.faces, [Dice()]*3)):  # Checks if there are any identical faces in the array by comparing each dice with a default instance of Dice.
            print("Yes")
            exit()
    
print("No")