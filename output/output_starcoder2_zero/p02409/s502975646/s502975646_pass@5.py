You can also find a solution at: https://www.codeeval.com/browse/381/
"""
# Code eval solution
import sys

read = sys.stdin.readline


def print_result(buildings):
    for floor in buildings:
        for building in floor:
            for block in building:
                print(block, end=' ')
            print()

        if not (index + 1) == len(buildings):
            # If we are not on the last floor, print the divider.
            print_divider(len(floor[0]))

    print()


def print_divider(length):
    for i in range(0, length):
        print('#', end='')
    print()


def main():
    """
    Main function to parse input and call appropriate functions.
    :return: None
    """
    # Read first line which contains total number of floors
    floor_count = int(read())

    # Create a list to hold the 3D building layout
    buildings = []

    # Parse each floor one by one
    for i in range(floor_count):
        # Each floor consists of three blocks
        buildings.append([[], [], []])

        # Read next 10 lines which contain information about
        # block level and number of houses
        for j in range(10):
            block_info = read().split()

            # Add the info to the block layout
            buildings[i][int(block_info[0]) - 1].append(int(block_info[2]))

    print_result(buildings)


if __name__ == "__main__":
    main()