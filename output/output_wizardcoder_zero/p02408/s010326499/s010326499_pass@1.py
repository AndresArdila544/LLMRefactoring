C = []
for _ in range(4): C += [list(range(1, 14))]
n = int(input())
[C[_-1].pop(int(input()-1) if i != 'S' else None for i in (input(),)*n]
print(*['D' if c else ('H' if b else ('S' if a else '')+str(b.index('')+1) for a,b in zip([C[0], C[1], C[2]] + [None]*4,[*range(13), None] * 3)])if c][:n], sep='\n')