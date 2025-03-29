import math

s = input().split()
q = int(input())
for i in range(q):
    n = list(map(int, input().split()))
    if 'print' in n:
        print(*[s[i] for i in range(n[1], n[2]+1)])
    elif 'reverse' in n:
        s.reverse()
    elif 'replace' in n:
        for _ in range(int(n[0])):
            s.pop(n[1])
        s[n[1]:n[2]+1] = list(map(str, input().split())) + [''] * (n[2] - n[1])
"""
Explanation: 
The program takes an input string and a number of queries. It then performs the specified operation on the given substring in the string for each query.

- 'print' operation prints the characters from index i to j in s (inclusive).
- 'reverse' operation reverses the order of the characters in the substring between indices i and j, inclusive. 
- 'replace' operation removes the characters in the range [i,j] and inserts new characters at index k starting from position i.

The refactored version uses list comprehension to print the string without using the end argument of the print() function, and removes the need for a separate variable for counting. The string is directly inserted into s instead of popping and inserting elements, reducing the number of lines of code. 
"""