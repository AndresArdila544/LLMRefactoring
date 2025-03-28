```
import math

# Math class
class mymath:
    pi = 3.14159265358979323846264338

    # Prime Number
    def pnum_eratosthenes(self, n):
        ptable = [0 for i in range(n+1)]
        plist = []
        for i in range(2, n+1):
            if ptable[i] == 0:
                plist.append(i)
                for j in range(i+i, n+1, i):
                    ptable[j] = 1
        return plist

    # GCD
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    # LCM
    def lcm(self, a, b):
        return (a*b)//self.gcd(a,b)

# Output class
class output:
    # List
    def list(self, l):
        print(" ".join(str(i) for i in l))

S = input()
N = int(input())
P = []
mymath = mymath()
output = output()
for i in range(N):
    P.append([x for x in input().split()])
for M in P:
    if M[0] == 'print':
        a, b = int(M[1]), int(M[2])+1
        print(S[a:b])
    elif M[0] == 'reverse':
        a, b = int(M[1]), int(M[2])+1
        T = S[a:b]
        S = S[:a]+T[::-1]+S[b:]
    elif M[0] == 'replace':
        a, b, c = int(M[1]), int(M[2])+1, M[3]
        S = S[:a]+c+S[b:]
```