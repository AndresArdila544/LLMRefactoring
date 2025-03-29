```python
import numpy as np

class Room:
    def __init__(self):
        self.room = []

def area():
    for _ in range(10):
        self.room.append(0)

def room_occupation(x):
    y = ""
    for i in range(len(x)-1):
        y += str(x[i]) + " "
    return y + str(x[-1])

fldic = {}
for floor in ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43"]:
    fldic[floor] = Room()

# Occupation of rooms
n = int(input())
for _ in range(n):
    floor, room, amount = map(int, input().split(" "))
    fldic["{}{}".format(floor)].room[room-1] += amount
    
# Printing occupied rooms by floors
for floor in ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43"]:
    print(room_occupation(fldic[floor].room))
    print("####################")
```