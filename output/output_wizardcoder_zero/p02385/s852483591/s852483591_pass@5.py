class Dice:
    def __init__(self, top, front, right, left, bottom):
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.bottom = bottom
        
    def move(self, direction):
        if direction == "N":
            self.top, self.front, self.left, self.bottom, self.right = self.front, self.bottom, self.left, self.top
        elif direction == "E":
            self.top, self.front, self.left, self.bottom, self.right = self.left, self.bottom, self.top, self.right
        elif direction == "S":
            self.top, self.front, self.left, self.bottom, self.right = self.bottom, self.left, self.top, self.front
        else:
            raise Exception("Invalid input")
    
    def is_same(d1, d2):
        for _ in range(4):
            d1.move("SIDE")
            if d1.top == d2.top and d1.front == d2.front \
                and d1.right == d2.right and d1.left == d2.left \
                and d1.bottom == d2.bottom:
                return True
        for _ in range(4):
            d1.move("N")
            if d1.top == d2.top and d1.front == d2.front \
                and d1.right == d2.right and d1.left == d2.left \
                and d1.bottom == d2.bottom:
                return True
        return False
    
    top, front, right, left, bottom = map(int,input().split())
    dice = Dice(top, front, right, left, bottom)
    top2, front2, right2, left2, bottom2 = map(int,input().split())
    dice2 = Dice(top2, front2, right2, left2, bottom2)
    
    if is_same(dice, dice2):
        print("Yes")
    else:
        print("No")