class Dice(object):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.sides = [s1, s2, s3, s4, s5, s6]
    
    def east(self):
        self.sides.insert(0, self.sides.pop())
    
    def west(self):
        self.sides.append(self.sides.pop(0))
    
    def north(self):
        self.sides[0], self.sides[1] = self.sides[1], self.sides[0]
    
    def south(self):
        self.sides[1], self.sides[2] = self.sides[2], self.sides[1]
    
    def rotate(self):
        self.sides.append(self.sides.pop(0))
    
    def top(self):
        return self.sides[0]
    
    def front(self):
        return self.sides[1]
    
    def right(self):
        return self.sides[2]
    
    def isSameDice(self, anotherDice):
        if self.sides == anotherDice.sides:
            return True
        return False