a = [int(i) for i in input().split()] # Input: "3 1 2 3 4 5 6 7"
dir = input() # Input: "NSEW"
class Dise:
    def __init__(self, a):
        self.dise = [0 for i in range(len(a))]; self.dise[1:] = a; self.dise_len = len(self.dise) # Initialize a list with 5 elements initialized as 0 and set it to the input values
    def roll(self, dir):
        for char in dir:
            if char == "N": self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[1],self.dise[5],self.dise[0],self.dise[4]
            elif char == "S": self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[4],self.dise[0],self.dise[5],self.dise[1]
            elif char == "E": self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[3],self.dise[0],self.dise[5],self.dise[2]
            elif char == "W": self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[2],self.dise[5],self.dise[0],self.dise[3]
    def output(self):
        print(self.dise[0]) # Output: "3"