#import numpy as np

class Room:
    def __init__(self):
        self.room = [0] * 10

def add_area(rooms, row, col, height):
    rooms[row][col - 1] += height

def print_floor(room):
    for r in room:
        print(" ".join([str(x) for x in r]))

def main():
    floor_11 = Room()
    floor_12 = Room()
    floor_13 = Room()
    floor_21 = Room()
    floor_22 = Room()
    floor_23 = Room()
    floor_31 = Room()
    floor_32 = Room()
    floor_33 = Room()
    floor_41 = Room()
    floor_42 = Room()
    floor_43 = Room()

    floors = {
        "11": [floor_11, floor_12, floor_13],
        "12": [floor_11, floor_22, floor_23],
        "13": [floor_11, floor_32, floor_33],
        "21": [floor_21, floor_22, floor_23],
        "22": [floor_21, floor_12, floor_42],
        "23": [floor_22, floor_32, floor_43],
        "31": [floor_31, floor_32, floor_33],
        "32": [floor_31, floor_22, floor_42],
        "33": [floor_31, floor_12, floor_43],
        "41": [floor_41, floor_42, floor_43],
        "42": [floor_41, floor_22, floor_43],
        "43": [floor_41, floor_32, floor_43]
    }

    n = int(input())
    for _ in range(n):
        room, row, col, height = map(int, input().split(" "))
        add_area(floors[str(row) + str(col)], row % 2 + 1, col - 1)

    print_floor(floor_11.room)
    print_floor(floor_12.room)
    print_floor(floor_13.room)
    print "####################"
    print_floor(floor_21.room)
    print_floor(floor_22.room)
    print_floor(floor_23.room)
    print "####################"
    print_floor(floor_31.room)
    print_floor(floor_32.room)
    print_floor(floor_33.room)
    print "####################"
    print_floor(floor_41.room)
    print_floor(floor_42.room)
    print_floor(floor_43.room)

main()