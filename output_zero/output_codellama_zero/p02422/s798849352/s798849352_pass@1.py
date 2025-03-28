def solve(inp_str, q):
    for _ in range(q):
        line = input().split()
        c = line[0]
        a = int(line[1])
        b = int(line[2]) + 1

        if c == "replace":
            inp_str = inp_str[:a] + line[3] + inp_str[b:]
        elif c == "reverse":
            inp_str = inp_str[:a] + inp_str[a:b][::-1] + inp_str[b:]
        else:
            print(inp_str[a:b])