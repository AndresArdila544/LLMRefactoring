import numpy as np

# Refactored version of the program

def area(x):
    return x[0]*x[1]

def kaijo(x):
    print "",
    for i in range(len(x)-1):
        print str(x[i]),
    print str(x[len(x)-1])

# Define the floors as lists of lists
floor_11 = [0] * 10
floor_12 = [0] * 10
floor_13 = [0] * 10
floor_21 = [0] * 10
floor_22 = [0] * 10
floor_23 = [0] * 10
floor_31 = [0] * 10
floor_32 = [0] * 10
floor_33 = [0] * 10
floor_41 = [0] * 10
floor_42 = [0] * 10
floor_43 = [0] * 10

# Create a dictionary with the floor numbers as keys and their areas as values
fldic = {"11": floor_11, "12": floor_12, "13": floor_13, "21": floor_21, "22": floor_22, "23": floor_23, "31": floor_31, "32": floor_32, "33": floor_33, "41": floor_41, "42": floor_42, "43": floor_43}

# Take input for the number of moves
n = int(raw_input())

# Loop through each move
for l in range(n):
    # Get the list of integers representing the move
    list_mojiretsu = raw_input().split(" ")
    henka = map(int, list_mojiretsu)
    
    # Update the floor area based on the move
    fldic[str(henka[0]) + str(henka[1])][henka[2] - 1] += henka[3]

# Print the areas of each floor
kaijo(floor_11)
kaijo(floor_12)
kaijo(floor_13)
print "####################"
kaijo(floor_21)
kaijo(floor_22)
kaijo(floor_23)
print "####################"
kaijo(floor_31)
kaijo(floor_32)
kaijo(floor_33)
print "####################"
kaijo(floor_41)
kaijo(floor_42)
kaijo(floor_43)