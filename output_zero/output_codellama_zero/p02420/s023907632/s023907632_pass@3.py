import itertools
import sys

while True:
    string = list(sys.stdin.readline().strip())
    if not string or string[0] == '-':
        break
    shuffle_count = int(input())
    for i in range(shuffle_count):
        shuffle_num = int(input())
        for _ in itertools.repeat(None, shuffle_num):
            string.append(string.pop(0))
    print("".join(string))