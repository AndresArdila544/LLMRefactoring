s = input()
q = int(input())
for _ in range(q):
    d = list(map(str, input().split()))
    if d[0] == 'print': print(s[int(d[1])-1:int(d[2])+1])
    elif d[0] == 'reverse': s = s[:int(d[1])-1] + s[int(d[1]):int(d[2])][::-1] + s[int(d[2]):]
    elif d[0] == 'replace': s = s.replace(s[int(d[1])-1:int(d[2]+1], d[3], 1)
    else: print("invalid input")