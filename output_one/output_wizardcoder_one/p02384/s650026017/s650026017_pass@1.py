class Dice:
    def __init__(self, a, b, c, d, e):
        self.state = [a, b, c, d, e]
    
    def is_right_surface(self, top, front):
        if (top == 1 and front == 2) or (top == 3 and front == 4) or (top == 5 and front == 6):
            return self.state[2], self.state[0], True
        elif (top == 1 and front == 3) or (top == 2 and front == 4) or (top == 3 and front == 6):
            return self.state[3], self.state[0], True
        elif (top == 2 and front == 5):
            return self.state[1], self.state[0], False
        elif (top == 4 and front == 6) or (top == 5 and front == 1):
            return self.state[3], self.state[1], True
        
    def move(self, moves_str):
        for m in moves_str:
            if m == "N":
                self.state[0], self.state[2] = self.state[2], self.state[0]
                self.state[1], self.state[3] = self.state[3], self.state[1]
            elif m == "E":
                self.state[0], self.state[2] = self.state[2], self.state[0]
                self.state[1], self.state[3] = self.state[3], self.state[1]
            elif m == "W":
                self.state[0], self.state[2] = self.state[2], self.state[0]
        return self.state[-1], self.state[0]

    def roll(self):
        roll_choice = ["N", "E", "W"]
        return random.choice(roll_choice)

a, b, c, d = map(int, input().split())
dice = Dice(a, b, c, d)
n = int(input())
for i in range(n):
    moves_str = input()
    right, left, is_swap = dice.is_right_surface(*map(int, input().split()))
    print(left if not is_swap else right)