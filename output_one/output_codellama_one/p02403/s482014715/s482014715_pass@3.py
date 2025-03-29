import sys
h, w = map(int, input().split())
while h:
    for i in range(h):
        print("#" * w)
    h = int(input())