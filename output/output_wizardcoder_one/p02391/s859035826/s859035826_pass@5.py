a = [int(e) for e in input().split()]
if a[0] < a[1]:
    print("a < b") if a[0] < a[1] else (print("a > b") if a[0] > a[1] else print("a == b"))