Here's a refactored version of the code:

while True:
    m,f,r = list(map(int, input().split()))
    if (m == -1 and f == -1) or m + f < 30:
        print("F")
    elif m + f >= 50 and r >= 50:
        print("A")
    else:
        print(["D", "C", "B"])[m + f // 10 - 4]