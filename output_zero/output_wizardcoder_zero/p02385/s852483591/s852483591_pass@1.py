class Dice:
    def __init__(self, top, front, right, left, bottom):
        self.TOP = top
        self.BOTTOM = bottom
        self.FRONT = front
        self.BACK = back
        self.LEFT = left
        self.RIGHT = right
        
    def move(self, direction):
        if direction == "N":
            self.TOP, self.BOTTOM = self.FRONT, self.BACK
        elif direction == "S":
            self.TOP, self.BOTTOM = self.BACK, self.FRONT
        elif direction == "W":
            self.TOP, self.LEFT, self.RIGHT = self.RIGHT, self.BOTTOM, self.LEFT
        elif direction == "E":
            self.TOP, self.LEFT, self.RIGHT = self.LEFT, self.BOTTOM, self.RIGHT
        else:
            raise Exception
    
top, front, right, left, bottom = map(int,input().split())
dice = Dice(top, front, right, left, bottom)
top2, front2, right2, left2, bottom2 = map(int,input().split())
dice2 = Dice(top2, front2, right2, left2, bottom2)

if dice.TOP == dice2.TOP and dice.FRONT == dice2.FRONT \
    and dice.RIGHT == dice2.RIGHT and dice.LEFT == dice2.LEFT \
    and dice.BACK == dice2.BACK and dice.BOTTOM == dice2.BOTTOM:
    print("Yes")
else:
    print("No")