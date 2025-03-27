str = input()
q = int(input())
for i in range(q):
    method, a, b, *p = input().split()

    if method == "print":
        print(str[int(a) : int(b) + 1])
    elif method == "reverse":
        pre = str[: int(a)]
        reverse = str[int(a) : int(b) + 1][::-1]
        after = str[int(b) + 1 :]
        str = pre + reverse + after
    elif method == "replace":
        pre = str[: int(a)]
        after = str[int(b) + 1 :]
        str = pre + "".join(p) + after

