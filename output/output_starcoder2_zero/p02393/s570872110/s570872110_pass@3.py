"""

import sys
from heapq import nlargest, nsmallest


def find_smallest(numbers):
    return nsmallest(3, numbers)[0] if len(numbers) > 2 else None


def find_median(numbers):
    return (nsmallest(2, numbers)[1], nsmallest(3, numbers)[0])[len(numbers) % 2] if len(numbers) > 2 else None


def find_largest(numbers):
    return nlargest(3, numbers)[-1] if len(numbers) > 2 else None


def main():
    input_lines = sys.stdin.readlines()

    # parse input lines and store them in `numbers` list
    numbers = [int(x) for x in input_lines[0].split()]

    smallest, median, largest = find_smallest(numbers), find_median(numbers), find_largest(numbers)

    if smallest is not None:
        print("{}".format(smallest))

    if median is not None:
        print("{}".format(median))

    if largest is not None:
        print("{}".format(largest))


if __name__ == '__main__':
    main()