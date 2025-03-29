import numpy as np

# Refactored version of area calculation
def calculate_area(rooms):
    return sum(room[0] for room in rooms)

# Refactored version of input function
def get_input():
    n = int(raw_input())
    list_mojiretsu=raw_input().split(" ")
    henka=map(int,list_mojiretsu)
    return henka[0], henka[1], henka[2]

# Refactored version of main function
def main():
    # Initialize floors and dictionary
    floor_11 = np.array([0])
    floor_12 = np.array([0])
    floor_13 = np.array([0])
    floor_21 = np.array([0])
    floor_22 = np.array([0])
    floor_23 = np.array([0])
    floor_31 = np.array([0])
    floor_32 = np.array([0])
    floor_33 = np.array([0])
    floor_41 = np.array([0])
    floor_42 = np.array([0])
    floor_43 = np.array([0])
    fldic = {
        "11": floor_11,
        "12": floor_12,
        "13": floor_13,
        "21": floor_21,
        "22": floor_22,
        "23": floor_23,
        "31": floor_31,
        "32": floor_32,
        "33": floor_33,
        "41": floor_41,
        "42": floor_42,
        "43": floor_43,
    }

    # Loop for inputting information about the mojiretsu
    n = int(raw_input())
    for _ in range(n):
        henka = get_input()
        fldic[str(henka[0]) + str(henka[1])][henka[2] - 1] += henka[3]

    # Print the areas of each floor
    print "Area of floor 1:", calculate_area(floor_11)
    print "Area of floor 2:", calculate_area(floor_12)
    print "Area of floor 3:", calculate_area(floor_13)
    print "####################"
    print "Area of floor 4:", calculate_area(floor_41)
    print "Area of floor 5:", calculate_area(floor_42)
    print "Area of floor 6:", calculate_area(floor_43)

if __name__ == '__main__':
    main()