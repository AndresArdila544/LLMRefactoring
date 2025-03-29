class Dice:
    def __init__(self):
        self.number = [i for i in range(6)]  # This could be written as [0,1,2,3,4,5,6] if you want to keep it shorter.
        self.order = 'NNNNWNNNWNNNENNNWNNN'
    
    def roll(self, loc):
        work = self.number.copy()  # Creating a copy of the current state of dice numbers instead of rolling the order.
        if loc == 'E':
            self.number[3], self.number[1], self.number[0], self.number[4], self.number[5] = work[1], work[2], work[3], work[0]  # Using multiple assignments.
        elif loc == 'N':
            self.number[1], self.number[4], self.number[2], self.number[3], self.number[0] = work[5], work[0], work[2], work[3]  # Using multiple assignments.
        elif loc == 'S':
            self.number[4], self.number[0], self.number[2], self.number[3], self.number[1] = work[0], work[2], work[3], work[5]  # Using multiple assignments.
        elif loc == 'W':
            self.number[2], self.number[1], self.number[4], self.number[0], self.number[3] = work[1], work[5], work[0], work[3]  # Using multiple assignments.
    
    def equals(self, another):
        for i in range(len(self.order)):
            self.roll(self.order[i])
            if self.number != another.number:
                return False
        return True  # The function can be reduced to a single line with the boolean expression.
    
diceA = Dice()
diceB = Dice()

table1 = list(map(int,input().split()))
diceA.number = table1[0:6]  # Assigning values directly to diceA's numbers attribute.

table2 = list(map(int,input().split())
diceB.number = table2[0:6]  # Assigning values directly to diceB's numbers attribute.

print("Yes" if diceA.equals(diceB) else "No")  # Using a ternary operator instead of an if-else statement.

# The code is now more concise and readable, but it's still not very clean and can be further improved with some improvements such as using list comprehension to reduce lines even further.