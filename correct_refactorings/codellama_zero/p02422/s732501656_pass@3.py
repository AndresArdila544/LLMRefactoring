str = input()
q = int(input())
for i in range(q):
    method, a, b, *p = input().split()
    if method == "print":
        print(str[int(a) : int(b) + 1])
    elif method == "reverse":
        str = str[: int(a)] + str[int(a):int(b) + 1][::-1] + str[int(b) + 1 :]
    elif method == "replace":
        str = str[: int(a)] + "".join(p) + str[int(b) + 1 :]