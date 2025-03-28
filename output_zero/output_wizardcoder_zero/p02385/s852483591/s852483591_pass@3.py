class Dice:
    def __init__(self, top, front, right, left, bottom):
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.bottom = bottom
    
    def move(self, direction):
        if direction == "N":
            self.top, self.front, self.bottom, self.left, self.right = self.front, self.bottom, self.left, self.top
        elif direction == "E":
            self.top, self.front, self.bottom, self.right, self.left = self.bottom, self.left, self.right, self.top
        elif direction == "S":
            self.top, self.front, self.bottom, self.left, self.right = self.bottom, self.right, self.top, self.left
        elif direction == "W":
            self.top, self.front, self.bottom, self.left, self.right = self.right, self.top, self.left, self.bottom
        else:
            raise Exception("Invalid input")
    
    def is_same(dice1, dice2):
        for _ in range(4):
            dice1.move("SIDE")
            if all([getattr(dice1, side) == getattr(dice2, side) for side in ["top", "front", "right", "left", "bottom"]]):
                return True
        for _ in range(4):
            dice1.move("N")
            if all([getattr(dice1, side) == getattr(dice2, side) for side in ["top", "front", "right", "left", "bottom"]]:
                return True
        return False
    
top, front, right, left, bottom = map(int,input().split())
dice1 = Dice(top, front, right, left, bottom)
top2, front2, right2, left2, bottom2 = map(int,input().split())
dice2 = Dice(top2, front2, right2, left2, bottom2)

if is_same(dice1, dice2):
    print("Yes")
else:
    print("No")