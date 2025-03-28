class Dice(object):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.states = [s1, s2, s3, s4, s5, s6]

    def move(self, direction, n):
        for _ in range(n):
            if direction == 'E':
                self.rotate('WNE')
            elif direction == 'W':
                self.rotate('ENW')
            elif direction == 'N':
                self.rotate('SWD')
            else:
                self.rotate('ESU')

    def rotate(self, directions):
        for d in directions[::-1]:
            if d == 'E':
                prev_s2 = self.states[2]
                self.states[2], self.states[4] = self.states[4], self.states[2]
                self.states[4], self.states[3] = self.states[3], prev_s2
            elif d == 'W':
                prev_s4 = self.states[4]
                self.states[4], self.states[1] = self.states[1], self.states[4]
                self.states[1], self.states[3] = self.states[3], prev_s4
            elif d == 'N':
                prev_s2 = self.states[2]
                self.states[2], self.states[5] = self.states[5], self.states[2]
                self.states[5], self.states[1] = self.states[1], prev_s2
            else:
                prev_s2 = self.states[2]
                self.states[2], self.states[3] = self.states[3], self.states[2]
                self.states[3], self.states[5] = self.states[5], prev_s2

    def isSameDice(self, anotherDice):
        return all([a == b for a, b in zip(self.states, anotherDice.states)])

# Input
s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice1 = Dice(s1, s2, s3, s4, s5)
dice2 = Dice(*map(int, input().split()))

# Function call
dice2.move('ESUE' * 6)

if dice2.isSameDice(dice1):
    print("Yes")
else:
    print("No")