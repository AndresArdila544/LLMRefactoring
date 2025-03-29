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
        if direction == "S":
            self.faces[5-1] = tmp[6-1]
            self.faces[1-1] = tmp[5-1]
            self.faces[2-1] = tmp[1-1]
            self.faces[6-1] = tmp[2-1]
        if direction == "W":
            self.faces[4-1] = tmp[1-1]
            self.faces[1-1] = tmp[3-1]
            self.faces[3-1] = tmp[6-1]
            self.faces[6-1] = tmp[4-1]
        if direction == "E":
            self.faces[3-1] = tmp[1-1]
            self.faces[1-1] = tmp[4-1]
            self.faces[4-1] = tmp[6-1]
            self.faces[6-1] = tmp[3-1]
        return 0
    
    def spin(self):
        self.faces[4-1], self.faces[2-1], self.faces[5-1], self.faces[3-1] =\
            self.faces[2-1], self.faces[3-1], self.faces[4-1], self.faces[5-1]
        return 0
    
def main():
    lines = int(input())
    dices = []
    for _ in range(lines):
        faces_of_dice = [int(x) for x in input().split()]
        dice = Dice()
        dice.faces = faces_of_dice
        dices.append(dice)
    
    for i, d1 in enumerate(dices):
        for j, d2 in enumerate(dices[i+1:], start=i+1):
            for _ in range(3):
                for _ in range(4):
                    if d1.faces != d2.faces and not any([d1.rotate("W"), d1.spin(), d1.rotate("N") or d1.rotate("E")]):
                        print("No")
                        return
                d2.rotate("W")
            d2.rotate("N")
    
    print("Yes")