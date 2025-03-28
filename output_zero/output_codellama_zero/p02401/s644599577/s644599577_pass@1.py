Here is a more efficient and readable way to solve this problem:

while True:
    try:
        a, op, b = map(int, input().split())
        if op == '?':
            break
        ans = eval(f"{a} {op} {b}")
        print(ans)
    except ValueError:
        break