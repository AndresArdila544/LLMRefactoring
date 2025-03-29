Here is the refactored code:
z = int(input())
a = list(map(int, input().split()))[::-1]
print(" ".join(map(str, a)))