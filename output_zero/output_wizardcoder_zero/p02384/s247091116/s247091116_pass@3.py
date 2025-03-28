def roll_dice(d0, d1):
    dice = Dice()
    commands = "NNNNENNNNENNNNNENNNNEENNNNWWSE"
    faces = [int(input()) for _ in range(6)]
    dice.set_number(*faces)
    
    for _ in range(int(input())):
        d0, d1 = map(int, input().split())
        
        for command in commands:
            try:
                dice.roll(command)
                if (dice.get_top() == d0 and
                    dice.number[1] == d1):
                    print(dice.get_d2(d0, d1))
                    break
            except:
                pass
            
class Dice:
    def __init__(self):
        self.faces = [i for i in range(6)]
    
    def set_number(self, d0, d1, d2, d3, d4, d5):
        self.faces[0], self.faces[1], self.faces[2], self.faces[3], self.faces[4] = d0, d1, d2, d3, d4
        
    def roll(self, command):
        if command == "E":
            self.faces = [self.faces[3], self.faces[1], self.faces[0], self.faces[4], self.faces[5]]
        elif command == "N":
            self.faces = [self.faces[1], self.faces[5], self.faces[2], self.faces[3], self.faces[0]]
        elif command == "S":
            self.faces = [self.faces[4], self.faces[0], self.faces[2], self.faces[3], self.faces[1]]
        elif command == "W":
            self.faces = [self.faces[2], self.faces[1], self.faces[5], self.faces[0], self.faces[4]]
    
    def get_top(self):
        return self.faces[0]
        
    def get_d2(self, d0, d1):
        for command in "NNNNENNNNENNNNNENNNNEENNNNWWSE":
            try:
                if (d0 == self.get_top() and
                    d1 == self.faces[1]):
                    return self.faces[2]
            except:
                pass
        raise

def main():
    faces = list(map(int, input().split()))
    
    for _ in range(int(input()):
        d0, d1 = map(int, input().split())
        
        try:
            print(roll_dice(d0, d1))
        except:
            pass
            
if __name__ == "__main__":
    main()