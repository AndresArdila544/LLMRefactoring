```
# coding=utf-8

import sys
import math

### input sample
N = int(input())
P = []
for _ in range(N):
    P.append([int(x) for x in input().split()])

### output class
class Output:
    def list(self, l):
        print(" ".join(str(i) for i in l))

output = Output()

### math class
class MyMath:
    pi = 3.14159265358979323846264338

    def pnum_eratosthenes(self, n):
        ptable = [0 for i in range(n+1)]
        plist = []
        for i in range(2, n+1):
            if ptable[i]==0:
                plist.append(i)
                for j in range(i+i, n+1, i):
                    ptable[j] = 1
        return plist

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    def lcm(self, a, b):
        return (a*b)//self.gcd(a,b)

mymath = MyMath()

### main function
def get_input():
    N = []
    while True:
        try:
            N.append(int(input()))
        except EOFError:
            break
    return N

S = input()
N = int(input())
P = []
for _ in range(N):
    P.append([int(x) for x in input().split()])

for M in P:
    if M[0] == 'print':
        a = int(M[1])
        b = int(M[2])+1
        output.list(S[a:b])
    elif M[0] == 'reverse':
        a = int(M[1])
        b = int(M[2])+1
        T = S[a:b]
        S = S[:a]+T[::-1]+S[b:]
    elif M[0] == 'replace':
        a = int(M[1])
        b = int(M[2])+1
        S = S[:a]+M[3]+S[b:]
```