N = int(input())
AP, BP = 0, 0
for i in range(N):
    A,B = input().split()
    X = max(len(A), len(B))
    sa = ''.join([char if char == A[j] else ('0' * (ord(char) - ord(A[j])) for j, char in enumerate(B)]).ljust(X,'0')
    if A == B or sa > B: AP += 1
    elif sa < B: BP += 1
    else: break
print(AP,BP)