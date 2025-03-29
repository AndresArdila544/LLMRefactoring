s = ""
while s != "-":
    m = int(input())
    for i in range(m):
        h = int(input())
        s = s[-h:] + s[:-h] if len(s) > 0 else ""
        print(s)