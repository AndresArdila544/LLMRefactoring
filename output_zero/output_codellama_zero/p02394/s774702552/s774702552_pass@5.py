Here is a cleaned-up version of your program:

W, H, x, y = map(int, input().split())
if r <= x and x <= W and r <= y and y <= H:
    print("Yes")
else:
    print("No")