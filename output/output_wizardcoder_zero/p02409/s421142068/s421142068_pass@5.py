# Refactoring the code to reduce complexity and improve readability
# We can use dictionaries to store the floor objects instead of separate variables, reduce the repetitive lines of initializing a new ryo object for each floor, and simplify the kaijo function.
import numpy as np
class Room:
    def __init__(self):
        self.room = np.zeros(10)

# Define a single class for both ryo and kurosu (the class names can be improved, but we'll keep it as is)
class Ryk:
    def init_room(self):
        return Room().room
        
# Define the kaijo function to simplify the code block for printing rooms
def kaijo(x):
    print ''.join([str(i) for i in x[:-1]) + str(x[-1])]
    
# Initialize all floors as an empty dictionary with keys representing their names and values as 0s of length 10 (representing the rows)
floors = {f"{floor}{row}": Ryk().init_room() for floor in range(4) for row in range(3)}

# Get input for number of commands to execute and execute them one by one
n = int(input())
for _ in range(n):
    cmd, floor, row, num = map(int, input().split())
    floors[f"{floor}{row+1}"][num-1] += 1 if cmd == 1 else -1 # Add/remove the value from the corresponding room based on command type and index
for i in range(4): # Iterate through each floor
    for j in range(3): # Iterate through each row of the floor
        kaijo(floors[f"{i+1}{j+1}"]) # Print each row of the floor using the simplified kaijo function