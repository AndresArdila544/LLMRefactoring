import sys

n = int(input())
a = list(map(int, input().split()))
print(" ".join(map(str, a[::-1])))