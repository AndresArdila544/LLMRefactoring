W = int(input())
H = W
x, y = map(int, input().split())
r = int(input())
W -= r
H -= r
if r <= x and x <= W and r <= y and y <= H:
    print("Yes")
else:
    print("No")