class Dice:
    def __init__(self):
        self.number = list(range(6))
        self.command_allpattern = "NNNNENNNNENNNNENNNNNENNNNEENNNNWWWSE"

    def set_number(self, d0, d1, d2, d3, d4, d5):
        self.number[0] = d0
        self.number[1] = d1
        self.number[2] = d2
        self.number[3] = d3
        self.number[4] = d4
        self.number[5] = d5

    def roll(self, command):
        if   command == "E":
            self.set_number(self.number[3],self.number[1],self.number[0],self.number[5],self.number[4],self.number[2])
        elif command == "N":
            self.set_number(self.number[1],self.number[5],self.number[2],self.number[3],self.number[0],self.number[4])
        elif command == "S":
            self.set_number(self.number[4],self.number[0],self.number[2],self.number[3],self.number[5],self.number[1])
        elif command == "W":
            self.set_number(self.number[2],self.number[1],self.number[5],self.number[0],self.number[4],self.number[3])
        else:
            raise

    def get_top(self):
        return self.number[0]

    def get_d2(self, d0, d1):
        flag_correct = False
        for command in self.command_allpattern:
            self.roll(command)
            if ((d0 == self.number[0]) and
                (d1 == self.number[1])):
                return self.number[2]
        raise


list_face = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    d0, d1 = map(int, input().split())
    print(Dice().get_d2(d0, d1))