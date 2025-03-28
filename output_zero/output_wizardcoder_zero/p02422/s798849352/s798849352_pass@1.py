str = input()
for _ in range(int(input())):
    op, a, b, *c = input().split()
    if op == "replace":
        str = str[:int(a)] + c[0] + str[int(b):]
    elif op == "reverse":
        str = str[:int(a)] + str[int(a):int(b)][::-1] + str[int(b):]
    else:
        print(str[int(a):int(b)])