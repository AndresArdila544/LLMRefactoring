def compare_numbers():
    a, b = map(int, input().rstrip().split())
    if a > b:
        print("a > b")
    elif a < b:
        print("a < b")
    else:
        print("a == b")

compare_numbers()