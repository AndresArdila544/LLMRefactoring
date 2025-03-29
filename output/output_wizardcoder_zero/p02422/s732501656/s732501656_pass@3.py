str = input()
q = int(input())
for i in range(q):
    method, a, b, *p = input().split()
    if method == "print":
        print(str[int(a) : int(b) + 1])
    else:
        str_list = list(str)
        if method == "reverse":
            pre = str[: int(a)]
            reverse = str_list[int(a): int(b) + 1]
            reverse.reverse()
            str_list[int(a): int(b) + 1] = reverse
        elif method == "replace":
            pre = str[: int(a)]
            after = str[int(b) + 1 :]
            str_list[int(a): int(b) + 1] = p
        str = "".join(str_list) + after
print(str)