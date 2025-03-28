```python
import random

class Dice:
    def __init__(self):
        self.dice = [i for i in range(6)]
        self.workspace = [i for i in range(6)]
        self.top = self.dice[0]

    def set(self, numbers):
        self.dice = [i for i in numbers]
        self.workspace = [i for i in numbers]

    def rotate(self, command):
        if command == "W":
            self.workspace = [self.dice[2], self.dice[1], self.dice[5], self.dice[0], self.dice[4]]
            self.dice = self.workspace
        elif command == "E":
            self.workspace = [self.dice[3], self.dice[1], self.dice[0], self.dice[5], self.dice[4]]
            self.dice = self.workspace
        elif command == "S":
            self.workspace = [self.dice[4], self.dice[0], self.dice[2], self.dice[3], self.dice[5]]
            self.dice = self.workspace
        elif command == "N":
            self.workspace = [self.dice[1], self.dice[5], self.dice[2], self.dice[3], self.dice[0]]
            self.dice = self.workspace
        
    def get_top(self):
        self.top = self.dice[0]
        print(self.top)

    def predict(self, num):
        for _ in range(num):
            top, front = map(int, input().split())
            while True:
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
        for _ in range(30):
            if top == self.dice[0] and front == self.dice[1] and right == self.dice[2]:
                print("Yes")
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
        if top != self.dice[0] or front != self.dice[1] or right != self.dice[2]:
            print("No")
```