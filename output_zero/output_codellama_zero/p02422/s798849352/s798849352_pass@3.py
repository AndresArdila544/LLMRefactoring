str = input()
q = int(input())
for i in range(q):
    line = input().split()
    c, a, b = line[0], int(line[1]), int(line[2]) + 1
    if c == "replace":
        str = str[:a] + line[3] + str[b:]
    elif c == "reverse":
        str = str[:a] + str[a:b][::-1] + str[b:]
    else:
        print(str[a:b])