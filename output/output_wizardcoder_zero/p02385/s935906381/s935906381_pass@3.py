class Dice:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.sides = [s1, s2, s3, s4, s5, s6]
    
    def move(self, direction, num_rotations=0):
        prev_s6 = self.sides[5]
        if direction == "east":
            self.sides[5], self.sides[3], self.sides[1], self.sides[4] = self.sides[1], self.sides[2], prev_s6, self.sides[0]
        elif direction == "west":
            self.sides[5], self.sides[3], self.sides[1], self.sides[4] = self.sides[1], self.sides[2], prev_s6, self.sides[0]
        elif direction == "north":
            self.sides[5], self.sides[3], self.sides[1], self.sides[4] = self.sides[1], self.sides[3], prev_s6, self.sides[2]
        elif direction == "south":
            self.sides[5], self.sides[3], self.sides[1], self.sides[4] = self.sides[1], self.sides[4], prev_s6, self.sides[2]
        elif direction == "rotate":
            for _ in range(num_rotations):
                prev_s2 = self.sides[2]
                self.sides[2], self.sides[4], self.sides[3], self.sides[5] = self.sides[4], self.sides[3], self.sides[1], prev_s2
        else:
            raise ValueError("Invalid direction")
            
    def isSameDice(self, anotherDice):
        return all(a == b for a, b in zip(self.sides, anotherDice.sides))
        
# Sample usage:
d1 = Dice(*map(int, input().split()))
d2 = Dice(*map(int, input().split())
for j in range(6):
    d2.move("west" if j % 2 == 0 else "north", 3) # Move the second dice for 3 rotations and then check if it's the same as the first dice
    for k in range(4):
        d2.move("rotate")
        if d1.isSameDice(d2):
            print("Yes")
            break
    else: # If no break is encountered, means dice are not same
        print("No")