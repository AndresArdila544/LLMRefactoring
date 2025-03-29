class Dice(object):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.state = [s1, s2, s3, s4, s5, s6]
    def move(self, direction):
        if direction == 'east':
            prev_s6 = self.state[0]
            self.state[0] = self.state[2]
            self.state[2] = self.state[4]
            self.state[4] = prev_s6
        elif direction == 'west':
            prev_s6 = self.state[0]
            self.state[0] = self.state[1]
            self.state[1] = self.state[3]
            self.state[3] = prev_s6
        elif direction == 'north':
            prev_s6 = self.state[2]
            self.state[2] = self.state[4]
            self.state[4] = self.state[0]
            self.state[0] = prev_s6
        elif direction == 'south':
            prev_s6 = self.state[2]
            self.state[2] = self.state[1]
            self.state[1] = self.state[3]
            self.state[3] = prev_s6
        elif direction == 'rotate':
            prev_s2 = self.state[0]
            self.state[0] = self.state[4]
            self.state[4] = self.state[1]
            self.state[1] = self.state[3]
            self.state[3] = prev_s2
    def top(self):
        return self.state[0]
    def front(self):
        return self.state[1]
    def right(self):
        return self.state[2]
    def isSameDice(self, anotherDice):
        if all([dice1_state == dice2_state for dice1_state, dice2_state in zip(self.state, anotherDice.state)]):
            return True
        else:
            return False

s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice1 = Dice([s1, s2, s3, s4, s5, s6])
s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice2 = Dice([s1, s2, s3, s4, s5, s6] if dice1.isSameDice(dice2) else None
for j in range(6):
    dice2.move('east' if j % 2 == 0 else 'west')
    for k in range(4):
        dice2.move('rotate')
    if dice2 is not None and dice1.isSameDice(dice2):
        print("Yes")
        break
else:
    print("No")