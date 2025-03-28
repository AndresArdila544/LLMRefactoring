import sys
import math
from collections import deque

class MyMath:
    def __init__(self):
        self.pi = 3.141592653589793238462643

    def prime_numbers(self, n):
        ptable = [0] * (n+1)
        plist = []
        for i in range(2, n+1):
            if not ptable[i]:
                plist.append(i)
                for j in range(i*i, n+1, i):
                    ptable[j] = 1
        return plist

    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a

    def lcm(self, a, b):
        return (a*b) // self.gcd(a,b)

    def matrix_multiply(self, A, B):
        ans = []
        for i in range(len(A)):
            c = 0
            for j in range(len(B[0])):
                for k in range(len(B)):
                    c += A[i][k] * B[j][k]
            ans.append([c])
        return ans

class Output:
    def list_print(self, l):
        print(" ".join(str(x) for x in l))

def get_input():
    N = []
    while True:
        try:
            N.append(input())
        except EOFError:
            break
    return N

# Main program
S = input()
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

for M in P:
    if M[0] == 'print':
        a, b = map(int, M[1:3])
        print(S[a:b+1])
    elif M[0] == 'reverse':
        a, b = map(int, M[1:3])
        T = deque(S[a:b+1])
        T.reverse()
        S = "".join([S[:a], "".join(T), S[b+1:]])
    elif M[0] == 'replace':
        a, b, c = map(int, M)
        S = f"{S[:a]}{c}{S[b+1:]}".replace(S[a:b+1], str(c))
    
output = Output()

output.list_print([math.pi])