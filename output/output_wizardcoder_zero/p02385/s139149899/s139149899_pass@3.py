```python
class Dice():
    def __init__(self):
        self.number = list(range(6))  # Use a list comprehension instead of for loop to generate a list of integers from 0-5.
        self.work = list(range(6))
        self.order = 'NNNNWNNNWNNNENNNENNNWNNN'  
    
    def roll(self, loc):
        # Use a copy of the original number to avoid modifying it.
        new_nums = list(self.number)
        if loc == 'E':
            new_nums[3], new_nums[1] = new_nums[1], new_nums[3]  # Swap values using tuple unpacking.
            new_nums[4], new_nums[0] = new_nums[0], new_nums[4]
        elif loc == 'N':
            new_nums[1], new_nums[5], new_nums[2], new_nums[3], new_nums[0], new_nums[4] = new_nums[1], new_nums[0], new_nums[2], new_nums[3], new_nums[4]
        elif loc == 'S':
            new_nums[4], new_nums[0], new_nums[2], new_nums[3], new_nums[5] = new_nums[0], new_nums[2], new_nums[3], new_nums[5], new_nums[1]
        elif loc == 'W':
            new_nums[2], new_nums[1] = new_nums[1], new_nums[2]  # Swap values using tuple unpacking.
            new_nums[4], new_nums[0] = new_nums[0], new_nums[4]
        
        self.number = new_nums
    
    def equals(self, another):
        for i in range(6):
            self.roll(self.order[i])  # Use a loop to apply all moves.
            if all(a == b for a, b in zip(self.number, another.number)):  # Use the built-in function `zip` and `all` to check if all elements are equal.
                return True
        
        return False

diceA = Dice()
diceB = Dice()

# Use list comprehension to convert input strings to integers.
table1, table2 = [int(x) for x in input().split()] + [int(x) for x in input().split()]  
diceA.number = table1[0], table1[1], table1[2], table1[3], table1[4], table1[5]
diceB.number = table2[0], table2[1], table2[2], table2[3], table2[4], table2[5]

print("Yes" if diceA.equals(diceB) else "No")  # Use ternary operator to reduce the lines of code.
``` 

I hope this helps! Let me know if you have any questions or concerns.