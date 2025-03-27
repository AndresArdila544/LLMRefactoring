Here is the refactored version of the code:
```
import numpy as np

# Define a function to create a floor
def create_floor(size):
    return list(np.zeros(size))

# Define a dictionary to store the floors
floors = {
    "11": create_floor(10),
    "12": create_floor(10),
    "13": create_floor(10),
    "21": create_floor(10),
    "22": create_floor(10),
    "23": create_floor(10),
    "31": create_floor(10),
    "32": create_floor(10),
    "33": create_floor(10),
    "41": create_floor(10),
    "42": create_floor(10),
    "43": create_floor(10)
}

# Define a function to print the floor
def print_floor(floor):
    for row in floor:
        print(" ".join(str(x) for x in row))
    print("####################")

# Get input from user
n = int(input())
list_mojiretsu = input().split()
henka = list(map(int, list_mojiretsu))
floors[str(henka[0]) + str(henka[1])][henka[2] - 1] += henka[3]

# Print the floors
print_floor(floors["11"])
print_floor(floors["12"])
print_floor(floors["13"])
print("####################")
print_floor(floors["21"])
print_floor(floors["22"])
print_floor(floors["23"])
print("####################")
print_floor(floors["31"])
print_floor(floors["32"])
print_floor(floors["33"])
print("####################")
print_floor(floors["41"])
print_floor(floors["42"])
print_floor(floors["43"])
```