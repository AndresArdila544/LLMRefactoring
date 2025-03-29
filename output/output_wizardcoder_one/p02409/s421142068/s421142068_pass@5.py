```python
import numpy as np
class Room:
    def __init__(self):
        self.room = [0] * 10
        
def initialize_rooms():
    return [Room() for i in range(3)]

def print_floor(floors):
    for floor in floors:
        print(', '.join(str(room) for room in floor.room))
        
# Initialize the rooms dictionary with all 0 values
floors = {
    "11": initialize_rooms(),
    "12": initialize_rooms(),
    "13": initialize_rooms(),
    "21": initialize_rooms(),
    "22": initialize_rooms(),
    "23": initialize_rooms(),
    "31": initialize_rooms(),
    "32": initialize_rooms(),
    "33": initialize_rooms()
}

# Get the number of input lines to process
n = int(input())
for i in range(n):
    # Split the input into a list of integers and add it to the appropriate floor's room index
    floor, room, amount = map(int, input().split())
    floors["{}{}".format(floor)][room - 1] += amount

# Print each floor in separate sections
print_floor(floors["11"])
print("####################")
print_floor(floors["12"])
print("####################")
print_floor(floors["13"])
print("####################")
print_floor(floors["21"])
print("####################")
print_floor(floors["22"])
print("####################")
print_floor(floors["23"])
print("####################")
print_floor(floors["31"])
print("####################")
print_floor(floors["32"])
print("####################")
print_floor(floors["33"])
```