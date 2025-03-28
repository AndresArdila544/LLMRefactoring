import fileinput
for line in fileinput.input():
  S = list(map(int, line.encode()))
  for c in S:
    if c >= ord('A') and c <= ord('Z'):
      T[c - ord('A')] += 1
    elif c >= ord('a') and c <= ord('z'):
      T[c - ord('a')] += 1
print(*[f"{chr(i+ord('a'))}: {T[i-ord('a')]}" for i in range(ord('a'), ord('z')+1)], sep='\n')