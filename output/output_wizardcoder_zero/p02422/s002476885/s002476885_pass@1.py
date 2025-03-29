import sys
from math import pi

class MathHelper:
    def __init__(self):
        self.pi = 3.141592653589793238462643
        
    def prime_numbers(self, n):
        ptable = [0 for _ in range(n+1)]
        primes = []
        for i in range(2, n+1):
            if not ptable[i]:
                primes.append(i)
                for j in range(i*i, n+1, i):
                    ptable[j] = 1
        return primes
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)
        
    def matrix_multiply(self, A, B):
        ans = [0] * len(A)
        for i in range(len(A)):
            c = 0
            for j, row in enumerate(A):
                c += row * B[j]
            ans.append(c)
        return ans
        
    def matrix_addition(self, A, B):
        return [a + b for a, b in zip(A, B)]
        
class OutputHelper:
    def list(self, l):
        print(' '.join(str(x) for x in l))
    
math = MathHelper()
output = OutputHelper()

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
for _ in range(N):
    P.append([int(x) for x in input().split()])
    
for M in P:
    if M[0] == 'print':
        a, b = map(int, M[1:3])
        output.list(S[a:b+1])
    elif M[0] == 'reverse':
        a, b = map(int, M[1:3])
        T = S[a:b+1][::-1]
        S = S[:a] + T + S[b+1:]
    elif M[0] == 'replace':
        a, b, c = map(int, M)
        S = S[:a] + str(c) + S[b+1:]

S