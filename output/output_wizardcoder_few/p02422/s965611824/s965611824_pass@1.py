n = int(input())
while n > 0:
    o = input().split()
    if o[0] == 'replace':
        s = s[:int(o[1])] + o[3] + s[int(o[2])+1:]
    elif o[0] == 'reverse':
        rev = s[int(o[1]): int(o[2])+1][::-1]
        s = s[:int(o[1])] + rev + s[int(o[2])+1:len(s)]
    elif o[0] == 'print':
        print(s[int(o[1]):int(o[2])+1])
    n -= 1