data = [[0]*10 for _ in range(4)]
for _ in range(int(input())):
    b, f, r, v = map(int, input().split())
    data[b-1][f-1] += v 
print('\n'.join(' '.join(str(col) for col in row) + ('\n' if i < 3 else '') for i, row in enumerate(data)))