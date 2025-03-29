import sys

n = sys.stdin.readlines()

print(min(list(map(int, n[1].split(" ")))), max(list(map(int, n[1].split(" ")))), sum(list(map(int, n[1].split(" ")))))