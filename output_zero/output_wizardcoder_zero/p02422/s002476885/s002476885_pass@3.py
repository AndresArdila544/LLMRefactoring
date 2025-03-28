# coding=utf-8
import sys
import math

class MyMath:
    pi = 3.141592653589793238462643
    
    @staticmethod
    def eratosthenes_prime(n):
        ptable = [0 for i in range(n+1)]
        prime_list = []
        
        for i in range(2, n+1):
            if ptable[i] == 0:
                prime_list.append(i)
                for j in range(i*i, n+1, i):
                    ptable[j] = 1
        
        return prime_list
    
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return MyMath.gcd(b, a % b)
    
    @staticmethod
    def lcm(a, b):
        return (a * b) // MyMath.gcd(a, b)
    
    @staticmethod
    def mat_mul(A, B):
        ans = []
        
        for a in A:
            c = 0
            for j, row in enumerate(a):
                c += row * B[j]
            ans.append(c)
            
        return ans
    
class Output:
    @staticmethod
    def list_print(l):
        l = list(l)
        
        for i, num in enumerate(l):
            print(num, end="")
            if i != len(l)-1:
                print(" ", end="")
        print()
    
    @staticmethod
    def output_print(A, B):
        return A // B, A % B, A / B

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
P = [list(map(int, input().split())) for i in range(N)]

for M in P:
    if M[0] == 'print':
        a, b = map(int, M[1:])
        print(S[a:b+1])
    elif M[0] == 'reverse':
        a, b = map(int, M[1:])
        T = S[a:b+1]
        S = S[:a] + T[::-1] + S[b+1:]
    elif M[0] == 'replace':
        a, b, c = map(int, M)
        S = S[:a] + str(c) + S[b+1:]
        
# Uncomment the following line to test the functions:
# get_input()
# Output().list_print([1, 2, 3, 4])
# print(Output.output_print(8, 2))
# print("{0} {1} {2:.5f}".format(12, 5, MyMath().pi))
# print("{0:.6f} {1:.6f}".format(math.sqrt(3), math.sqrt(3) * 2 * math.pi))
# S = "abcdefghijklmnopqrstuvwxyz"
# Output().list_print([ord('a'), ord('c'), ord('e')])
# print("{}".format(S[0]))
# print(MyMath().eratosthenes_prime(50))