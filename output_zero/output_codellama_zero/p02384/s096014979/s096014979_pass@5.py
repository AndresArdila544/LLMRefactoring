import random

class Dice:
    def __init__(self):
        self.dice = list(range(6))
        self.workspace = self.dice.copy()
        
    def set(self, numbers):
        self.dice = numbers
        self.workspace = self.dice.copy()
    
    def rotate(self, command):
        if command == "W":
            self.workspace = [self.dice[2], self.dice[1], self.dice[5], self.dice[0], self.dice[4], self.dice[3]]
        elif command == "E":
            self.workspace = [self.dice[3], self.dice[1], self.dice[0], self.dice[5], self.dice[4], self.dice[2]]
        elif command == "S":
            self.workspace = [self.dice[4], self.dice[0], self.dice[2], self.dice[3], self.dice[5], self.dice[1]]
        elif command == "N":
            self.workspace = [self.dice[1], self.dice[5], self.dice[2], self.dice[3], self.dice[0], self.dice[4]]
        
    def get_top(self):
        return self.dice[0]
    
    def predict(self, num):
        for i in range(num):
            top, front = map(int, input().split())
            while (True):
                if top == self.dice[0] and front == self.dice[1]:
                    break
                command_num = random.randint(1, 4)
                if command_num == 1:
                    self.rotate("W")
                elif command_num == 2:
                    self.rotate("E")
                elif command_num == 3:
                    self.rotate("S")
                elif command_num == 4:
                    self.rotate("N")
            print(self.dice[2])
    
    def getter(self):
        return self.dice[0], self.dice[1], self.dice[2]
    
    def predict_same(self, top, front, right):
        for n in range(30):
            if top ==self.dice[0] and front== self.dice[1] and right ==self.dice[2]:
                print("Yes")
                break
            command_num=random.randint(1,4)
            if command_num == 1:
                    self.rotate("W")
            elif command_num == 2:
                    self.rotate("E")
            elif command_num == 3:
                    self.rotate("S")
            elif command_num == 4:
                    self.rotate("N")
        
        if top!=self.dice[0] or front!=self.dice[1] or front!=self.dice[2]:
            print("No")
            
numbers = list(map(int, input().split()))
dice = Dice()
dice.set(numbers)
q = int(input())
for i in range(q):
    top, front = map(int, input().split())
    dice.predict_same(top, front, dice.getter()[2])