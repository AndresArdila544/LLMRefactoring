N = int(input())
AP = BP = 0
for A,B in (map(str.split, [input() for _ in range(N)]):
    X = max(len(A), len(B))
    A = A.ljust(X, '0')
    B = B.ljust(X, '0')
    AP += int(all(ord(a) <= ord(b) for a,b in zip(A,B)))
    BP += int(any(ord(a) < ord(b) for a,b in zip(A,B))
print(AP, BP)