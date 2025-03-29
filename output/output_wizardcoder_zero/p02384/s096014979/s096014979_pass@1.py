# Refactoring the code to reduce its lines and improve its readability.
class Dice:
    def __init__(self):
        self.dice = [i for i in range(6)]
        self.workspace = [i for i in range(6)
        
    def set(self, numbers):
        self.dice = [*numbers]
        self.workspace = [*numbers]
        
    def rotate(self, command):
        if command == "W":
            self.workspace = [self.dice[2], self.dice[1], self.dice[5], self.dice[0], self.dice[4]]
            self.dice = self.workspace
        elif command == "E":
            self.workspace = [self.dice[3], self.dice[1], self.dice[0], self.dice[5], self.dice[4]]
            self.dice = self.workspace
        if command == "S":
            self.workspace = [self.dice[4], self.dice[0], self.dice[2], self.dice[3], self.dice[5]]
            self.dice = self.workspace
        elif command == "N":
            self.workspace = [self.dice[1], self.dice[5], self.dice[2], self.dice[3], self.dice[0]]
            self.dice = self.workspace
    
    def get_top(self):
        top, front = map(int, input().split())
        print(self.dice[0])
         
    def predict(self, num):
        for i in range(num):
            top, front = map(int, input().split())
            while True:
                if top == self.dice[0] and front == self.dice[1]:
                    break
                rand_int = random.randint(1, 4)
                commands = ["W", "E", "S", "N"]
                self.rotate(commands[rand_int-1])
            print(self.dice[2])
        
    def getter(self):
        return self.dice[0], self.dice[1], self.dice[2]
     
    def predict_same(self, top, front, right):
        for _ in range(30):
            if top == self.dice[0] and front == self.dice[1] and right == self.dice[2]:
                print("Yes")
                break
            commands = ["W", "E", "S", "N"]
            rand_int = random.randint(1, 4)
            self.rotate(commands[rand_int-1])
        else:
            print("No")