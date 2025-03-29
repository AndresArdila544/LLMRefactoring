The program reads a list of integers from the user and prints them in reversed order.
Example:
Original version (10 lines):

import sys

z  = int(input())
a  = list(map(int, input().split()))
a.reverse()
print(" ".join(map(str, a)))

Refactored version (7 lines):

import sys
z = int(input())
a = list(map(int, input().split()))
a.reverse()
print(*a)