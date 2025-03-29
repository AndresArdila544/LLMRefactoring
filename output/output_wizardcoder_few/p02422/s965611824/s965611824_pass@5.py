Refactored version of the original program:

n = int(input())
for _ in range(n):
    o = input().split()
    if o[0] == 'replace':
        s, a, b, c = map(str,o)
        s = s[:int(a)] + c + s[int(b)+1:]
    elif o[0] == 'reverse':
        i, j = map(int, o[1:])
        s = s[:i] + s[i:j+1][::-1] + s[j+1:]
    else: # o[0] == 'print'
        print(s[int(o[1]): int(o[2]+1)

Refactored version of the code:

n = int(input())
for _ in range(n):
    i, j = map(int, input().split()) if o[0] == 'reverse' else None
    s, *ops = input().split()
    for op in ops:
        if op == 'replace':
            a, b, c = map(str, o)
            s = s[:int(a)] + c + s[int(b)+1:]
        elif op == 'print':
            print(s[int(i): int(j)+1])
        else: # op == 'reverse'
            s = s[:i] + s[i:j+1][::-1] + s[j+1:]