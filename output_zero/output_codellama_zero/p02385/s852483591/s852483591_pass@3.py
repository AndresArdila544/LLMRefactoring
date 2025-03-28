class Dice:
def __init__(self, top, front, right, left, back, bottom):
    self.TOP = top
    self.BOTTOM = bottom
    self.FRONT = front
    self.BACK = back
    self.LEFT = left
    self.RIGHT = right

def move(self, direction):
    if direction == "N":
        tmp = self.TOP
        self.TOP = self.FRONT
        self.FRONT = self.BOTTOM
        self.BOTTOM = self.BACK
        self.BACK = tmp

    elif direction == "S":
        tmp = self.TOP
        self.TOP = self.BACK
        self.BACK = self.BOTTOM
        self.BOTTOM = self.FRONT
        self.FRONT = tmp

    elif direction == "W":
        tmp = self.TOP
        self.TOP = self.RIGHT
        self.RIGHT = self.BOTTOM
        self.BOTTOM = self.LEFT
        self.LEFT = tmp

    elif direction == "E":
        tmp = self.TOP
        self.TOP = self.LEFT
        self.LEFT = self.BOTTOM
        self.BOTTOM = self.RIGHT
        self.RIGHT = tmp

    elif direction == "SIDE":
        tmp = self.FRONT
        self.FRONT = self.RIGHT
        self.RIGHT = self.BACK
        self.BACK = self.LEFT
        self.LEFT = tmp

    else:
        raise Exception

top, front, right, left, back, bottom = map(int, input().split())
dice1 = Dice(top, front, right, left, back, bottom)

top2, front2, right2, left2, back2, bottom2 = map(int,input().split())
dice2 = Dice(top2, front2, right2, left2, back2, bottom2)

if is_same():
    print("Yes")
else:
    print("No")