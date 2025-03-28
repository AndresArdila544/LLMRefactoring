import sys
from collections import Counter

if __name__ == "__main__":
    dict = {}
    for i in range(97, 123):
        dict[chr(i)] = 0

    lines = sys.stdin.readlines()

    ctr = Counter()
    for line in lines:
        ctr.update(line.lower())

    l = list(ctr.items())
    for i in l:
        print(f"{i[0]} : {i[1]}")