str = input()
for _ in range(int(input())):
    cmd, a, b, *c = input().split()
    if cmd == "replace":
        str = str[:a] + c[0] + str[b:]
    elif cmd == "reverse":
        str = str[:a] + str[a:b][::-1] + str[b:]
    else:
        print(str[int(a):int(b)])