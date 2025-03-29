import sys

while True:
    s = input()
    if s != '0':
        print(sum(map(int, s)))
    else:
        break