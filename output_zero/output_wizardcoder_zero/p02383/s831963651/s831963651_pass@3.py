a = list(map(int, input().split()))
for d in ["N", "E", "S"]:
    if d == "N":
        print(a[1])
    elif d == "E":
        print(a[3])
    else:
        print(a[2])