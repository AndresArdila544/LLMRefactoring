import sys
import math

class Math:
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

    def mul(self, A, B):
        ans = []
        for a in A:
            c = 0
            for j, row in enumerate(a):
                c += row*B[j]
            ans.append(c)
        return ans

class Output:
    def list(self, l):
        print(" ".join([str(num) for num in l]))

def get_input():
    N = []
    while True:
        try:
            N.append(input())
        except EOFError:
            break
    return N

S = input()
N = int(input())
P = []

for i in range(N):
    P.append([x for x in input().split()])

for M in P:
    if M[0] == 'print':
        a, b = map(int, M[1:3])
        print(S[a:b])
    elif M[0] == 'reverse':
        a, b = map(int, M[1:3])
        T = S[a:b]
        S = S[:a]+T[::-1]+S[b:]
    elif M[0] == 'replace':
        a, b = map(int, M[1:3])
        S = S[:a]+M[3]+S[b:]