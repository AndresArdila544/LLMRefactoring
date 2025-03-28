class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.east = east
        self.west = west
        self.north = north
        self.bottom = bottom

    def rotate(self, times=1):
        for _ in range(times):
            tmp = self.north
            self.north = self.east
            self.east = self.south
            self.south = self.west
            self.west = tmp

    def print_top(self):
        print(self.top)

    def get_top(self, target):
        if self.top == target:
            return
        for _ in range(3):
            self.rotate()
            if self.top == target:
                return
        else:
            print("Error")


if __name__ == "__main__":
    n = input().split()
    count = int(input())
    dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3]), int(n[4]), int(n[5]))

    for _ in range(count):
        buf = input().split()

        dice.get_top(int(buf[0]))
        dice.rotate(int(buf[1]))
        dice.print_top()