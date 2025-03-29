a = []
while True:
    n = input()
    if n == '0 0': break
    x, y = map(int, n.split())
    print(x, y) if x > y else print(n)