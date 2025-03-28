s = input()
while True:
    try:
        o = input().split()
        if o[0] == 'replace':
            s = s[:int(o[1])] + o[3] + s[int(o[2])+1:]
        elif o[0] == 'reverse':
            rev_start, rev_end = int(o[1]), int(o[2])
            s = s[:rev_start] + s[rev_start:rev_end+1][::-1] + s[rev_end+1:]
        elif o[0] == 'print':
            print(s[int(o[1]):int(o[2])+1])
            break
    except EOFError:
        break