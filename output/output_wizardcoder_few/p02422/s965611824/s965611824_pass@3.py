s = input()
q = int(input())
for _ in range(q):
    o = input().split()
    if o[0] == 'replace':
        s = s[:int(o[1])] + o[3] + s[int(o[2]+1:]
    elif o[0] == 'reverse':
        rev = s[int(o[1]):int(o[2]+1][::-1]
        s = s[:int(o[1])] + rev + s[int(o[2]+1:len(s)]
    elif o[0] == 'print':
        print(s[int(o[1]:int(o[2]+1])
refactored_version = """
s = input()
q = int(input())
for _ in range(q):
    o = input().split()
    if o[0] == 'replace':
        s = s[:int(o[1])] + o[3] + s[int(o[2]+1:]
    elif o[0] == 'reverse':
        rev = s[int(o[1]):int(o[2]+1][::-1]
        s = s[:int(o[1])] + rev + s[int(o[2]+1:len(s)
    elif o[0] == 'print':
        print(s[int(o[1]:int(o[2]+1)
"""