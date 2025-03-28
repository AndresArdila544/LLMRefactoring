z = int(input())
a = list(map(int, input().split()))[::-1]
print(" ".join(str(x) for x in a))