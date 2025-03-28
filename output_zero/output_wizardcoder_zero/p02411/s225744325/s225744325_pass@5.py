M = []
F = []
R = []
while True:
    m, f, r = map(int, input().split())
    if (m, f) == (-1, -1):
        break
    M.append(m)
    F.append(f)
    R.append(r)

for i in range(len(M)):
    if m <= 30 or f <= 30:
        print('F')
    elif m + f >= 80:
        print('A')
    elif 65 < m + f < 80:
        print('B')
    else:
        print('C' if R[i] >= 50 else 'D')