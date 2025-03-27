import sys
m = 0
f = 0
r = 0
M = []
F = []
R = []
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    M.append(m)
    F.append(f)
    R.append(r)
for i in range(len(M)):
    total = m+f
    if total<30 or total>80:
        print('F')
    elif total>=80:
        print('A')
    elif 65<=total<80:
        print('B')
    elif 50<=total<65:
        print('C')
    else:
        if R[i]>=50:
            print('C')
        else:
            print('D')